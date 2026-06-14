# 中文學習資源研究計畫

[English](chinese-learning-sources.md)

## 目的

這份文件用來整理中文社群中的 Agent / MCP / Memory / Multi-Agent 教學資源，並將其轉換成原創英文教材的靈感來源。

重點不是直接翻譯或搬運文章，而是觀察中文學習者常遇到的問題、常見範例與概念盲點，再重新設計成英文教材、實作任務與架構圖。

---

## 可以研究的來源類型

- 知乎文章與討論
- Bilibili 技術教學影片
- 微信技術文章
- 中文 GitHub 專案
- 中文開發者部落格
- 中文 AI 社群筆記

---

## 建議蒐集主題

### Agent 基礎

可搜尋：

- 什麼是 AI Agent
- ReAct Pattern
- Tool Calling
- Planning and Execution
- Agent Loop

### MCP

可搜尋：

- Model Context Protocol 入門
- MCP Client / Server 範例
- filesystem MCP
- database MCP
- browser/search MCP
- MCP 安全風險

### Memory

可搜尋：

- 長期記憶
- 向量資料庫記憶
- 使用者 Profile Memory
- Multi-Agent Shared Memory
- Memory Pollution
- Memory Governance

### Workflow 與 LangGraph

可搜尋：

- LangGraph State Machine
- Graph-based Agent Workflow
- Planner-Executor-Reviewer Pattern
- Retry and Fallback
- Human-in-the-loop

### Multi-Agent Systems

可搜尋：

- CrewAI
- AutoGen
- LangGraph Multi-Agent
- Supervisor-Worker Pattern
- Debate Agents
- Role Specialization

### Production Agent Systems

可搜尋：

- Agent Evaluation
- RAG Evaluation
- Tracing and Observability
- Langfuse
- Prompt Injection
- Tool Permission Control

---

## 如何轉換成原創英文教材

建議流程：

```text
中文來源
   ↓
抽取概念、學習痛點、範例類型
   ↓
移除原文表述與原始結構
   ↓
重新撰寫成原創英文解釋
   ↓
加入 Hands-on Task
   ↓
加入架構圖與 Checklist
   ↓
以 Reference 形式標註來源，而不是搬運內容
```

---

## 資源整理模板

每個來源可以用以下格式記錄：

```text
Source title:
Source URL:
Platform:
Topic:
Key ideas:
Learner pain points:
Example used:
How to transform into original English lesson:
Potential exercise:
Reference status:
```

---

## 可轉換成的英文教材類型

- Concept Explanation
- Architecture Walkthrough
- Step-by-step Tutorial
- Hands-on Coding Lab
- Debugging Guide
- Comparison Table
- Safety Checklist
- Production Design Pattern

---

## 初步研究觀察

目前公開搜尋結果顯示，最值得整理成教材的主題群包括：

1. MCP 作為 Agent 與外部工具之間的整合層。
2. LangGraph 作為可控 Agent Workflow / State Machine 框架。
3. Agent Memory 是獨立的系統設計問題，不只是 Vector Search。
4. Multi-Agent Systems 應該被設計成角色分工 Workflow，而不是單純角色扮演。
5. Production Safety 需要涵蓋 Tool Permission、Prompt Injection 與 Memory Governance。

---

## 版權原則

不要直接複製中文文章或影片逐字稿。

可以：

- 摘要高層概念
- 標註來源連結
- 撰寫原創說明
- 製作原創架構圖
- 撰寫新的程式範例
- 設計新的練習題

不可以：

- 直接全文翻譯文章
- 逐段照搬教學結構
- 未授權使用截圖
- 未確認授權就複製程式碼
- 移除原作者署名
