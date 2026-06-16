# 17 MCP Modernization

## Goal

Understand the modern MCP-style integration surface beyond simple tool calling.

## Why It Matters

Early agent demos often treat MCP as "a way to call tools."

Production integrations need more structure:

- tools for actions
- resources for readable context
- prompts for reusable task templates
- authorization for scoped access
- elicitation when required information is missing
- gateway policies across many servers

## Mental Model

MCP-style design separates authority from capability.

```text
agent
   ↓
gateway / client
   ↓
authorization + policy
   ↓
tools, resources, prompts
```

The agent should not directly own every integration. The gateway enforces what can be read, what can be called, and what needs clarification.

## Core Concepts

| Concept | Meaning |
|---|---|
| Tool | Callable action or computation |
| Resource | Readable context identified by URI |
| Prompt | Reusable task template |
| Authorization | Capability-scoped access control |
| Elicitation | Ask for missing required information |
| Gateway | Policy and routing layer across integrations |

## Common Failure Modes

### Tool-Only Thinking

Everything becomes a tool, even read-only context. Permissions become too broad.

### No Authorization Boundary

Every agent can call every integration.

### Missing Elicitation

The agent guesses required arguments instead of asking for them.

### No Gateway Policy

Each server implements its own safety rules inconsistently.

## Practical Exercise

Run:

```bash
python examples/14-modern-mcp-gateway/main.py
```

Inspect:

- capability listing
- resource read
- prompt access
- tool call authorization
- elicitation for missing arguments

## Production Checklist

- [ ] Tools and resources have separate permissions
- [ ] Tokens are scoped by capability
- [ ] Missing required arguments trigger elicitation
- [ ] Gateway logs every denied operation
- [ ] High-risk tools require approval
- [ ] Resources expose identifiers before raw content
- [ ] Prompts are versioned
- [ ] Tool schemas reject unexpected arguments

