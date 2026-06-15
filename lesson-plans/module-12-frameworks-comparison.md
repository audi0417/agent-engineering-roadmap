# Module 12 教案 - Agent Frameworks Comparison

## 本堂課一句話

選 agent framework 不是看哪個最紅，而是看你的問題需要 workflow、tools、memory、graph、evaluation 還是 deployment。

## 學習目標

學生上完後應該能：

- 比較 agent framework 的核心抽象
- 判斷何時不用 framework
- 設計 framework spike
- 建立選型 criteria
- 為 capstone 選擇技術路線

## 課前準備

- 閱讀：`curriculum/12-agent-frameworks-comparison_zh.md`
- Pattern：`patterns/README_zh.md`
- Capstone：`projects/capstone-agent-colony.md`

## 90 分鐘課程流程

| 時間 | 活動 |
|---:|---|
| 0-10 | 問：為什麼 framework 不能替你解決架構問題？ |
| 10-25 | 講 framework selection dimensions |
| 25-40 | 比較 hand-rolled、LangGraph、CrewAI、AutoGen、Agents SDK |
| 40-55 | Live demo：同一個 workflow 如何映射到不同 framework |
| 55-75 | 學生為 capstone 做 framework decision record |
| 75-85 | 討論 lock-in、debugging、observability |
| 85-90 | Recap：先懂 pattern，再選 framework |

## 板書心智模型

```text
Problem Shape
  ↓
Required Pattern
  ↓
Runtime Needs
  ↓
Observability Needs
  ↓
Team Familiarity
  ↓
Framework Choice
```

## Live Demo

同一個 planner-reviewer workflow：

- hand-rolled Python：最透明
- graph framework：分支清楚
- multi-agent framework：角色協作方便
- hosted agents SDK：整合與部署方便

## 課堂練習

學生為自己的 capstone 填：

```text
Required patterns:
Tools:
Memory:
Graph complexity:
Human approval:
Eval needs:
Deployment target:
Chosen framework:
Why not the alternatives:
```

## 常見誤解

- 誤解：用了 agent framework，系統就比較 production-ready。
- 修正：framework 提供抽象，不會自動補 evaluation、safety、domain boundary。

## 作業

寫一份 1 頁 Architecture Decision Record，說明 capstone 選型。

## 評量標準

| 項目 | 通過標準 |
|---|---|
| Criteria | 不是只看流行度 |
| Fit | framework 對應問題形狀 |
| Tradeoff | 說得出替代方案缺點 |
| Debug | 考慮 observability |
| Capstone | 能支持最終專案需求 |
