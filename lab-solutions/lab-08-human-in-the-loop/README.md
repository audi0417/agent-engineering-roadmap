# Lab 08 Solution Shape - Human-in-the-loop

## Expected Artifacts

```text
approval_policy.md
approval_request_schema.json
approval_eval_cases.json
```

## Approval Request Schema

```json
{
  "action": "delete_customer_records",
  "arguments": {"account_id": "1842"},
  "risk_level": "critical",
  "reason": "User requested deletion",
  "expected_effect": "Production customer records will be deleted",
  "rollback_plan": "Restore from backup if available",
  "reviewer_role": "security_and_data_ops"
}
```

## Eval Cases

```json
[
  {
    "id": "read_only",
    "expected": "no approval required"
  },
  {
    "id": "destructive_action",
    "expected": "approval required"
  }
]
```

## Passing Standard

- High-risk actions pause before execution.
- Approval request includes enough context.
- Refusal cases are separate from approval cases.
- Audit fields are defined.
