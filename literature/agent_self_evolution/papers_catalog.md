# Agent 自进化、技能沉淀与轨迹学习论文目录

- 生成日期：2026-06-06
- 手工种子论文：91 篇
- 说明：`status=preprint/workshop/project` 的条目适合继续跟踪，不应与已发表会议/期刊论文等量看待。

## 主题统计

- 评测、轨迹审计与安全：17 篇
- 基础架构、推理-行动与工具使用：12 篇
- 反思、经验学习与长期记忆：11 篇
- 综述与路线图：10 篇
- 自训练、测试时学习与强化学习式自进化：10 篇
- 记忆系统与记忆管理：9 篇
- 技能沉淀、技能库与生命周期：8 篇
- 轨迹挖掘、轨迹到技能与轨迹监督：8 篇
- 代码/科学发现中的自改进 agent：6 篇

## 综述与路线图

| 年份 | 论文 | 状态 | 作用/备注 |
|---:|---|---|---|
| 2023 | [The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864) | preprint | Early broad survey of LLM agents and the move from static prompting to agent systems. |
| 2024 | [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) | peer-reviewed | LLM agent architecture overview: profile, memory, planning, action, and evaluation. |
| 2024 | [A Survey on Self-Evolution of Large Language Models](https://arxiv.org/abs/2404.14387) | preprint | Defines self-evolution as cycles of experience acquisition, refinement, updating, and evaluation. |
| 2024 | [A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13501) | peer-reviewed | Memory mechanisms from cognitive analogy, self-evolution, and applications. |
| 2025 | [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence](https://arxiv.org/abs/2507.21046) | preprint | Agent-centric taxonomy: what component evolves, when it evolves, and how feedback drives evolution. |
| 2025 | [LLM-Based Agents for Tool Learning: A Survey](https://link.springer.com/article/10.1007/s41019-025-00296-9) | peer-reviewed | Tool learning survey useful for separating tools, APIs, and higher-level reusable skills. |
| 2026 | [A Systematic Survey of Self-Evolving Agents: From Model-Centric to Environment-Driven Co-Evolution](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6626878) | preprint | Frames model-centric, environment-centric, and model-environment co-evolution. |
| 2026 | [Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward](https://arxiv.org/abs/2602.12430) | preprint | Focused survey on the emerging skill abstraction layer, MCP, acquisition, portability, and governance. |
| 2026 | [Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers](https://arxiv.org/abs/2603.07670) | preprint | Recent memory survey emphasizing consolidation, retrieval, forgetting, privacy, and engineering budgets. |
| 2026 | [SoK: Agentic Skills -- Beyond Tool Use in LLM Agents](https://arxiv.org/abs/2602.20867) | preprint | Maps skill lifecycle, representation, scope, and supply-chain/security risks. |

## 基础架构、推理-行动与工具使用

| 年份 | 论文 | 状态 | 作用/备注 |
|---:|---|---|---|
| 2021 | [WebGPT: Browser-assisted question-answering with human feedback](https://arxiv.org/abs/2112.09332) | preprint | Early browser-action trajectories and human preference feedback for web-grounded answering. |
| 2022 | [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691) | peer-reviewed | Connects language planning with executable affordances, relevant to skill feasibility checks. |
| 2022 | [Inner Monologue: Embodied Reasoning through Planning with Language Models](https://arxiv.org/abs/2207.05608) | peer-reviewed | Embodied feedback as text observations in a planning loop. |
| 2022 | [MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning](https://arxiv.org/abs/2205.00445) | preprint | Early modular view of LLMs coordinating specialized tools and symbolic components. |
| 2022 | [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) | peer-reviewed | Canonical reasoning-action-observation trajectory pattern used by many later self-improving agents. |
| 2023 | [API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs](https://arxiv.org/abs/2304.08244) | peer-reviewed | Benchmark for planning API calls and using tools over multi-turn tasks. |
| 2023 | [Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents](https://arxiv.org/abs/2302.01560) | preprint | Open-world embodied planning with feedback and selection, an important predecessor to Voyager-like agents. |
| 2023 | [Gorilla: Large Language Model Connected with Massive APIs](https://arxiv.org/abs/2305.15334) | preprint | API retrieval/calling benchmark and model training for robust tool invocation. |
| 2023 | [HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face](https://arxiv.org/abs/2303.17580) | peer-reviewed | LLM as controller over many expert models; useful for tool orchestration background. |
| 2023 | [ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](https://arxiv.org/abs/2307.16789) | preprint | Tool-use dataset, API retrieval, and decision-making benchmark. |
| 2023 | [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) | peer-reviewed | Self-supervised tool-use annotation and training, important precursor to tool/skill acquisition. |
| 2023 | [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) | peer-reviewed | Search over intermediate reasoning states; informs agent trajectory branching and reflection. |

## 反思、经验学习与长期记忆

| 年份 | 论文 | 状态 | 作用/备注 |
|---:|---|---|---|
| 2023 | [ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144) | peer-reviewed | Extracts natural-language knowledge from training experiences and reuses it on test tasks. |
| 2023 | [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) | peer-reviewed | Memory stream, reflection, and planning architecture for believable agents. |
| 2023 | [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | peer-reviewed | Stores verbal reflections in episodic memory to improve subsequent trials. |
| 2023 | [Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization](https://arxiv.org/abs/2308.02151) | peer-reviewed | Learns a retrospective model to tune agent prompts from environment feedback. |
| 2024 | [Devil's Advocate: Anticipatory Reflection for LLM Agents](https://arxiv.org/abs/2405.16334) | preprint | Uses anticipatory reflection before acting, complementing post-hoc reflection loops. |
| 2024 | [MetaReflection: Learning Instructions for Language Agents using Past Reflections](https://arxiv.org/abs/2405.13009) | preprint | Offline reinforcement learning over past reflections; turns reflections into improved instructions. |
| 2024 | [Positive Experience Reflection for Agents in Text-Based Games](https://openreview.net/pdf?id=YwqlQubiiv) | workshop/preprint | Studies learning from successful trajectories, not only failures. |
| 2024 | [Self-Reflection in LLM Agents: Effects on Problem-Solving Performance](https://arxiv.org/abs/2405.06682) | preprint | Empirical analysis of when self-reflection helps or fails. |
| 2025 | [ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://openreview.net/forum?id=jL7fwchScm) | preprint | Distills successes and failures into reasoning memory and combines it with memory-aware test-time scaling. |
| 2025 | [SAMULE: Self-Learning Agents Enhanced by Multi-level Reflection](https://aclanthology.org/2025.emnlp-main.839.pdf) | peer-reviewed | Multi-level reflection and self-learning framework; useful comparison to Reflexion/ExpeL/Retroformer. |
| 2026 | [RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback](https://arxiv.org/abs/2603.08561) | preprint | Combines numerical intrinsic feedback and language feedback for online agent evolution. |

## 记忆系统与记忆管理

| 年份 | 论文 | 状态 | 作用/备注 |
|---:|---|---|---|
| 2023 | [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) | preprint | OS-inspired memory hierarchy and explicit memory-management actions. |
| 2023 | [MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250) | preprint | Long-term memory mechanism for personalized and persistent interactions. |
| 2025 | [How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior](https://arxiv.org/abs/2505.16067) | preprint | Shows retrieval choices can strongly steer agent outputs toward prior experiences. |
| 2025 | [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) | preprint | Production-oriented long-term memory layer for agent applications. |
| 2025 | [Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning](https://arxiv.org/abs/2508.19828) | preprint | RL framework for explicit memory add/update/delete/no-op operations. |
| 2026 | [Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents](https://arxiv.org/abs/2601.01885) | preprint | Learns memory operations as tool actions using progressive RL and step-wise GRPO. |
| 2026 | [Lightweight LLM Agent Memory with Small Language Models](https://arxiv.org/abs/2604.07798) | preprint | Organizes short-, mid-, and long-term memory while reducing heavyweight LLM calls. |
| 2026 | [PlugMem: A Task-Agnostic Plugin Memory Module for LLM Agents](https://www.microsoft.com/en-us/research/publication/plugmem-a-task-agnostic-plugin-memory-module-for-llm-agents/) | preprint | Knowledge-centric memory graph for task-agnostic plugin memory. |
| 2026 | [TA-Mem: Tool-Augmented Autonomous Memory Retrieval for LLM in Long-Term Conversational QA](https://arxiv.org/abs/2603.09297) | preprint | Tool-augmented adaptive memory extraction and retrieval selection. |

## 技能沉淀、技能库与生命周期

| 年份 | 论文 | 状态 | 作用/备注 |
|---:|---|---|---|
| 2023 | [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | peer-reviewed | Automatic curriculum, iterative prompting, and an ever-growing executable skill library in Minecraft. |
| 2025 | [Reinforcement Learning for Self-Improving Agent with Skill Library](https://arxiv.org/abs/2512.17102) | preprint | Skill Augmented GRPO for self-evolution over task chains with accumulating skills. |
| 2026 | [AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution](https://arxiv.org/abs/2603.01145) | preprint | Abstracts dialogue and interaction traces into reusable, shareable, dynamically injected skills. |
| 2026 | [CoEvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification](https://arxiv.org/abs/2604.01687) | preprint | Skill generator and surrogate verifier co-evolve to create multi-file skill packages. |
| 2026 | [From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills](https://microsoft.github.io/SkillLens/) | preprint/project | Studies the experience-generation, skill-extraction, and skill-consumption lifecycle. |
| 2026 | [MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation](https://arxiv.org/abs/2605.27366) | preprint | Skill-centric lifecycle covering creation, memory, management, evaluation, and refinement. |
| 2026 | [SKILLFOUNDRY: Building Self-Evolving Agent Skill Libraries from Heterogeneous Scientific Resources](https://arxiv.org/abs/2604.03964) | preprint | Mines procedural scientific resources into validated agent skills with provenance and tests. |
| 2026 | [SkillOS: Learning Skill Curation for Self-Evolving Agents](https://arxiv.org/abs/2605.06614) | preprint | Trains a skill curator that updates an external SkillRepo from accumulated experience. |

## 轨迹挖掘、轨迹到技能与轨迹监督

| 年份 | 论文 | 状态 | 作用/备注 |
|---:|---|---|---|
| 2026 | [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://openreview.net/forum?id=TZAhZYtTn7) | preprint | Optimizes persistent/evolving contexts offline and online for agents and domain tasks. |
| 2026 | [CLEAR: Context Augmentation from Contrastive Learning of Experience via Agentic Reflection](https://arxiv.org/abs/2604.07487) | preprint | Contrastive reflection over trajectories to produce reusable task context. |
| 2026 | [ExpWeaver: LLM Agents Learn from Experience via Latent RAG](https://arxiv.org/abs/2606.01041) | preprint | Learning from experience through latent retrieval-augmented generation. |
| 2026 | [Learning to Retrieve from Agent Trajectories](https://arxiv.org/abs/2604.04949) | preprint | Mines browsing actions and reasoning traces as supervision for agent-oriented retrieval. |
| 2026 | [Retrieval-Augmented LLM Agents: Learning to Learn from Experience](https://arxiv.org/abs/2603.18272) | preprint | Compares fine-tuning and retrieval over past experience for agent generalization. |
| 2026 | [SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories](https://arxiv.org/abs/2606.01311) | preprint | Step-level failure attribution and acceptance checks for training-free skill updates. |
| 2026 | [Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills](https://arxiv.org/abs/2603.25158) | work in progress | Consolidates execution trajectories into transferable SOP-like skills without parameter updates. |
| 2026 | [Trajectory-Informed Memory Generation for Self-Improving Agent Systems](https://arxiv.org/abs/2603.10600) | preprint | Extracts strategy, recovery, and optimization tips from execution trajectories. |

## 自训练、测试时学习与强化学习式自进化

| 年份 | 论文 | 状态 | 作用/备注 |
|---:|---|---|---|
| 2023 | [ReST meets ReAct: Self-Improvement for Multi-Step Reasoning LLM Agent](https://arxiv.org/abs/2312.10003) | preprint | Iteratively trains on previous ReAct trajectories with AI feedback for self-improvement/distillation. |
| 2023 | [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) | peer-reviewed | General self-feedback/refinement loop, widely reused inside agent designs. |
| 2024 | [Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models](https://arxiv.org/abs/2401.01335) | peer-reviewed | Self-play fine-tuning with model-generated responses; model-level precursor to agent self-evolution. |
| 2024 | [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) | preprint | LLM generates and judges instruction-following data, a self-feedback training route. |
| 2025 | [Agent0: Unleashing Self-Evolving Agents from Zero Data via Tool-Integrated Reasoning](https://arxiv.org/abs/2511.16043) | preprint | Curriculum agent and executor agent co-evolve with tool-integrated reasoning. |
| 2025 | [R-Zero: Self-Evolving Reasoning LLM from Zero Data](https://arxiv.org/abs/2508.05004) | preprint | Challenger-solver co-evolution creates curriculum without existing tasks or labels. |
| 2025 | [SE-Agent: Self-Evolution Trajectory Optimization in Multi-Step Reasoning with LLM-Based Agents](https://arxiv.org/abs/2508.02085) | preprint | Trajectory optimization for multi-step reasoning agents. |
| 2025 | [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/abs/2504.16084) | preprint | Test-time RL as a model-level route toward adaptive behavior. |
| 2026 | [Confidence-Orchestrated Self-Evolution against Uncertain LLM Feedback](https://arxiv.org/abs/2605.28010) | preprint | Confidence-weighted PPO and prioritized replay to reduce damage from uncertain self-judgments. |
| 2026 | [TT-SI: Self-Improving LLM Agents with Test-Time Training](https://openreview.net/forum?id=k30IrbNYSG) | preprint | Detects uncertain samples, self-augments similar examples, and trains at test time. |

## 代码/科学发现中的自改进 agent

| 年份 | 论文 | 状态 | 作用/备注 |
|---:|---|---|---|
| 2025 | [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228) | preprint | Coding agent edits its own scaffolding and improves on SWE-bench/LiveCodeBench-style tasks. |
| 2025 | [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131) | white paper/preprint | Evolutionary coding agent driven by automated evaluators. |
| 2025 | [Mathematical exploration and discovery at scale](https://arxiv.org/abs/2511.02864) | preprint | Uses AlphaEvolve for large-scale mathematical construction discovery. |
| 2025 | [SIVA: Self-Improving Vulnerability Agent](https://openreview.net/forum?id=JDN0x8eTPm) | workshop/preprint | Memory-guided meta-learning and dynamic prompt optimization for vulnerability detection. |
| 2025 | [Scientific Algorithm Discovery by Augmenting AlphaEvolve with Deep Research](https://arxiv.org/abs/2510.06056) | preprint | Combines deep research, external knowledge retrieval, code editing, and evolutionary evaluation. |
| 2026 | [AccelOpt: A Self-Improving LLM Agentic System for AI Accelerator Kernel Optimization](https://openreview.net/forum?id=SBS4NJHYjZ) | preprint | Kernel optimization system with optimization memory and iterative self-improvement. |

## 评测、轨迹审计与安全

| 年份 | 论文 | 状态 | 作用/备注 |
|---:|---|---|---|
| 2022 | [WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://arxiv.org/abs/2207.01206) | peer-reviewed | Shopping web interaction environment widely reused in agent skill/memory evaluation. |
| 2023 | [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688) | peer-reviewed | Multi-environment benchmark for LLM-as-agent reasoning and decision-making. |
| 2023 | [GAIA: A Benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983) | peer-reviewed | Assistant benchmark that later self-improving agents use for evaluating task success. |
| 2023 | [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) | peer-reviewed | Issue-resolution benchmark that made coding-agent trajectories and regression tests central. |
| 2023 | [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854) | peer-reviewed | Realistic website environment for long-horizon web agents. |
| 2024 | [AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/hash/877b40688e330a0e2a3fc24084208dfa-Abstract-Datasets_and_Benchmarks_Track.html) | peer-reviewed | Analytical evaluation framework with progress/trajectory measures for multi-turn agents. |
| 2024 | [AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](https://arxiv.org/abs/2407.18901) | preprint | Interactive code-generation benchmark with tool/API state and realistic app tasks. |
| 2024 | [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972) | peer-reviewed | Computer-use benchmark relevant to skill packages, GUI grounding, and persistent agents. |
| 2024 | [Tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045) | preprint | Interactive user/tool benchmark for realistic service-domain agents. |
| 2025 | [AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories](https://arxiv.org/abs/2504.08942) | preprint | LLM-as-judge benchmark for trajectory success, side effects, and repetitiveness. |
| 2025 | [Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions](https://arxiv.org/abs/2507.05257) | preprint | MemoryAgentBench: retrieval, test-time learning, long-range understanding, and conflict resolution. |
| 2026 | [ATBench: A Diverse and Realistic Trajectory Benchmark for Long-Horizon Agent Safety](https://arxiv.org/abs/2604.02022) | preprint | Trajectory-level safety benchmark organized by risk source, failure mode, and harm. |
| 2026 | [BenchTrace: A Benchmark for Testing Reflection Ability and Controlled Evolution in LLM Agents](https://arxiv.org/abs/2605.29225) | preprint | Evaluates failure identification and whether past failures produce controlled avoidance behavior. |
| 2026 | [ContextBench: A Benchmark for Context Retrieval in Coding Agents](https://arxiv.org/abs/2602.05892) | preprint | Process-oriented evaluation of context retrieval in coding-agent trajectories. |
| 2026 | [EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective](https://arxiv.org/abs/2605.18421) | preprint | Evaluates in-episode/cross-episode and knowledge/execution memory for self-evolving agents. |
| 2026 | [LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues](https://arxiv.org/abs/2605.12493) | preprint | Long-term memory benchmark with trajectory-like workplace evidence. |
| 2026 | [SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks](https://www.skillsbench.ai/skillsbench.pdf) | preprint/project | Benchmark for measuring skill usefulness across diverse agent tasks. |
