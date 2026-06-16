# Lab 08 - Human-in-the-loop

## Objective

Add approval gates for high-impact actions.

## Estimated Time

45-60 minutes

## Read First

- `curriculum/08-human-in-the-loop.md`
- `templates/safety-gate-template.md`
- `examples/09-graph-approval-agent/README.md`

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

## Hands-on Path

1. Run `python examples/09-graph-approval-agent/main.py`.
2. Try a destructive action such as deleting production records.
3. Confirm the graph routes to `request_approval`.
4. Add a required approval field to the output.
5. Add an eval case that fails if approval is skipped.
