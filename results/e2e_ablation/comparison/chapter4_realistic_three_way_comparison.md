# 第4章真实任务三组消融对比

- 生成时间：2026-06-07T04:08:38Z
- no-skill结果：`/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/results/e2e_ablation/chapter4_realistic_no_skill_20260605_091920/chapter3_evaluation/chapter3_full_evaluation_results.json`
- abstract-skill结果：`/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/results/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308/chapter3_evaluation/chapter3_full_evaluation_results.json`
- concrete-verifier-skill结果：`/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/results/e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034/chapter3_evaluation/chapter3_full_evaluation_results.json`
- case数：12

## 总体指标

| 指标 | no-skill | abstract-skill | concrete-verifier-skill |
|---|---:|---:|---:|
| `case_count` | 12 | 12 | 12 |
| `strict_pass_count` | 7 | 7 | 8 |
| `strict_pass_rate` | 58.33% | 58.33% | 66.67% |
| `core_execution_pass_count` | 7 | 7 | 8 |
| `core_execution_pass_rate` | 58.33% | 58.33% | 66.67% |
| `mean_overall_score` | 0.8552 | 0.8743 | 0.9324 |

## 终态分布

### no_skill
| 终态 | 数量 |
|---|---:|
| `success` | 7 |
| `execution_failed` | 3 |
| `artifact_incomplete` | 1 |
| `workflow_state_mismatch` | 1 |

### abstract_skill
| 终态 | 数量 |
|---|---:|
| `success` | 7 |
| `execution_failed` | 4 |
| `workflow_state_mismatch` | 1 |

### concrete_verifier_skill
| 终态 | 数量 |
|---|---:|
| `success` | 8 |
| `execution_failed` | 2 |
| `review_failed` | 1 |
| `workflow_state_mismatch` | 1 |

## 逐case对比

| case | no-skill | abstract | concrete | abstractΔ | concreteΔ(no-skill) | concreteΔ(abstract) |
|---|---|---|---|---:|---:|---:|
| `bls_two_box_interference_pressure_history` | `success` | `success` | `workflow_state_mismatch` | 0.0 | -0.1319 | -0.1319 |
| `building_corner_diffraction_probe_grid` | `success` | `success` | `success` | 0.0 | 0.0 | 0.0 |
| `building_facade_pressure_probe_smoke` | `execution_failed` | `execution_failed` | `success` | -0.04 | 0.3402 | 0.3802 |
| `erdc_internal_airblast_vent_pipe_probe` | `success` | `success` | `success` | 0.0 | 0.004 | 0.004 |
| `gable_roof_building_envelope_pressure_smoke` | `workflow_state_mismatch` | `workflow_state_mismatch` | `success` | -0.008 | 0.1239 | 0.1319 |
| `hemicylinder_obstacle_reflection_probe_smoke` | `execution_failed` | `execution_failed` | `execution_failed` | 0.104 | 0.048 | -0.056 |
| `reconass_400kg_external_facade_smoke` | `execution_failed` | `execution_failed` | `execution_failed` | -0.004 | 0.0803 | 0.0843 |
| `shock_tube_short_validation` | `success` | `success` | `success` | 0.0 | 0.0119 | 0.0119 |
| `surface_burst_scaled_probe_smoke` | `success` | `success` | `success` | 0.0159 | 0.0119 | -0.004 |
| `three_level_building_room_pressure_smoke` | `success` | `success` | `review_failed` | 0.0119 | -0.044 | -0.0559 |
| `vented_confined_gas_explosion_window_smoke` | `success` | `success` | `success` | -0.0039 | -0.0079 | -0.004 |
| `vertical_wall_shielding_probe_line_smoke` | `artifact_incomplete` | `execution_failed` | `success` | 0.1527 | 0.489 | 0.3363 |

## 结论边界

本对比只使用从第3章tutorial评测失败证据中抽取并冻结的技能库，不使用第4章12个真实任务作为技能来源。结论应同时报告严格通过率、核心执行通过率、平均得分、终态分布和错误分类，不能只用单一指标概括自进化效果。
