# Agent Self-Evolution Literature Pack

本目录用于存放 agent 自进化、技能沉淀、经验/轨迹学习、长期记忆和相关评测的论文与综述材料。

## 目录

- `agent_self_evolution_review.md`：中文研究综述，面向第 4 章“智能体自进化/技能沉淀”写作。
- `papers_catalog.md`：按主题分类的论文目录，共 91 篇手工种子论文。
- `references.bib`：上述论文的 BibTeX 初稿，后续正式写作前建议逐条用 Crossref/DBLP/arXiv 再校对作者全名。
- `search_log.md`：检索策略、数据源和限制说明。
- `data/openalex/`：OpenAlex 原始 JSON 召回结果。
- `data/manual_seed_papers.json`：手工种子论文结构化数据。
- `data/openalex_top_titles.md`：OpenAlex 召回摘要。
- `figures/*.png`：使用外部图像 API 生成的综述配图。
- `figures/prompts.txt`：上述 PNG 配图的生成 prompt、模型和参数记录。
- `figures/*.mmd`：Mermaid 结构图，可在 Markdown 或 Mermaid CLI 中渲染，作为可编辑源图。
- `papers/`：开放获取 PDF 的存放位置；`papers/README.md` 给出建议下载清单。

## 使用建议

1. 写论文时优先引用 `papers_catalog.md` 中 `peer-reviewed` 和关键 arXiv 论文。
2. 对 2026 年新预印本保持“可用但需复核”的表述，尤其是技能库安全、技能自生成、测试时学习类工作。
3. 第 4 章可以直接借用综述中的“轨迹 -> 经验 -> 技能 -> 检索/注入 -> 验证 -> 更新”的闭环框架。
