# 24 Agent Product UX

## 目標

學會設計讓 Agent 可信、可復原、可理解的使用者體驗。

## 為什麼重要？

Agent 技術上正確，不代表使用者會覺得安全。

Agent UX 必須解釋：

- Agent 正在做什麼
- Agent 被允許做什麼
- 什麼時候需要 approval
- 如何 undo 或 stop work
- 為什麼拒答
- 使用了哪些 evidence

## UX Patterns

| Pattern | 用途 |
|---|---|
| Approval preview | 顯示 tool、arguments、risk、expected effect、rollback |
| Activity timeline | 讓 Agent steps 可見 |
| Evidence drawer | 顯示 retrieved sources 與 trace summary |
| Undo or rollback | 從 approved side effects 復原 |
| Confidence boundary | 分開 facts、assumptions、recommendations |
| Escalation path | 把 high-risk work 交給人 |

## 實作 Artifact

使用：

```text
product-ux/agent-product-ux-checklist.md
```

## Production Checklist

- [ ] 使用者看得到 Agent 正在做什麼
- [ ] High-risk actions 需要 preview 和 approval
- [ ] Refusals 會說明 safe alternative
- [ ] Evidence 可用，但不淹沒使用者
- [ ] 可行時設計 undo 或 rollback
- [ ] 使用者可以 stop 或 escalate Agent

