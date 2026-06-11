# 第3章与第4章Benchmark重构任务执行文档

生成日期：2026-06-05

本文档用于交给后续agent执行。目标是重构毕业论文第3章和第4章的实验体系，避免当前单一12-casebenchmark同时支撑两个章节导致实验范围过窄、章节贡献边界不清的问题。

## 1. 总体目标

当前只有一个12-case真实任务benchmark，同时被第3章和第4章使用。该设计存在三个问题：

- 第3章的系统评测样本量过小，难以支撑“多智能体仿真工作流具有较广泛任务适应性”的结论。
- 第4章的自进化实验与第3章评测使用同一benchmark，章节之间的因果链条不够清楚。
- 如果第4章技能从该12-case失败证据中提取，再用同一12-case评测技能效果，会产生测试集泄漏风险。

新的实验体系应拆分为两个benchmark：

1. 第3章使用大型tutorial modification benchmark。该benchmark从blastFoam/OpenFOAMtutorial中抽取典型参考算例，构造约150个修改任务，覆盖简单、中等和困难难度，用于评估第3章多智能体工作流的基础能力、覆盖面和失败模式。
2. 第4章使用当前真实12-casebenchmark。该benchmark定位为真实使用过程模拟，用于检验从第3章失败经验中沉淀出的技能是否能提升真实复杂任务中的严格通过率、终态一致性、报告质量和可审查性。

最终论文叙事应调整为：

- 第3章：构建并评估一个覆盖面较大的OpenFOAM/blastFoam修改任务benchmark，证明系统在可控tutorial迁移任务上的基础能力，并暴露失败模式。
- 第4章：基于第3章失败证据进行经验抽取、技能沉淀和技能注入，在真实任务benchmark上检验自进化机制的作用。

## 2. 关键目录

后续agent应优先在以下目录工作：

| 用途 | 路径 |
|---|---|
| 第3章评测结果根目录 | `/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/` |
| 第3章系统源码 | `/data/graduation-projects/PrincipiaBlastFoam/` |
| 第4章自进化项目 | `/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/` |
| 第4章实验结果根目录 | `/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/results/` |
| blastFoam源码与tutorial | `/data/OpenFOAM/blastfoam/` |
| 补充tutorial材料 | `/data/graduation-projects/blastFoam_tutorials/` |
| 历史工作流输出 | `/data/PrincipiaBlastFoam_output/` |
| 毕业论文和答辩材料 | `/data/graduation-docs/` |

注意：

- 不要把`/data/PrincipiaBlastFoam_output/`当作可维护源码目录。它主要用于诊断、复盘和取证。
- 第3章benchmark、评分脚本和结果应优先放在`experiment_results/chapter3_end_to_end_evaluation/`下，保持对原始系统代码的黑盒评测边界。
- 第4章技能沉淀、技能检索、技能注入和消融评测应优先放在`PrincipiaBlastFoam-SelfEvolution/`下。

## 3. 实验体系重构原则

### 3.1 第3章benchmark定位

第3章benchmark应定位为“tutorial驱动的大规模修改任务评测”。它不是纯真实应用案例，而是从已有教程算例中系统构造的任务集，用于评估工作流是否能完成常见算例修改、配置迁移、后处理设置和短时执行验证。

第3章应重点回答：

- 系统能否理解自然语言修改任务并定位到正确算例和配置文件？
- 系统能否完成简单参数修改、多文件一致性修改和复杂后处理配置？
- 系统在不同难度、不同任务类型、不同参考tutorial上的成功率如何？
- 失败主要来自需求理解、文件修改、物理约束、OpenFOAM字典语法、求解执行、后处理还是报告审查？

### 3.2 第4章benchmark定位

第4章benchmark应定位为“真实使用过程模拟”。当前12-casebenchmark可以继续使用，但角色应从第3章主评测集调整为第4章真实任务扩展评测集。

第4章应重点回答：

- 从第3章失败证据中抽取的技能是否能迁移到更真实、更综合的仿真任务？
- 抽象技能和具体验证技能在真实任务中分别带来什么收益和风险？
- 自进化机制是否改善严格通过率、报告质量、终态一致性和可审查性？
- 哪些失败模式仍不能被现有技能覆盖？

### 3.3 数据泄漏控制

必须避免把第4章真实12-casebenchmark既作为技能来源又作为最终测试集。

推荐执行方式：

1. 用第3章tutorial modification benchmark运行第3章系统。
2. 从第3章失败结果中抽取技能。
3. 冻结技能库。
4. 在第4章真实12-casebenchmark上运行no-skill、abstract-skill和concrete-verifier-skill三组对比。

