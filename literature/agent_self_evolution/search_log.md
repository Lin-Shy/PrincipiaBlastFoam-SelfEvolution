# 检索记录

## 日期

- 2026-06-06

## 检索目标

围绕 `agent 自进化 / self-evolving agents`、`skill library / skill lifecycle / skill curation`、`trajectory learning / execution traces`、`reflection / experiential learning`、`agent memory`、`test-time learning / self-training` 进行广泛召回，优先保留论文一手页面。

## 数据源

- OpenAlex API：使用 `LLM agent self evolution reflection skill learning trajectory`、`language agent skill library lifelong learning Voyager Reflexion ExpeL`、`LLM agent trajectory learning tool use web navigation self improvement`、`autonomous agent memory reflection planning large language models` 等查询，原始 JSON 存在 `data/openalex/`。
- arXiv 页面与搜索：校验核心 arXiv ID、提交日期、标题、摘要和 DOI。
- OpenReview：补充 2025-2026 年 workshop/ARR/MLSys 等最新 agent 自改进论文。
- ACL Anthology / NeurIPS Proceedings / Springer / Microsoft Research：补充已发表论文和项目页。

## 检索式示例

- `LLM agents self-evolution skill library trajectory learning paper 2025`
- `site:arxiv.org/abs LLM agent skill library self evolution`
- `large language model agents learn skills from trajectories paper`
- `LLM agent self-improvement reflection experience paper`
- `LLM agent memory reflection experience learning MemoryBank MemGPT papers`
- `Learning to Retrieve from Agent Trajectories`
- `SkillOS Learning Skill Curation for Self-Evolving Agents`
- `Agent Skills for Large Language Models Architecture Acquisition Security`

## 质量控制

- 目录优先收录 arXiv/OpenReview/ACL/NeurIPS/Springer/ACM/Microsoft Research 等一手或准一手来源。
- 搜索结果中的博客、Hugging Face daily papers、Emergent Mind、Pith 等只作为发现线索，不作为最终证据的唯一来源。
- 2026 年大量条目仍是预印本或 workshop 稿，综述中单独标注为“快速发展/待复核”。

## 工具限制

- 本地未安装 `parallel-cli` 和 `jq`，因此没有使用 literature-review 技能推荐的 parallel-web 流程。
- Semantic Scholar 公共接口触发 429 限流，未作为主要数据源。
- `scientific-schematics` 需要 `OPENROUTER_API_KEY`，当前环境未设置；本资料包先提供 Mermaid 图，未生成 AI 位图示意图。
