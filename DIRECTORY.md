# Directory

This file provides a structured index for the Agent Engineering Roadmap.

Use it to quickly navigate the curriculum, examples, architecture notes, papers, and domain tracks.

---

## Curriculum

| Module | English | 繁體中文 |
|---|---|---|
| 00 Agent Foundations | [English](curriculum/00-agent-foundations.md) | [繁體中文](curriculum/00-agent-foundations_zh.md) |
| 01 Agent Architecture | [English](curriculum/01-agent-architecture.md) | [繁體中文](curriculum/01-agent-architecture_zh.md) |
| 02 Tool Calling | [English](curriculum/02-tool-calling.md) | [繁體中文](curriculum/02-tool-calling_zh.md) |
| 03 Memory Systems | [English](curriculum/03-memory-systems.md) | [繁體中文](curriculum/03-memory-systems_zh.md) |
| 04 RAG and Embeddings | [English](curriculum/04-rag-and-embeddings.md) | [繁體中文](curriculum/04-rag-and-embeddings_zh.md) |
| 05 Workflow Orchestration | [English](curriculum/05-workflow-orchestration.md) | [繁體中文](curriculum/05-workflow-orchestration_zh.md) |
| 06 Graph-based Agents | [English](curriculum/06-graph-based-agents.md) | [繁體中文](curriculum/06-graph-based-agents_zh.md) |
| 07 Multi-Agent Systems | [English](curriculum/07-multi-agent-systems.md) | [繁體中文](curriculum/07-multi-agent-systems_zh.md) |
| 08 Human-in-the-loop | [English](curriculum/08-human-in-the-loop.md) | [繁體中文](curriculum/08-human-in-the-loop_zh.md) |
| 09 Production Agent Systems | [English](curriculum/09-production-agent-systems.md) | [繁體中文](curriculum/09-production-agent-systems_zh.md) |
| 10 Domain Agent: Healthcare | [English](curriculum/10-domain-agent-healthcare.md) | [繁體中文](curriculum/10-domain-agent-healthcare_zh.md) |
| 11 Domain Agent: Finance | [English](curriculum/11-domain-agent-finance.md) | [繁體中文](curriculum/11-domain-agent-finance_zh.md) |
| 12 Agent Frameworks Comparison | [English](curriculum/12-agent-frameworks-comparison.md) | [繁體中文](curriculum/12-agent-frameworks-comparison_zh.md) |
| 13 Agent Observability | [English](curriculum/13-agent-observability.md) | [繁體中文](curriculum/13-agent-observability_zh.md) |
| 14 Agent Security | [English](curriculum/14-agent-security.md) | [繁體中文](curriculum/14-agent-security_zh.md) |
| 15 Agent Cost And Latency Engineering | [English](curriculum/15-agent-cost-latency-engineering.md) | [繁體中文](curriculum/15-agent-cost-latency-engineering_zh.md) |
| 16 Durable Agent Runtime | [English](curriculum/16-durable-agent-runtime.md) | [繁體中文](curriculum/16-durable-agent-runtime_zh.md) |
| 17 MCP Modernization | [English](curriculum/17-mcp-modernization.md) | [繁體中文](curriculum/17-mcp-modernization_zh.md) |
| 18 Agent Memory Governance | [English](curriculum/18-agent-memory-governance.md) | [繁體中文](curriculum/18-agent-memory-governance_zh.md) |
| 19 Agent Identity And Permission | [English](curriculum/19-agent-identity-permission.md) | [繁體中文](curriculum/19-agent-identity-permission_zh.md) |
| 21 Agent Incident Response | [English](curriculum/21-agent-incident-response.md) | [繁體中文](curriculum/21-agent-incident-response_zh.md) |
| 22 Advanced Agent Evaluation | [English](curriculum/22-advanced-agent-evaluation.md) | [繁體中文](curriculum/22-advanced-agent-evaluation_zh.md) |
| 24 Agent Product UX | [English](curriculum/24-agent-product-ux.md) | [繁體中文](curriculum/24-agent-product-ux_zh.md) |
| 25 Enterprise Agent Operating Model | [English](curriculum/25-enterprise-agent-operating-model.md) | [繁體中文](curriculum/25-enterprise-agent-operating-model_zh.md) |

