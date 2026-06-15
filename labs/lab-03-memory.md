# Lab 03 - Memory

## Objective

Design memory as a policy, not a pile of stored text.

## Estimated Time

60 minutes

## Read First

- `curriculum/03-memory-systems.md`
- `examples/04-memory-agent/README.md`
- `templates/memory-policy-template.md`

## Task

Extend Example 04 with one new memory rule.

Choose one:

- update an existing memory when the user corrects it
- delete memory when the user asks to forget it
- add expiration dates
- mark sensitive memory as review-required

## Acceptance Criteria

Your memory system must:

- explain why a memory was written
- retrieve only relevant memories
- avoid storing sensitive data by default
- support correction or deletion

## Extension

Replace keyword retrieval with embeddings, but keep the same policy.
