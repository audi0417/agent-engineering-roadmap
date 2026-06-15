# Module 02 教案 - Tool Calling

## 本堂課一句話

Tool calling 讓 agent 能做事，但也讓錯誤從文字變成真實世界的副作用。

## 學習目標

學生上完後應該能：

- 判斷什麼時候需要 tool
- 寫 tool schema
- 驗證 tool arguments
- 設計 tool risk level
- 記錄 tool call log

## 課前準備

- 閱讀：`curriculum/02-tool-calling_zh.md`
- 範例：`examples/02-tool-using-agent/README.md`
- 模板：`templates/safety-gate-template.md`

## 90 分鐘課程流程

| 時間 | 活動 |
|---:|---|
| 0-10 | 問：文字答錯和 tool call 錯，差在哪？ |
| 10-25 | 講 tool schema、validation、permission |
| 25-40 | 拆 Example 02 的 tools.py |
| 40-55 | Live demo：新增 calculator 或 mock lookup |
| 55-75 | 學生新增一個 tool |
| 75-85 | 互評：這個 tool 有沒有 risk level？ |
| 85-90 | Recap：工具越強，邊界要越清楚 |

## 板書心智模型

```text
Need external capability?
  ↓
Select tool
  ↓
Validate arguments
  ↓
Check risk
  ↓
Execute
  ↓
Interpret result
  ↓
Log
```

## Live Demo

新增一個 `calculate(expression)` tool，但限制只允許基本算術。

## 課堂練習

學生新增一個 read-only tool，並寫明：

- input schema
- validation
- risk level
- failure behavior

## 常見誤解

- 誤解：agent 會自己知道什麼 tool 安全。
- 修正：安全是系統政策，不是模型直覺。

## 作業

把一個 tool 改成 high-risk action，並加入 approval gate。

## 評量標準

| 項目 | 通過標準 |
|---|---|
| Schema | 明確定義 input |
| Validation | 錯誤參數會被拒絕 |
| Risk | 有 low/medium/high |
| Logging | 記錄 tool name、args、result |
| Approval | 高風險 action 不會自動執行 |
