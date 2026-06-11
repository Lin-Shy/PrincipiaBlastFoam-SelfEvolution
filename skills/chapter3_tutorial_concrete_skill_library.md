# 第4章来自第3章 Tutorial 失败的具体验证技能库

- 生成时间：2026-06-06T10:58:29Z
- 来源结果：`/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/results/model_runs/deepseek-v4-pro/chapter3_tutorial_modification_20260605_20260606/B_short_30`
- 技能数量：6

## Execution failure triage before report success (boundary)

- id: `skill.chapter3_tutorial.execution.boundary`
- status: `candidate`
- source_failure_tasks: deflagrationtodetonationtransition_boundary_medium_005, delayeddetonation_boundary_medium_006, forwardstep_boundary_medium_007, freefield_boundary_medium_008, internaldetonation_internaldetonation_boundary_medium_009, internaldetonation_internaldetonation_withob_boundary_medium_010, internaldetonation_internaldetonation_withob_boundary_medium_011, movingcone_boundary_medium_012, obliqueshock_boundary_medium_013, reacting_boundary_medium_014

操作建议：
- Separate environment blockers, mesh/setup failures, solver failures, and post-processing failures.
- Require a clean solver End marker and non-empty execution_status evidence before reporting execution success.
- Do not let a completed report override a failed or timed-out run.

验证条件：
- run.exit_code == 0 and timed_out is false.
- log.blastFoam or solver log contains a clean End marker.
- execution_status.json records a completed run state.

## Execution failure triage before report success (charge)

- id: `skill.chapter3_tutorial.execution.charge`
- status: `candidate`
- source_failure_tasks: forwardstep_charge_medium_007, freefield_charge_medium_008, internaldetonation_internaldetonation_charge_medium_009, internaldetonation_internaldetonation_withob_charge_medium_010, internaldetonation_internaldetonation_withob_charge_medium_011, reacting_2_charge_medium_014, reacting_charge_medium_012, reactingparticles_charge_medium_013, setrefinedfields_charge_hard_015, shocktube_polydisperse_charge_hard_016, shocktube_tabulated_charge_hard_017

操作建议：
- Separate environment blockers, mesh/setup failures, solver failures, and post-processing failures.
- Require a clean solver End marker and non-empty execution_status evidence before reporting execution success.
- Do not let a completed report override a failed or timed-out run.

验证条件：
- run.exit_code == 0 and timed_out is false.
- log.blastFoam or solver log contains a clean End marker.
- execution_status.json records a completed run state.

## Execution failure triage before report success (mesh)

- id: `skill.chapter3_tutorial.execution.mesh`
- status: `candidate`
- source_failure_tasks: forwardstep_mesh_medium_007, freefield_mesh_medium_008, internaldetonation_internaldetonation_mesh_medium_009, internaldetonation_internaldetonation_withob_mesh_medium_010, internaldetonation_internaldetonation_withob_mesh_medium_011, movingcone_mesh_medium_012, obliqueshock_mesh_medium_013, reacting_mesh_hard_014, reactingparticles_mesh_hard_015

操作建议：
- Separate environment blockers, mesh/setup failures, solver failures, and post-processing failures.
- Require a clean solver End marker and non-empty execution_status evidence before reporting execution success.
- Do not let a completed report override a failed or timed-out run.

验证条件：
- run.exit_code == 0 and timed_out is false.
- log.blastFoam or solver log contains a clean End marker.
- execution_status.json records a completed run state.

## Report and artifact contract completion (boundary)

- id: `skill.chapter3_tutorial.report_artifact.boundary`
- status: `candidate`
- source_failure_tasks: deflagrationtodetonationtransition_boundary_medium_005, delayeddetonation_boundary_medium_006, forwardstep_boundary_medium_007, freefield_boundary_medium_008, internaldetonation_internaldetonation_boundary_medium_009, internaldetonation_internaldetonation_withob_boundary_medium_010, internaldetonation_internaldetonation_withob_boundary_medium_011, movingcone_boundary_medium_012, obliqueshock_boundary_medium_013, reacting_boundary_medium_014

操作建议：
- Check that physics_report.md, execution_report.md, execution_status.json, and review_report.md exist when requested.
- Reject placeholder continuation responses as reports.
- Require reports to cite concrete file, log, or postProcessing evidence.

验证条件：
- All required report artifacts exist and are non-empty.
- review_report.md is not a placeholder continuation.
- Reports cite actual generated files or logs.

## Report and artifact contract completion (charge)

- id: `skill.chapter3_tutorial.report_artifact.charge`
- status: `candidate`
- source_failure_tasks: forwardstep_charge_medium_007, freefield_charge_medium_008, internaldetonation_internaldetonation_charge_medium_009, internaldetonation_internaldetonation_withob_charge_medium_010, internaldetonation_internaldetonation_withob_charge_medium_011, reacting_2_charge_medium_014, reacting_charge_medium_012, reactingparticles_charge_medium_013, setrefinedfields_charge_hard_015, shocktube_polydisperse_charge_hard_016, shocktube_tabulated_charge_hard_017

操作建议：
- Check that physics_report.md, execution_report.md, execution_status.json, and review_report.md exist when requested.
- Reject placeholder continuation responses as reports.
- Require reports to cite concrete file, log, or postProcessing evidence.

验证条件：
- All required report artifacts exist and are non-empty.
- review_report.md is not a placeholder continuation.
- Reports cite actual generated files or logs.

## Report and artifact contract completion (mesh)

- id: `skill.chapter3_tutorial.report_artifact.mesh`
- status: `candidate`
- source_failure_tasks: forwardstep_mesh_medium_007, freefield_mesh_medium_008, internaldetonation_internaldetonation_mesh_medium_009, internaldetonation_internaldetonation_withob_mesh_medium_010, internaldetonation_internaldetonation_withob_mesh_medium_011, movingcone_mesh_medium_012, obliqueshock_mesh_medium_013, reacting_mesh_hard_014, reactingparticles_mesh_hard_015

操作建议：
- Check that physics_report.md, execution_report.md, execution_status.json, and review_report.md exist when requested.
- Reject placeholder continuation responses as reports.
- Require reports to cite concrete file, log, or postProcessing evidence.

验证条件：
- All required report artifacts exist and are non-empty.
- review_report.md is not a placeholder continuation.
- Reports cite actual generated files or logs.
