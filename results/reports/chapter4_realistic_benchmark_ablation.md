# 第4章真实任务Benchmark技能消融报告

- 生成时间：2026-06-07T04:08:38Z
- benchmark：`/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/benchmarks/chapter4_realistic_application_benchmark.json`
- no-skill：`/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/results/e2e_ablation/chapter4_realistic_no_skill_20260605_091920`
- abstract-skill：`/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/results/e2e_ablation/chapter4_realistic_abstract_from_chapter3_20260606_051308`
- concrete-verifier-skill：`/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/results/e2e_ablation/chapter4_realistic_concrete_from_chapter3_20260606_065034`

## 消融设置

三组实验使用同一个12-case真实任务benchmark，并保持workflow超时、runner超时和OpenFOAM执行环境一致。技能库来源限定为第3章tutorial短时workflow失败证据，避免使用第4章真实任务失败记录进行技能沉淀。

## 指标对比

| group | case数 | 严格通过 | 严格通过率 | 核心执行通过率 | 平均得分 | 终态分布 |
|---|---:|---:|---:|---:|---:|---|
| `no_skill` | 12 | 7 | 58.33% | 58.33% | 0.8552 | `{'success': 7, 'execution_failed': 3, 'workflow_state_mismatch': 1, 'artifact_incomplete': 1}` |
| `abstract_skill` | 12 | 7 | 58.33% | 58.33% | 0.8743 | `{'success': 7, 'execution_failed': 4, 'workflow_state_mismatch': 1}` |
| `concrete_verifier_skill` | 12 | 8 | 66.67% | 66.67% | 0.9324 | `{'workflow_state_mismatch': 1, 'success': 8, 'execution_failed': 2, 'review_failed': 1}` |

## 分析要点

真实任务benchmark同时考察算例选择、物理分析、OpenFOAM执行、后处理、报告产物和终态仲裁。若某一技能组没有提升严格通过率，也需要结合平均得分、失败终态迁移和报告完整性判断其作用范围。

## 结论边界

本报告不把旧的12-case技能来源实验作为主结论。旧skill-abstraction、Hermes prompt-injection和历史诊断结果目录已经清理；主消融证据来自本轮第3章失败证据生成的技能库和第4章真实任务重新运行结果。
