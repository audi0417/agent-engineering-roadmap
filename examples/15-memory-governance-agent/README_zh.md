# 範例 15：Memory Governance Agent

這個範例示範 production agent 的 memory governance。

## 執行

```bash
python examples/15-memory-governance-agent/main.py
```

## 展示重點

- 依 category 分類 memory
- 儲存前 redaction PII
- 合併重複 memory
- 隨時間降低 confidence
- 刪除敏感 memory
- 保留 audit log

## 學習檢查

- 哪些 memory 適合 long-term？
- 哪些 memory 應該 session 結束就過期？
- 哪些欄位儲存前需要 redaction？

