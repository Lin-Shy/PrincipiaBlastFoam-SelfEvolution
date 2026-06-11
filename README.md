# PrincipiaBlastFoam-SelfEvolution

This project now keeps only the Chapter 4 main experiment assets used by the
PrincipiaBlastFoam thesis benchmark restructure.

## Boundary

- Chapter 3 system code remains in `../PrincipiaBlastFoam/`.
- Chapter 3 benchmark evidence is archived under
  `../experiment_results/chapter3_end_to_end_evaluation/`.
- Chapter 4 uses the canonical realistic 12-case benchmark as the held-out
  realistic application benchmark.
- Chapter 4 skills for the main result come only from Chapter 3 tutorial
  benchmark failures, not from the Chapter 4 12-case test set.

## Structure

- `benchmarks/chapter4_realistic_application_benchmark.json`: canonical
  12-case realistic benchmark.
- `skills/chapter3_tutorial_concrete_skill_library.*`: concrete verifier skills
  generated from Chapter 3 tutorial failures.
- `skills/chapter3_tutorial_abstract_skill_library.*`: abstract skills generated
  from the same Chapter 3 failure evidence.
- `scripts/ingest_chapter3_tutorial_failures.py`: regenerates the current skill
  libraries from Chapter 3 tutorial failure taxonomy.
- `scripts/run_chapter4_e2e_ablation.py`: creates no-skill, abstract-skill, and
  concrete-verifier-skill benchmark variants and runs the black-box evaluator.
- `scripts/verifiers/`: deterministic artifact/log helper modules used by the
  current evaluation workflow.
- `results/`: retained Chapter 4 ablation outputs and thesis-facing result
  reports.
- `docs/project_boundary.md`: concise boundary note for Chapter 3 baseline
  versus Chapter 4 self-evolution comparison.
- `docs/benchmark_restructure_task_plan.md`: experiment-system restructure
  plan that explains the Chapter 3 baseline versus Chapter 3 + Chapter 4
  comparison boundary.

Historical skill-abstraction, Hermes prompt-injection, old local skill-library,
and old comparison artifacts were removed after the 2026-06-06 main results were
completed.

## Current Results

Current experiment outputs are stored inside this project:

```text
results/
```

Retained Chapter 4 main result directories:

- `e2e_ablation/chapter4_realistic_no_skill_20260605_091920/`
- `e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/`
- `e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034/`
- `e2e_ablation/comparison/`

Retained thesis-facing reports:

- `reports/chapter4_realistic_benchmark_ablation.md`
- `reports/chapter4_self_evolution_final_conclusion.md`

## Commands

Regenerate Chapter 4 skills from the Chapter 3 B-layer failure evidence:

```bash
/data/miniconda3/bin/python scripts/ingest_chapter3_tutorial_failures.py \
  --chapter3-result-dir ../experiment_results/chapter3_end_to_end_evaluation/results/model_runs/deepseek-v4-pro/chapter3_tutorial_modification_20260605_20260606/B_short_30
```

Run the abstract-skill group:

```bash
/data/miniconda3/bin/python scripts/run_chapter4_e2e_ablation.py \
  --condition abstract \
  --execute \
  --run-as-user openfoam \
  --workflow-timeout 1200 \
  --benchmark-runner-timeout 18000
```

Run the concrete-verifier-skill group:

```bash
/data/miniconda3/bin/python scripts/run_chapter4_e2e_ablation.py \
  --condition concrete_verifier \
  --concrete-skills skills/chapter3_tutorial_concrete_skill_library.json \
  --execute \
  --run-as-user openfoam \
  --workflow-timeout 1200 \
  --benchmark-runner-timeout 18000
```

## Latest Metrics

| group | cases | strict pass | strict pass rate | mean score |
|---|---:|---:|---:|---:|
| no-skill | 12 | 7 | 58.33% | 0.8552 |
| abstract-skill | 12 | 7 | 58.33% | 0.8743 |
| concrete-verifier-skill | 12 | 8 | 66.67% | 0.9324 |
