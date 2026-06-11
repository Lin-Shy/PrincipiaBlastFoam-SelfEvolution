#!/usr/bin/env python3
"""Run Chapter 4 skill-injected E2E ablations on the realistic benchmark.

The script does not modify Hermes or PrincipiaBlastFoam source code. It creates
benchmark files whose user requests are prefixed with retrieved skills, then
optionally invokes the existing Chapter 3 black-box evaluator.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GRADUATION_PROJECTS_ROOT = PROJECT_ROOT.parent
EXPERIMENT_RESULTS_ROOT = GRADUATION_PROJECTS_ROOT / "experiment_results"
CHAPTER3_EVALUATION_ROOT = EXPERIMENT_RESULTS_ROOT / "chapter3_end_to_end_evaluation"
CHAPTER4_RESULTS_ROOT = EXPERIMENT_RESULTS_ROOT / "chapter4_self_evolution"
DEFAULT_BENCHMARK_CASES = CHAPTER4_RESULTS_ROOT / "benchmarks" / "chapter4_realistic_application_benchmark.json"
DEFAULT_CHAPTER3_EVALUATOR = CHAPTER3_EVALUATION_ROOT / "scripts" / "run_chapter3_full_evaluation.py"
DEFAULT_CONCRETE_SKILLS = CHAPTER4_RESULTS_ROOT / "skills" / "chapter3_tutorial_concrete_skill_library.json"
DEFAULT_ABSTRACT_SKILLS = CHAPTER4_RESULTS_ROOT / "skills" / "chapter3_tutorial_abstract_skill_library.json"
DEFAULT_RESULTS_ROOT = CHAPTER4_RESULTS_ROOT / "e2e_ablation"
DEFAULT_PYTHON = Path("/data/miniconda3/bin/python")
TOKEN_RE = re.compile(r"[A-Za-z0-9_./+-]+|[\u4e00-\u9fff]{2,}")


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def run_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


def load_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def tokenize(text: str) -> Counter[str]:
    tokens: Counter[str] = Counter()
    for match in TOKEN_RE.finditer(text.lower()):
        token = match.group(0).strip()
        if len(token) > 1:
            tokens[token] += 1
    return tokens


def list_field(skill: Dict[str, Any], *names: str) -> List[str]:
    values: List[str] = []
    for name in names:
        value = skill.get(name)
        if isinstance(value, list):
            values.extend(str(item) for item in value if str(item).strip())
        elif isinstance(value, str) and value.strip():
            values.append(value)
    return values


def skill_text(skill: Dict[str, Any]) -> str:
    fields = [
        skill.get("id", ""),
        skill.get("title", ""),
        skill.get("summary", ""),
        " ".join(list_field(skill, "trigger_terms", "trigger_conditions", "trigger")),
        " ".join(list_field(skill, "applies_to", "applicable_task_types", "task_types")),
        " ".join(list_field(skill, "procedure", "operation_recommendations", "action", "policy")),
        " ".join(list_field(skill, "validation", "validation_conditions", "verification")),
        " ".join(list_field(skill, "evidence_source_cases", "source_failure_tasks")),
        " ".join(str(item) for item in skill.get("evidence_sources", [])),
        " ".join(list_field(skill, "risks", "possible_side_effects")),
        " ".join(list_field(skill, "do_not_apply_when", "not_applicable_when")),
    ]
    return "\n".join(str(field) for field in fields)


def retrieve(skills: List[Dict[str, Any]], query: str, limit: int) -> List[Tuple[float, Dict[str, Any]]]:
    query_tokens = tokenize(query)
    scored: List[Tuple[float, Dict[str, Any]]] = []
    for skill in skills:
        tokens = tokenize(skill_text(skill))
        overlap = sum(min(query_tokens[token], tokens.get(token, 0)) for token in query_tokens)
        trigger_terms = list_field(skill, "trigger_terms", "trigger_conditions")
        trigger_bonus = sum(1 for term in trigger_terms if str(term).lower() in query.lower()) * 2.0
        norm = math.sqrt(sum(value * value for value in tokens.values())) or 1.0
        score = (overlap / norm) + trigger_bonus
        if score > 0:
            scored.append((round(score, 4), skill))
    return sorted(scored, key=lambda item: item[0], reverse=True)[:limit]


def skill_block(skills: Iterable[Dict[str, Any]]) -> str:
    lines: List[str] = []
    for index, skill in enumerate(skills, start=1):
        triggers = list_field(skill, "trigger_terms", "trigger_conditions", "trigger")[:3]
        procedures = list_field(skill, "procedure", "operation_recommendations", "action", "policy")[:3]
        validations = list_field(skill, "validation", "validation_conditions", "verification")[:3]
        lines.append(f"{index}. {skill.get('title', skill.get('id', 'skill'))}")
        lines.append(f"   - 适用原因：{skill.get('summary') or '；'.join(triggers)}")
        if procedures:
            lines.append("   - 执行策略：" + "；".join(procedures))
        if validations:
            lines.append("   - 验证条件：" + "；".join(validations))
    return "\n".join(lines)


def inject_request(original_request: str, condition: str, retrieved: List[Tuple[float, Dict[str, Any]]]) -> str:
    if condition == "no_skill":
        return original_request

    skills = [skill for _, skill in retrieved]
    return (
        "【第4章自进化技能注入】\n"
        "以下技能来自历史端到端评测和抽象策略库，只作为执行前诊断、产物检查和审查约束；"
        "不得修改Hermes源码，不得修改PrincipiaBlastFoam源码，只允许在本次生成case和报告中落实这些检查。\n"
        "请在完成原始任务时优先满足：环境预检查、最小必要配置修改、物理假设审查、输出字段绑定、"
        "execution_status与求解器日志一致性、review_report完整性。\n\n"
        f"{skill_block(skills)}\n\n"
        "【原始第3章端到端benchmark任务】\n"
        f"{original_request}"
    )


def split_case_ids(values: Sequence[str]) -> List[str]:
    case_ids: List[str] = []
    for value in values:
        for item in str(value).split(","):
            case_id = item.strip()
            if case_id:
                case_ids.append(case_id)
    return case_ids


def select_cases(cases: List[Dict[str, Any]], case_ids: Sequence[str], limit: int | None) -> List[Dict[str, Any]]:
    selected = cases
    if case_ids:
        wanted = list(dict.fromkeys(case_ids))
        by_id = {str(case.get("id")): case for case in cases}
        missing = [case_id for case_id in wanted if case_id not in by_id]
        if missing:
            raise SystemExit(f"Unknown case id(s): {', '.join(missing)}")
        selected = [by_id[case_id] for case_id in wanted]
    if limit:
        selected = selected[:limit]
    return selected


def build_cases_payload(
    base_payload: Dict[str, Any],
    skills: List[Dict[str, Any]],
    condition: str,
    top_k: int,
    limit: int | None,
    case_ids: Sequence[str],
) -> Dict[str, Any]:
    cases = base_payload.get("cases", [])
    cases = select_cases(cases, case_ids, limit)

    generated_cases = []
    retrieval_rows = []
    for case in cases:
        user_request = str(case.get("user_request", ""))
        query = f"{case.get('id', '')}\n{case.get('title', '')}\n{user_request}\n{' '.join(case.get('tags', []))}"
        retrieved = retrieve(skills, query, limit=top_k) if condition != "no_skill" else []
        generated = dict(case)
        generated["user_request"] = inject_request(user_request, condition, retrieved)
        generated["chapter4_skill_condition"] = condition
        generated["base_case_id"] = case.get("id")
        generated["injected_skill_ids"] = [skill.get("id") for _, skill in retrieved]
        generated_cases.append(generated)
        retrieval_rows.append(
            {
                "case_id": case.get("id"),
                "condition": condition,
                "top_skills": [
                    {"score": score, "id": skill.get("id"), "title": skill.get("title")}
                    for score, skill in retrieved
                ],
            }
        )

    payload = dict(base_payload)
    payload["name"] = f"{base_payload.get('name', 'chapter3_benchmark')}_{condition}"
    payload["version"] = f"{base_payload.get('version', '0.0.0')}+chapter4-{condition}"
    payload["description"] = (
        f"Chapter 4 {condition} ablation benchmark generated from the canonical Chapter 4 realistic 12-case benchmark. "
        "The task set and expected checks are unchanged; only the user request is skill-injected."
    )
    payload["chapter4_ablation"] = {
        "created_at": utc_now(),
        "condition": condition,
        "top_k": top_k,
        "source_benchmark": str(DEFAULT_BENCHMARK_CASES),
        "selected_case_ids": [str(case.get("id")) for case in generated_cases],
        "case_count": len(generated_cases),
        "retrieval_rows": retrieval_rows,
    }
    payload["cases"] = generated_cases
    return payload


def run_chapter3_evaluator(args: argparse.Namespace, cases_file: Path, results_dir: Path) -> Dict[str, Any]:
    command = [
        str(args.python),
        str(args.chapter3_evaluator),
        "--execute-workflow",
        "--cases-file",
        str(cases_file),
        "--results-dir",
        str(results_dir),
        "--workflow-timeout",
        str(args.workflow_timeout),
        "--benchmark-runner-timeout",
        str(args.benchmark_runner_timeout),
        "--cleanup-interval",
        str(args.cleanup_interval),
        "--no-include-history",
    ]
    if args.cleanup_final:
        command.append("--cleanup-final")
    else:
        command.append("--no-cleanup-final")
    if args.run_as_user:
        command.extend(["--run-as-user", args.run_as_user])
    if args.allow_root_openfoam:
        command.append("--allow-root-openfoam")
    if args.limit:
        command.extend(["--limit", str(args.limit)])

    process = subprocess.run(
        command,
        cwd=str(CHAPTER3_EVALUATION_ROOT),
        text=True,
        capture_output=True,
        check=False,
    )
    result = {
        "command": command,
        "exit_code": process.returncode,
        "stdout": process.stdout,
        "stderr": process.stderr,
    }
    write_json(results_dir / "chapter4_ablation_invocation.json", result)
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate and optionally run Chapter 4 skill-injected E2E ablations.")
    parser.add_argument("--condition", choices=["no_skill", "concrete", "concrete_verifier", "abstract"], default="abstract")
    parser.add_argument(
        "--benchmark-cases",
        "--chapter3-cases",
        dest="benchmark_cases",
        type=Path,
        default=DEFAULT_BENCHMARK_CASES,
    )
    parser.add_argument("--chapter3-evaluator", type=Path, default=DEFAULT_CHAPTER3_EVALUATOR)
    parser.add_argument("--concrete-skills", type=Path, default=DEFAULT_CONCRETE_SKILLS)
    parser.add_argument("--abstract-skills", type=Path, default=DEFAULT_ABSTRACT_SKILLS)
    parser.add_argument("--results-root", type=Path, default=DEFAULT_RESULTS_ROOT)
    parser.add_argument("--python", type=Path, default=DEFAULT_PYTHON)
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--case-ids", default="", help="Comma-separated case ids to include in the generated benchmark.")
    parser.add_argument("--case-id", action="append", default=[], help="Single case id to include. Can be repeated.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--workflow-timeout", type=int, default=1200)
    parser.add_argument("--benchmark-runner-timeout", type=int, default=18000)
    parser.add_argument("--cleanup-interval", type=int, default=1)
    parser.add_argument("--cleanup-final", dest="cleanup_final", action="store_true", default=True)
    parser.add_argument("--no-cleanup-final", dest="cleanup_final", action="store_false")
    parser.add_argument("--run-as-user", default="")
    parser.add_argument("--allow-root-openfoam", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    base_payload = load_json(args.benchmark_cases, {})
    if not base_payload.get("cases"):
        raise SystemExit(f"No cases found in {args.benchmark_cases}")
    case_ids = split_case_ids([args.case_ids, *args.case_id])

    if args.condition == "abstract":
        skills = load_json(args.abstract_skills, [])
    elif args.condition in {"concrete", "concrete_verifier"}:
        skills = load_json(args.concrete_skills, [])
    else:
        skills = []

    condition_slug = {
        "no_skill": "chapter4_realistic_no_skill",
        "abstract": "chapter4_realistic_abstract_from_chapter3",
        "concrete": "chapter4_realistic_concrete_from_chapter3",
        "concrete_verifier": "chapter4_realistic_concrete_from_chapter3",
    }[args.condition]
    output_dir = args.results_root / f"{condition_slug}_{run_id()}"
    payload = build_cases_payload(base_payload, skills, args.condition, args.top_k, args.limit, case_ids)
    cases_file = output_dir / f"chapter4_{len(payload['cases'])}case_{args.condition}_benchmark.json"
    write_json(cases_file, payload)

    response = {
        "output_dir": str(output_dir),
        "cases_file": str(cases_file),
        "condition": args.condition,
        "case_count": len(payload["cases"]),
        "selected_case_ids": [case.get("id") for case in payload["cases"]],
        "cleanup_final": args.cleanup_final,
        "execute": args.execute,
    }
    if args.execute:
        eval_results_dir = output_dir / "chapter3_evaluation"
        response["evaluation_results_dir"] = str(eval_results_dir)
        response["invocation"] = run_chapter3_evaluator(args, cases_file, eval_results_dir)

    print(json.dumps(response, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
