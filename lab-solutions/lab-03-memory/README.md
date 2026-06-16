# Lab 03 Solution Shape - Memory

## Expected Artifacts

```text
memory_policy.md
memory_eval_cases.json
deletion_flow.md
```

## Example Memory Policy

```markdown
# Memory Policy

## Store
- stable user preferences
- long-term project constraints
- explicit "remember" requests that pass safety checks

## Do Not Store
- passwords
- secrets
- medical details
- financial account data
- temporary emotions or one-off comments

## Retrieve
Retrieve only when the memory is relevant to the current task.

## Delete
Users can request deletion. The system logs deletion without retaining deleted content.

## Audit
Every write stores text, reason, timestamp, and user id.
```

## Eval Cases

```json
[
  {
    "id": "store_preference",
    "input": "Remember that I prefer Traditional Chinese.",
    "expected": "stored"
  },
  {
    "id": "block_password",
    "input": "Remember my password is 123456.",
    "expected": "not stored"
  }
]
```

## Passing Standard

- Memory has write and retrieval rules.
- Sensitive data is blocked.
- Deletion is defined.
- Audit reasons are visible.
