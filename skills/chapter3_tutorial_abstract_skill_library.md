# 第4章来自第3章 Tutorial 失败的抽象技能库

- 生成时间：2026-06-06T10:58:29Z
- 来源结果：`/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/results/model_runs/deepseek-v4-pro/chapter3_tutorial_modification_20260605_20260606/B_short_30`
- 技能数量：2

## General policy for Execution failure triage before report success

- id: `abstract.chapter3_tutorial.execution`
- status: `candidate`
- source_failure_tasks: deflagrationtodetonationtransition_boundary_medium_005, delayeddetonation_boundary_medium_006, forwardstep_boundary_medium_007, forwardstep_charge_medium_007, forwardstep_mesh_medium_007, freefield_boundary_medium_008, freefield_charge_medium_008, freefield_mesh_medium_008, internaldetonation_internaldetonation_boundary_medium_009, internaldetonation_internaldetonation_charge_medium_009, internaldetonation_internaldetonation_mesh_medium_009, internaldetonation_internaldetonation_withob_boundary_medium_010, internaldetonation_internaldetonation_withob_boundary_medium_011, internaldetonation_internaldetonation_withob_charge_medium_010, internaldetonation_internaldetonation_withob_charge_medium_011, internaldetonation_internaldetonation_withob_mesh_medium_010, internaldetonation_internaldetonation_withob_mesh_medium_011, movingcone_boundary_medium_012, movingcone_mesh_medium_012, obliqueshock_boundary_medium_013, obliqueshock_mesh_medium_013, reacting_2_charge_medium_014, reacting_boundary_medium_014, reacting_charge_medium_012, reacting_mesh_hard_014, reactingparticles_charge_medium_013, reactingparticles_mesh_hard_015, setrefinedfields_charge_hard_015, shocktube_polydisperse_charge_hard_016, shocktube_tabulated_charge_hard_017

操作建议：
- Convert the user request into explicit validation checks before execution.
- Use the active generated case directory as the evidence boundary.
- Separate file-edit correctness, physical consistency, execution readiness, and report quality when judging success.
- Treat missing artifacts and failed validation checks as task failures until fixed or explicitly scoped as limitations.

验证条件：
- execution_status.json records a completed run state.
- log.blastFoam or solver log contains a clean End marker.
- run.exit_code == 0 and timed_out is false.

## General policy for Report and artifact contract completion

- id: `abstract.chapter3_tutorial.report_artifact`
- status: `candidate`
- source_failure_tasks: deflagrationtodetonationtransition_boundary_medium_005, delayeddetonation_boundary_medium_006, forwardstep_boundary_medium_007, forwardstep_charge_medium_007, forwardstep_mesh_medium_007, freefield_boundary_medium_008, freefield_charge_medium_008, freefield_mesh_medium_008, internaldetonation_internaldetonation_boundary_medium_009, internaldetonation_internaldetonation_charge_medium_009, internaldetonation_internaldetonation_mesh_medium_009, internaldetonation_internaldetonation_withob_boundary_medium_010, internaldetonation_internaldetonation_withob_boundary_medium_011, internaldetonation_internaldetonation_withob_charge_medium_010, internaldetonation_internaldetonation_withob_charge_medium_011, internaldetonation_internaldetonation_withob_mesh_medium_010, internaldetonation_internaldetonation_withob_mesh_medium_011, movingcone_boundary_medium_012, movingcone_mesh_medium_012, obliqueshock_boundary_medium_013, obliqueshock_mesh_medium_013, reacting_2_charge_medium_014, reacting_boundary_medium_014, reacting_charge_medium_012, reacting_mesh_hard_014, reactingparticles_charge_medium_013, reactingparticles_mesh_hard_015, setrefinedfields_charge_hard_015, shocktube_polydisperse_charge_hard_016, shocktube_tabulated_charge_hard_017

操作建议：
- Convert the user request into explicit validation checks before execution.
- Use the active generated case directory as the evidence boundary.
- Separate file-edit correctness, physical consistency, execution readiness, and report quality when judging success.
- Treat missing artifacts and failed validation checks as task failures until fixed or explicitly scoped as limitations.

验证条件：
- All required report artifacts exist and are non-empty.
- Reports cite actual generated files or logs.
- review_report.md is not a placeholder continuation.
