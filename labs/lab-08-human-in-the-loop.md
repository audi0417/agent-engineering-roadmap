# Lab 08 - Human-in-the-loop

## Objective

Add approval gates for high-impact actions.

## Estimated Time

45-60 minutes

## Read First

- `curriculum/08-human-in-the-loop.md`
- `templates/safety-gate-template.md`

## Task

Define an approval policy for one agent.

Your policy should classify actions as:

- allowed automatically
- allowed with logging
- requires approval
- refused

## Acceptance Criteria

Your policy must cover:

- read-only tool calls
- write actions
- messages sent to other people
- financial or medical advice
- deletion or irreversible changes

## Extension

Add an approval transcript format that records who approved what and why.
