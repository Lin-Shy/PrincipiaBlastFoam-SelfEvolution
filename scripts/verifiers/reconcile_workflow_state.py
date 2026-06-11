#!/usr/bin/env python3
"""Reconcile workflow terminal state with solver and artifact evidence."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from common import collect_openfoam_log_evidence, load_json, report_status, write_json  # noqa: E402


def load_score_record(path: Path, case_id: str) -> Dict[str, Any]:
    payload = load_json(path, {})
    rows = payload.get("latest_case_results") or payload.get("case_results") if isinstance(payload, dict) else payload
    if not isinstance(rows, list):
        return {}
    for row in rows:
        if str(row.get("case_id")) == case_id:
            return row
    return {}


def classify(case_dir: Path, score: Dict[str, Any]) -> Dict[str, Any]:
    logs = collect_openfoam_log_evidence(case_dir)
    reports = report_status(case_dir)
    raw_checks = score.get("raw_checks") or {}
    run = score.get("run") or {}
    terminal = str(score.get("terminal_status", "unknown"))
    artifact_missing = any(not item["exists"] for item in reports["reports"].values())
    placeholder = any(item["placeholder"] for item in reports["reports"].values())
    solver_completed = logs["has_solver_clean_end"] or raw_checks.get("solver_log_has_end") is True
    execution_completed = raw_checks.get("execution_status_completed") is True or reports["execution_status"].get("final_status") == "success"
    workflow_failed = run.get("exit_code") not in (0, None) or raw_checks.get("workflow_failure_absent") is False

    if logs["has_openfoam_blocking_error"] or (not solver_completed and execution_completed):
        reconciliation = "true_failure"
    elif artifact_missing or placeholder or terminal == "artifact_incomplete":
        reconciliation = "artifact_incomplete"
    elif solver_completed and execution_completed and workflow_failed:
        reconciliation = "workflow_state_mismatch"
    elif solver_completed and execution_completed and terminal in {"review_missing", "review_report_incomplete", "review_failed"}:
        reconciliation = "review_only_failure"
    elif solver_completed and execution_completed:
        reconciliation = "partial_success_solver_completed"
    else:
        reconciliation = "true_failure"

    return {
        "case_dir": str(case_dir),
        "case_id": score.get("case_id") or case_dir.name,
        "terminal_status": terminal,
        "strict_pass": bool(score.get("strict_pass")),
        "core_execution_pass": bool(score.get("core_execution_pass")),
        "solver_completed": solver_completed,
        "execution_status_completed": execution_completed,
        "workflow_failed": workflow_failed,
        "artifact_missing_or_placeholder": artifact_missing or placeholder,
        "openfoam_blocking_error": logs["has_openfoam_blocking_error"],
        "reconciliation": reconciliation,
        "evidence": {
            "solver": {
                "has_solver_clean_end": logs["has_solver_clean_end"],
                "categories": logs["categories"],
            },
            "reports": reports["reports"],
            "raw_checks": raw_checks,
            "run": run,
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Reconcile workflow state for a case directory.")
    parser.add_argument("case_dir", type=Path)
    parser.add_argument("--score-json", type=Path, required=True)
    parser.add_argument("--case-id", default="")
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    case_id = args.case_id or args.case_dir.name
    payload = classify(args.case_dir, load_score_record(args.score_json, case_id))
    if args.output:
        write_json(args.output, payload)
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
