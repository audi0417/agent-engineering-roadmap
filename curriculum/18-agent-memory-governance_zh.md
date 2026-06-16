# 18 Agent Memory Governance

## 目標

學會治理 Agent 可以記住、合併、遮蔽、衰退與刪除的資訊。

## 為什麼重要？

Memory 不只是 vector database。Production memory 是一個受治理的資料系統。

Agent memory layer 需要政策來決定：

- 什麼可以被儲存
- 什麼必須 redacted
- 什麼可以成為 long-term memory
- 什麼應該 expire
- 重複 facts 如何 merge
- confidence 如何 decay
- 使用者如何要求 deletion
- memory writes 如何 audit

## 直覺模型

```text
candidate memory
   ↓
classification
   ↓
redaction
   ↓
write / merge / reject
   ↓
decay / review / delete
```

模型可以建議一段 memory，但 governance layer 決定它能不能被存。

## 常見錯誤

### Store Everything

Agent 記住敏感、過期或不相關的資訊。

### Vector-Only Memory

系統可以 retrieve memory，但無法解釋誰寫入、為什麼存在、什麼時候該刪除。

### 沒有 Merge Policy

重複 facts 變成雜訊。

### 沒有 Forget Policy

使用者無法移除敏感或過期 memories。

## 實作練習

執行：

```bash
python examples/15-memory-governance-agent/main.py
```

觀察範例如何 redacts contact information、merge repeated preference、decay confidence、delete session PII。

## Production Checklist

- [ ] Memory categories 明確
- [ ] PII 儲存前會 redacted
- [ ] Long-term memory 需要 reason
- [ ] Memory writes 會 audit
- [ ] Duplicate facts 會 merge
- [ ] Confidence 可以 decay
- [ ] 使用者可以要求 deletion
- [ ] Memory retrieval 遵守 scope 和 sensitivity

