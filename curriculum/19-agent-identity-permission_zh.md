# 19 Agent Identity And Permission

## 目標

學會把 Agent 當成具有 owner、scope、permission 與 access review 的身份。

## 為什麼重要？

Production 裡的 Agent 不只是程式碼，而是一個 actor。

如果 Agent 可以讀文件、看 ticket、寄訊息、要求 approval，security team 需要知道：

- 誰擁有這個 Agent
- 它可以 access 什麼
- 它有哪些 scopes
- 哪些 action 需要 review
- 它實際做了什麼
- 什麼時候應該 revoke access

## 直覺模型

```text
agent identity
   ↓
scoped permission
   ↓
authorization check
   ↓
allowed / denied / review required
   ↓
audit log
```

Agent 應該像 human user 和 service account 一樣遵守 least privilege。

## 常見錯誤

### Shared Super Token

每個 Agent 都用同一個超大權限 API key。

### 沒有 Owner

Agent 出事時沒人知道誰負責。

### 沒有 Access Review

舊 Agent 在任務改變後仍保留權限。

### 沒有 Audit Log

團隊無法重建哪個 Agent access 哪個系統。

## 實作練習

執行：

```bash
python examples/16-agent-permission-system/main.py
```

觀察 researcher agent 可以 read docs，但不能 inspect tickets。

## Production Checklist

- [ ] 每個 Agent 都有 owner
- [ ] 每個 Agent 都有 risk tier
- [ ] Permissions 使用 scopes
- [ ] High-risk actions 需要 review
- [ ] Denied actions 會被 logged
- [ ] Access reviews 有排程
- [ ] 避免 shared broad tokens
- [ ] Inactive agents 會被 disabled

