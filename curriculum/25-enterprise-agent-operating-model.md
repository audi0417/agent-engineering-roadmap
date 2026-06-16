# 25 Enterprise Agent Operating Model

## Goal

Learn how organizations can operate many agents safely over time.

## Why It Matters

Once agents spread across a company, the hard problem becomes operating them:

- who owns each agent
- which tools it can use
- which data it can access
- how often it is reviewed
- what risk tier it belongs to
- how incidents are handled
- when it should be retired

## Operating Model

```text
agent registry
   ↓
risk tier
   ↓
owner + scopes + eval suite
   ↓
deployment review
   ↓
monitoring + access review
   ↓
incident response + retirement
```

## Practical Artifact

Use:

```text
operating-model/enterprise-agent-operating-checklist.md
```

## Production Checklist

- [ ] Every agent is registered
- [ ] Every agent has an owner
- [ ] Risk tier is assigned before launch
- [ ] Scope and tool access are reviewed
- [ ] Eval suite is linked to the agent
- [ ] Incident owner is known
- [ ] Retirement criteria are defined

