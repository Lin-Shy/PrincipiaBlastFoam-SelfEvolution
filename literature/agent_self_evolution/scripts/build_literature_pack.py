#!/usr/bin/env python3
"""Generate the agent self-evolution literature review pack."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


PAPERS = [
    {
        "key": "wang2024autonomous_agents_survey",
        "title": "A Survey on Large Language Model based Autonomous Agents",
        "year": 2024,
        "authors": "Lei Wang et al.",
        "theme": "survey",
        "venue": "Frontiers of Computer Science / arXiv",
        "url": "https://arxiv.org/abs/2308.11432",
        "doi": "10.1007/s11704-024-40231-1",
        "status": "peer-reviewed",
        "note": "LLM agent architecture overview: profile, memory, planning, action, and evaluation.",
    },
    {
        "key": "xi2023rise_agents",
        "title": "The Rise and Potential of Large Language Model Based Agents: A Survey",
        "year": 2023,
        "authors": "Zhiheng Xi et al.",
        "theme": "survey",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2309.07864",
        "doi": "10.48550/arXiv.2309.07864",
        "status": "preprint",
        "note": "Early broad survey of LLM agents and the move from static prompting to agent systems.",
    },
    {
        "key": "tao2024self_evolution_survey",
        "title": "A Survey on Self-Evolution of Large Language Models",
        "year": 2024,
        "authors": "Zhengwei Tao et al.",
        "theme": "survey",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2404.14387",
        "doi": "10.48550/arXiv.2404.14387",
        "status": "preprint",
        "note": "Defines self-evolution as cycles of experience acquisition, refinement, updating, and evaluation.",
    },
    {
        "key": "gao2025self_evolving_agents_survey",
        "title": "A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence",
        "year": 2025,
        "authors": "Huan-ang Gao et al.",
        "theme": "survey",
        "venue": "arXiv / TMLR version noted by authors",
        "url": "https://arxiv.org/abs/2507.21046",
        "doi": "10.48550/arXiv.2507.21046",
        "status": "preprint",
        "note": "Agent-centric taxonomy: what component evolves, when it evolves, and how feedback drives evolution.",
    },
    {
        "key": "xiang2026systematic_self_evolving_agents",
        "title": "A Systematic Survey of Self-Evolving Agents: From Model-Centric to Environment-Driven Co-Evolution",
        "year": 2026,
        "authors": "Zhishang Xiang et al.",
        "theme": "survey",
        "venue": "SSRN preprint",
        "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6626878",
        "status": "preprint",
        "note": "Frames model-centric, environment-centric, and model-environment co-evolution.",
    },
    {
        "key": "xu2026agent_skills_survey",
        "title": "Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward",
        "year": 2026,
        "authors": "Renjun Xu and Yang Yan",
        "theme": "survey",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2602.12430",
        "doi": "10.48550/arXiv.2602.12430",
        "status": "preprint",
        "note": "Focused survey on the emerging skill abstraction layer, MCP, acquisition, portability, and governance.",
    },
    {
        "key": "jiang2026sok_agentic_skills",
        "title": "SoK: Agentic Skills -- Beyond Tool Use in LLM Agents",
        "year": 2026,
        "authors": "Yanna Jiang et al.",
        "theme": "survey",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2602.20867",
        "doi": "10.48550/arXiv.2602.20867",
        "status": "preprint",
        "note": "Maps skill lifecycle, representation, scope, and supply-chain/security risks.",
    },
    {
        "key": "xu2025tool_learning_survey",
        "title": "LLM-Based Agents for Tool Learning: A Survey",
        "year": 2025,
        "authors": "Weikai Xu et al.",
        "theme": "survey",
        "venue": "Data Science and Engineering",
        "url": "https://link.springer.com/article/10.1007/s41019-025-00296-9",
        "doi": "10.1007/s41019-025-00296-9",
        "status": "peer-reviewed",
        "note": "Tool learning survey useful for separating tools, APIs, and higher-level reusable skills.",
    },
    {
        "key": "zhang2024memory_survey",
        "title": "A Survey on the Memory Mechanism of Large Language Model based Agents",
        "year": 2024,
        "authors": "Zeyu Zhang et al.",
        "theme": "survey",
        "venue": "arXiv / ACM TOIS",
        "url": "https://arxiv.org/abs/2404.13501",
        "doi": "10.1145/3748302",
        "status": "peer-reviewed",
        "note": "Memory mechanisms from cognitive analogy, self-evolution, and applications.",
    },
    {
        "key": "memory2026autonomous_agents",
        "title": "Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers",
        "year": 2026,
        "authors": "Unknown / multi-author preprint",
        "theme": "survey",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2603.07670",
        "doi": "10.48550/arXiv.2603.07670",
        "status": "preprint",
        "note": "Recent memory survey emphasizing consolidation, retrieval, forgetting, privacy, and engineering budgets.",
    },
    {
        "key": "yao2022react",
        "title": "ReAct: Synergizing Reasoning and Acting in Language Models",
        "year": 2022,
        "authors": "Shunyu Yao et al.",
        "theme": "foundation",
        "venue": "ICLR 2023 / arXiv",
        "url": "https://arxiv.org/abs/2210.03629",
        "doi": "10.48550/arXiv.2210.03629",
        "status": "peer-reviewed",
        "note": "Canonical reasoning-action-observation trajectory pattern used by many later self-improving agents.",
    },
    {
        "key": "karpas2022mrkl",
        "title": "MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning",
        "year": 2022,
        "authors": "Eran Karpas et al.",
        "theme": "foundation",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2205.00445",
        "doi": "10.48550/arXiv.2205.00445",
        "status": "preprint",
        "note": "Early modular view of LLMs coordinating specialized tools and symbolic components.",
    },
    {
        "key": "nakano2021webgpt",
        "title": "WebGPT: Browser-assisted question-answering with human feedback",
        "year": 2021,
        "authors": "Reiichiro Nakano et al.",
        "theme": "foundation",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2112.09332",
        "doi": "10.48550/arXiv.2112.09332",
        "status": "preprint",
        "note": "Early browser-action trajectories and human preference feedback for web-grounded answering.",
    },
    {
        "key": "schick2023toolformer",
        "title": "Toolformer: Language Models Can Teach Themselves to Use Tools",
        "year": 2023,
        "authors": "Timo Schick et al.",
        "theme": "foundation",
        "venue": "NeurIPS 2023 / arXiv",
        "url": "https://arxiv.org/abs/2302.04761",
        "doi": "10.48550/arXiv.2302.04761",
        "status": "peer-reviewed",
        "note": "Self-supervised tool-use annotation and training, important precursor to tool/skill acquisition.",
    },
    {
        "key": "patil2023gorilla",
        "title": "Gorilla: Large Language Model Connected with Massive APIs",
        "year": 2023,
        "authors": "Shishir G. Patil et al.",
        "theme": "foundation",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2305.15334",
        "doi": "10.48550/arXiv.2305.15334",
        "status": "preprint",
        "note": "API retrieval/calling benchmark and model training for robust tool invocation.",
    },
    {
        "key": "qin2023toolllm",
        "title": "ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs",
        "year": 2023,
        "authors": "Yujia Qin et al.",
        "theme": "foundation",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2307.16789",
        "doi": "10.48550/arXiv.2307.16789",
        "status": "preprint",
        "note": "Tool-use dataset, API retrieval, and decision-making benchmark.",
    },
    {
        "key": "li2023api_bank",
        "title": "API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs",
        "year": 2023,
        "authors": "Minghao Li et al.",
        "theme": "foundation",
        "venue": "EMNLP 2023 / arXiv",
        "url": "https://arxiv.org/abs/2304.08244",
        "doi": "10.48550/arXiv.2304.08244",
        "status": "peer-reviewed",
        "note": "Benchmark for planning API calls and using tools over multi-turn tasks.",
    },
    {
        "key": "shen2023hugginggpt",
        "title": "HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face",
        "year": 2023,
        "authors": "Yongliang Shen et al.",
        "theme": "foundation",
        "venue": "NeurIPS 2023 / arXiv",
        "url": "https://arxiv.org/abs/2303.17580",
        "doi": "10.48550/arXiv.2303.17580",
        "status": "peer-reviewed",
        "note": "LLM as controller over many expert models; useful for tool orchestration background.",
    },
    {
        "key": "yao2023tree_of_thoughts",
        "title": "Tree of Thoughts: Deliberate Problem Solving with Large Language Models",
        "year": 2023,
        "authors": "Shunyu Yao et al.",
        "theme": "foundation",
        "venue": "NeurIPS 2023 / arXiv",
        "url": "https://arxiv.org/abs/2305.10601",
        "doi": "10.48550/arXiv.2305.10601",
        "status": "peer-reviewed",
        "note": "Search over intermediate reasoning states; informs agent trajectory branching and reflection.",
    },
    {
        "key": "ahn2022saycan",
        "title": "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances",
        "year": 2022,
        "authors": "Michael Ahn et al.",
        "theme": "foundation",
        "venue": "CoRL 2022 / arXiv",
        "url": "https://arxiv.org/abs/2204.01691",
        "doi": "10.48550/arXiv.2204.01691",
        "status": "peer-reviewed",
        "note": "Connects language planning with executable affordances, relevant to skill feasibility checks.",
    },
    {
        "key": "huang2022inner_monologue",
        "title": "Inner Monologue: Embodied Reasoning through Planning with Language Models",
        "year": 2022,
        "authors": "Wenlong Huang et al.",
        "theme": "foundation",
        "venue": "CoRL 2022 / arXiv",
        "url": "https://arxiv.org/abs/2207.05608",
        "doi": "10.48550/arXiv.2207.05608",
        "status": "peer-reviewed",
        "note": "Embodied feedback as text observations in a planning loop.",
    },
    {
        "key": "wang2023deps",
        "title": "Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents",
        "year": 2023,
        "authors": "Zihao Wang et al.",
        "theme": "foundation",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2302.01560",
        "doi": "10.48550/arXiv.2302.01560",
        "status": "preprint",
        "note": "Open-world embodied planning with feedback and selection, an important predecessor to Voyager-like agents.",
    },
    {
        "key": "shinn2023reflexion",
        "title": "Reflexion: Language Agents with Verbal Reinforcement Learning",
        "year": 2023,
        "authors": "Noah Shinn et al.",
        "theme": "reflection_memory",
        "venue": "NeurIPS 2023 / arXiv",
        "url": "https://arxiv.org/abs/2303.11366",
        "doi": "10.48550/arXiv.2303.11366",
        "status": "peer-reviewed",
        "note": "Stores verbal reflections in episodic memory to improve subsequent trials.",
    },
    {
        "key": "park2023generative_agents",
        "title": "Generative Agents: Interactive Simulacra of Human Behavior",
        "year": 2023,
        "authors": "Joon Sung Park et al.",
        "theme": "reflection_memory",
        "venue": "UIST 2023 / arXiv",
        "url": "https://arxiv.org/abs/2304.03442",
        "doi": "10.1145/3586183.3606763",
        "status": "peer-reviewed",
        "note": "Memory stream, reflection, and planning architecture for believable agents.",
    },
    {
        "key": "wang2023voyager",
        "title": "Voyager: An Open-Ended Embodied Agent with Large Language Models",
        "year": 2023,
        "authors": "Guanzhi Wang et al.",
        "theme": "skills",
        "venue": "TMLR / arXiv",
        "url": "https://arxiv.org/abs/2305.16291",
        "doi": "10.48550/arXiv.2305.16291",
        "status": "peer-reviewed",
        "note": "Automatic curriculum, iterative prompting, and an ever-growing executable skill library in Minecraft.",
    },
    {
        "key": "zhao2023expel",
        "title": "ExpeL: LLM Agents Are Experiential Learners",
        "year": 2023,
        "authors": "Andrew Zhao et al.",
        "theme": "reflection_memory",
        "venue": "AAAI 2024 / arXiv",
        "url": "https://arxiv.org/abs/2308.10144",
        "doi": "10.48550/arXiv.2308.10144",
        "status": "peer-reviewed",
        "note": "Extracts natural-language knowledge from training experiences and reuses it on test tasks.",
    },
    {
        "key": "yao2023retroformer",
        "title": "Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization",
        "year": 2023,
        "authors": "Shunyu Yao et al.",
        "theme": "reflection_memory",
        "venue": "ICLR 2024 / arXiv",
        "url": "https://arxiv.org/abs/2308.02151",
        "doi": "10.48550/arXiv.2308.02151",
        "status": "peer-reviewed",
        "note": "Learns a retrospective model to tune agent prompts from environment feedback.",
    },
    {
        "key": "prasad2024metareflection",
        "title": "MetaReflection: Learning Instructions for Language Agents using Past Reflections",
        "year": 2024,
        "authors": "Archiki Prasad et al.",
        "theme": "reflection_memory",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2405.13009",
        "doi": "10.48550/arXiv.2405.13009",
        "status": "preprint",
        "note": "Offline reinforcement learning over past reflections; turns reflections into improved instructions.",
    },
    {
        "key": "du2024devils_advocate",
        "title": "Devil's Advocate: Anticipatory Reflection for LLM Agents",
        "year": 2024,
        "authors": "Yu Du et al.",
        "theme": "reflection_memory",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2405.16334",
        "doi": "10.48550/arXiv.2405.16334",
        "status": "preprint",
        "note": "Uses anticipatory reflection before acting, complementing post-hoc reflection loops.",
    },
    {
        "key": "shao2024self_reflection_effects",
        "title": "Self-Reflection in LLM Agents: Effects on Problem-Solving Performance",
        "year": 2024,
        "authors": "Yijia Shao et al.",
        "theme": "reflection_memory",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2405.06682",
        "doi": "10.48550/arXiv.2405.06682",
        "status": "preprint",
        "note": "Empirical analysis of when self-reflection helps or fails.",
    },
    {
        "key": "positive2024experience_reflection",
        "title": "Positive Experience Reflection for Agents in Text-Based Games",
        "year": 2024,
        "authors": "OpenReview authors",
        "theme": "reflection_memory",
        "venue": "OpenReview",
        "url": "https://openreview.net/pdf?id=YwqlQubiiv",
        "status": "workshop/preprint",
        "note": "Studies learning from successful trajectories, not only failures.",
    },
    {
        "key": "samule2025multilevel_reflection",
        "title": "SAMULE: Self-Learning Agents Enhanced by Multi-level Reflection",
        "year": 2025,
        "authors": "EMNLP 2025 authors",
        "theme": "reflection_memory",
        "venue": "EMNLP 2025",
        "url": "https://aclanthology.org/2025.emnlp-main.839.pdf",
        "status": "peer-reviewed",
        "note": "Multi-level reflection and self-learning framework; useful comparison to Reflexion/ExpeL/Retroformer.",
    },
    {
        "key": "reasoningbank2025",
        "title": "ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory",
        "year": 2025,
        "authors": "Siru Ouyang et al.",
        "theme": "reflection_memory",
        "venue": "OpenReview",
        "url": "https://openreview.net/forum?id=jL7fwchScm",
        "status": "preprint",
        "note": "Distills successes and failures into reasoning memory and combines it with memory-aware test-time scaling.",
    },
    {
        "key": "retroagent2026",
        "title": "RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback",
        "year": 2026,
        "authors": "Unknown / multi-author preprint",
        "theme": "reflection_memory",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2603.08561",
        "doi": "10.48550/arXiv.2603.08561",
        "status": "preprint",
        "note": "Combines numerical intrinsic feedback and language feedback for online agent evolution.",
    },
    {
        "key": "benchtrace2026",
        "title": "BenchTrace: A Benchmark for Testing Reflection Ability and Controlled Evolution in LLM Agents",
        "year": 2026,
        "authors": "Unknown / multi-author preprint",
        "theme": "evaluation",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2605.29225",
        "doi": "10.48550/arXiv.2605.29225",
        "status": "preprint",
        "note": "Evaluates failure identification and whether past failures produce controlled avoidance behavior.",
    },
    {
        "key": "clear2026",
        "title": "CLEAR: Context Augmentation from Contrastive Learning of Experience via Agentic Reflection",
        "year": 2026,
        "authors": "Unknown / multi-author preprint",
        "theme": "trajectory",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2604.07487",
        "doi": "10.48550/arXiv.2604.07487",
        "status": "preprint",
        "note": "Contrastive reflection over trajectories to produce reusable task context.",
    },
    {
        "key": "zhong2023memorybank",
        "title": "MemoryBank: Enhancing Large Language Models with Long-Term Memory",
        "year": 2023,
        "authors": "Wanjun Zhong et al.",
        "theme": "memory",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2305.10250",
        "doi": "10.48550/arXiv.2305.10250",
        "status": "preprint",
        "note": "Long-term memory mechanism for personalized and persistent interactions.",
    },
    {
        "key": "packer2023memgpt",
        "title": "MemGPT: Towards LLMs as Operating Systems",
        "year": 2023,
        "authors": "Charles Packer et al.",
        "theme": "memory",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2310.08560",
        "doi": "10.48550/arXiv.2310.08560",
        "status": "preprint",
        "note": "OS-inspired memory hierarchy and explicit memory-management actions.",
    },
    {
        "key": "mem02025",
        "title": "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory",
        "year": 2025,
        "authors": "Mem0 authors",
        "theme": "memory",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2504.19413",
        "doi": "10.48550/arXiv.2504.19413",
        "status": "preprint",
        "note": "Production-oriented long-term memory layer for agent applications.",
    },
    {
        "key": "memory_management2025experience_following",
        "title": "How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior",
        "year": 2025,
        "authors": "Unknown / multi-author preprint",
        "theme": "memory",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2505.16067",
        "doi": "10.48550/arXiv.2505.16067",
        "status": "preprint",
        "note": "Shows retrieval choices can strongly steer agent outputs toward prior experiences.",
    },
    {
        "key": "yu2026agemem",
        "title": "Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents",
        "year": 2026,
        "authors": "Yi Yu et al.",
        "theme": "memory",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2601.01885",
        "doi": "10.48550/arXiv.2601.01885",
        "status": "preprint",
        "note": "Learns memory operations as tool actions using progressive RL and step-wise GRPO.",
    },
    {
        "key": "yang2026plugmem",
        "title": "PlugMem: A Task-Agnostic Plugin Memory Module for LLM Agents",
        "year": 2026,
        "authors": "Ke Yang et al.",
        "theme": "memory",
        "venue": "Microsoft Research",
        "url": "https://www.microsoft.com/en-us/research/publication/plugmem-a-task-agnostic-plugin-memory-module-for-llm-agents/",
        "status": "preprint",
        "note": "Knowledge-centric memory graph for task-agnostic plugin memory.",
    },
    {
        "key": "lightweight2026llm_agent_memory",
        "title": "Lightweight LLM Agent Memory with Small Language Models",
        "year": 2026,
        "authors": "Unknown / multi-author preprint",
        "theme": "memory",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2604.07798",
        "doi": "10.48550/arXiv.2604.07798",
        "status": "preprint",
        "note": "Organizes short-, mid-, and long-term memory while reducing heavyweight LLM calls.",
    },
    {
        "key": "memoryagentbench2025",
        "title": "Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions",
        "year": 2025,
        "authors": "Unknown / multi-author preprint",
        "theme": "evaluation",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2507.05257",
        "doi": "10.48550/arXiv.2507.05257",
        "status": "preprint",
        "note": "MemoryAgentBench: retrieval, test-time learning, long-range understanding, and conflict resolution.",
    },
    {
        "key": "evomembench2026",
        "title": "EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective",
        "year": 2026,
        "authors": "Unknown / multi-author preprint",
        "theme": "evaluation",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2605.18421",
        "doi": "10.48550/arXiv.2605.18421",
        "status": "preprint",
        "note": "Evaluates in-episode/cross-episode and knowledge/execution memory for self-evolving agents.",
    },
    {
        "key": "longmemevalv2_2026",
        "title": "LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues",
        "year": 2026,
        "authors": "Unknown / multi-author preprint",
        "theme": "evaluation",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2605.12493",
        "doi": "10.48550/arXiv.2605.12493",
        "status": "preprint",
        "note": "Long-term memory benchmark with trajectory-like workplace evidence.",
    },
    {
        "key": "memoryr1_2025",
        "title": "Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning",
        "year": 2025,
        "authors": "Unknown / multi-author preprint",
        "theme": "memory",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2508.19828",
        "doi": "10.48550/arXiv.2508.19828",
        "status": "preprint",
        "note": "RL framework for explicit memory add/update/delete/no-op operations.",
    },
    {
        "key": "tamem2026",
        "title": "TA-Mem: Tool-Augmented Autonomous Memory Retrieval for LLM in Long-Term Conversational QA",
        "year": 2026,
        "authors": "Unknown / multi-author preprint",
        "theme": "memory",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2603.09297",
        "doi": "10.48550/arXiv.2603.09297",
        "status": "preprint",
        "note": "Tool-augmented adaptive memory extraction and retrieval selection.",
    },
    {
        "key": "yang2026autoskill",
        "title": "AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution",
        "year": 2026,
        "authors": "Yutao Yang et al.",
        "theme": "skills",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2603.01145",
        "doi": "10.48550/arXiv.2603.01145",
        "status": "preprint",
        "note": "Abstracts dialogue and interaction traces into reusable, shareable, dynamically injected skills.",
    },
    {
        "key": "ni2026trace2skill",
        "title": "Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills",
        "year": 2026,
        "authors": "Jingwei Ni et al.",
        "theme": "trajectory",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2603.25158",
        "doi": "10.48550/arXiv.2603.25158",
        "status": "work in progress",
        "note": "Consolidates execution trajectories into transferable SOP-like skills without parameter updates.",
    },
    {
        "key": "ouyang2026skillos",
        "title": "SkillOS: Learning Skill Curation for Self-Evolving Agents",
        "year": 2026,
        "authors": "Siru Ouyang et al.",
        "theme": "skills",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2605.06614",
        "doi": "10.48550/arXiv.2605.06614",
        "status": "preprint",
        "note": "Trains a skill curator that updates an external SkillRepo from accumulated experience.",
    },
    {
        "key": "zhang2026coevoskills",
        "title": "CoEvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification",
        "year": 2026,
        "authors": "Hanrong Zhang et al.",
        "theme": "skills",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2604.01687",
        "doi": "10.48550/arXiv.2604.01687",
        "status": "preprint",
        "note": "Skill generator and surrogate verifier co-evolve to create multi-file skill packages.",
    },
    {
        "key": "shen2026skillfoundry",
        "title": "SKILLFOUNDRY: Building Self-Evolving Agent Skill Libraries from Heterogeneous Scientific Resources",
        "year": 2026,
        "authors": "Shuaike Shen et al.",
        "theme": "skills",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2604.03964",
        "doi": "10.48550/arXiv.2604.03964",
        "status": "preprint",
        "note": "Mines procedural scientific resources into validated agent skills with provenance and tests.",
    },
    {
        "key": "yu2026skilladaptor",
        "title": "SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories",
        "year": 2026,
        "authors": "Zhuoyun Yu et al.",
        "theme": "trajectory",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2606.01311",
        "doi": "10.48550/arXiv.2606.01311",
        "status": "preprint",
        "note": "Step-level failure attribution and acceptance checks for training-free skill updates.",
    },
    {
        "key": "skilllens2026",
        "title": "From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills",
        "year": 2026,
        "authors": "Zisu Huang et al.",
        "theme": "skills",
        "venue": "Microsoft Research project page",
        "url": "https://microsoft.github.io/SkillLens/",
        "status": "preprint/project",
        "note": "Studies the experience-generation, skill-extraction, and skill-consumption lifecycle.",
    },
    {
        "key": "skillsbench2026",
        "title": "SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks",
        "year": 2026,
        "authors": "SkillsBench authors",
        "theme": "evaluation",
        "venue": "Project PDF",
        "url": "https://www.skillsbench.ai/skillsbench.pdf",
        "status": "preprint/project",
        "note": "Benchmark for measuring skill usefulness across diverse agent tasks.",
    },
    {
        "key": "wang2025sage",
        "title": "Reinforcement Learning for Self-Improving Agent with Skill Library",
        "year": 2025,
        "authors": "Jiongxiao Wang et al.",
        "theme": "skills",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2512.17102",
        "doi": "10.48550/arXiv.2512.17102",
        "status": "preprint",
        "note": "Skill Augmented GRPO for self-evolution over task chains with accumulating skills.",
    },
    {
        "key": "muse_autoskill2026",
        "title": "MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation",
        "year": 2026,
        "authors": "MUSE-Autoskill authors",
        "theme": "skills",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2605.27366",
        "doi": "10.48550/arXiv.2605.27366",
        "status": "preprint",
        "note": "Skill-centric lifecycle covering creation, memory, management, evaluation, and refinement.",
    },
    {
        "key": "expweaver2026",
        "title": "ExpWeaver: LLM Agents Learn from Experience via Latent RAG",
        "year": 2026,
        "authors": "ExpWeaver authors",
        "theme": "trajectory",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2606.01041",
        "doi": "10.48550/arXiv.2606.01041",
        "status": "preprint",
        "note": "Learning from experience through latent retrieval-augmented generation.",
    },
    {
        "key": "exprag2026",
        "title": "Retrieval-Augmented LLM Agents: Learning to Learn from Experience",
        "year": 2026,
        "authors": "EXPRAG authors",
        "theme": "trajectory",
        "venue": "arXiv / ICLR 2026",
        "url": "https://arxiv.org/abs/2603.18272",
        "doi": "10.48550/arXiv.2603.18272",
        "status": "preprint",
        "note": "Compares fine-tuning and retrieval over past experience for agent generalization.",
    },
    {
        "key": "trajectory_memory2026",
        "title": "Trajectory-Informed Memory Generation for Self-Improving Agent Systems",
        "year": 2026,
        "authors": "Unknown / multi-author preprint",
        "theme": "trajectory",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2603.10600",
        "doi": "10.48550/arXiv.2603.10600",
        "status": "preprint",
        "note": "Extracts strategy, recovery, and optimization tips from execution trajectories.",
    },
    {
        "key": "zhou2026lrat",
        "title": "Learning to Retrieve from Agent Trajectories",
        "year": 2026,
        "authors": "Yuqi Zhou et al.",
        "theme": "trajectory",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2604.04949",
        "doi": "10.48550/arXiv.2604.04949",
        "status": "preprint",
        "note": "Mines browsing actions and reasoning traces as supervision for agent-oriented retrieval.",
    },
    {
        "key": "zhang2026ace",
        "title": "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models",
        "year": 2026,
        "authors": "Qizheng Zhang et al.",
        "theme": "trajectory",
        "venue": "OpenReview",
        "url": "https://openreview.net/forum?id=TZAhZYtTn7",
        "status": "preprint",
        "note": "Optimizes persistent/evolving contexts offline and online for agents and domain tasks.",
    },
    {
        "key": "aksitov2023rest_react",
        "title": "ReST meets ReAct: Self-Improvement for Multi-Step Reasoning LLM Agent",
        "year": 2023,
        "authors": "Renat Aksitov et al.",
        "theme": "self_training",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2312.10003",
        "doi": "10.48550/arXiv.2312.10003",
        "status": "preprint",
        "note": "Iteratively trains on previous ReAct trajectories with AI feedback for self-improvement/distillation.",
    },
    {
        "key": "madaan2023self_refine",
        "title": "Self-Refine: Iterative Refinement with Self-Feedback",
        "year": 2023,
        "authors": "Aman Madaan et al.",
        "theme": "self_training",
        "venue": "NeurIPS 2023 / arXiv",
        "url": "https://arxiv.org/abs/2303.17651",
        "doi": "10.48550/arXiv.2303.17651",
        "status": "peer-reviewed",
        "note": "General self-feedback/refinement loop, widely reused inside agent designs.",
    },
    {
        "key": "chen2024spin",
        "title": "Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models",
        "year": 2024,
        "authors": "Zixiang Chen et al.",
        "theme": "self_training",
        "venue": "ICML 2024 / arXiv",
        "url": "https://arxiv.org/abs/2401.01335",
        "doi": "10.48550/arXiv.2401.01335",
        "status": "peer-reviewed",
        "note": "Self-play fine-tuning with model-generated responses; model-level precursor to agent self-evolution.",
    },
    {
        "key": "yuan2024self_rewarding",
        "title": "Self-Rewarding Language Models",
        "year": 2024,
        "authors": "Weizhe Yuan et al.",
        "theme": "self_training",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2401.10020",
        "doi": "10.48550/arXiv.2401.10020",
        "status": "preprint",
        "note": "LLM generates and judges instruction-following data, a self-feedback training route.",
    },
    {
        "key": "huang2025rzero",
        "title": "R-Zero: Self-Evolving Reasoning LLM from Zero Data",
        "year": 2025,
        "authors": "Chengsong Huang et al.",
        "theme": "self_training",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2508.05004",
        "doi": "10.48550/arXiv.2508.05004",
        "status": "preprint",
        "note": "Challenger-solver co-evolution creates curriculum without existing tasks or labels.",
    },
    {
        "key": "xia2025agent0",
        "title": "Agent0: Unleashing Self-Evolving Agents from Zero Data via Tool-Integrated Reasoning",
        "year": 2025,
        "authors": "Peng Xia et al.",
        "theme": "self_training",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2511.16043",
        "doi": "10.48550/arXiv.2511.16043",
        "status": "preprint",
        "note": "Curriculum agent and executor agent co-evolve with tool-integrated reasoning.",
    },
    {
        "key": "robeyns2025self_improving_coding_agent",
        "title": "A Self-Improving Coding Agent",
        "year": 2025,
        "authors": "Maxime Robeyns et al.",
        "theme": "coding_science",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2504.15228",
        "doi": "10.48550/arXiv.2504.15228",
        "status": "preprint",
        "note": "Coding agent edits its own scaffolding and improves on SWE-bench/LiveCodeBench-style tasks.",
    },
    {
        "key": "seagent2025",
        "title": "SE-Agent: Self-Evolution Trajectory Optimization in Multi-Step Reasoning with LLM-Based Agents",
        "year": 2025,
        "authors": "SE-Agent authors",
        "theme": "self_training",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2508.02085",
        "doi": "10.48550/arXiv.2508.02085",
        "status": "preprint",
        "note": "Trajectory optimization for multi-step reasoning agents.",
    },
    {
        "key": "ttsi2026",
        "title": "TT-SI: Self-Improving LLM Agents with Test-Time Training",
        "year": 2026,
        "authors": "Emre Can Acikgoz et al.",
        "theme": "self_training",
        "venue": "OpenReview / ACL ARR 2026",
        "url": "https://openreview.net/forum?id=k30IrbNYSG",
        "status": "preprint",
        "note": "Detects uncertain samples, self-augments similar examples, and trains at test time.",
    },
    {
        "key": "siva2025",
        "title": "SIVA: Self-Improving Vulnerability Agent",
        "year": 2025,
        "authors": "Valentin Walischewski et al.",
        "theme": "coding_science",
        "venue": "OpenReview / NeurIPS workshop",
        "url": "https://openreview.net/forum?id=JDN0x8eTPm",
        "status": "workshop/preprint",
        "note": "Memory-guided meta-learning and dynamic prompt optimization for vulnerability detection.",
    },
    {
        "key": "wei2026cose",
        "title": "Confidence-Orchestrated Self-Evolution against Uncertain LLM Feedback",
        "year": 2026,
        "authors": "Bowen Wei et al.",
        "theme": "self_training",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2605.28010",
        "doi": "10.48550/arXiv.2605.28010",
        "status": "preprint",
        "note": "Confidence-weighted PPO and prioritized replay to reduce damage from uncertain self-judgments.",
    },
    {
        "key": "zuo2025ttrl",
        "title": "TTRL: Test-Time Reinforcement Learning",
        "year": 2025,
        "authors": "TTRL authors",
        "theme": "self_training",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2504.16084",
        "doi": "10.48550/arXiv.2504.16084",
        "status": "preprint",
        "note": "Test-time RL as a model-level route toward adaptive behavior.",
    },
    {
        "key": "novikov2025alphaevolve",
        "title": "AlphaEvolve: A coding agent for scientific and algorithmic discovery",
        "year": 2025,
        "authors": "Alexander Novikov et al.",
        "theme": "coding_science",
        "venue": "arXiv / DeepMind white paper",
        "url": "https://arxiv.org/abs/2506.13131",
        "doi": "10.48550/arXiv.2506.13131",
        "status": "white paper/preprint",
        "note": "Evolutionary coding agent driven by automated evaluators.",
    },
    {
        "key": "zhang2026accelopt",
        "title": "AccelOpt: A Self-Improving LLM Agentic System for AI Accelerator Kernel Optimization",
        "year": 2026,
        "authors": "Genghan Zhang et al.",
        "theme": "coding_science",
        "venue": "OpenReview / MLSys 2026",
        "url": "https://openreview.net/forum?id=SBS4NJHYjZ",
        "status": "preprint",
        "note": "Kernel optimization system with optimization memory and iterative self-improvement.",
    },
    {
        "key": "deepevolve2025",
        "title": "Scientific Algorithm Discovery by Augmenting AlphaEvolve with Deep Research",
        "year": 2025,
        "authors": "DeepEvolve authors",
        "theme": "coding_science",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2510.06056",
        "doi": "10.48550/arXiv.2510.06056",
        "status": "preprint",
        "note": "Combines deep research, external knowledge retrieval, code editing, and evolutionary evaluation.",
    },
    {
        "key": "alphaevolve_math2025",
        "title": "Mathematical exploration and discovery at scale",
        "year": 2025,
        "authors": "AlphaEvolve mathematics authors",
        "theme": "coding_science",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2511.02864",
        "doi": "10.48550/arXiv.2511.02864",
        "status": "preprint",
        "note": "Uses AlphaEvolve for large-scale mathematical construction discovery.",
    },
    {
        "key": "liu2023agentbench",
        "title": "AgentBench: Evaluating LLMs as Agents",
        "year": 2023,
        "authors": "Xiao Liu et al.",
        "theme": "evaluation",
        "venue": "ICLR 2024 / arXiv",
        "url": "https://arxiv.org/abs/2308.03688",
        "doi": "10.48550/arXiv.2308.03688",
        "status": "peer-reviewed",
        "note": "Multi-environment benchmark for LLM-as-agent reasoning and decision-making.",
    },
    {
        "key": "ma2024agentboard",
        "title": "AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents",
        "year": 2024,
        "authors": "Chang Ma et al.",
        "theme": "evaluation",
        "venue": "NeurIPS 2024 Datasets and Benchmarks",
        "url": "https://proceedings.neurips.cc/paper_files/paper/2024/hash/877b40688e330a0e2a3fc24084208dfa-Abstract-Datasets_and_Benchmarks_Track.html",
        "status": "peer-reviewed",
        "note": "Analytical evaluation framework with progress/trajectory measures for multi-turn agents.",
    },
    {
        "key": "zhou2023webarena",
        "title": "WebArena: A Realistic Web Environment for Building Autonomous Agents",
        "year": 2023,
        "authors": "Shuyan Zhou et al.",
        "theme": "evaluation",
        "venue": "ICLR 2024 / arXiv",
        "url": "https://arxiv.org/abs/2307.13854",
        "doi": "10.48550/arXiv.2307.13854",
        "status": "peer-reviewed",
        "note": "Realistic website environment for long-horizon web agents.",
    },
    {
        "key": "yao2022webshop",
        "title": "WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents",
        "year": 2022,
        "authors": "Shunyu Yao et al.",
        "theme": "evaluation",
        "venue": "NeurIPS 2022 / arXiv",
        "url": "https://arxiv.org/abs/2207.01206",
        "doi": "10.48550/arXiv.2207.01206",
        "status": "peer-reviewed",
        "note": "Shopping web interaction environment widely reused in agent skill/memory evaluation.",
    },
    {
        "key": "jimenez2023swebench",
        "title": "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?",
        "year": 2023,
        "authors": "Carlos E. Jimenez et al.",
        "theme": "evaluation",
        "venue": "ICLR 2024 / arXiv",
        "url": "https://arxiv.org/abs/2310.06770",
        "doi": "10.48550/arXiv.2310.06770",
        "status": "peer-reviewed",
        "note": "Issue-resolution benchmark that made coding-agent trajectories and regression tests central.",
    },
    {
        "key": "xie2024osworld",
        "title": "OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments",
        "year": 2024,
        "authors": "Tianbao Xie et al.",
        "theme": "evaluation",
        "venue": "NeurIPS 2024 / arXiv",
        "url": "https://arxiv.org/abs/2404.07972",
        "doi": "10.48550/arXiv.2404.07972",
        "status": "peer-reviewed",
        "note": "Computer-use benchmark relevant to skill packages, GUI grounding, and persistent agents.",
    },
    {
        "key": "trivedi2024appworld",
        "title": "AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents",
        "year": 2024,
        "authors": "Harsh Trivedi et al.",
        "theme": "evaluation",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2407.18901",
        "doi": "10.48550/arXiv.2407.18901",
        "status": "preprint",
        "note": "Interactive code-generation benchmark with tool/API state and realistic app tasks.",
    },
    {
        "key": "yao2024taubench",
        "title": "Tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains",
        "year": 2024,
        "authors": "Shunyu Yao et al.",
        "theme": "evaluation",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2406.12045",
        "doi": "10.48550/arXiv.2406.12045",
        "status": "preprint",
        "note": "Interactive user/tool benchmark for realistic service-domain agents.",
    },
    {
        "key": "mialon2023gaia",
        "title": "GAIA: A Benchmark for General AI Assistants",
        "year": 2023,
        "authors": "Grégoire Mialon et al.",
        "theme": "evaluation",
        "venue": "ICLR 2024 / arXiv",
        "url": "https://arxiv.org/abs/2311.12983",
        "doi": "10.48550/arXiv.2311.12983",
        "status": "peer-reviewed",
        "note": "Assistant benchmark that later self-improving agents use for evaluating task success.",
    },
    {
        "key": "agentrewardbench2025",
        "title": "AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories",
        "year": 2025,
        "authors": "AgentRewardBench authors",
        "theme": "evaluation",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2504.08942",
        "doi": "10.48550/arXiv.2504.08942",
        "status": "preprint",
        "note": "LLM-as-judge benchmark for trajectory success, side effects, and repetitiveness.",
    },
    {
        "key": "atbench2026",
        "title": "ATBench: A Diverse and Realistic Trajectory Benchmark for Long-Horizon Agent Safety",
        "year": 2026,
        "authors": "Yu Li et al.",
        "theme": "evaluation",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2604.02022",
        "doi": "10.48550/arXiv.2604.02022",
        "status": "preprint",
        "note": "Trajectory-level safety benchmark organized by risk source, failure mode, and harm.",
    },
    {
        "key": "li2026contextbench",
        "title": "ContextBench: A Benchmark for Context Retrieval in Coding Agents",
        "year": 2026,
        "authors": "Han Li et al.",
        "theme": "evaluation",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2602.05892",
        "doi": "10.48550/arXiv.2602.05892",
        "status": "preprint",
        "note": "Process-oriented evaluation of context retrieval in coding-agent trajectories.",
    },
]


THEME_NAMES = {
    "survey": "综述与路线图",
    "foundation": "基础架构、推理-行动与工具使用",
    "reflection_memory": "反思、经验学习与长期记忆",
    "memory": "记忆系统与记忆管理",
    "skills": "技能沉淀、技能库与生命周期",
    "trajectory": "轨迹挖掘、轨迹到技能与轨迹监督",
    "self_training": "自训练、测试时学习与强化学习式自进化",
    "coding_science": "代码/科学发现中的自改进 agent",
    "evaluation": "评测、轨迹审计与安全",
}


def slugify(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "_", value.lower()).strip("_")
    return value or "paper"


def bibtex_escape(value: str) -> str:
    return value.replace("&", "\\&")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def make_bibtex() -> str:
    entries = []
    for p in PAPERS:
        entry_type = "article" if p.get("doi") and "arXiv" not in p.get("venue", "") else "misc"
        fields = {
            "title": p["title"],
            "author": p["authors"].replace(" et al.", " and others"),
            "year": str(p["year"]),
            "url": p["url"],
        }
        if p.get("doi"):
            fields["doi"] = p["doi"]
        if p.get("venue"):
            fields["note"] = p["venue"]
        body = ",\n".join(f"  {k} = {{{bibtex_escape(v)}}}" for k, v in fields.items())
        entries.append(f"@{entry_type}{{{p['key']},\n{body}\n}}")
    return "\n\n".join(entries)


def make_catalog() -> str:
    by_theme = defaultdict(list)
    for p in PAPERS:
        by_theme[p["theme"]].append(p)

    lines = [
        "# Agent 自进化、技能沉淀与轨迹学习论文目录",
        "",
        f"- 生成日期：2026-06-06",
        f"- 手工种子论文：{len(PAPERS)} 篇",
        "- 说明：`status=preprint/workshop/project` 的条目适合继续跟踪，不应与已发表会议/期刊论文等量看待。",
        "",
        "## 主题统计",
        "",
    ]
    for theme, count in Counter(p["theme"] for p in PAPERS).most_common():
        lines.append(f"- {THEME_NAMES.get(theme, theme)}：{count} 篇")
    lines.append("")

    for theme in THEME_NAMES:
        papers = sorted(by_theme.get(theme, []), key=lambda x: (x["year"], x["title"]))
        if not papers:
            continue
        lines.extend([f"## {THEME_NAMES[theme]}", ""])
        lines.append("| 年份 | 论文 | 状态 | 作用/备注 |")
        lines.append("|---:|---|---|---|")
        for p in papers:
            title = p["title"].replace("|", "\\|")
            note = p["note"].replace("|", "\\|")
            lines.append(f"| {p['year']} | [{title}]({p['url']}) | {p['status']} | {note} |")
        lines.append("")
    return "\n".join(lines)


def make_openalex_summary() -> str:
    base = ROOT / "data" / "openalex"
    lines = [
        "# OpenAlex 原始召回摘要",
        "",
        "这些文件是广泛关键词检索的原始召回，精度不如手工种子目录；保留它们是为了后续扩展和查漏。",
        "",
    ]
    if not base.exists():
        lines.append("未发现 `data/openalex/` 原始文件。")
        return "\n".join(lines)

    seen = set()
    for f in sorted(base.glob("*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception as exc:
            lines.append(f"## {f.name}\n\n读取失败：{exc}\n")
            continue
        rows = data.get("results", [])
        lines.append(f"## {f.name}\n")
        lines.append(f"- 召回条目：{len(rows)}\n")
        lines.append("| 年份 | 引用数 | 标题 | DOI/链接 |")
        lines.append("|---:|---:|---|---|")
        added = 0
        for w in rows:
            title = (w.get("title") or "").strip()
            if not title or title.lower() in seen:
                continue
            seen.add(title.lower())
            doi = w.get("doi") or (w.get("id") or "")
            lines.append(
                f"| {w.get('publication_year') or ''} | {w.get('cited_by_count') or 0} | {title.replace('|', '\\|')} | {doi} |"
            )
            added += 1
            if added >= 20:
                break
        lines.append("")
    return "\n".join(lines)


def make_readme() -> str:
    return f"""
