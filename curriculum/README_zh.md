# Agent Engineering Curriculum

[English](README.md)

這份課程將 Agent Engineering 的核心主題，重新整理成原創、結構化的學習計畫。

目標是幫助學習者從基礎 Agent 概念，一路進階到可部署的 Multi-Agent Systems 與 Agent Colony。

---

## 課程結構

| Module | 主題 | 目標 |
|---|---|---|
| 00 | Agent Foundations | 理解 Agent 是什麼，以及它和 Chatbot 的差異 |
| 01 | Agent Architecture | 學習 Agent 系統的核心組件 |
| 02 | Tool Calling | 讓 Agent 安全地呼叫外部工具 |
| 03 | Memory Systems | 設計短期、長期、使用者與共享記憶 |
| 04 | RAG and Embeddings | 將 Agent 連接到知識庫與檢索流程 |
| 05 | Workflow Orchestration | 建立可控的 Planning、Execution 與 Review Flow |
| 06 | Graph-based Agents | 將 Agent Workflow 建模成 Graph 與 State Machine |
| 07 | Multi-Agent Systems | 透過結構化協作協調多個專家 Agent |
| 08 | Human-in-the-loop | 加入人工審核、回饋與升級機制 |
| 09 | Production Agent Systems | 加入評估、觀測、安全與部署模式 |
| 10 | Domain Agent: Healthcare | 建立具備安全邊界的 Healthcare Agent Workflow |
| 11 | Domain Agent: Finance | 建立具備風險控管的 Finance Research Agent |
| 12 | Agent Frameworks Comparison | 比較常見 Agent Framework 以及適用時機 |
| 13 | Agent Observability | Trace、replay、debug production agent runs |
| 14 | Agent Security | 防守 prompt injection、不安全工具與 memory leakage |
| 15 | Agent Cost And Latency Engineering | 依 budget、latency、quality needs 做 task routing |
| 16 | Durable Agent Runtime | Checkpoint、resume、recover long-running workflows |
| 17 | MCP Modernization | 使用 tools、resources、prompts、authorization、elicitation |

---

## 學習理念

這份課程遵守三個原則：

1. 先建立簡單 Agent，再加入工具。
2. 先加入 Memory 與 Workflow，再加入多 Agent。
3. Production Safety 應該是系統設計的一部分，而不是最後才補上。

---

## 建議學習路線

```text
Foundations
   ↓
Architecture
   ↓
Tool Calling
   ↓
Memory
   ↓
RAG
   ↓
Workflow
   ↓
Graph-based Agents
   ↓
Multi-Agent Systems
   ↓
Human Feedback
   ↓
Production
   ↓
Domain Applications
```

---

## 如何使用這份課程

每個 module 建議包含：

- goal
- why it matters
- mental model
- core concepts
- architecture diagram
- hands-on exercise
- checklist
- common mistakes
- outcome

---

## 狀態

課程目前包含概念章節、可執行 examples、guided labs、patterns、templates、assessments、glossary 與 capstone project。

---

## Module 與實作對照

| Module | Read | Run | Practice | Assess |
|---|---|---|---|---|
| 00 | `00-agent-foundations_zh.md` | - | `labs/lab-00-agent-spec.md` | `assessments/quiz-bank.md` |
| 01 | `01-agent-architecture_zh.md` | `examples/01-single-agent` | `labs/lab-01-single-agent.md` | `assessments/rubrics.md` |
| 02 | `02-tool-calling_zh.md` | `examples/02-tool-using-agent` | `labs/lab-02-tool-calling.md` | `assessments/quiz-bank.md` |
| 03 | `03-memory-systems_zh.md` | `examples/04-memory-agent` | `labs/lab-03-memory.md` | `templates/memory-policy-template.md` |
| 04 | `04-rag-and-embeddings_zh.md` | `examples/08-mini-rag` | `labs/lab-04-rag.md` | retrieval eval cases |
| 05 | `05-workflow-orchestration_zh.md` | `examples/05-multi-agent-workflow` | `labs/lab-05-workflow.md` | workflow review rubric |
| 06 | `06-graph-based-agents_zh.md` | `examples/09-graph-approval-agent` | `labs/lab-06-graph-agent.md` | graph design review |
| 07 | `07-multi-agent-systems_zh.md` | `examples/06-agent-colony` | `labs/lab-07-multi-agent.md` | routing tests |
| 08 | `08-human-in-the-loop_zh.md` | `examples/09-graph-approval-agent` | `labs/lab-08-human-in-the-loop.md` | approval policy review |
| 09 | `09-production-agent-systems_zh.md` | `examples/07-evaluation-harness`, `examples/09-graph-approval-agent` | `labs/lab-09-evaluation.md` | regression suite |
| 10 | `10-domain-agent-healthcare_zh.md` | `examples/06-agent-colony` | domain safety plan | production rubric |
| 11 | `11-domain-agent-finance_zh.md` | `examples/06-agent-colony` | domain risk plan | production rubric |
| 12 | `12-agent-frameworks-comparison_zh.md` | `capstone-starter` | `labs/lab-10-capstone-prep.md` | architecture review |
| 13 | `13-agent-observability_zh.md` | `examples/10-observable-agent` | trace review | incident replay |
| 14 | `14-agent-security_zh.md` | `examples/11-prompt-injection-defense` | `security/prompt-injection-lab.md` | security eval cases |
| 15 | `15-agent-cost-latency-engineering_zh.md` | `examples/12-cost-aware-agent` | routing budget review | cost and latency checks |
| 16 | `16-durable-agent-runtime_zh.md` | `examples/13-durable-workflow-agent` | checkpoint review | resume test |
| 17 | `17-mcp-modernization_zh.md` | `examples/14-modern-mcp-gateway` | gateway policy review | authorization and elicitation tests |

---

## 完成路線

```text
讀一個 module
   ↓
跑最接近的 example
   ↓
完成 lab
   ↓
回答 review questions
   ↓
更新你的 capstone design
```
