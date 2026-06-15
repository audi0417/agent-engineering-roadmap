# Agent Engineering Course

This course turns the repository into a complete learning program for building useful, inspectable, and production-aware AI agents.

## One-Sentence Summary

An agent is not a chatbot with a longer prompt. An agent is a task system that combines goals, context, tools, memory, workflow, evaluation, and human approval.

## Who This Course Is For

- software engineers building LLM applications
- AI engineers moving from demos to production workflows
- founders and product teams designing agentic products
- researchers who want a practical engineering map
- students who want a structured agent learning path

## Prerequisites

You should know:

- basic Python
- HTTP APIs and JSON
- command-line usage
- basic LLM concepts such as prompts, tokens, context windows, and embeddings

You do not need to know every agent framework before starting. Frameworks come after the mental model.

## Course Tracks

| Track | Best for | Path |
|---|---|---|
| Beginner Builder | New to agents | Modules 00-05, Labs 00-05, Examples 01-04 |
| Agent Engineer | Building real workflows | Modules 00-09, Labs 00-09, Examples 01-07 |
| Domain Builder | Healthcare, finance, enterprise | Modules 00-12, domain tracks, capstone |
| Production Lead | Responsible for deployment | Modules 08-09, evaluation harness, safety templates |

## Course Map

![Agent Engineering Course Map](assets/diagrams/course-map.svg)

```text
Part 1: Foundations
  00 Agent Foundations
  01 Agent Architecture
  02 Tool Calling

Part 2: Context And Knowledge
  03 Memory Systems
  04 RAG And Embeddings

Part 3: Control
  05 Workflow Orchestration
  06 Graph-based Agents
  07 Multi-Agent Systems
  08 Human-in-the-loop

Part 4: Production
  09 Production Agent Systems
  12 Agent Frameworks Comparison

Part 5: Domain Systems
  10 Healthcare Agents
  11 Finance Agents
  Capstone Agent Colony
```

## How To Study

For each module:

1. Read the curriculum chapter.
2. Read the matching roadmap level.
3. Run the closest example.
4. Complete the lab.
5. Answer the assessment questions.
6. Add one improvement to the example before moving on.

## Graduation Criteria

You have completed the course when you can:

- define an agent's goal, scope, inputs, outputs, and tools
- build a single-purpose agent with structured output
- add tools with validation and approval gates
- design memory with write, retrieval, deletion, and audit rules
- build a RAG pipeline and evaluate retrieval quality
- orchestrate planner, executor, reviewer, and evaluator stages
- coordinate multiple agents without losing control
- run an evaluation suite before shipping changes
- explain production risks such as prompt injection, data leakage, runaway cost, and unsafe tool use
- complete the capstone project

## Repository Sections

| Section | Purpose |
|---|---|
| `curriculum/` | Concept chapters |
| `assets/` | Visual diagrams and teaching images |
| `roadmap/` | Level-by-level learning milestones |
| `examples/` | Runnable minimal implementations |
| `showcases/` | First-run demos with sample outputs |
| `labs/` | Guided hands-on exercises |
| `lesson-plans/` | Instructor-ready 90-minute teaching plans |
| `patterns/` | Reusable architecture patterns |
| `templates/` | Project templates and safety/eval documents |
| `assessments/` | Quiz bank and review questions |
| `projects/` | Capstone and portfolio projects |
| `glossary/` | Agent engineering terms |

## Teaching Principle

Every topic should answer four questions:

- What problem appears if we do not have this?
- What is the simplest mental model?
- What mechanism makes it work?
- How do we know it is safe and useful?

If a lesson cannot answer these four questions, it is not finished yet.
