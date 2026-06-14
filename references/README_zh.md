# References 參考資料

[English](README.md)

這個資料夾整理支撐 Agent Engineering Roadmap 的公開參考資料。

References 的用途是提升教材品質，而不是複製內容。本專案中的課程仍應維持原創說明、原創範例與原創架構圖。

---

## 核心研究參考

| 領域 | Reference | 年份 | 在本專案中的用途 |
|---|---|---:|---|
| Reasoning + Acting | ReAct: Synergizing Reasoning and Acting in Language Models | 2022 | 支撐 Agent 會結合 reasoning steps 與外部工具 / 環境 action 的概念。 |
| Agent Reliability | On the Brittle Foundations of ReAct Prompting for Agentic Large Language Models | 2024 | 提醒學習者 prompting pattern 可能脆弱，不能盲目信任，必須評估。 |
| Multi-Agent Systems | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | 2025 | 支撐 multi-agent structures、roles 與 coordination protocols 的課程內容。 |
| Agent Memory | Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers | 2026 | 支撐 memory design、write/read loop、memory governance 與 evaluation。 |

---

## MCP 參考

| 領域 | Reference | 在本專案中的用途 |
|---|---|---|
| MCP concept | Model Context Protocol public documentation and ecosystem descriptions | 支撐 Example 03 使用的 MCP-style client/server architecture。 |
| MCP risks | Recent public security reports on MCP-style integrations | 支撐 production safety 與 tool permission 章節。 |

---

## 如何使用 References

每個 curriculum module 後續都應該逐步加入簡短的 `References` 區塊。

好的 references 應該支撐：

- 一個概念
- 一個設計模式
- 一個已知限制
- 一個安全風險
- 一個評估方法

References 不應該被用來複製文章結構或原文。

---

## Citation Style

使用簡短、可讀的引用格式：

```text
- Yao et al. (2022), ReAct: Synergizing Reasoning and Acting in Language Models.
```

如果是 tutorial 或 code example，引用建議放在文件結尾的 `References` 區塊。

---

## Reference Expansion Plan

後續可擴充類別：

- Tool use and function calling
- RAG and retrieval evaluation
- Agent memory
- Workflow orchestration
- Multi-agent systems
- Human-in-the-loop systems
- Agent evaluation
- MCP and tool security
- Healthcare AI safety
- Finance AI risk controls
