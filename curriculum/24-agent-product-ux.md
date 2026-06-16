# 24 Agent Product UX

## Goal

Learn how to design user experiences that make agents trustworthy, recoverable, and understandable.

## Why It Matters

An agent can be technically correct and still feel unsafe to users.

Agent UX must explain:

- what the agent is doing
- what it is allowed to do
- when it needs approval
- how to undo or stop work
- why it refused
- what evidence it used

## UX Patterns

| Pattern | Purpose |
|---|---|
| Approval preview | Show tool, arguments, risk, expected effect, rollback |
| Activity timeline | Make agent steps visible |
| Evidence drawer | Show retrieved sources and trace summary |
| Undo or rollback | Recover from approved side effects |
| Confidence boundary | Separate facts, assumptions, and recommendations |
| Escalation path | Move high-risk work to humans |

## Practical Artifact

Use:

```text
product-ux/agent-product-ux-checklist.md
```

## Production Checklist

- [ ] User can see what the agent is doing
- [ ] High-risk actions require preview and approval
- [ ] Refusals explain the safe alternative
- [ ] Evidence is available without overwhelming the user
- [ ] Undo or rollback is designed where possible
- [ ] Users can stop or escalate the agent