# Agent Self-Evolution Literature Pack

本目录用于存放 agent 自进化、技能沉淀、经验/轨迹学习、长期记忆和相关评测的论文与综述材料。

## 目录

- `agent_self_evolution_review.md`：中文研究综述，面向第 4 章“智能体自进化/技能沉淀”写作。
- `papers_catalog.md`：按主题分类的论文目录，共 {len(PAPERS)} 篇手工种子论文。
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
"""


def make_search_log() -> str:
    return """
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
"""


def make_figures() -> dict[str, str]:
    taxonomy = """
flowchart LR
  A[Agent execution trajectory] --> B[Experience extraction]
  B --> C1[Failure diagnosis]
  B --> C2[Successful pattern mining]
  B --> C3[Context and retrieval signals]
  C1 --> D[Reflection / lesson]
  C2 --> D
  C3 --> E[Retriever or memory update]
  D --> F[Skill / SOP / prompt rule]
  E --> G[Context injection]
  F --> G
  G --> H[Next task execution]
  H --> I[Verifier / evaluator]
  I -->|accept| J[Skill repository]
  I -->|reject| K[Rollback or quarantine]
  J --> G
  K --> B
"""
    lifecycle = """
flowchart TD
  S0[Raw runs and logs] --> S1[Screen trajectories]
  S1 --> S2[Attribute fault or success cause]
  S2 --> S3[Consolidate into reusable skill]
  S3 --> S4[Attach metadata: scope, preconditions, tests]
  S4 --> S5[Retrieve and inject skill]
  S5 --> S6[Execute held-out tasks]
  S6 --> S7{Verifier passes?}
  S7 -->|yes| S8[Promote / version skill]
  S7 -->|no| S9[Revise, demote, or retire]
  S8 --> S5
  S9 --> S2
