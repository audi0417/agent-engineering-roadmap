# Lab 06 - Graph Agent

## Objective

Model an agent workflow as a state machine.

## Estimated Time

45-75 minutes

## Read First

- `curriculum/06-graph-based-agents.md`
- `examples/09-graph-approval-agent/README.md`

## Task

Draw a graph for one agent workflow.

Required nodes:

- receive input
- classify task
- gather context
- decide action
- call tool
- review result
- final response
- error handling

## Acceptance Criteria

Your graph must include:

- start and end states
- at least one conditional branch
- at least one failure branch
- at least one human approval path

## Extension

Implement the graph as a Python dictionary or with a graph orchestration framework.

## Hands-on Path

1. Run `python examples/09-graph-approval-agent/main.py`.
2. Add one new risk category to `graph_agent.py`.
3. Add one eval case that should route to `request_approval`.
4. Run `python examples/09-graph-approval-agent/main.py` again.
5. Explain whether your change affected path correctness or final output only.
