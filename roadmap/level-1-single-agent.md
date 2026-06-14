# Level 1 — Single Agent

## Goal

Build your first AI agent that can follow instructions, reason through tasks, and produce structured outputs.

A single agent is the smallest useful unit in Agent Engineering. It has a role, a task boundary, a behavior policy, and an output contract.

---

## What is an Agent?

A simple agent can be described as:

```text
Goal + Context + Reasoning + Action + Output
```

In Level 1, the agent may not use external tools yet. The focus is on role design, task control, structured output, and reliability.

---

## Basic Agent Loop

```text
Receive task
   ↓
Understand goal
   ↓
Plan response
   ↓
Generate answer
   ↓
Validate format
   ↓
Return result
```

This loop becomes more powerful in later levels when tools, memory, and workflows are added.

---

## Core Topics

### Role Design

A good agent role defines:

- what the agent is responsible for
- what it should not do
- what input it expects
- what output it must produce
- what quality standard it should follow

Bad role:

```text
You are a helpful assistant.
```

Better role:

```text
You are a research summary agent. Your job is to turn long technical notes into concise, structured summaries with key claims, evidence, risks, and next steps.
```

### Task Boundary

Agents become unreliable when the task is too broad.

Good task boundaries:

- summarize this document
- classify this email
- extract fields from this message
- rewrite this paragraph
- generate a test plan

Weak task boundaries:

- solve my business
- manage my whole company
- be my autonomous employee

### System Prompt

The system prompt defines the agent's durable behavior.

A strong system prompt usually includes:

- role
- goal
- constraints
- output format
- safety rules
- examples
- escalation behavior

### Structured Output

Single agents should produce predictable outputs.

Examples:

- JSON
- Markdown table
- checklist
- scorecard
- report template
- action plan

### Error Handling

Even a single agent should know what to do when input is incomplete or ambiguous.

Common strategies:

- ask a clarifying question
- make a clearly labeled assumption
- return partial results
- refuse unsafe requests
- explain missing information

---

## Agent Design Template

```text
Agent Name:
Purpose:
Inputs:
Outputs:
Allowed Actions:
Not Allowed:
Quality Criteria:
Failure Behavior:
Examples:
```

---

## Hands-on Projects

### Project 1 — Personal Assistant Agent

Build an agent that turns messy user notes into clear action items.

Learning points:

- role prompting
- task boundaries
- Markdown output
- action extraction

### Project 2 — Research Summary Agent

Build an agent that summarizes articles, papers, or reports.

Learning points:

- structured summaries
- key claim extraction
- uncertainty labeling
- evidence-aware writing

### Project 3 — Code Explanation Agent

Build an agent that explains code snippets for beginners.

Learning points:

- technical explanation
- step-by-step output
- error identification
- safer code interpretation

### Project 4 — JSON Extraction Agent

Build an agent that extracts structured fields from raw text.

Learning points:

- schema design
- validation
- retry logic
- deterministic outputs

---

## Checklist

You are ready for Level 2 when you can:

- define a clear agent role
- write a useful system prompt
- constrain an agent's task boundary
- produce structured outputs
- handle incomplete input
- design a small agent test set
- compare good and bad agent outputs

---

## Common Mistakes

- Making the agent role too broad
- Using vague instructions
- Not defining the output format
- Asking a single agent to do too many jobs
- Treating the agent as autonomous before it is reliable
- Not testing edge cases

---

## Outcome

You should be able to build a single-purpose agent with a clear role, task boundary, and output format.

This level prepares you to add external tools in Level 2.
