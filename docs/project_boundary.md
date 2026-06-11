# PrincipiaBlastFoam-SelfEvolution Project Boundary

## Purpose

This project contains the Chapter 4 self-evolution work for PrincipiaBlastFoam:
skill extraction, skill abstraction, skill injection, deterministic verifiers,
the canonical 12-case realistic benchmark, and retained ablation results.

## Relationship to Chapter 3

- Base system source: `../PrincipiaBlastFoam/`
- Chapter 3 baseline benchmark evidence:
  `../experiment_results/chapter3_end_to_end_evaluation/`
- Chapter 4 project root:
  `../PrincipiaBlastFoam-SelfEvolution/`

Chapter 3 should be treated as the baseline system and evidence source. Chapter
4 should be treated as the self-evolution extension evaluated by comparing:

- `no_skill`: original Chapter 3 workflow on the Chapter 4 realistic benchmark.
- `abstract_skill`: same workflow with abstract skills mined from Chapter 3
  tutorial failures.
- `concrete_verifier_skill`: same workflow with concrete verifier skills mined
  from Chapter 3 tutorial failures.

## Local Structure

- `benchmarks/`: Chapter 4 benchmark definitions.
- `skills/`: generated concrete and abstract skill libraries.
- `scripts/`: ingestion, benchmark generation, ablation runner, and verifier
  helpers.
- `results/`: retained Chapter 4 ablation outputs and thesis-facing reports.
- `literature/`: literature review material for agent self-evolution.
- `docs/`: project boundary, dependency notes, and benchmark restructure plan.

## Leakage Rule

Do not mine skills from the Chapter 4 12-case benchmark when reporting strict
generalization. Thesis-facing Chapter 4 results should use skills derived from
Chapter 3 tutorial benchmark failures, then evaluate on the Chapter 4 realistic
benchmark.
