# Lab 00 - Agent Specification

## Objective

Design a narrow, testable agent before writing code.

## Estimated Time

30-45 minutes

## Read First

- `curriculum/00-agent-foundations.md`
- `templates/agent-spec-template.md`

## Task

Pick one agent idea and write a complete specification.

Good beginner ideas:

- meeting notes summarizer
- support ticket classifier
- finance article summarizer
- study plan generator
- personal research assistant

## Acceptance Criteria

Your spec must include:

- one-sentence goal
- primary user
- inputs and outputs
- allowed actions
- prohibited actions
- tools
- memory policy
- human approval rules
- failure behavior
- evaluation criteria

## Common Mistake

The most common mistake is making the agent too broad.

Bad:

```text
Help users with finance.
```

Better:

```text
Summarize one company earnings call into business drivers, risks, and unanswered questions.
```

## Extension

Write three test cases:

- one happy path
- one missing-information case
- one unsafe or out-of-scope request
