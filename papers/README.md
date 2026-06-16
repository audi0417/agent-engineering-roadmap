# Papers

[繁體中文](README_zh.md)

This folder connects the hands-on Agent Engineering Roadmap with research papers from major labs, universities, and open research communities.

The goal is not to collect every paper. The goal is to help learners understand the research lineage behind tools, memory, workflow, multi-agent systems, evaluation, safety, and production agents.

## PDF Policy

This repository links to official paper pages and PDF URLs, but does not commit PDF files.

Reasons:

- paper licenses differ across arXiv, ACM, ACL, OpenReview, company sites, and conference proceedings
- external official links are easier to keep current
- original course notes are more useful than copied PDFs

When adding a paper, include the title, year, organization, official link, PDF link when available, related modules, and an original engineering summary.

## Start Here

| File | Purpose |
|---|---|
| [Paper Reading Roadmap](paper-reading-roadmap.md) | Chapter-by-chapter paper map |
| [Paper Notes](paper-notes/README.md) | Short engineering notes for key papers |
| [Paper Reading Roadmap zh](paper-reading-roadmap_zh.md) | 繁體中文論文閱讀路線 |
| [Paper Notes zh](paper-notes/README_zh.md) | 繁體中文重點論文導讀 |

## Recommended Papers

| Topic | Paper | Year | Organization | Why it matters |
|---|---|---:|---|---|
| Browser agent | [WebGPT: Browser-assisted question-answering with human feedback](https://arxiv.org/abs/2112.09332) | 2021 | OpenAI | Early reference for browsing agents, citation collection, and human feedback. |
| Reasoning and acting | [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) | 2022 | Google Research / Princeton | Foundation for interleaving reasoning traces and actions. |
| Safety training | [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) | 2022 | Anthropic | Important background for safety principles, critique, revision, and AI feedback. |
| Tool use | [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) | 2023 | Meta AI | Shows how language models can learn when and how to call APIs. |
| Reflection | [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | 2023 | Princeton / Northeastern | Connects feedback, episodic memory, and better future agent behavior. |
| Self-improvement | [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) | 2023 | Allen AI / CMU / UW / others | Background for reviewer agents and iterative output improvement. |
| Agent memory | [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) | 2023 | Stanford / Google | Classic observation, memory, reflection, and planning architecture. |
| Planning | [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) | 2023 | Princeton / Google DeepMind | Introduces search over reasoning paths for harder planning tasks. |
| Lifelong agent | [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | 2023 | NVIDIA / Caltech / UT Austin / Stanford / ASU | Skill library, automatic curriculum, environment feedback, and self-verification. |
| RAG foundation | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | 2020 | Meta AI / UCL / NYU / FAIR | Core paper for parametric plus non-parametric memory. |
| Long context | [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) | 2023 | Stanford / UC Berkeley / Samaya AI | Shows why long context is not the same as reliable retrieval or memory. |
| Multi-agent framework | [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) | 2023 | Microsoft Research | Connects multi-agent conversation patterns, tools, humans, and framework design. |
| Multi-agent software | [ChatDev: Communicative Agents for Software Development](https://arxiv.org/abs/2307.07924) | 2023 | Tsinghua / OpenBMB | Role-based multi-agent software development workflow. |
| Agent benchmark | [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688) | 2023 | Tsinghua / Ohio State / UC Berkeley | Evaluates LLMs as agents across interactive environments. |
| Agent survey | [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) | 2023 | Renmin University / others | Broad taxonomy for LLM-based autonomous agents. |
| RAG eval | [RAGAS: Automated Evaluation of Retrieval Augmented Generation](https://arxiv.org/abs/2309.15217) | 2023 | Exploding Gradients / CardiffNLP | Practical reference for RAG evaluation dimensions. |
| Software agents | [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) | 2024 | Princeton | Shows why the interface between agent and computer matters. |
| Prompt injection | [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499) | 2023 | Nanyang Technological University / Zhejiang University / others | Useful for security modules and tool-result injection threat modeling. |
| Deceptive behavior | [Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://arxiv.org/abs/2401.05566) | 2024 | Anthropic / collaborators | Shows why safety testing should include hidden-trigger and persistence risks. |
| LLM-as-judge | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) | 2023 | LMSYS / UC Berkeley | Foundation for using model judges while understanding bias and limits. |

## Reading Order

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

## Paper Note Template

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

## Contribution Rule

When adding a new paper:

- link to the official paper page
- link to the official PDF only when available
- write your own summary
- explain the engineering implication
- connect it to at least one course module or example
- do not copy abstracts, figures, or PDF contents into this repository
