# Agent Engineering Patterns

Pattern 是常見 agent 設計問題的可重用解法。

你可以把這份 catalog 當成「看到症狀時，要選哪種架構」的索引。

## Pattern 索引

| Pattern | 什麼時候用 | 什麼時候不要用 |
|---|---|---|
| Single-Purpose Agent | 一個窄任務就夠 | 任務需要外部 action |
| Tool-Using Agent | 模型需要外部能力 | 工具有高風險副作用但沒有 approval gate |
| RAG Agent | 答案依賴外部知識 | Retrieval quality 無法評估 |
| Memory Agent | 穩定 context 需要跨 session 保存 | 資訊敏感或不穩定 |
| Planner-Executor | 任務有多步驟 | 任務簡單到一次 call 就能完成 |
| Reviewer-Evaluator | 輸出前要先檢查品質 | Rubric 很模糊 |
| Router-Specialist | 不同任務需要不同 handler | Routing 模糊且沒有測試 |
| Supervisor Multi-Agent | 多個 specialists 需要合作 | 沒有人負責 final answer |
| Human Approval Gate | 行動高風險或不可逆 | 行動低風險且頻繁 |
| Evaluation Harness | 需要 regression protection | 沒有定義 expected behavior |

## 最重要的觀念

不要因為 pattern 聽起來高級就使用它。

比如說，一個分類任務用 single-purpose agent 就可以解決，你硬要做 multi-agent，通常只是把 debugging 變困難而已。Agent Engineering 的重點不是炫，是控制。

## Pattern 選擇法

先問三個問題：

1. 這個任務需要外部資訊嗎？需要的話，考慮 RAG 或 tool use。
2. 這個任務需要跨 session 記住東西嗎？需要的話，考慮 memory。
3. 這個任務如果做錯會不會有高風險？會的話，先加 approval gate 和 evaluation。

如果三個答案都是 no，先做 single-purpose agent 就好。

## 常見錯誤

- 把 workflow 問題誤解成 prompt 問題
- 把 retrieval 問題誤解成 model 能力問題
- 把 memory 當成無限文字倉庫
- 以為多 agent 自動比單 agent 強
- 沒有 evaluation 就換模型或改 prompt

## 實作順序

```text
Single-purpose agent
   ↓
Tool use
   ↓
Memory or RAG
   ↓
Workflow
   ↓
Evaluation
   ↓
Human approval
   ↓
Multi-agent
```

你可能會想說，為什麼 multi-agent 放這麼後面？因為多一個 agent，就多一個 failure mode。你先把單一 agent、tool、memory、evaluation 控好，再加多 agent，系統才不會變成大家一起失控。
