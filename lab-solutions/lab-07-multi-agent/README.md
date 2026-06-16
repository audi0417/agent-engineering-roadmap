# Lab 07 Solution Shape - Multi-Agent

## Expected Artifacts

```text
team_spec.md
routing_table.md
handoff_schema.json
conflict_policy.md
```

## Example Routing Table

| Task Type | Route | Reason |
|---|---|---|
| finance research | finance_specialist | domain-specific risk boundary |
| health education | healthcare_specialist | safety escalation needed |
| ticket routing | enterprise_specialist | operational workflow |

## Handoff Schema

```json
{
  "task": "...",
  "context": "...",
  "constraints": ["..."],
  "expected_output": "...",
  "risk_level": "low|medium|high"
}
```

## Passing Standard

- Supervisor has final authority.
- Specialist roles do not overlap too much.
- Handoffs are structured.
- Conflict resolution is explicit.
- Shared memory has write rules.
