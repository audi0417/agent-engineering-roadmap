# Lab 05 Solution Shape - Workflow

## Expected Artifacts

```text
workflow.md
workflow_eval_cases.json
retry_policy.md
```

## Example Workflow

```text
Input
  ↓
Classify task
  ↓
Plan steps
  ↓
Execute draft
  ↓
Review with rubric
  ↓
Pass → Final
Fail → Revise until max_rounds
```

## Review Rubric

```text
Must include:
- goal
- implementation steps
- risk or limitation
- next action
```

## Eval Cases

```json
[
  {
    "id": "happy_path",
    "expected": "review passes"
  },
  {
    "id": "missing_risk",
    "expected": "review fails and asks revision"
  }
]
```

## Passing Standard

- Each step has an artifact.
- Review has a rubric.
- Retry has a maximum.
- Failure behavior is visible.
