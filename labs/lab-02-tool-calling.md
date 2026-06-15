# Lab 02 - Tool Calling

## Objective

Add tools without giving the agent unlimited power.

## Estimated Time

60-90 minutes

## Read First

- `curriculum/02-tool-calling.md`
- `examples/02-tool-using-agent/README.md`
- `templates/safety-gate-template.md`

## Task

Add one new tool to Example 02.

Possible tools:

- calculator
- unit converter
- mock database lookup
- document search
- task creator that writes to a local JSON file

## Acceptance Criteria

The tool must include:

- input schema
- validation
- error handling
- risk level
- logging
- a rule for when not to call it

## Common Mistake

Do not let the agent call tools just because tools exist. Tool calls should be useful, necessary, and bounded.

## Extension

Add a high-risk tool action that requires approval before execution.
