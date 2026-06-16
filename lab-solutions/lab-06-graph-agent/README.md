# Lab 06 Solution Shape - Graph Agent

## Expected Artifacts

```text
graph_spec.md
transition_table.md
graph_eval_cases.json
```

## Example Transition Table

| Current State | Condition | Next State |
|---|---|---|
| START | any input | classify_risk |
| classify_risk | low or medium risk | execute_read_only |
| classify_risk | high or critical risk | request_approval |
| execute_read_only | completed | review |
| request_approval | approval packet created | review |
| review | passed | END |

## Eval Cases

```json
[
  {
    "id": "high_risk_delete",
    "expected_path": ["START", "classify_risk", "request_approval", "review", "END"]
  }
]
```

## Passing Standard

- Graph has start and end states.
- Every edge has a condition.
- Failure and approval paths exist.
- Eval checks path correctness.

## Suggested Starting Point

```bash
python examples/09-graph-approval-agent/main.py
```
