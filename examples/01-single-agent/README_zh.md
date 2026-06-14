# Example 01 — Single Agent

[English](README.md)

這個範例示範如何建立一個簡單、單一任務導向的 AI Agent。

這裡的目標不是打造完全自主的 Agent，而是學會 Agent Engineering 中最小、最可靠的基本單位：

```text
角色 + 任務邊界 + 輸入 + 輸出契約
```

---

## 這個範例會建立什麼？

一個 **Research Summary Agent**，可以把雜亂筆記整理成結構化摘要。

Agent 會產生：

- Key Points：重點整理
- Action Items：待辦事項
- Risks or Uncertainties：風險或不確定性
- Suggested Next Steps：建議下一步

---

## 資料夾結構

```text
01-single-agent/
├── README.md
├── README_zh.md
├── main.py
├── agent_config.yaml
├── requirements.txt
└── .env.example
```

---

## 快速開始

```bash
cd examples/01-single-agent
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python main.py
```

執行前，請先在 `.env` 裡加入你的 API key。

---

## Agent 設計

| 欄位 | 說明 |
|---|---|
| Agent name | Research Summary Agent |
| Purpose | 將雜亂筆記轉換成結構化摘要 |
| Input | 使用者提供的原始筆記 |
| Output | Markdown 摘要 |
| Allowed actions | 摘要、組織資訊、辨識風險、建議下一步 |
| Not allowed | 編造不存在的事實、引用未提供的來源、做出無根據的推論 |

---

## 學習目標

完成這個範例後，你應該能理解：

- 如何定義單一 Agent 的角色
- 如何撰寫 system prompt
- 如何限制輸出格式
- 如何將設定檔與程式碼分離
- 如何處理缺少 API key 的情況
- 如何為後續 Tool Use 範例做準備

---

## 執行流程

```text
使用者輸入筆記
   ↓
讀取 agent_config.yaml
   ↓
建立 system prompt
   ↓
呼叫 LLM
   ↓
輸出 Markdown 摘要
```

---

## 為什麼這個範例重要？

很多 Agent 專案一開始就加入工具、記憶、多 Agent 協作，導致系統很快變得複雜。

這個範例刻意保持簡單，讓你先掌握：

```text
一個 Agent 應該先有明確角色與可靠輸出，再追求更多能力。
```

---

## 下一步

完成這個範例後，可以繼續：

```text
examples/02-tool-using-agent
```

下一個範例會讓 Agent 學會呼叫外部工具。