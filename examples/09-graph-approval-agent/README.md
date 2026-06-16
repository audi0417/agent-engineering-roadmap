# Example 09 - Graph Approval Agent

This example demonstrates a small graph-based agent with a human approval gate.

It connects three course topics:

- Module 06: Graph-based Agents
- Module 08: Human-in-the-loop
- Module 09: Production Agent Systems

The goal is not to build a framework. The goal is to see the control logic directly.

## What this example teaches

- how to represent agent state explicitly
- how to move through graph nodes with conditional edges
- how to route high-risk actions to approval instead of execution
- how to test graph transitions with deterministic eval cases
- how production gates prevent unsafe autonomy

## Files

| File | Purpose |
|---|---|
| `main.py` | Runs one graph execution and the eval suite |
| `graph_agent.py` | State, nodes, transition logic, and approval behavior |
| `eval_cases.json` | Regression cases for graph transitions |

## Run

```bash
python main.py
```

Try:

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

## Production note

The important part is not the specific code. The important part is the control surface:

- high-risk actions do not execute directly
- every transition is visible
- evals check the path, not only the final text
