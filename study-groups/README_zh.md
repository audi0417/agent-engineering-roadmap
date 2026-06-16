# 讀書會套件

這個套件可以用來把 Agent Engineering Roadmap 變成讀書會、內訓或 community workshop。

## 形式

| 形式 | 適合對象 | 時間投入 |
|---|---|---|
| 4 週 sprint | 有經驗的工程師 | 每週 2 次 |
| 8 週 cohort | 程度混合的學習者 | 每週 1 次 |
| 1 日 workshop | 團隊 kickoff | 4 個主題區塊 |

## 4 週 Sprint

| Week | 重點 | 執行 | 交付成果 |
|---|---|---|---|
| 1 | Foundations、tools、MCP | Examples 01-03 | Agent spec 與 tool contract |
| 2 | Memory、RAG、workflow | Examples 04, 05, 08 | RAG eval 與 workflow sketch |
| 3 | Graph、multi-agent、approval | Examples 06, 09 | Approval graph 與 routing tests |
| 4 | Production、observability、security | Examples 10, 11, benchmark | Trace review 與 injection defense |

## 8 週 Cohort

| Week | 主題 | 討論問題 |
|---|---|---|
| 1 | Agent 是什麼？ | Chatbot 哪裡開始不夠用？ |
| 2 | Tool use 與 MCP | 哪些工具不能無審核呼叫？ |
| 3 | Memory | Agent 應該忘記什麼？ |
| 4 | RAG | 怎麼知道答案有 grounded？ |
| 5 | Workflow graphs | 哪些狀態應該明確建模？ |
| 6 | Multi-agent systems | 什麼時候加更多 agent 反而變差？ |
| 7 | Observability | 哪一段 trace 能解釋錯誤答案？ |
| 8 | Security 與 capstone | 哪種攻擊會打壞你的設計？ |

## 每次聚會模板

1. 用一個 failure story 開場。
2. 畫出 mental model。
3. 跑最小 example。
4. 改一個東西，先預測結果。
5. 跑 benchmark 或 eval。
6. 把一個改善點記成 issue。

## 主持人 Checklist

- [ ] 每次聚會前選好一個 runnable example
- [ ] 準備一個 failure case
- [ ] 討論要連回 observable behavior
- [ ] 每週請學員交一個 artifact
- [ ] 每次聚會最後收斂成一個 repo improvement

