# 19 Agent Identity And Permission

## Goal

Learn how to treat agents as identities with owners, scopes, permissions, and access reviews.

## Why It Matters

In production, an agent is not just code. It is an actor.

If an agent can read documents, inspect tickets, send messages, or request approvals, security teams need to know:

- who owns the agent
- what it can access
- which scopes it has
- which actions require review
- what it actually did
- when access should be revoked

## Mental Model

```text
agent identity
   ↓
scoped permission
   ↓
authorization check
   ↓
allowed / denied / review required
   ↓
audit log
```

Agents should follow least privilege just like human users and service accounts.

## Common Failure Modes

### Shared Super Token

Every agent uses the same broad API key.

### No Owner

Nobody knows who is responsible when the agent misbehaves.

### No Access Review

Old agents keep permissions long after their purpose changes.

### No Audit Log

The team cannot reconstruct which agent accessed which system.

## Practical Exercise

Run:

```bash
python examples/16-agent-permission-system/main.py
```

Observe how the researcher agent can read docs but cannot inspect tickets.

## Production Checklist

- [ ] Every agent has an owner
- [ ] Every agent has a risk tier
- [ ] Permissions use scopes
- [ ] High-risk actions require review
- [ ] Denied actions are logged
- [ ] Access reviews are scheduled
- [ ] Shared broad tokens are avoided
- [ ] Inactive agents are disabled

