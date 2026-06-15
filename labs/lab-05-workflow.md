# Lab 05 - Workflow

## Objective

Turn a vague task into a controlled workflow with review.

## Estimated Time

60 minutes

## Read First

- `curriculum/05-workflow-orchestration.md`
- `examples/05-multi-agent-workflow/README.md`

## Task

Modify Example 05 so the reviewer can fail the draft for one additional reason.

Examples:

- missing citations
- missing uncertainty
- too many steps
- unsafe recommendation
- no next action

## Acceptance Criteria

Your workflow must:

- produce intermediate artifacts
- review against a rubric
- retry or revise when review fails
- stop after a maximum number of rounds

## Extension

Add a `human_review_required` flag when the reviewer detects high risk.