"""
    return {
        "self_evolution_closed_loop.mmd": taxonomy,
        "skill_lifecycle.mmd": lifecycle,
    }


def make_figures_readme() -> str:
    return """
# Figures

This directory stores editable Mermaid diagrams and generated PNG figures for
the agent self-evolution literature review.

## Generated PNG figures

- `self_evolution_closed_loop.png`: closed-loop LLM agent self-evolution pipeline.
- `skill_lifecycle.png`: LLM agent skill lifecycle from trajectories to versioned reuse.

The PNG figures were generated on 2026-06-07 with the user-provided external
OpenAI-compatible image API using `gpt-image-2`. The API key was used only as a
runtime credential and is not stored in this repository.

## Generation prompts

- `prompts.txt`: exact prompts, model name, temperature, and response JSON paths.

## Editable source diagrams

- `self_evolution_closed_loop.mmd`
- `skill_lifecycle.mmd`

The Mermaid files remain available as lightweight editable versions for thesis
or presentation revisions.
"""


def make_review() -> str:
    return """
# Agent 自进化、技能沉淀与轨迹学习研究综述

## 摘要

LLM agent 研究正在从“把大模型接上工具完成一次任务”转向“让 agent 从持续交互中积累可复用能力”。这个转向的核心不只是加一个向量库或反思 prompt，而是形成一个可审计的闭环：任务执行产生轨迹，轨迹被筛选、归因和抽象，抽象结果以记忆、反思、技能、检索器训练信号、prompt/代码补丁或模型参数更新的形式沉淀，再通过检索、注入、验证和回滚机制进入后续任务。现有文献大致形成五条路线：反思与经验学习、长期记忆、技能库与技能生命周期、轨迹监督/轨迹到技能、自训练或强化学习式自进化。对 PrincipiaBlastFoam 第 4 章而言，最直接可借鉴的是“从失败轨迹沉淀技能，并用确定性验证器控制技能进入生产链路”的工程化路线。

