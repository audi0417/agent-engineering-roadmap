# Level 8 — Production, Evaluation & Safety

## Goal

Deploy agent systems that are observable, secure, cost-controlled, and measurable.

A prototype agent can impress users. A production agent must be monitored, evaluated, secured, and governed. This level focuses on the engineering practices required to operate agents in real-world environments.

---

## Production Agent Requirements

A production-ready agent system should have:

- clear task boundaries
- reliable tool use
- memory governance
- evaluation datasets
- tracing and observability
- cost and latency monitoring
- security controls
- human approval gates
- rollback and recovery paths

---

## Core Topics

### Agent Evaluation

Agent evaluation checks whether the system completes tasks correctly and safely.

Evaluate:

- task completion
- factual accuracy
- instruction following
- output format
- safety compliance
- user satisfaction
- latency and cost

### Tool-Use Evaluation

Tool-use evaluation checks whether the agent selected the right tool and used it correctly.

Track:

- whether a tool was needed
- whether the correct tool was selected
- whether arguments were valid
- whether the result was interpreted correctly
- whether unsafe actions were blocked

### RAG Evaluation

RAG evaluation checks both retrieval and generation.

Metrics and checks:

- retrieval precision
- retrieval recall
- answer faithfulness
- citation quality
- source relevance
- hallucination rate

### Observability

Production agents need traces, logs, and dashboards.

Track:

- prompts
- model calls
- tool calls
- memory reads and writes
- retrieved documents
- evaluator feedback
- user feedback
- cost
- latency
- errors

### Cost Control

Agent systems can become expensive because they may involve multiple model calls, retrieval steps, and tool calls.

Cost control strategies:

- use smaller models for simple tasks
- cache repeated results
- limit tool calls
- summarize long context
- set maximum workflow steps
- monitor token usage
- route tasks by complexity

### Prompt Injection Defense

Prompt injection happens when untrusted content tries to manipulate the agent.

Defense strategies:

- separate system instructions from retrieved content
- treat tool outputs as untrusted
- restrict tool permissions
- validate actions before execution
- use allowlists
- add human approval for sensitive actions

### Data Privacy

Agents may handle sensitive user, company, medical, or financial data.

Privacy practices:

- minimize data exposure
- redact sensitive fields
- use role-based access
- log memory writes
- support deletion
- encrypt storage where needed
- avoid sending unnecessary data to models

### Human Approval Gates

Some actions should not be fully autonomous.

Require approval for:

- sending messages
- changing records
- deleting data
- making purchases
- medical recommendations
- financial trades
- publishing content
- writing sensitive memory

---

## Hands-on Projects

### Project 1 — Agent Evaluation Suite

Build a small evaluation set for an agent and run automated checks.

Learning points:

- golden datasets
- rubric-based evaluation
- regression testing
- pass/fail thresholds

### Project 2 — Tool Safety Checklist

Create a checklist and wrapper for tool execution.

Learning points:

- permission levels
- human approval gates
- argument validation
- tool call logging

### Project 3 — Memory Audit Workflow

Build a workflow for reviewing memory reads and writes.

Learning points:

- memory governance
- sensitive data detection
- audit logs
- deletion and correction

### Project 4 — Production Deployment Template

Create a deployment template for an agent service.

Learning points:

- API service design
- environment variables
- tracing
- error handling
- cost monitoring
- deployment checklist

---

## Production Checklist

Before deploying an agent, ask:

- What is the agent allowed to do?
- What is it forbidden from doing?
- Which tools are read-only?
- Which tools require approval?
- What data can the agent access?
- What memory can it write?
- How is quality evaluated?
- How are failures handled?
- How are prompts and tool calls logged?
- How are cost and latency monitored?
- How can the system be rolled back?

---

## Common Mistakes

- Shipping without evaluation
- Logging too little to debug failures
- Logging sensitive data unnecessarily
- Giving tools excessive permissions
- Skipping human approval for high-risk actions
- Letting memory grow without audit
- Treating prompt injection as only a prompt problem
- Ignoring cost until the system is expensive
- Measuring only final answers and not intermediate steps

---

## Outcome

You should be able to move from prototype agents to production-grade agent systems.

This level completes the roadmap by connecting agent design with safety, evaluation, observability, governance, and deployment.
