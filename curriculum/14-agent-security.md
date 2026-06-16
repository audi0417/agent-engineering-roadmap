# 14 Agent Security

## Goal

Learn how to defend agent systems against prompt injection, tool misuse, memory leakage, and unsafe authority transfer.

## Why It Matters

An agent is more dangerous than a chatbot because it can act.

When an agent can retrieve documents, call tools, remember user data, and hand work to other agents, an attacker can try to influence any of those channels.

Security is not a single filter at the end. It is a set of boundaries around every input and action.

## The Core Rule

Retrieved documents, tool results, emails, web pages, tickets, and user uploads are data.

They are not authority.

Only trusted policy and explicitly approved user intent should control the agent.

## Threat Model

| Threat | Example | Defense |
|---|---|---|
| Prompt injection | A document says "ignore previous instructions" | Treat retrieved content as untrusted data |
| Tool misuse | Agent calls delete or payment tool too early | Add approval gates and tool allowlists |
| Memory leakage | Agent reveals private user memory | Classify memory and restrict retrieval |
| Data exfiltration | Tool result asks agent to send secrets elsewhere | Block external transfer without approval |
| Handoff confusion | Specialist agent accepts unsafe delegated task | Preserve policy across handoffs |
| Over-permissioned MCP server | Tool has broader access than needed | Use least privilege and scoped credentials |

## Black Box View

```text
input
   ↓
agent
   ↓
tool / retrieval / memory / handoff
   ↓
output
```

This view hides the problem: every arrow is a possible attack surface.

## Mechanism View

```text
User input ─────────────┐
Retrieved documents ────┼──> trust classifier ──> safe context
Tool results ───────────┘
                                ↓
Trusted policy + user intent -> agent planner -> approved action
```

The agent should not merge all text into one authority level.

## Practical Exercise

Run:

```bash
python examples/11-prompt-injection-defense/main.py
```

The example retrieves a trusted policy document and a poisoned customer note. The poisoned note is blocked because it tries to override system policy.

## Security Checklist

- [ ] Separate trusted policy from untrusted content
- [ ] Scan retrieved text for instruction override attempts
- [ ] Require approval for destructive actions
- [ ] Keep tool permissions narrow
- [ ] Preserve policy during handoffs
- [ ] Redact secrets before logging
- [ ] Evaluate refusal and escalation behavior
- [ ] Record security decisions in traces

## Common Misconceptions

### "The LLM will know it is malicious"

Sometimes it will. Sometimes it will not.

Security should not depend on the model noticing every attack.

### "Prompt injection only happens on the web"

It can appear in PDFs, emails, support tickets, calendar invites, tool results, database rows, and memory.

### "A better system prompt fixes it"

A stronger system prompt helps, but system prompts are not enough. You also need tool permissions, content isolation, approval gates, and evals.

## References

- [Model Context Protocol Security Principles](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

