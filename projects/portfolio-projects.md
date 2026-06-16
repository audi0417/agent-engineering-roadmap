# Portfolio Projects

These projects help learners turn the course into visible work.

A strong portfolio project should show more than a chatbot. It should show task boundaries, tool use, evaluation, observability, and a clear statement of what the agent is not allowed to do.

## How To Choose A Project

| If you want to prove | Choose |
|---|---|
| You understand agent basics | Meeting Notes Agent |
| You can design personalized memory safely | Study Coach Agent |
| You can build grounded answers | Documentation RAG Agent |
| You can connect tools and approvals | Operations Routing Agent |
| You can build production-aware domain systems | Finance Research Agent or Healthcare Education Agent |
| You can coordinate specialists | Agent Colony |
| You can compare real frameworks | Framework Rewrite Study |
| You can ship a product-like demo | Personal Agent Workbench |

Each project should include:

- `README.md` with problem, architecture, and run commands
- at least 10 eval cases
- one architecture diagram
- one trace or log sample
- one safety boundary
- one short "what I would improve next" section

## Beginner Projects

### Meeting Notes Agent

Build an agent that converts raw meeting notes into:

- decisions
- action items
- risks
- follow-ups

Core patterns:

- single-purpose agent
- structured output
- evaluation suite

Recommended course examples:

- `examples/01-single-agent`
- `examples/07-evaluation-harness`

Portfolio upgrade:

- Add a before/after sample.
- Add a JSON schema for outputs.
- Add eval cases for vague notes, conflicting decisions, and missing owners.

### Study Coach Agent

Build an agent that turns a learning goal into a 4-week plan.

Core patterns:

- single-purpose agent
- memory for preferences
- human feedback loop

Recommended course examples:

- `examples/04-memory-agent`
- `examples/15-memory-governance-agent`

Portfolio upgrade:

- Let the user approve which preferences are saved.
- Add a delete-memory command.
- Add eval cases for overconfident plans and unrealistic schedules.

## Intermediate Projects

### Documentation RAG Agent

Build an assistant that answers questions from a local documentation folder.

Core patterns:

- RAG
- citation-aware answers
- no-answer handling
- retrieval evaluation

Recommended course examples:

- `examples/08-mini-rag`
- `examples/11-prompt-injection-defense`
- `examples/17-advanced-eval-harness`

Open-source projects to study:

