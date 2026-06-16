# Module 01 教案 - Agent Architecture

## 本堂課一句話

Agent architecture 的重點不是 prompt 寫很長，而是把 role、state、tools、output 和 validation 分清楚。

## 學習目標

學生上完後應該能：

- 畫出 single-agent architecture
- 區分 prompt、state、tool result、memory
- 設計 structured output
- 說明 validation 在哪裡發生
- 修改 Example 01 成自己的 agent

## 課前準備

- 閱讀：`curriculum/01-agent-architecture_zh.md`
- 範例：`examples/01-single-agent/README.md`
- Lab：`labs/lab-01-single-agent.md`

## 90 分鐘課程流程

| 時間 | 活動 |
|---:|---|
| 0-10 | 問：為什麼只有 prompt 不等於 architecture？ |
| 10-25 | 講 input、system prompt、model、parser、validator |
| 25-40 | 拆 Example 01：config、prompt、model call、output |
| 40-55 | Live demo：把 summary agent 改成 ticket classifier |
| 55-75 | 學生改 Example 01 |
| 75-85 | 分享 output schema 與 failure behavior |
| 85-90 | Recap：架構是讓錯誤有地方被攔下來 |

## 板書心智模型

```text
User Input
  ↓
Task Contract
  ↓
System Prompt
  ↓
Model
  ↓
Output Parser
  ↓
Validation
  ↓
Application Response
```

## Live Demo

把自由文字輸出改成固定 section：

```text
## Category
## Priority
## Reason
## Next Action
```

## 課堂練習

學生要修改 Example 01 的 `agent_config.json`，讓 agent 變成一個窄任務 agent。

## 常見誤解

- 誤解：system prompt 裡寫清楚就會穩。
- 修正：prompt 是其中一層，還需要 schema、validation、eval。

## 作業

替你的 agent 新增 5 個測試輸入與 expected behavior。

## 評量標準

| 項目 | 通過標準 |
|---|---|
| Role | 不超過一個主要任務 |
| Output | 有固定格式 |
| Rules | 至少 3 條且可測 |
| Failure | 缺資訊時會澄清 |
| Test cases | 包含負例 |
