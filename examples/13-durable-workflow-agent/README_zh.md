# 範例 13：Durable Workflow Agent

這個範例示範 long-running agent workflow 的 checkpoint 與 resume。

## 執行

```bash
python examples/13-durable-workflow-agent/main.py
```

## 展示重點

- 每個 step 後保存 workflow state
- 中途停止 run
- 從最新 checkpoint 繼續
- 重啟後保留 artifacts
- 驗證 resumed run 安全完成

## 學習檢查

- 哪些 state 必須保存，才能安全 resume？
- 哪些 tool call 可以 retry？
- 哪些 side effects 需要 idempotency keys？