如果由于时间限制必须复用已有技能库，需要在报告中明确标注该结果为“诊断性消融实验”，不能强行表述为严格泛化评测。

## 4. 第3章大型Tutorial Modification Benchmark设计

### 4.1 目标规模

目标构造约150个修改任务。允许范围为140到160个，但最终论文表格建议固定为一个清晰数字，例如150个。

推荐难度分布：

| 难度 | 建议数量 | 比例 | 任务特征 |
|---|---:|---:|---|
| 简单 | 50 | 33.3% | 单文件、单参数修改，主要检查定位和基础编辑能力 |
| 中等 | 65 | 43.3% | 多文件一致性修改，涉及控制参数、物性参数、边界条件或后处理联动 |
| 困难 | 35 | 23.3% | 涉及几何、patch命名、复杂后处理、反应/颗粒/耦合、多约束一致性 |

如果实际tutorial覆盖不足，可以调整为简单55、中等60、困难35，但必须在`dataset_coverage`报告中解释。

### 4.2 参考tutorial选择原则

从tutorial中选择具有代表性的源算例，不要求覆盖所有tutorial，但要覆盖典型物理场景和典型求解器特征。

优先选择以下类型：

- 激波管和一维验证问题：用于时间控制、网格分辨率、数值格式和验证报告任务。
- 自由场爆炸和地面爆炸：用于炸药当量、测点、缩比距离、压力历史和冲击波传播任务。
- 建筑物外爆和绕射：用于patch、建筑外表面压力、遮挡效应和探针网格任务。
- 内部爆炸和通风泄爆：用于封闭空间、开口边界、内部测点和压力释放任务。
- 多装药或延迟起爆：用于多源初始化、时间延迟、场初始化一致性任务。
- 反应流或颗粒任务：用于物性、相模型、反应参数和颗粒耦合任务。
- FSI或固体耦合相关tutorial：仅在现有工作流能较稳定处理时纳入困难子集，否则只作为扩展候选。

后续agent应先扫描以下位置：

```text
/data/OpenFOAM/blastfoam/
/data/graduation-projects/blastFoam_tutorials/
/data/graduation-projects/PrincipiaBlastFoam/data/cases_description/
/data/graduation-projects/PrincipiaBlastFoam/data/knowledge_graph/case_content_bundles/
```

### 4.3 任务类型覆盖

150个任务应覆盖以下类别。每类至少应有若干样本，不要让benchmark被单一时间控制或单一物性修改主导。

| 类别 | 建议数量 | 说明 |
|---|---:|---|
| 时间控制与输出控制 | 15 | 结束时间、时间步长、输出间隔、写出控制 |
| 网格与几何尺度 | 15 | 网格分辨率、区域尺寸、建筑尺寸、障碍物尺度 |
| 边界条件与patch一致性 | 18 | 入口/出口、墙面、对称面、patch名称一致性 |
| 装药与初始条件 | 18 | 炸药质量、位置、半径、起爆时间、多装药配置 |
| 物性与模型参数 | 12 | 气体参数、湍流/反应/颗粒参数 |
| 数值格式与求解控制 | 12 | 离散格式、残差阈值、线性求解器设置 |
| 探针和函数对象 | 20 | 压力测点、测线、测点网格、场极值、采样频率 |
| 后处理与报告 | 15 | 结果摘要、压力峰值、冲量、限制说明、审查报告 |
| 多文件一致性任务 | 15 | 同时修改控制文件、物性文件、网格和后处理配置 |
| 高风险复杂任务 | 10 | 复杂建筑、内部爆炸、通风、耦合或困难失败模式 |

类别数量可以微调，但最终应输出覆盖统计并解释偏差。

### 4.4 Benchmark数据结构

建议创建主benchmark文件：

```text
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/data/chapter3_tutorial_modification_benchmark.json
```

建议同时输出CSV和Markdown摘要：

```text
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/data/chapter3_tutorial_modification_benchmark.csv
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/data/chapter3_tutorial_modification_benchmark_summary.md
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/data/tutorial_case_manifest.json
```

每条benchmark记录建议包含以下字段：

