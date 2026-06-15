# Module 09 教案 - Production Agent Systems

## 本堂課一句話

Production agent 不是 demo 變漂亮，而是 evaluation、observability、security、cost control 和 rollback 都到位。

## 學習目標

學生上完後應該能：

- 建立 regression eval suite
- 說明 observability 要記錄什麼
- 設計 cost and latency guardrails
- 說明 prompt injection 防線
- 跑 Example 07 evaluation harness

## 課前準備

- 閱讀：`curriculum/09-production-agent-systems_zh.md`
- 範例：`examples/07-evaluation-harness/README.md`
- Lab：`labs/lab-09-evaluation.md`

## 90 分鐘課程流程

| 時間 | 活動 |
|---:|---|
| 0-10 | 問：demo 會動和 production 可用差在哪？ |
| 10-25 | 講 eval suite 與 regression |
| 25-40 | 跑 Example 07 |
| 40-55 | Live demo：新增一個 failing eval case |
| 55-70 | 講 traces、logs、cost、latency |
| 70-82 | 學生設計 release gate |
| 82-90 | Recap：沒有 eval 就沒有 production confidence |

## 板書心智模型

```text
Change
  ↓
Eval Suite
  ↓
Trace Review
  ↓
Safety Check
  ↓
Cost Check
  ↓
Release or Block
```

## Live Demo

新增一個 unsafe case，觀察 pass rate 下降，然後修 mock agent。

## 課堂練習

學生寫 10 個 eval cases，至少包含：

- happy path
- missing context
- unsafe request
- tool use
- memory use

## 常見誤解

- 誤解：production 就是把 agent 部署到 server。
- 修正：部署只是開始。你還要知道它何時壞、為什麼壞、怎麼回滾。

## 作業

替 capstone 定義 release blocking criteria。

## 評量標準

| 項目 | 通過標準 |
|---|---|
| Eval | 包含正例與負例 |
| Observability | 記錄 model/tool/memory/cost |
| Security | 有 prompt injection 防線 |
| Cost | 有 step/token/tool 限制 |
| Rollback | 有回復路徑 |
