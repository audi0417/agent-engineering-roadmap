# Module 07 教案 - Multi-Agent Systems

## 本堂課一句話

Multi-agent 的重點不是 agent 數量，而是 supervisor、specialist、shared state 和 final ownership。

## 學習目標

學生上完後應該能：

- 判斷何時需要多 agent
- 設計 supervisor routing policy
- 定義 specialist input/output contract
- 處理 agent conflict
- 修改 Example 06 加入新 domain agent

## 課前準備

- 閱讀：`curriculum/07-multi-agent-systems_zh.md`
- 範例：`examples/06-agent-colony/README.md`
- Lab：`labs/lab-07-multi-agent.md`

## 90 分鐘課程流程

| 時間 | 活動 |
|---:|---|
| 0-10 | 問：多 agent 一定比單 agent 強嗎？ |
| 10-25 | 講 supervisor-specialist pattern |
| 25-40 | 拆 Example 06 routing |
| 40-55 | Live demo：新增 education agent |
| 55-75 | 學生新增一個 specialist |
| 75-85 | 討論 conflict resolution |
| 85-90 | Recap：multi-agent 要有 final owner |

## 板書心智模型

```text
Task
  ↓
Supervisor
  ↓
Specialist A / Specialist B
  ↓
Shared Memory
  ↓
Evaluator
  ↓
Final Owner
```

## Live Demo

新增 domain：

```yaml
education:
  keywords: [learn, course, study, exam]
  disclaimer: Educational planning only.
```

## 課堂練習

學生替 colony 新增一個 specialist，並設計：

- routing keywords
- domain boundary
- recommended workflow
- human review rule

## 常見誤解

- 誤解：把任務拆給多個 agent，品質自然會變好。
- 修正：拆分會增加 coordination cost。沒有 routing、contract、evaluation，就只是多幾個可能出錯的地方。

## 作業

為你的 multi-agent system 寫 5 個 routing eval cases。

## 評量標準

| 項目 | 通過標準 |
|---|---|
| Routing | 可測且不只靠感覺 |
| Specialist | scope 清楚 |
| Shared state | 不亂寫 |
| Conflict | 有解決規則 |
| Final answer | 有單一 owner |