```json
{
  "case_id": "unique_snake_case_id",
  "benchmark": "chapter3_tutorial_modification",
  "source_tutorial": "relative/or/absolute/source/case/path",
  "source_case_name": "blastFoam_freeField",
  "solver_family": "blastFoam",
  "physics_scenario": "free_field_blast",
  "difficulty": "simple|medium|hard",
  "task_category": "time_control|mesh|boundary|charge|numerics|probe|postprocessing|multi_file|complex",
  "task_prompt_zh": "自然语言修改任务",
  "expected_files": [
    "system/controlDict",
    "constant/...",
    "system/..."
  ],
  "expected_change_summary": [
    "需要修改的参数或配置行为",
    "需要保持一致的物理或数值约束"
  ],
  "must_not_change": [
    "不应改变的求解器类型或基础物理场景"
  ],
  "validation_checks": [
    {
      "type": "file_contains",
      "target": "system/controlDict",
      "expectation": "contains updated end time"
    },
    {
      "type": "openfoam_dictionary_parse",
      "target": "system/controlDict"
    }
  ],
  "requires_execution": false,
  "execution_tier": "none|syntax|short_run|representative_full",
  "expected_runtime_seconds": 0,
  "scoring_weights": {
    "requirement_satisfaction": 0.30,
    "file_edit_correctness": 0.25,
    "physical_consistency": 0.15,
    "execution_readiness": 0.15,
    "report_quality": 0.15
  },
  "tags": [
    "tutorial_derived",
    "single_file",
    "probe_pressure"
  ],
  "leakage_group": "chapter3_train_candidate"
}
```

字段说明：

- `case_id`必须全局唯一，建议包含源场景、任务类别和难度信息。
- `difficulty`只能使用`simple`、`medium`、`hard`三类。
- `task_prompt_zh`应模拟用户自然语言，但不能含有答案式文件路径提示，除非该任务本身是文件级修改评测。
- `expected_files`用于自动评分，不应直接暴露给被测工作流。
- `validation_checks`应尽量可自动执行，避免完全依赖人工阅读。
- `requires_execution`用于区分是否需要真实求解运行。
- `execution_tier`用于控制成本。150个任务不应全部做完整求解。
- `leakage_group`用于后续划分技能来源和测试集，防止第4章泄漏。

### 4.5 样例任务

简单任务样例：

```json
{
  "case_id": "free_field_end_time_simple_001",
  "benchmark": "chapter3_tutorial_modification",
  "source_case_name": "blastFoam_freeField",
  "solver_family": "blastFoam",
  "physics_scenario": "free_field_blast",
  "difficulty": "simple",
  "task_category": "time_control",
  "task_prompt_zh": "将该自由场爆炸算例调整为更短的烟雾测试，只运行到0.001s，并保持原有输出字段不变。",
  "expected_files": ["system/controlDict"],
  "expected_change_summary": [
    "结束时间应调整为0.001s",
    "不应改变求解器和主要物理模型"
  ],
  "validation_checks": [
    {"type": "dictionary_value", "target": "system/controlDict", "key": "endTime", "expected": 0.001}
  ],
  "requires_execution": false,
  "execution_tier": "syntax",
  "expected_runtime_seconds": 0,
  "tags": ["simple", "time_control", "single_file"]
}
```

中等任务样例：

```json
{
  "case_id": "building_facade_probe_medium_001",
  "benchmark": "chapter3_tutorial_modification",
  "source_case_name": "blastFoam_building3D",
  "solver_family": "blastFoam",
  "physics_scenario": "building_external_blast",
  "difficulty": "medium",
  "task_category": "probe",
  "task_prompt_zh": "在建筑迎爆面布置三个压力测点，输出压力随时间变化，并保证测点位置位于计算域内部或有效边界附近。",
  "expected_files": ["system/controlDict"],
  "expected_change_summary": [
    "应增加压力采样设置",
    "测点坐标应与建筑几何和计算域范围一致",
    "采样设置不应引入OpenFOAM字典语法错误"
  ],
  "validation_checks": [
    {"type": "function_object_present", "target": "system/controlDict", "field": "p"},
    {"type": "probe_count_min", "expected": 3},
    {"type": "openfoam_dictionary_parse", "target": "system/controlDict"}
  ],
  "requires_execution": true,
  "execution_tier": "short_run",
  "expected_runtime_seconds": 180,
  "tags": ["medium", "probe", "building", "postprocessing"]
}
```

困难任务样例：

