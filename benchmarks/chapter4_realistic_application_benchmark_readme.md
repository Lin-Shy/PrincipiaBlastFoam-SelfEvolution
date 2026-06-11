# 第4章真实应用 Benchmark

生成日期：2026-06-05

`chapter4_realistic_application_benchmark.json` 是第4章 canonical 真实应用模拟 benchmark。它保留原 12-case 真实复杂任务集，但角色已经从“第3章主评测集”调整为“第4章技能自进化迁移与消融评测集”。

## 定位

- 任务数量：12 条。
- 任务性质：真实爆炸安全、建筑冲击波、内部爆炸、遮挡绕射、压力测点和后处理需求的短时 workflow 代理任务。
- 主要用途：比较 no-skill、abstract-skill、concrete-verifier-skill 三组在真实复杂任务上的严格通过率、核心执行通过率、终态一致性、产物完整性和报告质量。
- 不承担的角色：不作为第3章“广覆盖基础能力”主 benchmark。

## 与第3章的边界

第3章主结果应来自：

```text
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/data/chapter3_tutorial_modification_benchmark.json
```

第4章技能来源应优先来自第3章 tutorial benchmark 的失败分类：

```text
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/results/model_runs/<model>/<campaign>/B_short_30/chapter3_tutorial_failure_taxonomy.json
```

当前 `deepseek-v4-pro` 基线对应路径为：

```text
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/results/model_runs/deepseek-v4-pro/chapter3_tutorial_modification_20260605_20260606/B_short_30/chapter3_tutorial_failure_taxonomy.json
```

旧 12-case 技能来源结果和旧技能库已经从当前主结果目录中清理。若以后从归档外部恢复这些旧结果，只能标注为“历史诊断性消融”，不能表述为严格泛化评测。

## 评测组

建议在该 benchmark 上运行三组：

- `no-skill`：不注入第4章技能。
- `abstract-skill`：注入从第3章 tutorial 失败中抽象得到的技能。
- `concrete-verifier-skill`：注入带验证条件的具体技能。

## 指标

- 严格通过率。
- 核心执行通过率。
- 求解器正常结束数。
- workflow 终态不一致数。
- 产物不完整数。
- 非占位报告齐备数。
- 报告质量。
- 平均总分。
- 错误类型变化。
- 与第3章失败技能来源之间的对应关系。

## 当前状态

当前文件已固化 benchmark 定义。2026-06-06 已使用第3章 tutorial 失败生成的技能库完成三组主消融：

- no-skill：12 条，严格通过 7 条，严格通过率 58.33%，平均得分 0.8552。
- abstract-skill：12 条，严格通过 7 条，严格通过率 58.33%，平均得分 0.8743。
- concrete-verifier-skill：12 条，严格通过 8 条，严格通过率 66.67%，平均得分 0.9324。

当前主结果保留在：

```text
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/results/e2e_ablation/
```
