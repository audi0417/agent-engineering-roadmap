# Capstone Project - Production-Aware Agent Colony

## Goal

Build a small but complete agent colony for one real domain.

This is the final project for the course. The goal is not to build the biggest agent system. The goal is to build a system that is useful, inspectable, evaluated, and bounded.

## Choose One Domain

Pick one:

- healthcare education assistant
- finance research assistant
- enterprise support workflow
- personal learning coach
- document operations assistant

## Required Components

Your capstone must include:

1. Supervisor agent
2. At least two specialist agents
3. At least one tool
4. Memory policy
5. Workflow graph
6. Human approval gate
7. Evaluation suite
8. Observability log
9. README with setup and limitations

## Suggested Architecture

```text
User Task
   |
   v
Supervisor
   |
   +--> Specialist Agent A
   +--> Specialist Agent B
   |
   v
Shared Memory
   |
   v
Tool Layer
   |
   v
Evaluator
   |
   v
Human Approval Gate
   |
   v
Final Output
```

## Milestones

### Milestone 1 - Specification

Create:

- agent specs
- allowed and prohibited actions
- user stories
- expected outputs

### Milestone 2 - Single Agent Baseline

Build the simplest useful version with one agent and no memory.

### Milestone 3 - Tool Use

Add one tool with validation, logging, and risk level.

### Milestone 4 - Memory

Add memory only if the system needs it.

Define:

- what can be stored
- what cannot be stored
- how memory is retrieved
- how memory is deleted
- what gets logged

### Milestone 5 - Workflow

Add planner, executor, reviewer, and evaluator stages.

### Milestone 6 - Multi-Agent

Split the system into supervisor and specialists.

Each specialist must have:

- domain scope
- input contract
- output contract
- failure behavior

### Milestone 7 - Evaluation

Create at least 15 eval cases:

- 5 happy path
- 3 missing context
- 3 unsafe or high-risk
- 2 tool-use
- 2 memory-related

### Milestone 8 - Production Readiness Review

Answer:

- What can go wrong?
- What is logged?
- What requires approval?
- What data is stored?
- How do you roll back?
- What score blocks release?

## Final Deliverables

Submit:

- `README.md`
- `architecture.md`
- `agent_specs/`
- `tools/`
- `memory_policy.md`
- `eval_cases.json`
- `run_eval.py`
- `safety_review.md`

## Grading Rubric

| Dimension | Points |
|---|---:|
| Clear scope and user problem | 15 |
| Agent architecture | 15 |
| Tool and memory safety | 15 |
| Workflow control | 15 |
| Evaluation quality | 20 |
| Observability and production readiness | 10 |
| Documentation clarity | 10 |

## Passing Standard

A passing capstone does not need to be fancy.

It must be:

- runnable
- inspectable
- evaluated
- safe by default
- honest about limitations

If the system can explain what it is doing and fail safely when it should not act, that is already a serious agent engineering project.