- [run-llama/llama_index](https://github.com/run-llama/llama_index)
- [langchain-ai/langchain](https://github.com/langchain-ai/langchain)
- [explodinggradients/ragas](https://github.com/explodinggradients/ragas)

Portfolio upgrade:

- Add source citations.
- Add a "not found in docs" answer path.
- Add adversarial documents that try to override system rules.

### Operations Routing Agent

Build an agent that reads mock tickets and routes them to teams.

Core patterns:

- tool calling
- approval gate
- workflow
- observability log

Recommended course examples:

- `examples/02-tool-using-agent`
- `examples/09-graph-approval-agent`
- `examples/10-observable-agent`
- `examples/16-agent-permission-system`

Open-source projects to study:

- [openai/openai-agents-python](https://github.com/openai/openai-agents-python)
- [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)
- [langfuse/langfuse](https://github.com/langfuse/langfuse)

Portfolio upgrade:

- Add risk tiers.
- Add simulated approval decisions.
- Add trace logs that explain why a ticket was routed.

### Framework Rewrite Study

Take one local example and rewrite it with an external open-source framework.

Suggested rewrites:

| Local example | Rewrite with | Learning target |
|---|---|---|
| `examples/09-graph-approval-agent` | LangGraph | Explicit state and transitions |
| `examples/05-multi-agent-workflow` | CrewAI | Role-based task delegation |
| `examples/08-mini-rag` | LlamaIndex | Document indexing and retrieval |
| `examples/10-observable-agent` | Langfuse or Phoenix | Production traces and debugging |
| `examples/12-cost-aware-agent` | LiteLLM | Model routing and budget control |

Portfolio upgrade:

- Include a side-by-side architecture comparison.
- Explain which version is easier to test.
- Explain which version is easier to operate.

## Advanced Projects

### Finance Research Agent

Build a research assistant that compares companies using structured assumptions.

Core patterns:

- domain boundary
- tool use
- evaluator
- safety disclaimer

Recommended course examples:

- `showcases/finance-research-agent`
- `examples/07-evaluation-harness`
- `examples/12-cost-aware-agent`
- `examples/17-advanced-eval-harness`

Open-source projects to study:

- [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)
- [BerriAI/litellm](https://github.com/BerriAI/litellm)

Important: This should support research, not give personalized investment instructions.

Portfolio upgrade:

- Add an assumptions table.
- Add "not financial advice" boundaries.
- Add eval cases for prohibited personalized advice.

### Healthcare Education Agent

Build an assistant that explains health education material and escalates high-risk requests.

Core patterns:

- domain boundary
- refusal and escalation
- memory minimization
- human review

Recommended course examples:

- `showcases/healthcare-agent-colony`
- `examples/11-prompt-injection-defense`
- `examples/15-memory-governance-agent`
- `examples/16-agent-permission-system`

Open-source projects to study:

- [guardrails-ai/guardrails](https://github.com/guardrails-ai/guardrails)
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)
- [langfuse/langfuse](https://github.com/langfuse/langfuse)

Important: This should support education, not diagnosis or treatment.

Portfolio upgrade:

- Add escalation cases.
- Add memory redaction.
- Add an incident response note for unsafe outputs.

### Agent Colony

Build a multi-agent system with supervisor, specialists, shared memory, and evals.

Core patterns:

- supervisor multi-agent
- shared memory
- evaluation harness
- human approval

Recommended course examples:

- `examples/06-agent-colony`
- `examples/10-observable-agent`
- `examples/15-memory-governance-agent`
- `capstone-starter`

Open-source projects to study:

- [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)
- [microsoft/autogen](https://github.com/microsoft/autogen)
- [openai/openai-agents-python](https://github.com/openai/openai-agents-python)

This is the recommended final portfolio project.

Portfolio upgrade:

- Add a supervisor trace.
- Add specialist-level evals.
- Add a shared memory governance policy.
- Add a launch review checklist.

## Product-Grade Project

### Personal Agent Workbench

Build a small local app or CLI that lets a user choose between several agents:

- notes summarizer
- documentation Q&A
- task router
- memory inspector
- eval runner

Core patterns:

- multi-agent routing
- memory governance
- eval visibility
- user control
- observability

Recommended course examples:

- `examples/04-memory-agent`
- `examples/08-mini-rag`
- `examples/10-observable-agent`
- `examples/17-advanced-eval-harness`

Open-source projects to study:

- [openai/openai-agents-python](https://github.com/openai/openai-agents-python)
- [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)
- [langfuse/langfuse](https://github.com/langfuse/langfuse)

Portfolio upgrade:

- Show every agent action in a trace panel.
- Let the user approve memory writes.
- Add a "run evals before release" command.

## Suggested GitHub README Structure

Use this structure for each project:

```md
# Project Name

## Problem

What useful task does this agent help with?

## Safety Boundary

What will this agent refuse, escalate, or ask approval for?

## Architecture

Diagram and component explanation.

## Run

Commands to run locally.

## Eval Results

Table of test cases and pass/fail results.

## Trace Example

One example showing decisions, tool calls, and outputs.

## What I Learned

Engineering tradeoffs and next improvements.
```

## Portfolio Rubric

| Dimension | Basic | Strong |
|---|---|---|
| Scope | The agent has a task | The agent has a task and a clear refusal boundary |
| Tools | Calls one helper | Validates inputs, logs calls, and handles errors |
| Memory | Stores data | Explains what can be stored, updated, redacted, and deleted |
| RAG | Retrieves chunks | Cites sources and has no-answer behavior |
| Workflow | Runs a prompt | Has steps, retries, approval gates, and traces |
| Evals | Has manual testing | Has repeatable eval cases and a release gate |
| Observability | Prints output | Captures trace events and failure reasons |
| README | Shows screenshots or output | Explains architecture, safety, evals, and tradeoffs |