---

## Course

| File | Description |
|---|---|
| [Course](COURSE.md) | Complete syllabus, tracks, and graduation criteria |
| [Course zh](COURSE_zh.md) | 完整課綱、學習 track 與完課標準 |

---

## Visual Assets

| File | Description |
|---|---|
| [Visual Assets](assets/README.md) | Diagram index |
| [Course Map](assets/diagrams/course-map.svg) | Full course map |
| [Agent Loop](assets/diagrams/agent-loop.svg) | Minimal agent loop |
| [Tool And MCP Layer](assets/diagrams/tool-mcp-layer.svg) | Tool and MCP integration |
| [Memory System](assets/diagrams/memory-system.svg) | Agent memory policy flow |
| [Workflow Orchestration](assets/diagrams/workflow-orchestration.svg) | Planner, executor, reviewer, retry |
| [Agent Colony](assets/diagrams/agent-colony.svg) | Supervisor and specialists |
| [Production Stack](assets/diagrams/production-stack.svg) | Production evaluation and safety |
| [Memory Governance](assets/diagrams/memory-governance.svg) | Memory classification, redaction, audit, and deletion |
| [Permission Model](assets/diagrams/permission-model.svg) | Agent identity, scopes, authorization, and audit |
| [Incident Response](assets/diagrams/incident-response.svg) | Detection, containment, trace review, hotfix, and postmortem |
| [Release Gate](assets/diagrams/release-gate.svg) | Regression, safety, adversarial, trace, benchmark, and ops checks |

---

## Examples

| Example | Description |
|---|---|
| [01 Single Agent](examples/01-single-agent/README.md) | Build a simple research summary agent. |
| [02 Tool-Using Agent](examples/02-tool-using-agent/README.md) | Add external tools to an agent. |
| [03 MCP Agent](examples/03-mcp-agent/README.md) | Connect an agent to MCP-style tools. |
| [04 Memory Agent](examples/04-memory-agent/README.md) | Add memory to an agent. |
| [05 Multi-Agent Workflow](examples/05-multi-agent-workflow/README.md) | Coordinate multiple agents in a workflow. |
| [06 Agent Colony](examples/06-agent-colony/README.md) | Build a colony-style multi-agent system. |
| [07 Evaluation Harness](examples/07-evaluation-harness/README.md) | Run regression checks against agent behavior. |
| [08 Mini RAG](examples/08-mini-rag/README.md) | Inspect retrieval, grounded answers, and RAG evals. |
| [09 Graph Approval Agent](examples/09-graph-approval-agent/README.md) | Test graph transitions and human approval gates. |
| [10 Observable Agent](examples/10-observable-agent/README.md) | Inspect traces, guardrails, and replayable agent runs. |
| [11 Prompt Injection Defense](examples/11-prompt-injection-defense/README.md) | Block unsafe instructions in retrieved content. |
| [12 Cost-Aware Agent](examples/12-cost-aware-agent/README.md) | Route tasks by quality, cost, and latency constraints. |
| [13 Durable Workflow Agent](examples/13-durable-workflow-agent/README.md) | Checkpoint and resume long-running workflows. |
| [14 Modern MCP Gateway](examples/14-modern-mcp-gateway/README.md) | Model tools, resources, prompts, authorization, and elicitation. |
| [15 Memory Governance Agent](examples/15-memory-governance-agent/README.md) | Redact, merge, decay, and delete agent memories. |
| [16 Agent Permission System](examples/16-agent-permission-system/README.md) | Enforce agent identity, scopes, and access reviews. |
| [17 Advanced Eval Harness](examples/17-advanced-eval-harness/README.md) | Run regression, safety, adversarial, and golden trace release gates. |

## Incident Response

| File | Topic |
|---|---|
| [Agent Incident Playbook](incident-response/agent-incident-playbook.md) | Trace-driven containment, hotfix, and postmortem workflow |

## Product And Operating Model