```json
{
  "case_id": "internal_vented_blast_multifile_hard_001",
  "benchmark": "chapter3_tutorial_modification",
  "source_case_name": "blastFoam_internalDetonation_withObstacleAndGlass",
  "solver_family": "blastFoam",
  "physics_scenario": "internal_vented_blast",
  "difficulty": "hard",
  "task_category": "multi_file",
  "task_prompt_zh": "将内部爆炸算例改造成带通风开口的短时压力释放测试，保留障碍物影响，输出房间中心和开口附近压力历史，并生成简短审查报告。",
  "expected_files": [
    "system/controlDict",
    "constant/...",
    "system/..."
  ],
  "expected_change_summary": [
    "开口边界、内部墙面和障碍物边界应保持命名一致",
    "后处理测点应与内部空间和通风开口位置匹配",
    "报告应说明该任务是短时近似测试而非完整工程复现"
  ],
  "validation_checks": [
    {"type": "patch_name_consistency"},
    {"type": "probe_location_validity"},
    {"type": "openfoam_dictionary_parse"},
    {"type": "non_placeholder_report"}
  ],
  "requires_execution": true,
  "execution_tier": "representative_full",
  "expected_runtime_seconds": 900,
  "tags": ["hard", "internal_blast", "venting", "multi_file", "report_contract"]
}
```

## 5. 第3章Benchmark构建任务

### Work Package 1：扫描tutorial并建立源算例清单

目标：

建立`tutorial_case_manifest.json`，记录可用于benchmark构造的tutorial源算例。

建议脚本：

```text
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/scripts/build_tutorial_case_manifest.py
```

输入来源：

- `/data/OpenFOAM/blastfoam/`
- `/data/graduation-projects/blastFoam_tutorials/`
- `/data/graduation-projects/PrincipiaBlastFoam/data/cases_description/`
- `/data/graduation-projects/PrincipiaBlastFoam/data/knowledge_graph/case_content_bundles/`

输出：

```text
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/data/tutorial_case_manifest.json
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/data/tutorial_case_manifest_summary.md
```

每个源算例至少记录：

- case名称
- 绝对路径或相对路径
- 求解器类型
- 物理场景
- 维度或几何复杂度
- 关键配置文件是否存在
- 是否含后处理设置
- 预计运行成本
- 适合生成哪些任务类别
- 是否建议纳入150任务benchmark

验收标准：

- 至少识别20个候选源算例。
- 至少覆盖5类物理场景。
- 至少覆盖简单、中等、困难三类任务所需的源算例。
- Markdown摘要中说明最终选择和排除的理由。

### Work Package 2：生成150个修改任务

目标：

基于源算例清单构造`chapter3_tutorial_modification_benchmark.json`。

建议脚本：

```text
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/scripts/build_chapter3_tutorial_modification_benchmark.py
```

输出：

```text
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/data/chapter3_tutorial_modification_benchmark.json
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/data/chapter3_tutorial_modification_benchmark.csv
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/data/chapter3_tutorial_modification_benchmark_summary.md
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/data/chapter3_tutorial_modification_benchmark_schema.json
```

生成策略：

- 优先使用程序化模板生成初稿。
- 对困难任务进行人工或agent复核，避免任务不物理、不合理或无法验证。
- 每个任务必须有可评分依据，不能只有自然语言描述。
- 每个任务必须标注是否需要执行求解。

验收标准：

- 总数在140到160之间，目标为150。
- 简单、中等、困难三类数量接近预设比例。
- 每类任务至少有5个样本，主要类别应达到10个以上。
- `case_id`无重复。
- 每条记录包含必要字段。
- 每条记录有至少1个自动验证项。
- 输出覆盖统计，包括难度、任务类别、源算例、求解器、是否执行求解。

### Work Package 3：实现benchmark静态校验

目标：

在正式评测前检查benchmark质量，避免无效任务污染第3章结果。

建议脚本：

```text
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/scripts/validate_chapter3_tutorial_benchmark.py
```

检查项：

- JSON格式合法。
- 必要字段齐全。
- `case_id`唯一。
- 难度枚举合法。
- 源算例路径存在或有明确引用说明。
- `expected_files`不为空。
- `validation_checks`不为空。
- `requires_execution`和`execution_tier`一致。
- 困难任务不应过度集中在单一源算例。
- 不应把当前第4章真实12-case作为第3章tutorialbenchmark来源。

输出：

```text
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/data/chapter3_tutorial_modification_benchmark_validation.json
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/data/chapter3_tutorial_modification_benchmark_validation.md
```

验收标准：

- 没有blocking级别错误。
- 若存在warning，必须在Markdown中说明是否接受。

## 6. 第3章评测执行设计

### 6.1 分层评测，不建议150个全部完整求解

150个任务如果全部执行完整OpenFOAM求解，成本过高且失败解释会变得混乱。建议使用三层评测：

