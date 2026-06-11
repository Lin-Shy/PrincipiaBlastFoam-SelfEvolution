#!/usr/bin/env python3
"""Classify OpenFOAM log evidence for one case directory."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from common import collect_openfoam_log_evidence, write_json  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Classify OpenFOAM logs for a case directory.")
    parser.add_argument("case_dir", type=Path)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = collect_openfoam_log_evidence(args.case_dir)
    if args.output:
        write_json(args.output, payload)
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
