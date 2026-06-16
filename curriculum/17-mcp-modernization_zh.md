# 17 MCP Modernization

## 目標

理解 modern MCP-style integration，不只停留在 simple tool calling。

## 為什麼重要？

早期 Agent demo 常把 MCP 想成「呼叫工具的方法」。

Production integrations 需要更多結構：

- tools：執行 action
- resources：讀取 context
- prompts：可重用 task template
- authorization：scoped access
- elicitation：缺少必要資訊時詢問
- gateway policies：跨多個 server 的治理層

## 直覺模型

MCP-style design 把 authority 和 capability 分開。

```text
agent
   ↓
gateway / client
   ↓
authorization + policy
   ↓
tools, resources, prompts
```

Agent 不應該直接擁有所有 integration。Gateway 負責執行：什麼能讀、什麼能 call、什麼需要 clarification。

## 核心概念

| 概念 | 意義 |
|---|---|
| Tool | 可呼叫的 action 或 computation |
| Resource | 用 URI 標記的 readable context |
| Prompt | 可重用 task template |
| Authorization | 以 capability 為範圍的 access control |
| Elicitation | 缺少必要資訊時詢問 |
| Gateway | 跨 integrations 的 policy 與 routing layer |

## 常見錯誤

### Tool-Only Thinking

所有東西都變成 tool，連 read-only context 也是。權限因此變得太廣。

### 沒有 Authorization Boundary

每個 Agent 都能 call 每個 integration。

### Missing Elicitation

Agent 在缺少必要 arguments 時亂猜，而不是詢問。

### 沒有 Gateway Policy

每個 server 自己實作 safety rules，最後規則不一致。

## 實作練習

執行：

```bash
python examples/14-modern-mcp-gateway/main.py
```

觀察：

- capability listing
- resource read
- prompt access
- tool call authorization
- missing arguments 時的 elicitation

## Production Checklist

- [ ] Tools 與 resources 有不同 permissions
- [ ] Tokens 依 capability scope
- [ ] 缺少必要 arguments 時觸發 elicitation
- [ ] Gateway 記錄每個 denied operation
- [ ] High-risk tools 需要 approval
- [ ] Resources 先暴露 identifiers，再暴露 raw content
- [ ] Prompts 有 version
- [ ] Tool schemas 拒絕 unexpected arguments