| 层级 | 覆盖数量 | 目标 | 验证方式 |
|---|---:|---|---|
| A层：配置与静态验证 | 全部约150个 | 检查自然语言理解、文件修改、字典语法和物理一致性 | 自动评分，不要求完整求解 |
| B层：短时执行验证 | 30到50个 | 检查生成算例能否短时启动并产出基本日志 | 缩短结束时间，设置超时 |
| C层：代表性完整链路验证 | 10到15个 | 检查完整端到端流程、后处理和报告审查 | 完整workflow与人工/自动复核结合 |

论文中第3章主表可以报告A层全量结果，同时用B层和C层说明执行层可靠性。

### 6.2 评分维度

建议第3章tutorialbenchmark使用以下评分维度：

| 维度 | 建议权重 | 含义 |
|---|---:|---|
| 需求满足度 | 0.30 | 是否完成用户要求的核心修改 |
| 文件修改正确性 | 0.25 | 是否改对文件、参数和位置 |
| 物理与数值一致性 | 0.15 | 是否保持基本物理合理性和数值稳定约束 |
| 执行准备度 | 0.15 | 字典语法、路径、patch、函数对象是否可被OpenFOAM接受 |
| 报告质量 | 0.15 | 是否生成非占位、可审查、说明限制条件的报告 |

对于B层和C层，可增加或强化以下指标：

- 求解器是否正常启动。
- 求解器是否正常结束。
- 是否出现阻塞性OpenFOAM错误。
- 后处理文件是否存在且非空。
- 报告是否引用实际运行证据。

### 6.3 建议评测脚本

可以扩展现有第3章评测器，也可以新建脚本。为降低风险，建议新建面向tutorialbenchmark的评测入口，保留原有12-case评测脚本。

建议脚本：

```text
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/scripts/run_chapter3_tutorial_modification_evaluation.py
```

建议参数：

```bash
/data/miniconda3/bin/python scripts/run_chapter3_tutorial_modification_evaluation.py \
  --benchmark-file data/chapter3_tutorial_modification_benchmark.json \
  --results-dir results/chapter3_tutorial_modification_eval_<timestamp> \
  --tier all \
  --run-as-user openfoam \
  --workflow-timeout 900 \
  --benchmark-runner-timeout 36000
```

建议支持参数：

- `--tier static|short_run|representative_full|all`
- `--limit N`
- `--difficulty simple,medium,hard`
- `--category probe,time_control,...`
- `--case-ids id1,id2`
- `--no-include-history`
- `--cleanup-final`和`--no-cleanup-final`
- `--run-as-user openfoam`
- `--workflow-timeout`
- `--benchmark-runner-timeout`

输出：

```text
results/chapter3_tutorial_modification_eval_<timestamp>/
  benchmark_runner_invocation.json
  chapter3_tutorial_case_scores.csv
  chapter3_tutorial_case_scores.json
  chapter3_tutorial_evaluation_results.json
  chapter3_tutorial_evaluation_summary.md
  chapter3_tutorial_failure_taxonomy.csv
  chapter3_tutorial_failure_taxonomy.json
  chapter3_tutorial_failure_taxonomy_summary.md
  dataset_coverage.json
  logs/
  raw_runs/
```

验收标准：

- 至少完成A层全量约150个任务评分。
- 至少完成B层30个以上短时执行任务。
- 如果时间允许，完成C层10个以上代表性完整链路任务。
- 结果文件包含完整覆盖统计和失败分类。

## 7. 第3章论文产物要求

第3章最终应生成以下论文可用文件：

```text
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/reports/chapter3_tutorial_benchmark_design.md
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/reports/chapter3_tutorial_benchmark_results.md
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/reports/chapter3_failure_mode_analysis.md
```

报告内容至少包括：

- benchmark构建依据。
- 源tutorial覆盖情况。
- 任务难度分布。
- 任务类别分布。
- 评分指标与权重。
- 全量A层结果。
- B层短时执行结果。
- C层代表性完整链路结果。
- 分难度成功率。
- 分任务类型成功率。
- 主要失败模式。
- 第4章技能沉淀所需的失败证据摘要。

建议论文结论边界：

- 可以说第3章系统在大规模tutorial修改任务中展示了基础自动化能力。
- 可以说失败模式为第4章技能自进化提供了经验来源。
- 不要声称第3章已经覆盖真实工程复杂度。真实复杂任务应交给第4章benchmark表述。

## 8. 第4章真实Benchmark重定位

### 8.1 当前12-casebenchmark的角色

当前12-casebenchmark应作为第4章真实使用模拟benchmark。它不是第3章主benchmark，而是第4章扩展评测集。

建议创建或确认第4章canonical benchmark文件：

