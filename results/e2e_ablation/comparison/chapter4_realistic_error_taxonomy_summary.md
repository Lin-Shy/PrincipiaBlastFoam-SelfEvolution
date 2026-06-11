# 第4章真实任务错误分类摘要

- 生成时间：2026-06-07T04:08:38Z
- 记录数：36

## 总体错误家族

| 错误家族 | 数量 |
|---|---:|
| `success` | 22 |
| `openfoam_blocking_failure` | 9 |
| `workflow_state_mismatch` | 3 |
| `artifact_incomplete` | 1 |
| `review_report_failure` | 1 |

## 分组错误家族

| group | error_family | count |
|---|---|---:|
| `abstract_skill` | `openfoam_blocking_failure` | 4 |
| `abstract_skill` | `success` | 7 |
| `abstract_skill` | `workflow_state_mismatch` | 1 |
| `concrete_verifier_skill` | `openfoam_blocking_failure` | 2 |
| `concrete_verifier_skill` | `review_report_failure` | 1 |
| `concrete_verifier_skill` | `success` | 8 |
| `concrete_verifier_skill` | `workflow_state_mismatch` | 1 |
| `no_skill` | `artifact_incomplete` | 1 |
| `no_skill` | `openfoam_blocking_failure` | 3 |
| `no_skill` | `success` | 7 |
| `no_skill` | `workflow_state_mismatch` | 1 |

## 后续技能方向

| recommended_followup | count |
|---|---:|
| `solver_end_and_workflow_state_reconciliation` | 10 |
| `non_placeholder_review_contract` | 4 |

## 解释边界

错误分类基于评测结果中的终态、失败项和OpenFOAM诊断摘要归纳，用于论文中的失败模式讨论；它不是人工逐行复盘的物理正确性判定。
