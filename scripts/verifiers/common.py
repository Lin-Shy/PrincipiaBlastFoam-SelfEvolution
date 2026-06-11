#!/usr/bin/env python3
"""Shared evidence extraction helpers for Chapter 4 verifiers."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


PLACEHOLDER_REPORT_RE = re.compile(
    r"(need to|i need|let me|i will|i'll|需要|我需要|继续|下一步|not yet|placeholder|TODO)",
    re.IGNORECASE,
)
NUMERIC_DIR_RE = re.compile(r"^[0-9]+(?:\.[0-9]+)?(?:e[-+]?[0-9]+)?$", re.IGNORECASE)
PATCH_NAME_RE = re.compile(r"(patch named .+ not found|patch .+ not found|unknown patch|cannot find patch)", re.IGNORECASE)


def load_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_text(path: Path, max_chars: Optional[int] = None) -> str:
    if not path.exists() or not path.is_file():
        return ""
    text = path.read_text(encoding="utf-8", errors="ignore")
    if max_chars is not None and len(text) > max_chars:
        return text[:max_chars]
    return text


def tail_text(path: Path, max_chars: int = 120_000) -> str:
    if not path.exists() or not path.is_file():
        return ""
    data = path.read_bytes()
    return data[-max_chars:].decode("utf-8", errors="ignore")


def is_placeholder_report_text(text: str) -> bool:
    compact = " ".join((text or "").strip().split())
    return bool(compact and len(compact) <= 300 and PLACEHOLDER_REPORT_RE.search(compact))


def is_non_placeholder_report(path: Path, min_chars: int = 250) -> bool:
    text = read_text(path)
    if not text or is_placeholder_report_text(text):
        return False
    return len(text.strip()) >= min_chars


def numeric_time_dirs(case_dir: Path) -> List[str]:
    if not case_dir.exists():
        return []
    return sorted(child.name for child in case_dir.iterdir() if child.is_dir() and NUMERIC_DIR_RE.match(child.name))


def case_log_paths(case_dir: Path) -> List[Path]:
    if not case_dir.exists():
        return []
    direct = sorted(path for path in case_dir.glob("log.*") if path.is_file())
    processor_logs = sorted(path for path in case_dir.glob("processor*/log.*") if path.is_file())
    return direct + processor_logs


def blastfoam_log_paths(case_dir: Path) -> List[Path]:
    paths = [case_dir / "log.blastFoam"]
    paths.extend(sorted(case_dir.glob("processor*/log.blastFoam")))
    return [path for path in paths if path.exists()]


def snippets(text: str, patterns: Iterable[str], max_items: int = 5, radius: int = 220) -> List[str]:
    found: List[str] = []
    lowered = text.lower()
    for pattern in patterns:
        start = lowered.find(pattern.lower())
        if start < 0:
            continue
        left = max(0, start - radius)
        right = min(len(text), start + len(pattern) + radius)
        compact = " ".join(text[left:right].split())
        if compact and compact not in found:
            found.append(compact)
        if len(found) >= max_items:
            break
    return found


def collect_openfoam_log_evidence(case_dir: Path) -> Dict[str, Any]:
    log_paths = case_log_paths(case_dir)
    blast_logs = blastfoam_log_paths(case_dir)
    texts = [read_text(path, max_chars=300_000) for path in log_paths]
    combined = "\n".join(texts)
    blast_tail = "\n".join(tail_text(path, max_chars=140_000) for path in blast_logs)
    lower = combined.lower()
    blast_lower = blast_tail.lower()
    has_probe_warning = any(
        needle in lower
        for needle in (
            "did not find location",
            "skipping location",
            "blastprobes were not found",
            "being moved to the nearest patch face",
            "moved probe",
        )
    )
    has_probe_adjusted = any(needle in lower for needle in ("being moved to the nearest patch face", "moved probe"))
    has_probe_skipped = any(needle in lower for needle in ("did not find location", "skipping location", "were not found"))
    clean_end = bool(re.search(r"(?m)^\s*End\s*$", blast_tail)) or "\nend\n" in blast_lower
    fatal = "foam fatal error" in lower or "fatal error" in lower
    wrong_token = "wrong token type" in lower
    patch_error = bool(PATCH_NAME_RE.search(combined))
    charge_mass = "requested mass is" in lower and "set mass is" in lower
    blocking = fatal or wrong_token or patch_error
    categories: List[str] = []
    if fatal:
        categories.append("openfoam_fatal")
    if wrong_token:
        categories.append("openfoam_parser_error")
    if patch_error:
        categories.append("patch_name_mismatch")
    if has_probe_warning:
        categories.append("probe_location_invalid_or_adjusted")
    if charge_mass:
        categories.append("charge_mass_discretization_warning")
    return {
        "case_dir": str(case_dir),
        "log_paths": [str(path) for path in log_paths],
        "blastfoam_log_paths": [str(path) for path in blast_logs],
        "has_solver_clean_end": clean_end,
        "has_openfoam_fatal": fatal,
        "has_openfoam_blocking_error": blocking,
        "has_write_interval_parser_error": wrong_token,
        "has_patch_name_error": patch_error,
        "has_probe_warning": has_probe_warning,
        "has_probe_skipped_warning": has_probe_skipped,
        "has_probe_adjusted_warning": has_probe_adjusted,
        "has_charge_mass_discretization": charge_mass,
        "categories": categories,
        "snippets": snippets(
            combined,
            [
                "FOAM FATAL ERROR",
                "wrong token type",
                "Patch named",
                "Did not find location",
                "blastProbes were not found",
                "Requested mass is",
            ],
        ),
    }


def report_status(case_dir: Path) -> Dict[str, Any]:
    required = ["physics_report.md", "execution_report.md", "review_report.md", "execution_status.json", "workflow_evidence.json"]
    reports: Dict[str, Dict[str, Any]] = {}
    for name in required:
        path = case_dir / name
        text = read_text(path, max_chars=800) if path.suffix in {".md", ".json"} else ""
        reports[name] = {
            "exists": path.exists(),
            "bytes": path.stat().st_size if path.exists() else 0,
            "placeholder": is_placeholder_report_text(text) if path.suffix == ".md" else False,
        }
    execution_status = load_json(case_dir / "execution_status.json", {})
    review_text = read_text(case_dir / "review_report.md", max_chars=20_000).lower()
    validation_terms = ("validation status", "validation decision", "passed", "failed", "not satisfied")
    limitation_terms = ("limitation", "limitations", "局限", "限制")
    return {
        "case_dir": str(case_dir),
        "reports": reports,
        "has_non_placeholder_physics_report": is_non_placeholder_report(case_dir / "physics_report.md", min_chars=600),
        "has_non_placeholder_execution_report": is_non_placeholder_report(case_dir / "execution_report.md", min_chars=250),
        "has_non_placeholder_review_report": is_non_placeholder_report(case_dir / "review_report.md", min_chars=250),
        "execution_status": execution_status if isinstance(execution_status, dict) else {},
        "review_has_validation_decision": any(term in review_text for term in validation_terms),
        "review_has_limitations": any(term in review_text for term in limitation_terms),
    }
