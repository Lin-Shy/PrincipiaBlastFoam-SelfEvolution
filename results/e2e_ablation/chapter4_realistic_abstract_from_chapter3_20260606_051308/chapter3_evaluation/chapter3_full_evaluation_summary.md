# 第3章完整评测报告

- 生成时间：2026-06-06T06:50:18Z
- 原始项目：`/data/graduation-projects/PrincipiaBlastFoam`
- 评测报告数：1

## 数据集覆盖

- 修改任务总数：130
- 难度分布：{'basic': 69, 'senior': 61}
- 参考案例数：7
- 目标文件数：16
- Top 5 目标文件：{'constant/phaseProperties': 31, 'system/controlDict': 24, 'system/fvSchemes': 16, 'system/blockMeshDict': 11, 'constant/turbulenceProperties': 8}

## 端到端评测汇总

- 评测 case 记录数：12
- 严格通过数：7
- 严格通过率：58.33%
- 核心执行通过数：7
- 核心执行通过率：58.33%
- 平均总分：0.8743
- 分项均分：{'artifact_completeness': 0.9167, 'execution_success': 0.75, 'report_quality': 0.8303, 'requirement_satisfaction': 0.9833, 'safety_reviewability': 1.0, 'workflow_stability': 0.8611}
- 终态分布：{'success': 7, 'execution_failed': 4, 'workflow_state_mismatch': 1}

## 最新一次每类样例结果

| case_id | terminal_status | strict_pass | core_execution_pass | score | key issues |
|---|---|---:|---:|---:|---|
| `bls_two_box_interference_pressure_history` | `success` | True | True | 1.0000 | observed OpenFOAM nonblocking warning: mesh_boundary_update; observed OpenFOAM nonblocking warning: probe_location_adjusted; observed OpenFOAM warning: charge_mass_discretization |
| `building_corner_diffraction_probe_grid` | `success` | True | True | 0.9921 | observed OpenFOAM nonblocking warning: probe_interpolation_downgraded; observed OpenFOAM warning: charge_mass_discretization |
| `building_facade_pressure_probe_smoke` | `execution_failed` | False | False | 0.6158 | failed check: OpenFOAM blocking diagnostics absent; failed check: endTime within expected; failed check: execution completed; failed check: review report present |
| `erdc_internal_airblast_vent_pipe_probe` | `success` | True | True | 0.9960 | observed OpenFOAM nonblocking warning: mesh_default_patch; observed OpenFOAM warning: openfoam_warning |
| `gable_roof_building_envelope_pressure_smoke` | `workflow_state_mismatch` | False | False | 0.8641 | failed check: OpenFOAM blocking diagnostics absent; failed check: workflow exit_code zero; failed check: workflow failure absent; observed OpenFOAM blocking diagnostic: openfoam_fatal |
| `hemicylinder_obstacle_reflection_probe_smoke` | `execution_failed` | False | False | 0.7237 | failed check: execution completed; failed check: review report present; failed check: solver log clean End; failed check: workflow exit_code zero |
| `reconass_400kg_external_facade_smoke` | `execution_failed` | False | False | 0.6558 | failed check: OpenFOAM blocking diagnostics absent; failed check: execution completed; failed check: review report present; failed check: solver log clean End |
| `shock_tube_short_validation` | `success` | True | True | 0.9881 | observed OpenFOAM nonblocking warning: mesh_default_patch |
| `surface_burst_scaled_probe_smoke` | `success` | True | True | 1.0000 | observed OpenFOAM nonblocking warning: fieldMinMax references missing dynamicP object; observed OpenFOAM nonblocking warning: mesh_default_patch; observed OpenFOAM nonblocking warning: probe_location_adjusted |
| `three_level_building_room_pressure_smoke` | `success` | True | True | 1.0000 | observed OpenFOAM nonblocking warning: mesh_boundary_update; observed OpenFOAM warning: charge_mass_discretization |
| `vented_confined_gas_explosion_window_smoke` | `success` | True | True | 0.9921 | observed OpenFOAM nonblocking warning: mesh_default_patch; observed OpenFOAM warning: openfoam_warning; observed workflow issue: agent attempted to read a non-existent path |
| `vertical_wall_shielding_probe_line_smoke` | `execution_failed` | False | False | 0.6637 | failed check: OpenFOAM blocking diagnostics absent; failed check: execution completed; failed check: review report present; failed check: solver log clean End |

## 主要发现

- Dataset covers 130 modification tasks: 69 basic and 61 senior.
- The most represented reference case is reactingParticles (28 tasks).
- The most frequent target file is constant/phaseProperties (31 tasks).
- The most frequent inferred modification category is time_control_endTime (15 tasks).
- Low-frequency categories need careful interpretation: heat_transfer, material_properties, multiphase_drag, reaction_kinetics, thermodynamics.
- Strict E2E pass rate is 58.33%; mean score is 0.8743.
- Core execution pass rate is 58.33%; this excludes final review/workflow-state-only failures.
- Weakest categories: execution_success=0.7500, report_quality=0.8303, workflow_stability=0.8611.
- Latest failed/partial cases: building_facade_pressure_probe_smoke (0.616), gable_roof_building_envelope_pressure_smoke (0.864), hemicylinder_obstacle_reflection_probe_smoke (0.724), reconass_400kg_external_facade_smoke (0.656), vertical_wall_shielding_probe_line_smoke (0.664).

## 输出文件

- dataset_coverage: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/dataset_coverage.json`
- case_scores_json: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/chapter3_case_scores.json`
- case_scores_csv: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/chapter3_case_scores.csv`
- summary_md: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/chapter3_full_evaluation_summary.md`
- workflow_issue_report: `/data/graduation-projects/experiment_results/agent_skill_evolution/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/principia_workflow_issue_report.md`
