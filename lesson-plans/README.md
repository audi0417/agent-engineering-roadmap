# Agent Engineering Lesson Plans

這個資料夾是「可直接拿來上課」的教案層。

好，前面的 `curriculum/` 比較像課本，`labs/` 比較像練習單。那 `lesson-plans/` 是什麼呢？它其實就是老師上課時手上那份流程表而已：這堂課先講什麼、demo 什麼、學生做什麼、怎麼檢查他到底懂不懂。

## 使用方式

每份教案都以 90 分鐘課程設計，但也可以拆成兩堂 45 分鐘。

建議流程：

1. 課前請學生讀對應 `curriculum/` 章節。
2. 課堂先用 10 分鐘建立問題意識。
3. 用 20-30 分鐘講核心機制。
4. 用 15-20 分鐘做 live demo。
5. 用 20 分鐘讓學生做 lab。
6. 最後 10 分鐘做 assessment 與 recap。

## 教案列表

| Module | 教案 | 對應內容 |
|---|---|---|
| 00 | [Agent Foundations](module-00-agent-foundations.md) | agent vs chatbot, agent loop, specification |
| 01 | [Agent Architecture](module-01-agent-architecture.md) | role, prompt, schema, state, boundaries |
| 02 | [Tool Calling](module-02-tool-calling.md) | tool schema, validation, risk, logging |
| 03 | [Memory Systems](module-03-memory-systems.md) | memory policy, retrieval, deletion, audit |
| 04 | [RAG And Embeddings](module-04-rag-and-embeddings.md) | retrieval, chunking, citations, eval |
| 05 | [Workflow Orchestration](module-05-workflow-orchestration.md) | planner, executor, reviewer, retry |
| 06 | [Graph-Based Agents](module-06-graph-based-agents.md) | state, edges, branches, failure paths |
| 07 | [Multi-Agent Systems](module-07-multi-agent-systems.md) | supervisor, specialists, routing, conflict |
| 08 | [Human-In-The-Loop](module-08-human-in-the-loop.md) | approval gates, escalation, audit |
| 09 | [Production Agent Systems](module-09-production-agent-systems.md) | eval, observability, cost, security |
| 10 | [Healthcare Agents](module-10-healthcare-agents.md) | safety boundary, education vs advice |
| 11 | [Finance Agents](module-11-finance-agents.md) | research vs recommendation, risk controls |
| 12 | [Frameworks Comparison](module-12-frameworks-comparison.md) | choosing frameworks by system need |

## 教學檢核

一堂課算完成，不是因為老師講完了，而是學生能做出以下事情：

- 用一句話說出這堂課解決的問題
- 畫出最小架構圖
- 修改一個 runnable example
- 說出至少一個 failure mode
- 寫出一個 eval case 或 approval rule

如果學生只會背名詞，不會畫流程、不會跑範例、不會說哪裡會壞，那這堂課還沒有真的完成。
