# Lab 00 Solution Shape - Agent Spec

## Expected Artifact

```text
agent_spec.md
```

## Minimal Passing Example

```markdown
# Agent Spec - Meeting Notes Agent

## Goal
Convert raw meeting notes into decisions, action items, risks, and follow-ups.

## Primary User
Team lead or project manager.

## Input
Raw meeting notes as plain text.

## Output
Markdown with fixed sections:
- Decisions
- Action Items
- Risks
- Follow-ups

## Allowed Actions
- summarize provided notes
- identify uncertainty
- organize tasks

## Not Allowed
- invent facts
- assign owners not mentioned
- cite sources not provided

## Failure Behavior
Ask for clearer notes if the input is empty or ambiguous.

## Evaluation Criteria
- includes all required sections
- does not invent facts
- marks uncertainty clearly
```

## Review Checklist

- Goal is narrow.
- Output format is testable.
- Forbidden behavior is explicit.
- Failure behavior is defined.

## Common Fix

If the goal says "help with meetings," narrow it to a concrete transformation.
