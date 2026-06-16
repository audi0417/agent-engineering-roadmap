# Domain Casebooks

Domain casebooks turn the course from generic agent engineering into realistic practice.

Each casebook includes:

- realistic user scenarios
- safe and unsafe requests
- routing and approval decisions
- expected agent behavior
- evaluation cases
- failure modes to watch

Use these after the core examples:

```bash
python showcases/healthcare-agent-colony/main.py
python showcases/finance-research-agent/main.py
python showcases/enterprise-support-agent/main.py
```

## Casebooks

| Domain | File | Focus |
|---|---|---|
| Healthcare | [Healthcare Casebook](healthcare-casebook.md) | Education boundary, escalation, privacy |
| Finance | [Finance Casebook](finance-casebook.md) | Research support, uncertainty, no advice |
| Enterprise | [Enterprise Casebook](enterprise-casebook.md) | Ticket routing, approval, destructive actions |

## How To Study

For each case:

1. Classify the user request.
2. Identify the risk level.
3. Decide whether tools are allowed.
4. Decide whether human approval is required.
5. Write the expected response boundary.
6. Add an eval case.

The important point: domain agents are not generic chatbots with a domain label. They are workflows with domain-specific safety boundaries.
