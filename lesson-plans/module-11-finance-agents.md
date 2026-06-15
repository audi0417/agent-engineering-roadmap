# Module 11 教案 - Finance Agents

## 本堂課一句話

Finance agent 應該支援研究與風險分析，不應該直接替使用者做投資決策。

## 學習目標

學生上完後應該能：

- 區分 research support 與 investment advice
- 設計 finance risk boundary
- 建立 assumptions table
- 寫 factor/risk-oriented output
- 設計 finance eval cases

## 課前準備

- 閱讀：`curriculum/11-domain-agent-finance_zh.md`
- Domain：`finance/finance-agent-colony.md`
- 範例：`examples/06-agent-colony/README.md`

## 90 分鐘課程流程

| 時間 | 活動 |
|---:|---|
| 0-10 | 問：研究報告和買賣建議差在哪？ |
| 10-25 | 講 finance agent boundary |
| 25-40 | 拆 finance colony |
| 40-55 | Live demo：比較兩家公司但不給買賣建議 |
| 55-75 | 學生設計 finance research workflow |
| 75-85 | 討論 stale data、source、assumptions |
| 85-90 | Recap：finance agent 要把 facts 和 opinions 分開 |

## 板書心智模型

```text
Finance Question
  ↓
Clarify scope
  ↓
Collect facts
  ↓
State assumptions
  ↓
Analyze risks
  ↓
No personalized recommendation
```

## Live Demo

輸入：

```text
我應該買 A 公司還是 B 公司？
```

安全輸出應該改成：

- compare business drivers
- list risks
- state assumptions
- suggest further research
- avoid direct buy/sell instruction

## 課堂練習

學生設計一份 company comparison template：

- business model
- growth drivers
- risks
- valuation questions
- missing data

## 常見誤解

- 誤解：只要資料正確，就可以給投資建議。
- 修正：個人投資建議需要知道風險承受度、目標、法規與責任邊界。

## 作業

寫 10 個 finance eval cases，至少 3 個 unsafe recommendation cases。

## 評量標準

| 項目 | 通過標準 |
|---|---|
| Boundary | research vs advice 清楚 |
| Facts | 與 assumptions 分開 |
| Risk | 明確列出 |
| Data | 標記缺失與時效 |
| Safety | 不給個人化買賣指令 |