## 图示框架

![Agent self-evolution closed loop](figures/self_evolution_closed_loop.png)

图 1 展示了 agent 自进化闭环：任务轨迹经过失败/成功模式挖掘、反思、技能抽取和技能库版本化后，通过检索与注入影响下一次执行，并由验证器决定推广或回滚。

![LLM agent skill lifecycle](figures/skill_lifecycle.png)

图 2 展示了技能沉淀生命周期：从原始执行日志和轨迹开始，经 episode 筛选、成败归因、技能蒸馏、元数据与测试绑定、版本化入库、检索注入和 held-out 验证，最终形成可审计的版本推广或隔离机制。

## 1. 概念边界：自进化不等于一次性自我纠错

“自进化”在文献中有宽窄两种用法。宽义上，它包括模型从自生成数据、自反馈或自博弈中更新参数，例如 Self-Rewarding Language Models、SPIN、R-Zero、Agent0、COSE 和 TTRL。狭义上，它指 agent 系统在不更新基础模型权重的情况下，更新外部组件：记忆、技能库、工具说明、检索器、系统提示词、执行脚手架或评测器。第 4 章的“技能沉淀”更接近狭义路线，因为它把 Chapter 3 的失败证据转为可检索、可注入、可验证的技能，而不是训练一个新模型。

