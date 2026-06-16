# 25 Enterprise Agent Operating Model

## 目標

學會組織如何長期安全地營運多個 Agent。

## 為什麼重要？

當 Agent 在公司裡擴散，真正困難的是營運：

- 每個 Agent 誰負責
- 它能用哪些 tools
- 它能 access 哪些 data
- 多久 review 一次
- 它屬於哪個 risk tier
- incident 如何處理
- 什麼時候應該 retire

## Operating Model

```text
agent registry
   ↓
risk tier
   ↓
owner + scopes + eval suite
   ↓
deployment review
   ↓
monitoring + access review
   ↓
incident response + retirement
```

## 實作 Artifact

使用：

```text
operating-model/enterprise-agent-operating-checklist.md
```

## Production Checklist

- [ ] 每個 Agent 都有 registry
- [ ] 每個 Agent 都有 owner
- [ ] Launch 前先分配 risk tier
- [ ] Scope 和 tool access 會 review
- [ ] Eval suite 連到 Agent
- [ ] Incident owner 明確
- [ ] Retirement criteria 明確

