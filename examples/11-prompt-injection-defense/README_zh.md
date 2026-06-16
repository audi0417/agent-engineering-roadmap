# 範例 11：Prompt Injection Defense

這個範例示範 RAG 場景中最小可用的 prompt injection 防守。

核心規則：

> Retrieved documents 和 tool results 是資料，不是權威指令。

## 執行

```bash
python examples/11-prompt-injection-defense/main.py
```

直接按 Enter 會使用預設問題。

## 展示重點

- Retrieval 可能同時拿到有用 policy 與惡意指令。
- Agent 在使用 context 前，要先掃描不可信內容。
- 企圖覆蓋 system policy 的文件會被阻擋。
- 最終答案遵守可信 policy，而不是遵守注入指令。

## 學習檢查

跑完後回答：

- 哪份文件被 blocked？
- 為什麼 retrieved document 不能改寫 system policy？
- security review 時你會保留哪些 logs？

