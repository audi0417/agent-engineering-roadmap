# Module 05 教案 - Workflow Orchestration

## 本堂課一句話

Workflow 是把 agent 的自由發揮變成可觀察、可重試、可審核的流程。

## 學習目標

學生上完後應該能：

- 拆解 planner、executor、reviewer、evaluator
- 設計 intermediate artifacts
- 寫 retry 與 stop condition
- 使用 rubric 檢查輸出
- 修改 Example 05 workflow

## 課前準備

- 閱讀：`curriculum/05-workflow-orchestration_zh.md`
- 範例：`examples/05-multi-agent-workflow/README.md`
- Lab：`labs/lab-05-workflow.md`

## 90 分鐘課程流程

| 時間 | 活動 |
|---:|---|
| 0-10 | 問：為什麼多步任務不能只靠一次 model call？ |
| 10-25 | 講 planner-executor-reviewer |
| 25-40 | 拆 Example 05 的 artifact flow |
| 40-55 | Live demo：新增 citation reviewer |
| 55-75 | 學生新增一條 review rule |
| 75-85 | 討論 retry loop 為什麼要有上限 |
| 85-90 | Recap：workflow 是 control surface |

## 板書心智模型

```text
Task
  ↓
Plan
  ↓
Execute
  ↓
Review
  ↓ pass
Final
  ↘ fail
   Revise or stop
```

## Live Demo

把 reviewer 改成檢查：

- clear goal
- implementation steps
- risk
- next action
- citations

## 課堂練習

學生替 workflow 新增一個 failure condition，並定義如何 revise。

## 常見誤解

- 誤解：workflow 會讓 agent 變聰明。
- 修正：workflow 不保證更聰明，但會讓錯誤比較可控。

## 作業

把自己的 agent 畫成 4-6 個 workflow steps。

## 評量標準

| 項目 | 通過標準 |
|---|---|
| Artifacts | 每步有明確輸入輸出 |
| Reviewer | 有具體 rubric |
| Retry | 有上限 |
| Failure | 有 stop / escalation |
| Inspectability | 中間結果可查看 |
