# PrincipiaBlastFoam-SelfEvolution

Chapter 4 code project for PrincipiaBlastFoam self-evolution experiments. This
repository keeps the scripts and verifier helpers only; benchmark data, skill
libraries, ablation outputs, and reports live in the shared experiment-results
tree.

## Boundaries

- Base system code: `../PrincipiaBlastFoam/`
- Chapter 3 baseline evidence: `../experiment_results/chapter3_end_to_end_evaluation/`
- Chapter 4 experiment assets: `../experiment_results/chapter4_self_evolution/`
- Thesis literature and writing assets: `/data/graduation-docs/`

## Code Layout

- `scripts/ingest_chapter3_tutorial_failures.py`: generate concrete and
  abstract skill libraries from Chapter 3 tutorial failures.
- `scripts/run_chapter4_e2e_ablation.py`: generate and optionally run no-skill,
  abstract-skill, and concrete-verifier-skill ablations.
- `scripts/verifiers/`: deterministic log/artifact verification helpers.
- `docs/`: short project-boundary and dependency notes.

## Commands

Regenerate Chapter 4 skills:

```bash
/data/miniconda3/bin/python scripts/ingest_chapter3_tutorial_failures.py \
  --chapter3-result-dir ../experiment_results/chapter3_end_to_end_evaluation/results/model_runs/deepseek-v4-pro/chapter3_tutorial_modification_20260605_20260606/B_short_30
```

Run the concrete-verifier-skill group:

```bash
/data/miniconda3/bin/python scripts/run_chapter4_e2e_ablation.py \
  --condition concrete_verifier \
  --execute \
  --run-as-user openfoam \
  --workflow-timeout 1200 \
  --benchmark-runner-timeout 18000
```