| File | Topic |
|---|---|
| [Agent Product UX Checklist](product-ux/agent-product-ux-checklist.md) | Approval, visibility, evidence, control, and recovery UX |
| [Enterprise Agent Operating Checklist](operating-model/enterprise-agent-operating-checklist.md) | Registry, owner, risk tier, review, and retirement workflow |

## Security

| File | Topic |
|---|---|
| [Prompt Injection Lab](security/prompt-injection-lab.md) | RAG and tool-result injection defense practice |

## Benchmarks

| File | Topic |
|---|---|
| [Benchmarks](benchmarks/README.md) | Lightweight behavior checks |
| [Benchmarks zh](benchmarks/README_zh.md) | 輕量行為檢查 |
| [Benchmark Runner](benchmarks/benchmark_runner.py) | Dependency-free benchmark script |

## Scripts And CI

| File | Description |
|---|---|
| [Verify Examples](scripts/verify_examples.py) | Runs all dependency-free examples and showcases |
| [Verify Examples Workflow](.github/workflows/verify-examples.yml) | GitHub Actions check for runnable course examples |

---

## Showcases

| Demo | Description |
|---|---|
| [Showcases](showcases/README.md) | Index of shareable demos |
| [Enterprise Support Agent](showcases/enterprise-support-agent/README.md) | Ticket routing and approval gates |
| [Finance Research Agent](showcases/finance-research-agent/README.md) | Finance research support with safety boundary |
| [Healthcare Agent Colony](showcases/healthcare-agent-colony/README.md) | Healthcare education boundary and escalation |

---

## Website And Launch

| File | Description |
|---|---|
| [Docs Site](docs/index.html) | Static GitHub Pages landing page |
| [Launch Kit](launch-kit/README.md) | Launch copy, topics, and checklist |
| [Launch Readiness](launch-kit/launch-readiness.md) | Public launch readiness checklist |
| [Social Posts](launch-kit/social-posts.md) | Ready-to-post launch copy |
| [Good First Issues](launch-kit/good-first-issues.md) | First contributor task index |
| [Changelog](CHANGELOG.md) | Release history and notable changes |
| [Release Checklist](release/RELEASE_CHECKLIST.md) | Release verification checklist |
| [v1.0 Readiness](release/V1_READINESS.md) | v1.0 readiness tracker |
| [Social Card](assets/social/agent-engineering-roadmap-2026.svg) | Share image for social posts |

---

## Labs

| Lab | Topic |
|---|---|
| [Labs Index](labs/README.md) | Guided lab sequence |
| [Lab 00](labs/lab-00-agent-spec.md) | Agent specification |
| [Lab 01](labs/lab-01-single-agent.md) | Single agent |
| [Lab 02](labs/lab-02-tool-calling.md) | Tool calling |
| [Lab 03](labs/lab-03-memory.md) | Memory |
| [Lab 04](labs/lab-04-rag.md) | RAG |
| [Lab 05](labs/lab-05-workflow.md) | Workflow |
| [Lab 06](labs/lab-06-graph-agent.md) | Graph agent |
| [Lab 07](labs/lab-07-multi-agent.md) | Multi-agent systems |
| [Lab 08](labs/lab-08-human-in-the-loop.md) | Human-in-the-loop |
| [Lab 09](labs/lab-09-evaluation.md) | Evaluation |
| [Lab 10](labs/lab-10-capstone-prep.md) | Capstone prep |
| [Lab Solution Guides](lab-solutions/README_zh.md) | Solution shapes and expected artifacts |

## Lab Solution Guides

| Lab | Guide |
|---|---|
| 00 | [Agent Spec](lab-solutions/lab-00-agent-spec/README.md) |
| 01 | [Single Agent](lab-solutions/lab-01-single-agent/README.md) |
| 02 | [Tool Calling](lab-solutions/lab-02-tool-calling/README.md) |
| 03 | [Memory](lab-solutions/lab-03-memory/README.md) |
| 04 | [RAG](lab-solutions/lab-04-rag/README.md) |
| 05 | [Workflow](lab-solutions/lab-05-workflow/README.md) |
| 06 | [Graph Agent](lab-solutions/lab-06-graph-agent/README.md) |
| 07 | [Multi-Agent](lab-solutions/lab-07-multi-agent/README.md) |
| 08 | [Human-in-the-loop](lab-solutions/lab-08-human-in-the-loop/README.md) |
| 09 | [Evaluation](lab-solutions/lab-09-evaluation/README.md) |
| 10 | [Capstone Prep](lab-solutions/lab-10-capstone-prep/README.md) |

