# Agent Engineering 完整課程

這份課程把 repository 變成一套完整教材，目標是教你打造有用、可檢查、能逐步走向 production 的 AI Agent。

## 一句話總結

Agent 不是比較長 prompt 的 Chatbot。Agent 其實是一個任務系統，把 goal、context、tools、memory、workflow、evaluation 和 human approval 組在一起。

## 適合誰

- 正在做 LLM app 的軟體工程師
- 想從 demo 走到 production workflow 的 AI engineer
- 正在設計 agentic product 的 founder 或產品團隊
- 想要工程化地理解 agent system 的研究者
- 想照著路線學完整 Agent Engineering 的學生

## 先備能力

你需要知道：

- 基礎 Python
- HTTP API 與 JSON
- command line 基本操作
- prompt、token、context window、embedding 等 LLM 基礎概念

你不需要一開始就懂所有 agent framework。先懂心智模型，再選工具。

## 學習 Track

| Track | 適合對象 | 路線 |
|---|---|---|
| Beginner Builder | 剛開始學 Agent | Modules 00-05, Labs 00-05, Examples 01-04 |
| Agent Engineer | 要做真實 workflow | Modules 00-09, Labs 00-09, Examples 01-08 |
| Domain Builder | 做 healthcare、finance、enterprise | Modules 00-12, domain tracks, capstone |
| Production Lead | 負責部署與治理 | Modules 08-09, evaluation harness, safety templates |

## 課程地圖

![Agent Engineering Course Map](assets/diagrams/course-map.svg)

```text
Part 1: Foundations
  00 Agent Foundations
  01 Agent Architecture
  02 Tool Calling

Part 2: Context And Knowledge
  03 Memory Systems
  04 RAG And Embeddings

Part 3: Control
  05 Workflow Orchestration
  06 Graph-based Agents
  07 Multi-Agent Systems
  08 Human-in-the-loop

Part 4: Production
  09 Production Agent Systems
  12 Agent Frameworks Comparison

Part 5: Domain Systems
  10 Healthcare Agents
  11 Finance Agents
  Capstone Agent Colony
```

## 怎麼學

每個 module 建議這樣走：

1. 讀 curriculum chapter。
2. 讀對應 roadmap level。
3. 跑最接近的 example。
4. 完成 lab。
5. 回答 assessment 問題。
6. 執行 `python scripts/verify_examples.py`。
7. 在進下一章前，替範例加一個小改進。

## 完課標準

你完成這門課時，應該要能做到：

- 定義 agent 的 goal、scope、input、output 和 tools
- 建立一個單一任務 agent，並輸出 structured result
- 加入 tool validation 與 approval gate
- 設計 memory write、retrieval、delete 與 audit 規則
- 建立 RAG pipeline，並評估 retrieval quality
- 編排 planner、executor、reviewer、evaluator stages
- 協調 multiple agents，但不失去控制權
- 在 shipping 前跑 evaluation suite
- 說明 prompt injection、data leakage、runaway cost、unsafe tool use 等 production 風險
- 完成 capstone project

## Repository 區塊

| 區塊 | 用途 |
|---|---|
| `curriculum/` | 概念章節 |
| `assets/` | 視覺圖表與教學圖片 |
| `roadmap/` | Level-by-level 學習里程碑 |
| `examples/` | 可執行最小實作 |
| `showcases/` | 第一次進 repo 就能跑的展示 demo |
| `labs/` | 引導式實作練習 |
| `teaching/` | 教學 audit、常見誤解、交付成果與 module blueprint |
| `lab-solutions/` | Labs 的解題骨架與預期 artifact |
| `lesson-plans/` | 每堂 90 分鐘、可直接上課的教案 |
| `patterns/` | 可重用架構模式 |
| `templates/` | 專案模板、安全模板、評估模板 |
| `assessments/` | 題庫與複習問題 |
| `projects/` | Capstone 與作品集專案 |
| `capstone-starter/` | 可執行的 final project starter scaffold |
| `glossary/` | Agent Engineering 術語 |

## 教學原則

每個主題都要回答四個問題：

- 如果沒有這個東西，系統會在哪裡壞掉？
- 最簡單的心智模型是什麼？
- 內部機制怎麼運作？
- 我們怎麼知道它安全而且有用？

如果一篇 lesson 回答不了這四個問題，它就還沒有完成。
