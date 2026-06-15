# Module 08 教案 - Human-In-The-Loop

## 本堂課一句話

Human-in-the-loop 不是「模型不行就找人」，而是把高風險決策放回人類控制。

## 學習目標

學生上完後應該能：

- 區分 review、approval、escalation
- 設計 risk level
- 寫 approval request
- 記錄 approval audit log
- 判斷何時應該拒絕而不是請人批准

## 課前準備

- 閱讀：`curriculum/08-human-in-the-loop_zh.md`
- 模板：`templates/safety-gate-template.md`
- Lab：`labs/lab-08-human-in-the-loop.md`

## 90 分鐘課程流程

| 時間 | 活動 |
|---:|---|
| 0-10 | 問：哪些 action 不應該自動執行？ |
| 10-25 | 講 low/medium/high/prohibited risk |
| 25-40 | 示範 approval request 格式 |
| 40-55 | Live demo：email sending approval gate |
| 55-75 | 學生設計自己的 approval policy |
| 75-85 | 討論 refuse vs ask approval |
| 85-90 | Recap：人類審核要有資訊，不是只按 OK |

## 板書心智模型

```text
Proposed Action
  ↓
Risk Classifier
  ↓ low: execute
  ↓ medium: log
  ↓ high: ask approval
  ↓ prohibited: refuse
```

## Live Demo

把「寄出 email」拆成：

- draft email
- show recipient
- show content
- show reason
- ask approval
- send only after approval

## 課堂練習

學生為一個 agent 定義 4 層 action policy。

## 常見誤解

- 誤解：approval gate 就是問一句「可以嗎？」
- 修正：approval request 必須提供 action、risk、reason、expected effect、rollback。

## 作業

寫出 3 個 approval transcript 範例。

## 評量標準

| 項目 | 通過標準 |
|---|---|
| Risk levels | 四層清楚 |
| Approval | 資訊足夠 |
| Audit | 記錄人、事、時、原因 |
| Refusal | 禁止事項會拒絕 |
| UX | 不讓人類盲目批准 |
