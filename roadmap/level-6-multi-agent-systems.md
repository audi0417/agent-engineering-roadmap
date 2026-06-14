# Level 6 — Multi-Agent Systems

## Goal

Build systems where multiple agents collaborate, critique, debate, or specialize.

Multi-agent systems are useful when a task benefits from role separation. Instead of asking one agent to do everything, you can assign different responsibilities to different agents and coordinate their work through a workflow.

---

## When to Use Multiple Agents

Use multiple agents when the task needs:

- different areas of expertise
- independent review or critique
- parallel research
- planning and execution separation
- safety or compliance checks
- role-based tool access
- different output responsibilities

Do not use multiple agents just because it sounds advanced.

A simple workflow with one agent is often better than an unnecessary multi-agent system.

---

## Basic Multi-Agent Pattern

```text
User Request
   ↓
Supervisor Agent
   ↓
Worker Agents
   ↓
Reviewer Agent
   ↓
Final Response
```

---

## Core Patterns

### Supervisor Pattern

A supervisor decomposes the task, assigns work, and synthesizes the final output.

```text
Supervisor
├── Researcher
├── Writer
└── Reviewer
```

Best for:

- reports
- research tasks
- document workflows
- enterprise task routing

### Debate Pattern

Two or more agents argue different perspectives before producing a conclusion.

```text
Agent A: Pro
Agent B: Con
Judge Agent: Final decision
```

Best for:

- decision support
- strategy analysis
- risk review
- product tradeoff discussions

### Reflection Pattern

One agent produces output and another agent critiques it.

```text
Generator Agent
   ↓
Critic Agent
   ↓
Revised Output
```

Best for:

- writing improvement
- code review
- factual consistency checks
- safety checks

### Specialist Pattern

Each agent focuses on one domain or responsibility.

```text
Healthcare Supervisor
├── Nutrition Agent
├── Vital Sign Agent
├── Psychology Agent
└── Safety Agent
```

Best for:

- healthcare
- finance
- legal
- customer support
- enterprise workflows

---

## Agent Communication

Agents should not communicate freely without structure.

Use structured messages:

```json
{
  "agent": "researcher",
  "task": "summarize evidence",
  "findings": [],
  "uncertainties": [],
  "next_actions": []
}
```

Structured communication improves reliability, debugging, and evaluation.

---

## Tool Access by Role

Not every agent should access every tool.

Example:

| Agent | Allowed Tools |
|---|---|
| Researcher | search, document retrieval |
| Writer | memory read, outline generator |
| Reviewer | evaluator, citation checker |
| Tool Agent | MCP tools |
| Safety Agent | policy checker, risk classifier |

This reduces risk and makes behavior easier to audit.

---

## Hands-on Projects

### Project 1 — Researcher + Writer + Reviewer

Build a system where one agent researches, one writes, and one reviews.

Learning points:

- role separation
- structured handoff
- review loop
- final synthesis

### Project 2 — Coder + Tester + Reviewer

Build a coding workflow where one agent writes code, one creates tests, and one reviews quality.

Learning points:

- code generation
- test generation
- critique loop
- failure correction

### Project 3 — Healthcare Specialist Team

Build a synthetic healthcare team that separates nutrition, vital signs, psychology, and safety review.

Learning points:

- domain specialization
- safety-aware output
- role-based memory access
- human approval gate

### Project 4 — Finance Research Team

Build a finance research team for market research, factor analysis, risk review, and report writing.

Learning points:

- investment research workflow
- data tool routing
- uncertainty labeling
- risk-aware reporting

---

## Design Checklist

Before using multiple agents, ask:

- What does each agent do?
- Why is one agent not enough?
- How do agents pass information?
- Who has final authority?
- Which tools can each agent use?
- Which memory can each agent access?
- How are conflicts resolved?
- How is the final answer evaluated?

---

## Common Mistakes

- Creating too many agents
- Giving agents overlapping roles
- Letting agents talk endlessly
- Not defining final authority
- Skipping structured handoff formats
- Giving all agents the same tools
- Treating roleplay as system design
- Using multi-agent systems when a simple workflow is enough

---

## Outcome

You should understand when multi-agent systems add value and when they introduce unnecessary complexity.

This level prepares you for Agent Colony design, where multiple agents share memory, tools, evaluation, and production boundaries.
