# Capstone Architecture

## One-Sentence System

This starter routes a user task through a supervisor, a researcher, and a reviewer before returning a bounded answer.

## Flow

```text
User Task
   |
   v
Supervisor routes task
   |
   v
Researcher drafts structured output
   |
   v
Reviewer checks scope and safety
   |
   v
Final response or refusal
```

## Components

| Component | Responsibility |
|---|---|
| Supervisor | Classify task and choose path |
| Researcher | Produce domain-bounded research support |
| Reviewer | Check safety, missing context, and output format |
| Mock tools | Provide deterministic tool outputs for evals |

## Replace This

- domain categories
- allowed tools
- specialist agents
- eval cases
- safety boundaries

## Do Not Skip

- refusal cases
- no-answer behavior
- high-risk approval path
- regression evals
