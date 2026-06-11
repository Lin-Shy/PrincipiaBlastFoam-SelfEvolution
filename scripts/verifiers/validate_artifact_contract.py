#!/usr/bin/env python3
"""Validate report and execution artifact contracts for one case directory."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from common import collect_openfoam_log_evidence, report_status, write_json  # noqa: E402


def build_payload(case_dir: Path) -> dict:
    reports = report_status(case_dir)
    logs = collect_openfoam_log_evidence(case_dir)
    execution_status = reports["execution_status"]
    final_status = str(execution_status.get("final_status", "")).lower()
    status_clean_end = execution_status.get("solver_log_has_clean_end")
    execution_status_consistent = True
    if final_status == "success" and logs["has_solver_clean_end"] is False:
        execution_status_consistent = False
    if status_clean_end is False and logs["has_solver_clean_end"] is True:
        execution_status_consistent = False
    missing = [name for name, item in reports["reports"].items() if not item["exists"]]
    placeholders = [name for name, item in reports["reports"].items() if item["placeholder"]]
    issues = []
    if missing:
        issues.append("missing required artifacts: " + ", ".join(missing))
    if placeholders:
        issues.append("placeholder reports: " + ", ".join(placeholders))
    if not execution_status_consistent:
        issues.append("execution_status does not match solver log clean End evidence")
    if not reports["review_has_validation_decision"]:
        issues.append("review_report lacks an explicit validation decision")
    if not reports["review_has_limitations"]:
        issues.append("review_report lacks limitations or caveats")
    return {
        "case_dir": str(case_dir),
        "ok": not issues,
        "issues": issues,
        **reports,
        "solver": {
            "has_solver_clean_end": logs["has_solver_clean_end"],
            "has_openfoam_blocking_error": logs["has_openfoam_blocking_error"],
            "categories": logs["categories"],
        },
        "execution_status_consistent_with_solver_log": execution_status_consistent,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate artifact contract for a case directory.")
    parser.add_argument("case_dir", type=Path)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = build_payload(args.case_dir)
    if args.output:
        write_json(args.output, payload)
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
