# Level 5 — Agent Workflow

## Goal

Move from free-form agent behavior to controlled, observable, and reliable workflows.

A workflow gives an agent system structure. Instead of letting the model decide everything in one large prompt, a workflow breaks the task into states, transitions, checks, retries, and approval gates.

---

## Why Workflows Matter

Free-form agents can be impressive in demos, but production systems need predictable behavior.

Workflows help with:

- task decomposition
- quality control
- error recovery
- human approval
- observability
- reproducibility
- cost control

---

## Basic Workflow Pattern

```text
Input
  ↓
Classify task
  ↓
Plan
  ↓
Execute
  ↓
Review
  ↓
Revise if needed
  ↓
Final output
```

---

## Core Topics

### State Machines

A state machine defines where the system is and what can happen next.

Example states:

- received
- planning
- retrieving context
- executing tools
- reviewing output
- waiting for approval
- completed
- failed

### Task Routing

Routing sends different tasks to different flows.

Examples:

- support question → support workflow
- document upload → document extraction workflow
- healthcare note → care summary workflow
- trading idea → research and backtest workflow

### Planning-Execution-Review Loop

A useful agent workflow often includes three phases:

```text
Plan: decide what to do
Execute: do the work
Review: check whether the result is good enough
```

### Retry and Fallback

Workflows should expect failure.

Common fallback strategies:

- retry with corrected input
- use a smaller task
- ask user for clarification
- escalate to human
- return partial output
- stop safely

### Human-in-the-loop

Some actions should require human approval.

Examples:

- sending an email
- changing a medical record
- writing long-term memory
- making financial decisions
- deleting data
- publishing content

### Observability

A workflow should produce traces.

Track:

- user input
- selected route
- prompts
- tool calls
- retrieved context
- intermediate outputs
- evaluator feedback
- final output
- cost and latency

---

## Hands-on Projects

### Project 1 — Research Workflow Agent

Build a workflow that researches a topic, summarizes findings, reviews quality, and produces a final report.

Learning points:

- task routing
- search and retrieval
- review loop
- citation discipline

### Project 2 — Document Processing Workflow

Build a workflow that extracts fields from a document, validates output, and flags uncertain fields.

Learning points:

- structured extraction
- validation
- confidence labels
- human review queue

### Project 3 — Care Management Workflow

Build a synthetic healthcare workflow that summarizes patient data and generates follow-up suggestions.

Learning points:

- safety gates
- domain routing
- memory retrieval
- evaluator agent

### Project 4 — Trading Research Workflow

Build a workflow that turns a trading idea into a research note, factor hypothesis, and backtest plan.

Learning points:

- research decomposition
- data tool routing
- risk review
- report generation

---

## Workflow Design Checklist

Before building a workflow, ask:

- What are the states?
- What triggers each transition?
- What tools are allowed in each state?
- What should happen when a tool fails?
- What output format is required?
- What needs human approval?
- What should be logged?
- How will quality be evaluated?

---

## Common Mistakes

- Letting the agent decide every step without constraints
- Creating a workflow that is too rigid for real user inputs
- Skipping retry and fallback paths
- Not logging intermediate steps
- Missing human approval gates
- Mixing planning, execution, and review in one prompt
- Treating workflow orchestration as an afterthought

---

## Outcome

You should be able to design agent workflows that are predictable enough for real products.

This level prepares you for multi-agent systems, where different agents may own different workflow steps.
