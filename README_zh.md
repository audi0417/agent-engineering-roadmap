# Agent Engineering Roadmap

> 從零開始打造具備 MCP、Memory、Multi-Agent 與 Agent Colony 的生產級 AI Agent 系統。

[English](README.md)

---

## 什麼是 Agent Engineering？

Agent Engineering 是一門設計、建構、評估與部署 AI Agent 系統的工程方法。它不只是在 LLM 外面包一層聊天介面，而是讓 AI 系統能夠使用工具、連接外部資料、保留長期記憶、與其他 Agent 協作，並且在真實產品環境中安全運作。

這個 Roadmap 適合想要從 Chatbot 進階到真實 Agentic Application 的開發者、研究者與創業團隊。

---

## 你會學到什麼？

- 單一 AI Agent
- Tool-Using Agent
- MCP-enabled Agent
- Persistent Memory System
- Multi-Agent Workflow
- Supervisor-Worker System
- Shared-Memory Agent Colony
- Healthcare / Finance Agent Demo
- Production-ready Agent Application

---

## 學習路線

```text
Level 0  AI 與 LLM 基礎
   ↓
Level 1  Single Agent
   ↓
Level 2  Tool Use
   ↓
Level 3  Model Context Protocol, MCP
   ↓
Level 4  Agent Memory
   ↓
Level 5  Agent Workflow
   ↓
Level 6  Multi-Agent Systems
   ↓
Level 7  Agent Colony
   ↓
Level 8  Production, Evaluation & Safety
```

---

## 核心架構

```mermaid
graph TD
    User[User] --> Supervisor[Supervisor Agent]
    Supervisor --> MemoryAgent[Memory Agent]
    Supervisor --> ResearchAgent[Research Agent]
    Supervisor --> ToolAgent[Tool Agent]
    Supervisor --> DomainAgent[Domain Agent]
    MemoryAgent --> SharedMemory[Shared Memory]
    ToolAgent --> MCP[MCP Servers]
    DomainAgent --> MCP
    ResearchAgent --> MCP
    Supervisor --> Evaluator[Evaluator Agent]
    Evaluator --> Final[Final Response]
    Final --> User
    Evaluator --> SharedMemory
```

---

## Repository Structure

```text
agent-engineering-roadmap/
├── README.md
├── README_zh.md
├── roadmap/
├── examples/
├── architecture/
├── templates/
├── healthcare/
├── finance/
└── resources/
```

---

## 真實應用 Track

### Healthcare Agent Engineering

建構照護管理、營養追蹤、個人健康記憶、醫療流程自動化相關的 Agent 系統。

### Finance Agent Engineering

建構研究 Agent、因子分析 Agent、投資組合 Agent、交易流程 Agent。

### Enterprise Agent Engineering

建構客服 Agent、內部知識庫 Agent、文件處理 Agent、企業流程自動化 Agent。

---

## 專案狀態

目前本專案處於初始 Roadmap 階段。

- [ ] 完成雙語 Roadmap
- [ ] 加入最小可執行範例
- [ ] 加入 MCP Server Templates
- [ ] 加入 Memory System Examples
- [ ] 加入 Healthcare Agent Colony Demo
- [ ] 加入 Finance Research Agent Demo
- [ ] 加入 Evaluation and Safety Templates

---

## License

To be decided.
