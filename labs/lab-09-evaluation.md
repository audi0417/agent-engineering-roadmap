# Lab 09 - Evaluation

## Objective

Build an evaluation suite that catches regressions.

## Estimated Time

60-90 minutes

## Read First

- `curriculum/09-production-agent-systems.md`
- `examples/07-evaluation-harness/README.md`
- `templates/evaluation-suite-template.yaml`

## Task

Create 10 eval cases for one agent.

Include:

- happy paths
- missing context
- unsafe requests
- tool-use cases
- memory-use cases
- format compliance

## Acceptance Criteria

Your eval suite must:

- define pass/fail behavior
- separate correctness from safety
- include at least two negative cases
- produce a summary score

## Extension

Add regression thresholds for release blocking.
