# Papers 論文閱讀清單

[English](README.md)

這個資料夾把 Agent Engineering 的實作教材，連到各大研究團隊與大廠論文。

目標不是收集所有論文，而是幫學習者看懂 tools、memory、workflow、multi-agent、evaluation、safety、production agent 背後的研究脈絡。

## PDF 政策

這個 repo 放官方論文頁與 PDF 連結，但不把 PDF 檔案直接 commit 進來。

原因：

- arXiv、ACM、ACL、OpenReview、公司網站與 conference proceedings 的授權規則不同
- 外部官方連結比較容易維護
- 原創導讀比複製 PDF 更有教學價值

新增論文時，請放標題、年份、組織、官方連結、PDF 連結、對應章節，以及自己寫的工程導讀。

## 從這裡開始

| 檔案 | 用途 |
|---|---|
| [Paper Reading Roadmap](paper-reading-roadmap.md) | 依章節整理的論文地圖 |
| [Paper Notes](paper-notes/README.md) | 重點論文工程導讀 |
| [Paper Reading Roadmap zh](paper-reading-roadmap_zh.md) | 繁體中文論文閱讀路線 |
| [Paper Notes zh](paper-notes/README_zh.md) | 繁體中文重點論文導讀 |

## 推薦論文

| 主題 | 論文 | 年份 | 組織 | 為什麼重要 |
|---|---|---:|---|---|
| Browser agent | [WebGPT: Browser-assisted question-answering with human feedback](https://arxiv.org/abs/2112.09332) | 2021 | OpenAI | 早期 browsing agent、引用收集與 human feedback 代表作。 |
| Reasoning and acting | [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) | 2022 | Google Research / Princeton | tool agent 幾乎都繞不開的 reasoning + action 起點。 |
| Safety training | [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) | 2022 | Anthropic | 理解 safety principles、critique、revision、AI feedback 的重要背景。 |
| Tool use | [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) | 2023 | Meta AI | 說明模型如何學會何時呼叫 API、如何使用工具結果。 |
| Reflection | [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | 2023 | Princeton / Northeastern | 把 feedback、episodic memory、下一次決策改善連在一起。 |
| Self-improvement | [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) | 2023 | Allen AI / CMU / UW / others | reviewer agent 與 iterative refinement 的研究背景。 |
| Agent memory | [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) | 2023 | Stanford / Google | observation、memory、reflection、planning 的經典 agent architecture。 |
| Planning | [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) | 2023 | Princeton / Google DeepMind | 把推理路徑當成搜尋樹，適合接 workflow / graph agent。 |
| Lifelong agent | [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | 2023 | NVIDIA / Caltech / UT Austin / Stanford / ASU | skill library、automatic curriculum、environment feedback、self-verification。 |
| RAG foundation | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | 2020 | Meta AI / UCL / NYU / FAIR | RAG 的核心起點：parametric memory + non-parametric memory。 |
| Long context | [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) | 2023 | Stanford / UC Berkeley / Samaya AI | 說明 long context 不等於可靠 retrieval 或 memory。 |
| Multi-agent framework | [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) | 2023 | Microsoft Research | 把 multi-agent conversation、tools、human input 與 framework design 連起來。 |
| Multi-agent software | [ChatDev: Communicative Agents for Software Development](https://arxiv.org/abs/2307.07924) | 2023 | Tsinghua / OpenBMB | role-based multi-agent software development workflow 代表案例。 |
| Agent benchmark | [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688) | 2023 | Tsinghua / Ohio State / UC Berkeley | 專門評估 LLM-as-agent 的 benchmark。 |
| Agent survey | [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) | 2023 | Renmin University / others | 建立 LLM autonomous agent 的完整分類地圖。 |
| RAG eval | [RAGAS: Automated Evaluation of Retrieval Augmented Generation](https://arxiv.org/abs/2309.15217) | 2023 | Exploding Gradients / CardiffNLP | production RAG agent 必須懂的評估維度。 |
| Software agents | [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) | 2024 | Princeton | 說明 agent-computer interface 為什麼會影響 coding agent 表現。 |
| Prompt injection | [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499) | 2023 | NTU / Zhejiang / others | 補 security module 與 tool-result injection threat model。 |
| Deceptive behavior | [Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://arxiv.org/abs/2401.05566) | 2024 | Anthropic / collaborators | 說明 safety training 不一定能移除 hidden-trigger 行為。 |
| LLM-as-judge | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) | 2023 | LMSYS / UC Berkeley | LLM-as-a-judge 的重要起點，也提醒 bias 與限制。 |

## 建議閱讀順序

1. ReAct
2. Toolformer
3. WebGPT
4. RAG
5. Lost in the Middle
6. Generative Agents
7. Reflexion
8. Self-Refine
9. Tree of Thoughts
10. Voyager
11. AutoGen
12. AgentBench
13. RAGAS
14. SWE-agent
15. Prompt Injection
16. Constitutional AI
17. Sleeper Agents

## 論文筆記模板

```text
Title:
Year:
Organization:
Official link:
PDF link:
Topic:
Problem:
Key idea:
System component:
Engineering takeaway:
Possible implementation:
Limitations:
Related roadmap modules:
Related examples:
```

## 貢獻規則

新增論文時：

- 放官方 paper page
- 如果有官方 PDF，放 PDF 連結
- 摘要要自己寫
- 說明工程啟發
- 至少對應一個課程章節或 example
- 不要複製 abstract、圖表或 PDF 原文內容進 repo