```text
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/benchmarks/chapter4_realistic_application_benchmark.json
```

该文件可以从当前12-case定义复制或引用，但需要在说明文档中明确其定位：

- 来源于真实爆炸安全、建筑冲击波、内部爆炸、遮挡绕射、压力测点和后处理需求。
- 任务数量较少，但复杂度高。
- 目标是模拟真实用户请求，而不是覆盖所有tutorial修改类型。
- 用于检验技能自进化后的真实任务迁移效果。

建议同时生成说明：

```text
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/benchmarks/chapter4_realistic_application_benchmark_readme.md
```

### 8.2 第4章技能来源

第4章技能应优先从第3章tutorialbenchmark失败结果中提取。

建议新增技能生成流程：

```text
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/scripts/ingest_chapter3_tutorial_failures.py
```

输入：

```text
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/results/chapter3_tutorial_modification_eval_<timestamp>/chapter3_tutorial_evaluation_results.json
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/results/chapter3_tutorial_modification_eval_<timestamp>/chapter3_tutorial_failure_taxonomy.json
```

输出：

```text
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/skills/chapter3_tutorial_concrete_skill_library.json
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/skills/chapter3_tutorial_concrete_skill_library.md
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/skills/chapter3_tutorial_abstract_skill_library.json
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/skills/chapter3_tutorial_abstract_skill_library.md
```

技能字段建议：

- 技能编号。
- 技能标题。
- 来源失败任务。
- 触发条件。
- 适用任务类型。
- 操作建议。
- 验证条件。
- 证据来源。
- 不适用条件。
- 可能副作用。

### 8.3 第4章消融实验设计

在真实12-casebenchmark上至少运行三组：

1. no-skill：不注入第4章技能。
2. abstract-skill：注入从第3章失败中抽象得到的技能。
3. concrete-verifier-skill：注入带验证条件的具体技能。

如果已有旧结果来自12-case自身失败经验，应将其归类为历史诊断结果。新的论文主结果应尽量使用从第3章tutorialbenchmark生成的技能库重新运行。

建议结果目录：

```text
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/results/e2e_ablation/chapter4_realistic_no_skill_<timestamp>/
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/results/e2e_ablation/chapter4_realistic_abstract_from_chapter3_<timestamp>/
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/results/e2e_ablation/chapter4_realistic_concrete_from_chapter3_<timestamp>/
```

输出对比文件：

```text
comparison/chapter4_realistic_three_way_comparison.md
comparison/chapter4_realistic_three_way_comparison.json
comparison/chapter4_realistic_case_comparison.csv
comparison/chapter4_realistic_error_taxonomy.csv
comparison/chapter4_realistic_error_taxonomy_summary.md
comparison/chapter4_final_realistic_benchmark_conclusion.md
```

第4章指标：

- 严格通过率。
- 核心执行通过率。
- 求解器正常结束数。
- 工作流终态不一致数。
- 产物不完整数。
- 非占位报告齐备数。
- 报告质量。
- 平均总分。
- 错误类型变化。
- 与第3章失败技能来源之间的对应关系。

## 9. 结果保留与清理规则

用户明确要求：每次有新的实验结果，就删除旧的实验结果。

执行规则如下：

1. 新结果生成后，先验证结果完整性。
2. 完整性验证通过后，再删除同类型旧结果目录。
3. 不删除源码、benchmark定义、脚本、技能库和最终论文报告。
4. 不删除仍作为对照组使用的最新结果。
5. 删除前必须确认同类型目录范围，避免误删第3章和第4章互相依赖的结果。

推荐保留规则：

| 类型 | 保留内容 |
|---|---|
| 第3章tutorialbenchmark数据 | 永久保留最新benchmark定义、schema、manifest和summary |
| 第3章tutorial评测结果 | 只保留最新完整run |
| 第4章真实benchmark定义 | 永久保留canonical benchmark |
| 第4章no-skill结果 | 只保留最新完整run |
| 第4章abstract-skill结果 | 只保留最新完整run |
| 第4章concrete-verifier结果 | 只保留最新完整run |
| 技能抽象评测结果 | 只保留最新完整run |
| comparison和论文结论 | 保留与最新run绑定的版本 |

建议维护索引文件：

```text
/data/graduation-projects/experiment_results/CURRENT_EXPERIMENT_RESULTS.md
```

该文件记录当前有效结果：

- 第3章tutorialbenchmark最新结果路径。
- 第4章真实benchmark最新no-skill结果路径。
- 第4章真实benchmark最新abstract-skill结果路径。
- 第4章真实benchmark最新concrete-verifier结果路径。
- 当前用于论文表格的主结果路径。
- 已删除旧结果的简要记录。