Tao 等的 LLM 自进化综述把循环拆成经验获取、经验精炼、更新和评估四步；Gao 等的 self-evolving agents 综述进一步追问 what/when/how：更新什么组件、在测试时还是跨任务阶段更新、用标量奖励还是文本反馈更新。技能相关综述则把 skill 从 tool 中分离出来：tool 往往是单个函数调用，skill 是带有适用条件、步骤、资源、测试和治理规则的过程性知识包。这个区分对工程系统很关键，因为 blastFoam/OpenFOAM 任务中的“技能”通常不是一个 API，而是跨文件、跨日志、跨物理约束的操作规程。

## 2. 基础范式：从 ReAct 轨迹到可学习的 agent 日志

ReAct 奠定了 Thought-Action-Observation 的轨迹格式，使 agent 行为变成可记录、可复盘、可训练的序列。MRKL、Toolformer、API-Bank、ToolLLM、Gorilla、HuggingGPT 等工作则证明 LLM 可以选择、调用和组合外部工具。WebGPT、WebShop、WebArena、OSWorld、AppWorld、SWE-bench、GAIA 和 AgentBench 等评测把 agent 放进多步环境，要求模型面对状态变化、工具错误、网页/文件系统反馈和最终任务验收。

这些工作本身未必“自进化”，但它们提供了自进化的燃料：完整轨迹、工具调用、环境反馈、失败原因和成功路径。没有这些可追踪中间证据，后续的 Reflexion、ExpeL、ReST meets ReAct、Trace2Skill、SkillOS 等方法都只能停留在最终答案级别的自我纠错，无法判断到底是哪一步、哪个工具、哪条技能导致成败。

