# Module 06 教案 - Graph-Based Agents

## 本堂課一句話

Graph-based agent 是把 workflow 變成明確的 state、edge 和 condition，讓系統知道下一步該去哪裡。

## 學習目標

學生上完後應該能：

- 解釋 state、edge、condition
- 把 agent workflow 畫成 graph
- 設計 success path 與 failure path
- 說明 graph 何時有用、何時太重
- 定義 human approval node

## 課前準備

- 閱讀：`curriculum/06-graph-based-agents_zh.md`
- Lab：`labs/lab-06-graph-agent.md`
- Pattern：`patterns/README_zh.md`

## 90 分鐘課程流程

| 時間 | 活動 |
|---:|---|
| 0-10 | 問：if/else 很多時，agent code 會怎麼壞？ |
| 10-25 | 講 state machine 心智模型 |
| 25-40 | 示範把 workflow 畫成 graph |
| 40-55 | Live demo：加入 failure branch |
| 55-75 | 學生畫自己的 graph |
| 75-85 | 互評：每個 edge 條件是否明確？ |
| 85-90 | Recap：graph 是複雜流程的地圖 |

## 板書心智模型

```text
State
  ↓ condition
Next State
  ↓ condition
Tool / Review / Approval / End
```

## Live Demo

把 support ticket agent 畫成：

```text
receive -> classify -> retrieve policy -> draft response -> review
review pass -> final
review fail -> revise
high risk -> human approval
tool error -> fallback
```

## 課堂練習

學生完成一張 graph，至少包含：

- start
- end
- tool node
- review node
- error branch
- approval branch

## 常見誤解

- 誤解：所有 agent 都應該用 graph。
- 修正：簡單任務用 graph 會過度設計；graph 是在流程分支變多時才有價值。

## 作業

把你的 capstone workflow 畫成 Mermaid graph。

## 評量標準

| 項目 | 通過標準 |
|---|---|
| State | 每個 state 有明確責任 |
| Edge | 條件清楚 |
| Failure | 有錯誤路徑 |
| Approval | 高風險行動會進 approval |
| End | 不會無限循環 |
