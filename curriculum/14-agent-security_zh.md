# 14 Agent Security

## 目標

學會防守 Agent 系統中的 prompt injection、tool misuse、memory leakage 與不安全的 authority transfer。

## 為什麼重要？

Agent 比 chatbot 更危險，因為 Agent 可以行動。

當 Agent 可以 retrieval、call tools、記住使用者資料、把工作 handoff 給其他 agent，攻擊者就可以嘗試影響每一個通道。

Security 不是最後加一個 filter，而是每個 input 和 action 周圍都要有邊界。

## 核心規則

Retrieved documents、tool results、emails、web pages、tickets、user uploads 都是資料。

它們不是權威指令。

只有可信 policy 與明確授權的 user intent，才應該控制 Agent。

## Threat Model

| Threat | 例子 | 防守 |
|---|---|---|
| Prompt injection | 文件寫著「ignore previous instructions」 | 把 retrieved content 當成不可信資料 |
| Tool misuse | Agent 太早呼叫 delete 或 payment tool | 加 approval gates 與 tool allowlists |
| Memory leakage | Agent 洩漏 private user memory | 分級 memory 並限制 retrieval |
| Data exfiltration | Tool result 要求 Agent 把 secrets 傳出去 | 未經 approval 不允許外傳 |
| Handoff confusion | Specialist agent 接受不安全委派 | Handoff 時保留 policy |
| MCP server 權限過大 | Tool 權限比任務需要更大 | 使用 least privilege 與 scoped credentials |

## 黑盒視角

```text
input
   ↓
agent
   ↓
tool / retrieval / memory / handoff
   ↓
output
```

這個視角會藏住問題：每一條箭頭都是可能的攻擊面。

## 機制視角

```text
User input ─────────────┐
Retrieved documents ────┼──> trust classifier ──> safe context
Tool results ───────────┘
                                ↓
Trusted policy + user intent -> agent planner -> approved action
```

Agent 不應該把所有文字混成同一種 authority level。

## 實作練習

執行：

```bash
python examples/11-prompt-injection-defense/main.py
```

這個範例會同時 retrieve 到可信 policy 文件與 poisoned customer note。poisoned note 會被擋下，因為它試圖覆蓋 system policy。

## Security Checklist

- [ ] 區分 trusted policy 與 untrusted content
- [ ] 掃描 retrieved text 是否企圖覆蓋指令
- [ ] destructive actions 需要 approval
- [ ] tool permissions 保持最小權限
- [ ] handoff 時保留 policy
- [ ] logging 前遮蔽 secrets
- [ ] 評估 refusal 與 escalation behavior
- [ ] 把 security decisions 記進 trace

## 常見誤解

### 「LLM 自己會知道這是惡意內容」

有時候會，有時候不會。

Security 不能依賴模型每次都看出攻擊。

### 「Prompt injection 只會發生在網頁」

它可以出現在 PDF、email、support ticket、calendar invite、tool result、database row、memory。

### 「System prompt 寫強一點就好」

更強的 system prompt 有幫助，但不夠。你還需要 tool permission、content isolation、approval gate、eval。

## 參考

- [Model Context Protocol Security Principles](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