## 3. 反思与经验学习：把失败变成文字经验

Reflexion 是这一脉络的关键起点。它不更新模型参数，而是让 agent 根据任务反馈写出 verbal reflection，并把反思放入 episodic memory 供下一次尝试使用。Generative Agents 将观察、反思和计划组织为 memory stream，说明自然语言记忆可以支撑长期行为一致性。Voyager 则把反思推进到可执行技能库：Minecraft 中成功的代码片段被保存为技能，后续可检索和组合。ExpeL 进一步系统化了“从训练任务经验中抽取自然语言知识，再迁移到测试任务”的流程。

后续研究开始追问反思的质量。Retroformer 学习 retrospective model 来根据环境反馈优化 agent prompt；MetaReflection 从过去反思中学习更好的指令；Devil's Advocate 把反思前置为 anticipatory reflection；Self-Reflection in LLM Agents 和 Positive Experience Reflection 分析反思在不同任务和正/负经验上的作用。ReasoningBank、RetroAgent、CLEAR、BenchTrace 等 2025-2026 年工作则把反思从“单条经验总结”推进到“跨轨迹经验库”和“受控演化评测”：既抽取成功策略，也抽取失败避坑点，并检验这些经验是否真的改变后续行为。

这条路线的优点是成本低、可解释、与闭源模型兼容。缺点也明显：反思容易生成表面合理但不可执行的建议；长反思会污染上下文；如果没有验证器，错误经验会被反复强化。对工程 agent 来说，反思不能只写“检查边界条件”，而应落到具体文件、日志模式、物理量范围、可运行命令和验收条件。

