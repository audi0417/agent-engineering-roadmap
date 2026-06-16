# Example 09 - Graph Approval Agent

[English](README.md)

這個範例示範一個小型 graph-based agent，並加入 human approval gate。

它把三個 module 接起來：

- Module 06：Graph-based Agents
- Module 08：Human-in-the-loop
- Module 09：Production Agent Systems

好，這個範例不是要教你自己發明 framework。它只是把 control logic 打開給你看。你會看到 state 怎麼走、node 怎麼跑、什麼時候不能直接 execute。

## 這個範例教什麼？

- 如何明確表示 agent state
- 如何用 conditional edges 移動到下一個 node
- 如何把 high-risk action 送到 approval，而不是直接執行
- 如何用 deterministic eval cases 測 graph transitions
- production gate 如何避免 unsafe autonomy

## 檔案

| File | Purpose |
|---|---|
| `main.py` | 執行單次 graph run 與 eval suite |
| `graph_agent.py` | State、nodes、transition logic、approval behavior |
| `eval_cases.json` | Graph transition regression cases |

## 執行

```bash
python main.py
```

可以試：

```text
Summarize this support ticket.
```

```text
Delete production customer records for account 1842.
```

## Graph

```text
START
  |
  v
classify_risk
  |
  +-- low/medium --> execute_read_only
  |
  +-- high/critical --> request_approval
  |
  v
review
  |
  v
END
```

## 生產環境重點

重點不是這段 code 多厲害。

重點是 control surface：

- high-risk actions 不會直接執行
- 每個 transition 都看得到
- eval 測的是 path，不只是 final text 順不順
