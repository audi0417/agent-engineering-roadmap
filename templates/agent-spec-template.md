# Agent Specification Template

## Agent Name

`<name>`

## One-Sentence Goal

This agent helps `<primary user>` accomplish `<task>` by `<method>`.

## Scope

### Allowed

- `<allowed behavior>`
- `<allowed behavior>`

### Not Allowed

- `<disallowed behavior>`
- `<disallowed behavior>`

## Inputs

| Input | Type | Required | Notes |
|---|---|---|---|
| `<input>` | `<string/json/file>` | yes | `<notes>` |

## Outputs

| Output | Format | Validation |
|---|---|---|
| `<output>` | `<markdown/json>` | `<schema or rubric>` |

## Tools

| Tool | Purpose | Risk | Approval Needed |
|---|---|---|---|
| `<tool>` | `<why it exists>` | low/medium/high | yes/no |

## Memory

| Memory Type | Store? | Reason |
|---|---|---|
| Short-term task state | yes/no | `<reason>` |
| User preference | yes/no | `<reason>` |
| Sensitive personal data | no | Avoid unsafe persistence |

## Failure Behavior

- If required input is missing, ask one focused clarification question.
- If a tool fails, explain the failure and continue only when safe.
- If the task is outside scope, refuse or redirect.

## Evaluation Criteria

| Dimension | Passing Behavior |
|---|---|
| Task success | `<what must be true>` |
| Faithfulness | Does not invent facts |
| Format | Matches expected structure |
| Safety | Avoids prohibited actions |
| Cost | Uses tools only when needed |