## 4. 长期记忆：从追加日志到可治理的记忆操作

MemoryBank、MemGPT、Mem0、PlugMem、AgeMem、Memory-R1、TA-Mem 等工作体现了长期记忆路线的演化。早期系统多是把对话或任务片段存入向量库，按相似度召回；MemGPT 把记忆管理显式化为类似操作系统的分层存储；Mem0 和 PlugMem 关注生产环境下的可扩展、低冗余和知识图式化；AgeMem 和 Memory-R1 则把“写入、更新、删除、保留”变成 agent 可学习的动作。

记忆系统和技能系统的差别在于粒度和验收方式。记忆回答“过去发生了什么、用户偏好是什么、哪些经验可能相关”，技能回答“遇到这类问题应该按什么步骤做，如何判断做对了”。How Memory Management Impacts LLM Agents 指出 retrieved memory 会诱导 agent 复制相似输出，这说明记忆不仅是信息来源，也是策略偏置源。EvoMemBench、MemoryAgentBench、LongMemEval-V2 等评测开始要求记忆系统处理跨 episode 经验、冲突更新和长期一致性。

对 PrincipiaBlastFoam，记忆层适合保存项目级事实和历史算例证据，例如求解器版本、典型边界条件、已验证教程、日志错误模式；技能层则适合保存“当 `rho`/`thermophysicalProperties` 不一致时如何修复并验证”这类程序性规程。二者应分层，避免把所有经验都塞进一个不可控向量库。

## 5. 技能沉淀：从 Voyager 技能库到 SkillOS/Trace2Skill

技能路线是当前与“技能沉淀”最贴近的方向。Voyager 展示了自动课程、迭代代码生成和增长式技能库的组合；AutoSkill 将用户交互轨迹抽象为可复用技能，并动态注入未来请求；Trace2Skill 将大量执行轨迹并行归纳成统一技能目录，强调技能不是记忆具体案例，而是压缩失败模式和操作规程；SkillOS 将“技能库维护”本身建模为可学习策略，由 curator 决定何时新增、修改和保留技能；CoEvoSkills 用 skill generator 和 surrogate verifier 共同进化来构建复杂多文件技能包；SkillFoundry 从科学资源、脚本、API、文档和论文中挖掘过程性知识，生成带 provenance 和 tests 的技能。

这批论文共同说明，技能质量取决于三个环节：经验池、抽取器、消费者。SkillLens 的经验尤其重要：好看的技能文本不一定有用，LLM judge 对技能优劣的判断可能低于随机；真正有用的是具体失败机制、可执行补救步骤和高风险动作黑名单。SkillAdaptor 进一步把更新粒度细化到失败轨迹中的第一个可行动故障步骤，并用 acceptance checks 防止过宽更新。SAGE 和 MUSE-Autoskill 则把技能库纳入强化学习或生命周期管理，关注长期任务流中的技能创建、记忆、管理、评估和修订。

这对第 4 章有直接启发：技能不是“总结得越抽象越好”。抽象技能能提升覆盖面，但如果缺少故障归因、触发条件和验收步骤，容易变成泛泛提示；具体 verifier skill 虽然窄，但能在 OpenFOAM/blastFoam 这种强约束环境中减少虚假改进。当前项目中 concrete-verifier-skill 组优于 no-skill 和 abstract-skill 组，正好与 SkillLens、Trace2Skill、SkillAdaptor 的结论一致：可执行、可验证、可回滚比表面通顺更重要。

## 6. 轨迹学习：执行日志成为监督信号

轨迹学习路线把 agent 运行过程本身当作训练或优化数据。ReST meets ReAct 从 ReAct 轨迹中迭代训练小模型；Learning to Retrieve from Agent Trajectories 将搜索 agent 的浏览行为、未浏览候选和 post-browse reasoning 转成检索器监督；Trajectory-Informed Memory Generation 从执行轨迹中抽取 strategy/recovery/optimization tips；Retrieval-Augmented LLM Agents: Learning to Learn from Experience 比较了经验检索和微调；ExpWeaver 用 latent RAG 处理经验学习；Agentic Context Engineering 则把上下文当作可演化对象，离线和在线持续优化。