## Teaching Layer

| File | Topic |
|---|---|
| [Teaching README](teaching/README_zh.md) | How to teach and study this course |
| [Study Group Kit](study-groups/README.md) | Cohort and workshop facilitation kit |
| [Study Group Kit zh](study-groups/README_zh.md) | 讀書會與 workshop 引導套件 |
| [Hung-Yi Lee Style Audit](teaching/hung-yi-lee-style-audit_zh.md) | Teaching-quality audit and gaps |
| [Module Teaching Blueprint](teaching/module-teaching-blueprint_zh.md) | Standard teaching structure for every module |
| [Misconception Map](teaching/misconception-map_zh.md) | Common wrong intuitions and correction checks |
| [Student Deliverables](teaching/student-deliverables_zh.md) | Required artifacts for each module |

---

## Lesson Plans

| Module | Lesson Plan |
|---|---|
| 00 | [Agent Foundations](lesson-plans/module-00-agent-foundations.md) |
| 01 | [Agent Architecture](lesson-plans/module-01-agent-architecture.md) |
| 02 | [Tool Calling](lesson-plans/module-02-tool-calling.md) |
| 03 | [Memory Systems](lesson-plans/module-03-memory-systems.md) |
| 04 | [RAG And Embeddings](lesson-plans/module-04-rag-and-embeddings.md) |
| 05 | [Workflow Orchestration](lesson-plans/module-05-workflow-orchestration.md) |
| 06 | [Graph-Based Agents](lesson-plans/module-06-graph-based-agents.md) |
| 07 | [Multi-Agent Systems](lesson-plans/module-07-multi-agent-systems.md) |
| 08 | [Human-In-The-Loop](lesson-plans/module-08-human-in-the-loop.md) |
| 09 | [Production Agent Systems](lesson-plans/module-09-production-agent-systems.md) |
| 10 | [Healthcare Agents](lesson-plans/module-10-healthcare-agents.md) |
| 11 | [Finance Agents](lesson-plans/module-11-finance-agents.md) |
| 12 | [Frameworks Comparison](lesson-plans/module-12-frameworks-comparison.md) |

---

## Roadmap

| Level | Topic |
|---|---|
| [Level 0](roadmap/level-0-ai-llm-fundamentals.md) | AI and LLM fundamentals |
| [Level 1](roadmap/level-1-single-agent.md) | Single agent |
| [Level 2](roadmap/level-2-tool-use.md) | Tool use |
| [Level 3](roadmap/level-3-mcp.md) | Model Context Protocol |
| [Level 4](roadmap/level-4-agent-memory.md) | Agent memory |
| [Level 5](roadmap/level-5-agent-workflow.md) | Agent workflow |
| [Level 6](roadmap/level-6-multi-agent-systems.md) | Multi-agent systems |
| [Level 7](roadmap/level-7-agent-colony.md) | Agent colony |
| [Level 8](roadmap/level-8-production-evaluation-safety.md) | Production, evaluation, and safety |

---

## Architecture

| File | Topic |
|---|---|
| [Colony Architecture](architecture/colony-architecture.md) | Agent colony system design |
| [Memory Architecture](architecture/memory-architecture.md) | Memory system design |
| [MCP Architecture](architecture/mcp-architecture.md) | MCP-style integration design |

---

## Templates

