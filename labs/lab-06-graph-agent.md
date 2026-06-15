# Lab 06 - Graph Agent

## Objective

Model an agent workflow as a state machine.

## Estimated Time

45-75 minutes

## Read First

- `curriculum/06-graph-based-agents.md`

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
