# Example 05 - Multi-Agent Workflow

This example demonstrates a simple planner -> researcher -> writer -> reviewer workflow.

好，各位同學看到 multi-agent 很容易想成「很多 AI 放在一起就會變聰明」。但其實沒有。很多 agent 放在一起，如果沒有 workflow，就只是很多人同時講話而已。蠻熱鬧，但不一定有用。

This demo keeps the agents deterministic so you can inspect the orchestration logic first.

## What this example teaches

- how to split one task into clear stages
- how to pass artifacts between agents
- how to review output with a rubric
- how to retry when a quality gate fails

## Files

| File | Purpose |
|---|---|
| `main.py` | Runs the workflow |
| `workflow.py` | Agent functions and orchestration loop |
| `agent_config.json` | Roles, rubric, and retry settings |

## Run

```bash
python main.py
```

## Workflow

```text
Task
  |
  v
Planner creates a plan
  |
  v
Researcher collects facts
  |
  v
Writer drafts an answer
  |
  v
Reviewer checks rubric
  |
  +-- pass --> final output
  |
  +-- fail --> revise with feedback
```

## Why this matters

The useful part of a multi-agent system is not the number of agents. The useful part is the contract between them.

Each stage should answer three questions:

- What artifact do I receive?
- What artifact do I produce?
- How will the next stage know whether my work is good enough?

If you cannot answer these questions, adding more agents will usually make the system harder to debug.
