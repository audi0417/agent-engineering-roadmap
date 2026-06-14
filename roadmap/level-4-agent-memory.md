# Level 4 — Agent Memory

## Goal

Design memory systems that allow agents to retain useful context across tasks and sessions.

Memory is one of the key differences between a chatbot and an agent. A chatbot responds to the current conversation. An agent with memory can learn from past tasks, retrieve user preferences, reuse domain knowledge, and coordinate with other agents.

---

## Memory Types

### Short-term Memory

Context used only during the current task or conversation.

Examples:

- current user request
- intermediate reasoning state
- temporary tool results
- active workflow state

### Episodic Memory

Records of past events, tasks, conversations, or decisions.

Examples:

- previous research tasks
- past user requests
- completed workflows
- historical care notes

### Semantic Memory

Reusable factual or conceptual knowledge.

Examples:

- product documentation
- medical guidelines
- investment research notes
- technical architecture decisions

### User Memory

User-specific preferences, constraints, and profile information.

Examples:

- preferred language
- writing style
- project background
- domain constraints

### Shared Memory

Memory that can be used across multiple agents in the same colony.

Examples:

- shared task board
- colony-level knowledge base
- cross-agent research notes
- domain-specific case memory

---

## Memory Architecture

```text
User / Task Input
      ↓
Memory Retrieval
      ↓
Agent Reasoning
      ↓
Tool Use / Workflow
      ↓
Memory Write Decision
      ↓
Memory Store + Audit Log
```

---

## What to Learn

- How to decide what should be remembered
- How to retrieve relevant memories
- How to rank memories by relevance and recency
- How to prevent memory pollution
- How to separate private memory from shared memory
- How to audit memory writes
- How to delete or update stale memory
- How to handle sensitive information

---

## Hands-on Projects

### Project 1 — Personal Memory Agent

Build an agent that remembers user preferences and reuses them in future responses.

Learning points:

- user profile memory
- memory retrieval
- memory update rules
- avoiding over-personalization

### Project 2 — Long-Term Task Memory

Build an agent that records completed tasks and can summarize previous work.

Learning points:

- episodic memory
- task history
- structured memory entries
- retrieval by project or date

### Project 3 — Shared Multi-Agent Memory

Build a shared memory layer for a researcher, writer, and reviewer agent.

Learning points:

- shared notes
- role-based memory access
- conflict handling
- source tracking

### Project 4 — Healthcare Memory Prototype

Build a synthetic healthcare memory system for care notes, nutrition logs, and follow-up history.

Learning points:

- sensitive data boundaries
- longitudinal health context
- safety-aware summaries
- human review before memory writes

---

## Memory Write Policy

A good memory system should not store everything.

Use a write policy such as:

```text
Store only if the information is:
1. stable over time
2. useful for future tasks
3. not overly sensitive
4. not already stored
5. approved by policy or user consent
```

---

## Common Mistakes

- Storing every conversation turn
- Mixing temporary context with long-term memory
- Saving sensitive information without consent
- Letting agents overwrite important facts too easily
- Retrieving too many irrelevant memories
- Treating vector search as the entire memory system
- Failing to audit memory writes

---

## Outcome

After this level, you should be able to build agents that remember useful information without polluting context or leaking sensitive data.

You should also understand that memory is a product and governance problem, not just a vector database problem.
