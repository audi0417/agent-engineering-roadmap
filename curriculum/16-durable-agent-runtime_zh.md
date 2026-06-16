# 16 Durable Agent Runtime

## 目標

學會設計能承受 crash、restart、retry 與 long-running tasks 的 Agent workflow。

## 為什麼重要？

很多有用的 Agent 任務不是一次 chat completion。

它們可能會：

- 呼叫慢工具
- 等待 approval
- 處理大量文件
- 在背景執行
- 明天再 resume
- failure 後 retry

如果 process 中途 crash，Agent 不應該忘記發生過什麼，也不應該重複危險 side effects。

## 直覺模型

Durable execution 是：

```text
做一步
   ↓
保存 checkpoint
   ↓
做下一步
   ↓
保存 checkpoint
   ↓
中斷後安全 resume
```

Checkpoint 是 workflow state 的記憶，不是 model memory。

## 核心機制

| 機制 | 用途 |
|---|---|
| Checkpoint | 每個 step 後保存 workflow state |
| Resume | 從最新安全狀態繼續 |
| Idempotency key | 避免重複 external side effects |
| Retry policy | 決定什麼可以 retry、retry 幾次 |
| Human wait state | 等 approval 時明確暫停 |
| Event log | 保存發生過什麼的證據 |
| Compensation | 定義 rollback 或 repair action |

## 常見錯誤

### 沒有 Checkpoint

Crash 後 workflow state 全部消失。

### Blind Retry

Agent 重複付款、寄信、刪除或 external write。

### Hidden Wait State

Agent 正在等 approval，但系統無法顯示原因。

### 混淆 Model Memory

團隊以為 model context 是 durable state。它不是。

## 實作練習

執行：

```bash
python examples/13-durable-workflow-agent/main.py
```

範例會跑兩步後停止，寫入 checkpoint，然後從 checkpoint resume。

## Production Checklist

- [ ] 每個 workflow step 有穩定名稱
- [ ] 每個 step 後 checkpoint state
- [ ] external writes 使用 idempotency keys
- [ ] approval wait 是明確 state
- [ ] retryable 和 non-retryable failures 分開
- [ ] resume logic 有測試
- [ ] checkpoint 盡量避免保存敏感 raw data