## 10. 推荐执行顺序

后续agent应按以下顺序执行，避免先跑昂贵实验再发现benchmark设计问题。

### 阶段1：准备与审计

1. 阅读本文件。
2. 阅读第3章结果目录README。
3. 阅读第4章项目README。
4. 阅读现有第3章评测脚本。
5. 阅读现有第4章消融脚本。
6. 确认当前12-casebenchmark定义和最新结果路径。
7. 确认tutorial源目录和可用case数量。

验收：

- 形成一份简短审计记录，说明哪些脚本可复用、哪些需要新增。

### 阶段2：构建tutorial源算例manifest

1. 扫描tutorial源目录。
2. 提取求解器、场景、关键配置文件、后处理信息。
3. 给每个源算例打标签。
4. 输出manifest和summary。

验收：

- 至少20个候选源算例。
- 场景和求解器覆盖统计完整。

### 阶段3：构建150个tutorial修改任务

1. 按难度和任务类别生成任务。
2. 对困难任务做复核。
3. 输出JSON、CSV、schema和summary。
4. 运行benchmark静态校验。

验收：

- 约150条任务。
- schema校验通过。
- 覆盖统计满足预设要求。

### 阶段4：实现第3章评测器或适配现有评测器

1. 支持A层静态评分。
2. 支持B层短时执行评分。
3. 支持C层代表性完整链路评分。
4. 支持按难度、类别、case id过滤。
5. 支持结果清理和不混入历史结果。

验收：

- 小样本dry run通过。
- 10个case试运行能生成评分JSON、CSV和Markdown摘要。

### 阶段5：运行第3章大型benchmark

1. 先跑A层全量。
2. 再跑B层30到50个短时执行任务。
3. 最后跑C层10到15个代表性完整链路任务。
4. 汇总结果和失败分类。

验收：

- 最新第3章tutorialbenchmark结果完整。
- 旧同类型第3章结果按规则清理。
- 报告能支撑第3章论文表格。

### 阶段6：从第3章失败中生成第4章技能

1. 读取第3章失败分类。
2. 抽取具体验证技能。
3. 抽象为可迁移技能。
4. 生成技能库JSON和Markdown。
5. 运行技能检索/抽象质量评测。

验收：

- 技能来源只来自第3章tutorialbenchmark结果，或明确标注例外。
- 每条技能有触发条件、操作建议和验证条件。

### 阶段7：运行第4章真实12-casebenchmark

1. 固化第4章真实benchmark定义。
2. 跑no-skill组。
3. 跑abstract-skill组。
4. 跑concrete-verifier-skill组。
5. 生成三组对比和错误分类。

验收：

- 三组均为12-case完整结果。
- 输出strict pass、core execution、solver clean end、workflow mismatch、artifact completeness、report quality。
- 旧同类型第4章结果按规则清理。

### 阶段8：生成论文结论

1. 写第3章benchmark设计与结果报告。
2. 写第3章失败模式分析。
3. 写第4章真实benchmark消融结果。
4. 写第4章自进化机制结论与局限。
5. 更新当前有效结果索引。

验收：

- 第3章和第4章的benchmark角色清楚区分。
- 不存在“同一12-case同时证明两个章节主要贡献”的问题。
- 第4章结论没有过度声称全面提升。

## 11. 最终交付物清单

### 第3章数据与脚本

```text
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/data/tutorial_case_manifest.json
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/data/tutorial_case_manifest_summary.md
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/data/chapter3_tutorial_modification_benchmark.json
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/data/chapter3_tutorial_modification_benchmark.csv
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/data/chapter3_tutorial_modification_benchmark_schema.json
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/data/chapter3_tutorial_modification_benchmark_summary.md
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/scripts/build_tutorial_case_manifest.py
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/scripts/build_chapter3_tutorial_modification_benchmark.py
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/scripts/validate_chapter3_tutorial_benchmark.py
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/scripts/run_chapter3_tutorial_modification_evaluation.py
```

### 第3章结果与报告

```text
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/results/chapter3_tutorial_modification_eval_<timestamp>/
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/reports/chapter3_tutorial_benchmark_design.md
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/reports/chapter3_tutorial_benchmark_results.md
/data/graduation-projects/experiment_results/chapter3_end_to_end_evaluation/reports/chapter3_failure_mode_analysis.md
```

### 第4章benchmark与技能

