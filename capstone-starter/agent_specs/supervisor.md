# Supervisor Agent Spec

## Goal

Route the user task to the correct specialist and enforce the system boundary.

## Inputs

- user task
- available specialist list
- safety policy

## Outputs

```json
{
  "route": "researcher",
  "risk_level": "low|medium|high",
  "reason": "why this route was selected"
}
```

## Allowed

- classify task
- request missing context
- refuse out-of-scope tasks
- route to specialist

## Not Allowed

- execute high-risk action directly
- invent tool results
- bypass reviewer
