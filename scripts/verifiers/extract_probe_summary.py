#!/usr/bin/env python3
"""Extract probe evidence from retained OpenFOAM outputs, reports, and logs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from common import collect_openfoam_log_evidence, read_text, snippets, write_json  # noqa: E402


def parse_numeric_row(line: str) -> List[float]:
    values: List[float] = []
    for token in line.replace("(", " ").replace(")", " ").split():
        try:
            values.append(float(token))
        except ValueError:
            continue
    return values


def probe_files(case_dir: Path) -> List[Path]:
    root = case_dir / "postProcessing"
    if not root.exists():
        return []
    candidates = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.name.startswith(".") or path.name.endswith((".vtk", ".vtp", ".obj")):
            continue
        candidates.append(path)
    return sorted(candidates)


def summarize_file(path: Path) -> Dict[str, Any]:
    rows: List[List[float]] = []
    header_lines = []
    for line in read_text(path, max_chars=2_000_000).splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            header_lines.append(stripped)
            continue
        numeric = parse_numeric_row(stripped)
        if len(numeric) >= 2:
            rows.append(numeric)
    peak_values = []
    if rows:
        width = max(len(row) for row in rows)
        for index in range(1, width):
            column = [abs(row[index]) for row in rows if len(row) > index]
            if column:
                peak_values.append(max(column))
    return {
        "path": str(path),
        "relative_path": str(path),
        "header_lines": header_lines[:8],
        "data_rows": len(rows),
        "last_time": rows[-1][0] if rows else None,
        "column_count": max((len(row) for row in rows), default=0),
        "peak_values": peak_values[:12],
    }


def build_payload(case_dir: Path) -> Dict[str, Any]:
    files = probe_files(case_dir)
    summaries = [summarize_file(path) for path in files]
    report_text = "\n".join(
        read_text(case_dir / name, max_chars=80_000)
        for name in ("physics_report.md", "execution_report.md", "review_report.md")
    )
    logs = collect_openfoam_log_evidence(case_dir)
    fallback_mentions = snippets(
        report_text,
        ["probe", "blastProbes", "pressureProbes", "overpressure", "impulse", "postProcessing"],
        max_items=8,
        radius=180,
    )
    return {
        "case_dir": str(case_dir),
        "probe_files_present": bool(files),
        "probe_file_count": len(files),
        "probe_files": summaries,
        "total_data_rows": sum(item["data_rows"] for item in summaries),
        "last_time": max((item["last_time"] for item in summaries if item["last_time"] is not None), default=None),
        "has_probe_warning": logs["has_probe_warning"],
        "has_probe_skipped_warning": logs["has_probe_skipped_warning"],
        "has_probe_adjusted_warning": logs["has_probe_adjusted_warning"],
        "fallback_report_mentions": fallback_mentions,
        "evidence_quality": "probe_files" if files else ("report_or_log_mentions" if fallback_mentions or logs["has_probe_warning"] else "missing"),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract probe summary for a case directory.")
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