| File | Topic |
|---|---|
| [Templates](templates/README.md) | How to use the reusable templates |
| [Agent Spec](templates/agent-spec-template.md) | Define agent scope, tools, outputs, and evaluation |
| [Memory Policy](templates/memory-policy-template.md) | Decide what memory can be written, retrieved, and deleted |
| [Evaluation Suite](templates/evaluation-suite-template.yaml) | Create regression cases and scoring dimensions |
| [Safety Gate](templates/safety-gate-template.md) | Define approval, refusal, and logging rules |
| [MCP Server Template](templates/mcp-server-template.py) | Minimal MCP-style tool registry |
| [Agent Registry](templates/agent-registry-template.md) | Register agent owner, scopes, tools, data, evals, and operations |
| [Risk Assessment](templates/risk-assessment-template.md) | Classify risk and required controls before launch |
| [Deployment Review](templates/deployment-review-template.md) | Review release gate and operational readiness |

---

## Patterns

| File | Topic |
|---|---|
| [Patterns](patterns/README.md) | Agent architecture pattern catalog |
| [Patterns zh](patterns/README_zh.md) | Agent architecture pattern catalog 繁中版 |

---

## Assessments

| File | Topic |
|---|---|
| [Quiz Bank](assessments/quiz-bank.md) | Module review questions |
| [Rubrics](assessments/rubrics.md) | Specification, example, and production readiness rubrics |

---

## Projects

| File | Topic |
|---|---|
| [Capstone Agent Colony](projects/capstone-agent-colony.md) | Final course project |
| [Capstone Starter](capstone-starter/README.md) | Runnable starter scaffold for final project |
| [Portfolio Projects](projects/portfolio-projects.md) | Suggested project ideas |

---

## Glossary

| File | Topic |
|---|---|
| [Glossary](glossary/agent-engineering-glossary.md) | Agent engineering terms |
| [Glossary zh](glossary/agent-engineering-glossary_zh.md) | Agent engineering terms 繁中版 |

---

## Domain Tracks

| Track | File |
|---|---|
| Healthcare | [Healthcare Agent Colony](healthcare/healthcare-agent-colony.md) |
| Taiwan Health MCP | [Taiwan Health MCP](healthcare/taiwan-health-mcp.md) |
| Finance Agent Colony | [Finance Agent Colony](finance/finance-agent-colony.md) |
| Quantitative Research Agent | [Quantitative Research Agent](finance/quantitative-research-agent.md) |

## Domain Casebooks

| Domain | File |
|---|---|
| Healthcare | [Healthcare Casebook](domain-casebooks/healthcare-casebook.md) |
| Finance | [Finance Casebook](domain-casebooks/finance-casebook.md) |
| Enterprise | [Enterprise Casebook](domain-casebooks/enterprise-casebook.md) |

---

## Papers

| File | Description |
|---|---|
| [Papers](papers/README.md) | Recent papers related to Agent Engineering |
| [Papers zh](papers/README_zh.md) | 論文閱讀清單繁中版 |
| [Paper Reading Roadmap](papers/paper-reading-roadmap.md) | Papers mapped to course modules and examples |
| [Paper Reading Roadmap zh](papers/paper-reading-roadmap_zh.md) | 依課程章節整理的繁中論文閱讀路線 |
| [Paper Notes](papers/paper-notes/README.md) | Short engineering notes for key papers |
| [Paper Notes zh](papers/paper-notes/README_zh.md) | 繁中重點論文工程導讀 |

---

## Resources

| File | Description |
|---|---|
| [Awesome Resources](resources/awesome-resources.md) | Curated learning resources |
| [Open Source Agent Projects](resources/open-source-agent-projects.md) | Curated open-source agent ecosystem map |
| [Agent Framework Selection Matrix](resources/agent-framework-selection-matrix.md) | Choose frameworks by engineering tradeoff |
| [How To Read Open Source Agent Repositories](resources/how-to-read-open-source-agent-repos.md) | Repository reading method for architecture learning |
| [DeepEval And RAGAS Evaluation Frameworks](resources/eval-frameworks-deepeval-ragas.md) | Practical guide to LLM and RAG evaluation frameworks |
| [Content Design Principles](resources/content-design-principles.md) | Internal rules for original educational content |
| [Content Design Principles zh](resources/content-design-principles_zh.md) | 原創內容設計原則繁中版 |
