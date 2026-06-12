#!/usr/bin/env python3
"""Ingest Chapter 3 tutorial benchmark failures into Chapter 4 skill libraries."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GRADUATION_PROJECTS_ROOT = PROJECT_ROOT.parent
EXPERIMENT_RESULTS_ROOT = GRADUATION_PROJECTS_ROOT / "graduation-experiment-results"
CHAPTER3_RESULTS_ROOT = EXPERIMENT_RESULTS_ROOT / "chapter3_end_to_end_evaluation" / "results"
CHAPTER4_RESULTS_ROOT = EXPERIMENT_RESULTS_ROOT / "chapter4_self_evolution"
DEFAULT_CONCRETE_JSON = CHAPTER4_RESULTS_ROOT / "skills" / "chapter3_tutorial_concrete_skill_library.json"
DEFAULT_CONCRETE_MD = CHAPTER4_RESULTS_ROOT / "skills" / "chapter3_tutorial_concrete_skill_library.md"
DEFAULT_ABSTRACT_JSON = CHAPTER4_RESULTS_ROOT / "skills" / "chapter3_tutorial_abstract_skill_library.json"
DEFAULT_ABSTRACT_MD = CHAPTER4_RESULTS_ROOT / "skills" / "chapter3_tutorial_abstract_skill_library.md"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def slugify(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_").lower()
    return value or "skill"


def latest_chapter3_tutorial_result(results_root: Path) -> Optional[Path]:
    if not results_root.exists():
        return None
    candidates = sorted(
        path
        for path in results_root.iterdir()
        if path.is_dir() and (path / "chapter3_tutorial_evaluation_results.json").exists()
    )
    return candidates[-1] if candidates else None


def load_failure_rows(result_dir: Path) -> List[Dict[str, Any]]:
    taxonomy = load_json(result_dir / "chapter3_tutorial_failure_taxonomy.json", {})
    rows = taxonomy.get("rows") if isinstance(taxonomy, dict) else []
    return rows if isinstance(rows, list) else []


def load_case_results(result_dir: Path) -> Dict[str, Dict[str, Any]]:
    payload = load_json(result_dir / "chapter3_tutorial_evaluation_results.json", {})
    rows = payload.get("case_results") if isinstance(payload, dict) else []
    if not isinstance(rows, list):
        return {}
    return {str(row.get("case_id")): row for row in rows}


def stage_title(stage: str) -> str:
    return {
        "file_edit_target": "File-target preflight for tutorial modification",
        "openfoam_dictionary_syntax": "OpenFOAM dictionary syntax guard",
        "requirement_validation": "Validation-check driven task closure",
        "execution": "Execution failure triage before report success",
        "report_artifact": "Report and artifact contract completion",
        "static_definition": "Static benchmark definition audit",
    }.get(stage, f"{stage} handling")


def concrete_action(stage: str, category: str) -> List[str]:
    if stage == "file_edit_target":
        return [
            "Before editing, resolve every expected file relative to the active case root.",
            "If a target file is absent, inspect the closest existing dictionary and document whether the task requires creating a new file.",
            "Do not claim a file-edit task is complete until the expected target exists or a justified alternative is recorded.",
        ]
    if stage == "openfoam_dictionary_syntax":
        return [
            "After each dictionary edit, run a brace-balance and semicolon-oriented static parse before execution.",
            "Prefer editing existing dictionary blocks instead of appending duplicate top-level entries.",
            "For fvSchemes/fvSolution/controlDict, validate the exact edited file rather than only the case directory.",
        ]
    if stage == "requirement_validation":
        return [
            "Translate the user request into explicit validation checks before judging success.",
            "Run the task-specific checks against the generated case artifacts.",
            "If a check fails, revise the case or mark the requirement as unmet instead of relying on narrative reports.",
        ]
    if stage == "execution":
        return [
            "Separate environment blockers, mesh/setup failures, solver failures, and post-processing failures.",
            "Require a clean solver End marker and non-empty execution_status evidence before reporting execution success.",
            "Do not let a completed report override a failed or timed-out run.",
        ]
    if stage == "report_artifact":
        return [
            "Check that physics_report.md, execution_report.md, execution_status.json, and review_report.md exist when requested.",
            "Reject placeholder continuation responses as reports.",
            "Require reports to cite concrete file, log, or postProcessing evidence.",
        ]
    return [
        "Keep the benchmark task, expected files, validation checks, and source tutorial aligned.",
        "Record any static uncertainty as a skill-source limitation.",
    ]


def concrete_validation(stage: str) -> List[str]:
    if stage == "execution":
        return [
            "run.exit_code == 0 and timed_out is false.",
            "log.blastFoam or solver log contains a clean End marker.",
            "execution_status.json records a completed run state.",
        ]
    if stage == "report_artifact":
        return [
            "All required report artifacts exist and are non-empty.",
            "review_report.md is not a placeholder continuation.",
            "Reports cite actual generated files or logs.",
        ]
    if stage == "openfoam_dictionary_syntax":
        return [
            "Edited dictionary has balanced braces.",
            "The expected OpenFOAM dictionary target exists under the generated case path.",
        ]
    return [
        "The original validation check that produced the failure passes on the revised case.",
        "The issue does not recur in the case-level score record.",
    ]


def build_concrete_skills(rows: Sequence[Dict[str, Any]], case_results: Dict[str, Dict[str, Any]], result_dir: Path) -> List[Dict[str, Any]]:
    grouped: Dict[tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row.get("stage")), str(row.get("task_category")))].append(row)

    skills: List[Dict[str, Any]] = []
    now = utc_now()
    for (stage, category), items in sorted(grouped.items()):
        source_tasks = sorted({str(item.get("case_id")) for item in items})
        source_cases = sorted({str(item.get("source_case_name")) for item in items})
        issues = [str(item.get("issue")) for item in items]
        skill_id = f"skill.chapter3_tutorial.{slugify(stage)}.{slugify(category)}"
        skills.append(
            {
                "id": skill_id,
                "title": f"{stage_title(stage)} ({category})",
                "status": "candidate",
                "created_at": now,
                "updated_at": now,
                "source": "chapter3_tutorial_modification_benchmark",
                "source_result_dir": str(result_dir),
                "source_failure_tasks": source_tasks,
                "source_tutorial_cases": source_cases,
                "failure_stage": stage,
                "failure_issues": issues[:20],
                "trigger_conditions": [
                    f"task_category == {category}",
                    f"failure_stage == {stage}",
                    "A generated tutorial-modification case has an unmet validation check or incomplete artifact.",
                ],
                "task_types": [category],
                "operation_recommendations": concrete_action(stage, category),
                "validation_conditions": concrete_validation(stage),
                "evidence_sources": [
                    {
                        "case_id": task_id,
                        "score": case_results.get(task_id, {}).get("overall_score"),
                        "terminal_status": case_results.get(task_id, {}).get("terminal_status"),
                    }
                    for task_id in source_tasks[:20]
                ],
                "do_not_apply_when": [
                    "The current task is not an OpenFOAM/blastFoam tutorial modification or generated-case review.",
                    "The source evidence comes from the Chapter 4 12-case benchmark rather than Chapter 3 tutorial failures.",
                ],
                "possible_side_effects": [
                    "Extra validation steps can increase runtime.",
                    "Overly rigid checks may reject acceptable alternative files unless the alternative is documented.",
                ],
            }
        )
    return skills


def build_abstract_skills(concrete_skills: Sequence[Dict[str, Any]], result_dir: Path) -> List[Dict[str, Any]]:
    by_stage: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for skill in concrete_skills:
        by_stage[str(skill.get("failure_stage"))].append(skill)
    now = utc_now()
    abstract: List[Dict[str, Any]] = []
    for stage, skills in sorted(by_stage.items()):
        task_types = sorted({item for skill in skills for item in skill.get("task_types", [])})
        source_tasks = sorted({item for skill in skills for item in skill.get("source_failure_tasks", [])})
        policy = [
            "Convert the user request into explicit validation checks before execution.",
            "Use the active generated case directory as the evidence boundary.",
            "Separate file-edit correctness, physical consistency, execution readiness, and report quality when judging success.",
            "Treat missing artifacts and failed validation checks as task failures until fixed or explicitly scoped as limitations.",
        ]
        abstract.append(
            {
                "id": f"abstract.chapter3_tutorial.{slugify(stage)}",
                "title": f"General policy for {stage_title(stage)}",
                "status": "candidate",
                "created_at": now,
                "updated_at": now,
                "source": "chapter3_tutorial_concrete_skill_library",
                "source_result_dir": str(result_dir),
                "source_concrete_skill_ids": [skill["id"] for skill in skills],
                "source_failure_tasks": source_tasks,
                "trigger_conditions": [
                    f"Observed or anticipated failure stage: {stage}.",
                    "The task requires case-file mutation, execution evidence, post-processing, or report review.",
                ],
                "applicable_task_types": task_types,
                "policy": policy,
                "operation_recommendations": policy,
                "validation_conditions": sorted({item for skill in skills for item in skill.get("validation_conditions", [])})[:12],
                "not_applicable_when": [
                    "The task is pure prose writing and has no generated case, validation check, or executable artifact.",
                    "The only evidence comes from the Chapter 4 test benchmark being evaluated.",
                ],
                "possible_side_effects": [
                    "May add review overhead to simple tasks.",
                    "May reduce apparent pass rate by enforcing stricter evidence boundaries.",
                ],
            }
        )
    return abstract


def skill_markdown(title: str, skills: Sequence[Dict[str, Any]], result_dir: Path, empty_note: str) -> str:
    lines = ["# " + title, "", f"- 生成时间：{utc_now()}", f"- 来源结果：`{result_dir}`", f"- 技能数量：{len(skills)}", ""]
    if not skills:
        lines.append(empty_note)
        lines.append("")
        return "\n".join(lines)
    for skill in skills:
        lines.extend(
            [
                f"## {skill['title']}",
                "",
                f"- id: `{skill['id']}`",
                f"- status: `{skill.get('status', 'candidate')}`",
                f"- source_failure_tasks: {', '.join(skill.get('source_failure_tasks', []))}",
                "",
            ]
        )
        recommendations = skill.get("operation_recommendations") or skill.get("policy") or []
        if recommendations:
            lines.append("操作建议：")
            lines.extend(f"- {item}" for item in recommendations)
            lines.append("")
        validations = skill.get("validation_conditions") or []
        if validations:
            lines.append("验证条件：")
            lines.extend(f"- {item}" for item in validations)
            lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Chapter 4 skills from Chapter 3 tutorial failure evidence.")
    parser.add_argument("--chapter3-result-dir", type=Path, default=None)
    parser.add_argument("--chapter3-results-root", type=Path, default=CHAPTER3_RESULTS_ROOT)
    parser.add_argument("--concrete-json", type=Path, default=DEFAULT_CONCRETE_JSON)
    parser.add_argument("--concrete-md", type=Path, default=DEFAULT_CONCRETE_MD)
    parser.add_argument("--abstract-json", type=Path, default=DEFAULT_ABSTRACT_JSON)
    parser.add_argument("--abstract-md", type=Path, default=DEFAULT_ABSTRACT_MD)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result_dir = args.chapter3_result_dir or latest_chapter3_tutorial_result(args.chapter3_results_root)
    if result_dir is None:
        raise SystemExit("No Chapter 3 tutorial evaluation result found. Pass --chapter3-result-dir.")
    rows = load_failure_rows(result_dir)
    case_results = load_case_results(result_dir)
    concrete = build_concrete_skills(rows, case_results, result_dir)
    abstract = build_abstract_skills(concrete, result_dir)
    write_json(args.concrete_json, concrete)
    write_json(args.abstract_json, abstract)
    args.concrete_md.parent.mkdir(parents=True, exist_ok=True)
    args.concrete_md.write_text(
        skill_markdown(
            "第4章来自第3章 Tutorial 失败的具体验证技能库",
            concrete,
            result_dir,
            "当前输入结果未包含失败分类，因此未生成具体验证技能。该状态可用于说明 A 层静态 benchmark 通过，但不能替代 B/C 层真实 workflow 失败证据。",
        ),
        encoding="utf-8",
    )
    args.abstract_md.parent.mkdir(parents=True, exist_ok=True)
    args.abstract_md.write_text(
        skill_markdown(
            "第4章来自第3章 Tutorial 失败的抽象技能库",
            abstract,
            result_dir,
            "当前输入结果未包含失败分类，因此未生成抽象技能。需要使用包含真实 workflow 失败项的第3章 tutorial 评测结果重新运行本脚本。",
        ),
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "chapter3_result_dir": str(result_dir),
                "failure_rows": len(rows),
                "concrete_skills": len(concrete),
                "abstract_skills": len(abstract),
                "concrete_json": str(args.concrete_json),
                "abstract_json": str(args.abstract_json),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