```text
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/benchmarks/chapter4_realistic_application_benchmark.json
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/benchmarks/chapter4_realistic_application_benchmark_readme.md
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/scripts/ingest_chapter3_tutorial_failures.py
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/skills/chapter3_tutorial_concrete_skill_library.json
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/skills/chapter3_tutorial_concrete_skill_library.md
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/skills/chapter3_tutorial_abstract_skill_library.json
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/skills/chapter3_tutorial_abstract_skill_library.md
```

### 第4章结果与报告

```text
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/results/e2e_ablation/chapter4_realistic_no_skill_<timestamp>/
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/results/e2e_ablation/chapter4_realistic_abstract_from_chapter3_<timestamp>/
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/results/e2e_ablation/chapter4_realistic_concrete_from_chapter3_<timestamp>/
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/results/reports/chapter4_realistic_benchmark_ablation.md
/data/graduation-projects/PrincipiaBlastFoam-SelfEvolution/results/reports/chapter4_self_evolution_final_conclusion.md
```

### 全局索引

```text
/data/graduation-projects/experiment_results/CURRENT_EXPERIMENT_RESULTS.md
```

## 12. 论文表述建议

第3章建议表述：

本章基于blastFoam/OpenFOAMtutorial构建了覆盖简单、中等和困难任务的大规模修改任务benchmark。该benchmark用于评估多智能体工作流在算例选择、配置修改、物理一致性检查、后处理设置和报告生成方面的基础能力。实验结果用于揭示系统在不同任务类型下的成功率和主要失败模式，并为第4章技能自进化提供经验来源。

第4章建议表述：

本章将第3章评测中暴露的失败模式转化为结构化技能，并在真实应用导向的12-casebenchmark上进行消融实验。与第3章tutorialbenchmark不同，该benchmark强调真实用户任务中的复杂几何、压力测点、内部爆炸、建筑绕射和报告审查需求。实验重点不只是严格通过率，还包括终态一致性、产物完整性和报告可审查性。

不建议表述：

- 不要说第4章方法已经全面提升所有端到端指标，除非结果确实支持。
- 不要把12-case真实benchmark描述为第3章主评测集。
- 不要把从12-case自身提取的技能再在同一12-case上作为严格泛化证据。
- 不要只报告平均分，应同时报告失败类型和case级变化。

## 13. 风险与处理建议

| 风险 | 影响 | 处理建议 |
|---|---|---|
| 150个任务生成质量不均 | 第3章结论不稳 | 加schema校验和人工/agent复核困难任务 |
| 全量求解成本过高 | 实验时间不可控 | 使用A/B/C三层评测，不全部完整求解 |
| 第4章测试集泄漏 | 泛化结论不成立 | 技能来源限定为第3章tutorialbenchmark失败 |
| 旧结果未清理 | 结果目录混乱 | 新结果验证后删除同类型旧run，并更新索引 |
| 复杂任务失败率高 | 结果看起来偏弱 | 如实报告失败模式，用第4章说明改进方向 |
| 修改主系统引入新变量 | 消融对比不公平 | 优先黑盒评测，不轻易改PrincipiaBlastFoam主workflow |

## 14. 最小成功标准

如果时间有限，至少完成以下内容：

1. 构建并校验约150条第3章tutorial modification benchmark。
2. 完成第3章A层全量静态评测。
3. 完成第3章B层至少30条短时执行评测。
4. 从第3章失败中生成一版技能库。
5. 在第4章真实12-casebenchmark上完成至少no-skill和concrete-verifier-skill两组对比。
6. 生成第3章结果报告、第4章消融报告和当前结果索引。

完整成功标准：

1. 第3章150任务benchmark构建、校验、全量静态评测和分层执行评测全部完成。
2. 第3章失败模式被结构化分类，并能作为第4章技能来源。
3. 第4章三组12-case消融实验完成。
4. 新旧结果按规则清理，只保留最新有效结果。
5. 论文结论清楚地区分第3章基础系统能力和第4章自进化能力。

## 15. 给后续agent的执行提醒

- 先读README和现有脚本，不要盲目重写已有评测器。
- 先构建数据和校验器，再跑昂贵实验。
- 每个benchmark任务必须可评分，不能只有自然语言prompt。
- 第3章主结果应来自tutorial modification benchmark。
- 第4章主结果应来自真实12-casebenchmark。
- 新结果完整后再删除旧结果。
- 删除前确认同类型范围，不能删除仍作为对照组的最新结果。
- 报告中要如实写负面结果，特别是核心执行通过率下降、超时、产物不完整和报告占位问题。
- 最终结论必须服务于论文逻辑：第3章暴露问题，第4章利用问题进行自进化改进。
