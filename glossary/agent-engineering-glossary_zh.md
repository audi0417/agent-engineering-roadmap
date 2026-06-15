# Agent Engineering Glossary 繁中版

## Agent

朝著明確目標完成任務的系統。它通常會結合 context、model call、tools、memory、workflow 和 evaluation。

## Agentic Workflow

有控制流程的 agent 任務鏈。通常包含 plan、act、observe、review 和 final output。

## Context Window

模型一次呼叫可以看到的最大文字或 token 範圍。

## Context Engineering

選擇、組織、壓縮、檢索與更新模型可見資訊的工程方法。

## Tool Calling

讓模型或 agent 呼叫外部 function、API、database 或 service 的能力。

## MCP

Model Context Protocol。用標準化方式把 model/agent 連到外部 tools、resources、prompts 的協定。

## Memory

可以跨回合、任務、使用者或 agent 重複使用的持久 context。

## Short-Term Memory

單一 session 或 workflow 內使用的暫時任務狀態。

## Long-Term Memory

未來 session 仍可能使用的持久資訊。

## Semantic Memory

事實、概念、偏好等知識型記憶。

## Episodic Memory

事件型記憶，比如做過哪些 action、做過哪些 decision、和使用者互動過什麼。

## Shared Memory

多個 agents 在 workflow 或 colony 中可共同讀寫的記憶。

## RAG

Retrieval-Augmented Generation。先檢索外部資訊，再把資訊交給模型產生答案的方法。

## Embedding

把文字、圖片或其他資料表示成 vector，讓 similarity search 可以運作。

## Vector Database

專門儲存 embedding 並搜尋相似項目的資料庫。

## Planner

把任務拆成步驟的 component 或 agent。

## Executor

執行 plan step 或 tool call 的 component 或 agent。

## Reviewer

根據 rubric 檢查 draft 或中間結果的 component 或 agent。

## Evaluator

用 expected criteria 評估 agent 行為的 component、model、script 或 human process。

## Human-in-the-loop

讓人類參與 review、approval、correction 或 escalation 的設計。

## Approval Gate

高風險 action 執行前必須經過人類批准的檢查點。

## Prompt Injection

不可信內容試圖覆蓋系統原本指令的攻擊或指令衝突。

## Guardrail

讓 agent 留在允許行為範圍內的 rule、validator、policy 或 runtime check。

## Evaluation Suite

用來測量 agent quality、safety、format、tool use 和 regression behavior 的測試集合。

## Regression

原本會過的行為，因為某次修改而失敗。

## Observability

可以檢查 model call、tool call、memory operation、error、cost、latency 與 decision 的能力。

## Agent Colony

一組 specialized agents，透過共同 goal、memory、workflow、evaluation 與 governance 來協作。