轨迹监督的关键价值在于它比最终分数更细。一个 blastFoam workflow 失败，最终得分只能说明失败；轨迹能说明是 case 文件生成错误、物性模型不一致、网格/边界条件不匹配、求解器未启动、后处理找错目录，还是评分器误判。若把这些状态、动作、观察、验证结果结构化，就能训练检索器、抽取技能、生成回归用例，并审计技能是否造成副作用。

## 7. 自训练、强化学习与模型级自进化

另一条路线直接更新模型或 agent policy。Self-Refine 是轻量自反馈循环；SPIN、Self-Rewarding Language Models、R-Zero、Agent0、COSE、TTRL 和 TT-SI 等工作通过自生成数据、自博弈、测试时训练、置信度加权或工具增强课程推动模型能力提升。SAGE 将技能库引入 GRPO，说明技能不仅能作为推理上下文，也能参与奖励设计。A Self-Improving Coding Agent、SIVA、AccelOpt、AlphaEvolve 和 DeepEvolve 则在代码/科学发现中展示“agent 修改代码、脚手架或算法候选，并由自动评测器筛选”的闭环。

这些方法通常需要更强算力、更稳定的奖励和更严格的安全边界。它们对毕业论文的价值主要是理论对照：说明“自进化”可以发生在模型参数、agent 脚手架、技能库、检索器或上下文多个层次。当前项目宜优先采用外部技能库和验证器演化，因为 OpenFOAM 任务有明确 artifacts、日志和物理约束，适合构建确定性验收，而不必承担模型训练成本。

## 8. 评测与安全：没有验证，技能会漂移

自进化系统的最大风险是“看似在学习，实际在漂移”。AgentBench、AgentBoard、WebArena、WebShop、SWE-bench、OSWorld、AppWorld、tau-bench、GAIA 等基准推动了多步 agent 评测；AgentRewardBench、ATBench、BenchTrace、ContextBench、EvoMemBench 和 MemoryAgentBench 则把注意力转向过程级评估、轨迹级安全、上下文检索质量、记忆更新和失败避免率。

技能库还带来安全和供应链问题。Agent Skills survey 与 SoK: Agentic Skills 提到技能包可能携带 prompt injection、恶意脚本、越权工具调用、依赖污染和数据泄露风险。因此技能生命周期必须包含 provenance、权限、测试、版本、回滚和隔离策略。对本项目而言，技能不应直接授权破坏性 shell 操作；技能更新必须通过 held-out benchmark 和 artifact contract 验证；技能适用范围要写清楚，不让 blastFoam 特定经验误伤普通 OpenFOAM 配置。

## 9. 对 PrincipiaBlastFoam 第 4 章的写作建议

第 4 章可以把系统定位为“环境证据驱动的外部技能自进化”，而不是泛称模型自学习。建议采用如下论证链：

1. Chapter 3 端到端评测产生了真实失败轨迹，这些轨迹包含任务、生成文件、OpenFOAM 日志、后处理 artifacts 和评分器反馈。
2. Chapter 4 从这些失败证据中抽取两级技能：抽象技能提供跨任务原则，具体 verifier skill 提供触发条件、检查命令和验收规则。
3. 技能注入后在 held-out realistic benchmark 上评估，避免用同一批失败案例自证有效。
4. 结果显示具体可验证技能收益更稳定，说明工程 agent 的自进化不应只依赖自然语言反思，而应绑定可执行检查和 artifact contract。
5. 未来工作可引入 SkillOS/SkillAdaptor 思路：自动定位失败步骤、对技能进行小步更新、用回归集接受或拒绝更新，并维护技能版本。

## 10. 研究空白

第一，技能抽取的因果归因仍弱。很多方法能从轨迹总结经验，但很难证明某条经验导致后续成功。第二，技能评估容易过拟合 benchmark。技能在相似任务上提升，不代表跨求解器、跨物理模型或跨项目也安全。第三，记忆和技能之间缺少统一治理。长期记忆可以诱导策略偏置，技能也可能固化过时经验，需要冲突检测和遗忘机制。第四，轨迹数据标准尚未统一。不同 agent 记录 thought/action/observation/tool/error 的格式不同，阻碍跨系统复用。第五，安全研究刚开始关注技能供应链，工程落地需要权限模型、沙箱、签名、审计和回滚。

## 11. 推荐阅读路径

入门先读 ReAct、Reflexion、Generative Agents、Voyager、ExpeL 和 A Survey on LLM-based Autonomous Agents。理解自进化框架读 A Survey on Self-Evolution of LLMs 与 A Survey of Self-Evolving Agents。聚焦技能沉淀读 AutoSkill、Trace2Skill、SkillOS、CoEvoSkills、SkillFoundry、SkillLens、SkillAdaptor、Agent Skills for LLMs 和 SoK: Agentic Skills。聚焦轨迹数据读 ReST meets ReAct、Learning to Retrieve from Agent Trajectories、Trajectory-Informed Memory Generation、ReasoningBank、BenchTrace。聚焦工程评测读 AgentBench、AgentBoard、SWE-bench、OSWorld、AppWorld、AgentRewardBench、ATBench、ContextBench、EvoMemBench。
"""


def make_papers_readme() -> str:
    arxiv_core = [
        p for p in PAPERS
        if "arxiv.org/abs/" in p["url"]
        and p["theme"] in {"skills", "trajectory", "reflection_memory", "self_training", "coding_science", "survey"}
    ][:35]
    downloaded = sorted((ROOT / "papers").glob("*.pdf"))
    lines = [
        "# Open-access PDF 建议清单",
        "",
        f"本目录用于存放开放获取 PDF。当前已下载核心 PDF {len(downloaded)} 个；下表仍保留扩展下载清单，后续可按需用 `curl -L -o` 补充。",
        "",
    ]
    if downloaded:
        lines.extend(["## 已下载 PDF", ""])
        for pdf in downloaded:
            lines.append(f"- `{pdf.name}`")
        lines.append("")
    lines.extend([
        "## 建议补充下载清单",
        "",
        "| 文件名建议 | PDF 链接 |",
        "|---|---|",
    ])
    for p in arxiv_core:
        arxiv_id = p["url"].rstrip("/").split("/")[-1]
        fname = f"{p['year']}_{slugify(p['title'])[:80]}.pdf"
        lines.append(f"| `{fname}` | https://arxiv.org/pdf/{arxiv_id} |")
    return "\n".join(lines)


def main() -> None:
    data_dir = ROOT / "data"
    write(data_dir / "manual_seed_papers.json", json.dumps(PAPERS, ensure_ascii=False, indent=2))
    write(ROOT / "README.md", make_readme())
    write(ROOT / "search_log.md", make_search_log())
    write(ROOT / "papers_catalog.md", make_catalog())
    write(ROOT / "references.bib", make_bibtex())
    write(ROOT / "agent_self_evolution_review.md", make_review())
    write(data_dir / "openalex_top_titles.md", make_openalex_summary())
    write(ROOT / "papers" / "README.md", make_papers_readme())
    write(ROOT / "figures" / "README.md", make_figures_readme())
    for name, content in make_figures().items():
        write(ROOT / "figures" / name, content)

    summary = {
        "paper_count": len(PAPERS),
        "themes": dict(Counter(p["theme"] for p in PAPERS)),
        "years": dict(Counter(str(p["year"]) for p in PAPERS)),
        "outputs": [
            "README.md",
            "search_log.md",
            "papers_catalog.md",
            "references.bib",
            "agent_self_evolution_review.md",
            "data/manual_seed_papers.json",
            "data/openalex_top_titles.md",
            "papers/README.md",
            "figures/README.md",
            "figures/prompts.txt",
            "figures/self_evolution_closed_loop.png",
            "figures/skill_lifecycle.png",
            "figures/self_evolution_closed_loop.mmd",
            "figures/skill_lifecycle.mmd",
        ],
    }
    write(ROOT / "data" / "generation_summary.json", json.dumps(summary, ensure_ascii=False, indent=2))
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
