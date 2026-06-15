# Module 00 教案 - Agent Foundations

## 本堂課一句話

Agent 不是會聊天的模型，而是圍繞一個目標運作的任務系統。

## 學習目標

學生上完後應該能：

- 分辨 chatbot 與 agent 的差異
- 說出最小 agent loop
- 寫出一份 agent specification
- 判斷一個 agent idea 是否太大
- 設計第一組 evaluation cases

## 課前準備

- 閱讀：`curriculum/00-agent-foundations_zh.md`
- 模板：`templates/agent-spec-template.md`
- Lab：`labs/lab-00-agent-spec.md`

## 90 分鐘課程流程

| 時間 | 活動 |
|---:|---|
| 0-10 | 問學生：Chatbot 和 Agent 差在哪？先收直覺答案 |
| 10-20 | 講 goal + context + reasoning + action + feedback |
| 20-35 | 拆一個壞例子：「幫助使用者」為什麼不是好 agent goal |
| 35-50 | 示範寫 Research Summary Agent spec |
| 50-70 | 學生各自寫一份 agent spec |
| 70-82 | 兩人互評：scope 是否太大？output 是否可評估？ |
| 82-90 | Recap：agent 可靠性從 specification 開始 |

## 板書心智模型

```text
Goal
  ↓
Context
  ↓
Reasoning
  ↓
Action
  ↓
Feedback
```

## Live Demo

示範把模糊需求改成 agent spec。

模糊需求：

```text
做一個可以幫我研究東西的 Agent。
```

收斂後：

```text
Agent name: Research Summary Agent
Goal: Convert one pasted article into key claims, evidence, uncertainty, and follow-up questions.
Output: Markdown with Claims, Evidence, Uncertainty, Next Questions.
Not allowed: Invent sources, browse web, make final decisions.
Evaluation: Faithfulness, completeness, uncertainty marking.
```

## 課堂練習

每位學生選一個 agent idea，填完 `agent-spec-template.md`。

## 常見誤解

- 誤解：agent 越通用越好。
- 修正：越通用越難評估，也越難保證安全。

## 作業

為你的 agent 寫三個 eval cases：

- happy path
- missing context
- unsafe or out-of-scope request

## 評量標準

| 項目 | 通過標準 |
|---|---|
| Goal | 具體、可觀察、可評估 |
| Scope | allowed / not allowed 清楚 |
| Output | 格式可驗證 |
| Failure behavior | 知道何時澄清、拒絕或升級 |
| Eval cases | 至少 3 類情境 |
