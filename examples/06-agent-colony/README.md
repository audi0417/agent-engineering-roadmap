# Example 06 - Agent Colony

This example demonstrates a small shared-memory agent colony.

所謂 Agent Colony，其實就是多個 agent 共用任務板、共享記憶、共享評估規則而已。聽起來很神奇，但打開來看，就是「誰負責什麼、資料放哪裡、誰檢查結果」。

This demo uses domain agents for healthcare, finance, and enterprise automation. It does not make real medical or investment decisions. It only shows the coordination pattern.

## What this example teaches

- how a supervisor routes tasks to domain agents
- how shared memory keeps colony-level context
- how an evaluator checks final output before delivery
- how to keep high-risk domains behind explicit disclaimers

## Files

| File | Purpose |
|---|---|
| `main.py` | Runs the colony demo |
| `colony.py` | Supervisor, domain agents, shared memory, evaluator |
| `colony_config.json` | Domain routing rules and safety policy |

## Run

```bash
python main.py
```

Try:

```text
Build a finance research workflow for comparing two companies.
```

## Architecture

```text
User task
  |
  v
Supervisor
  |
  +--> Healthcare Agent
  +--> Finance Agent
  +--> Enterprise Agent
  |
  v
Shared Memory
  |
  v
Evaluator
  |
  v
Final answer
```

## Production notes

In production, each domain agent should have its own tools, permissions, evaluation set, and human approval gate. The colony should not be a giant prompt with a list of roles. A colony is an operating model for agent teams.
