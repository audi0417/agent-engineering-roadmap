# 範例 10：Observable Agent

這個範例示範如何讓 Agent Run 變得可觀測。

Agent 會寫出一份 JSONL trace，內容包含：

- run start / end events
- risk 與 category 決策
- tool call 與 tool result
- guardrail trigger
- 可 replay 的 trace summary

## 執行

```bash
python examples/10-observable-agent/main.py
```

直接按 Enter 會使用預設的高風險 ticket。

## 為什麼重要？

Production Agent 會壞在很多地方：模型判斷、工具呼叫、記憶檢索、policy gate、handoff。沒有 trace，debug 就只能猜。

最小可用 trace 需要：

- `run_id`：把同一次 agent run 的事件串起來
- `span_id`：標記每個操作
- `parent_span_id`：表示父子關係
- `event_type`：讓過濾與統計變容易
- `payload`：記錄決策或觀察結果

## 學習檢查

跑完後打開 `trace.jsonl`，回答：

- 哪個 event 讓 human approval 變成必要？
- incident review 時你會展示哪些 event？
- 哪些 payload 欄位送到外部 observability vendor 前需要遮蔽？

