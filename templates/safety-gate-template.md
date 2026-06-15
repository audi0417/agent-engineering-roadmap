# Safety Gate Template

## Purpose

Define when an agent may continue, ask for approval, or refuse.

## Risk Levels

| Level | Description | Default Action |
|---|---|---|
| Low | Reversible text-only task | continue |
| Medium | Tool call that reads data or drafts changes | continue with logging |
| High | Writes data, spends money, sends messages, affects users | ask approval |
| Prohibited | Illegal, credential theft, harmful, or policy-violating action | refuse |

## Approval Gate

Ask for human approval when the action:

- writes to an external system
- sends a message on behalf of a user or company
- changes money, access, permissions, or production data
- makes medical, legal, or financial decisions
- uses uncertain retrieved information in a high-impact context

## Refusal Pattern

```text
I cannot perform that action because <specific safety reason>.
I can help with <safe alternative>.
```

## Logging

For every blocked or approved action, record:

```text
action:
risk_level:
reason:
user_approved:
timestamp:
tool_called:
result:
```
