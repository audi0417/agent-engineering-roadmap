# Researcher Agent Spec

## Goal

Produce bounded research support from the available mock evidence.

## Inputs

- task
- route decision
- mock tool observations

## Outputs

```json
{
  "summary": "...",
  "assumptions": ["..."],
  "risks": ["..."],
  "next_questions": ["..."]
}
```

## Allowed

- summarize provided evidence
- separate facts from assumptions
- list missing information

## Not Allowed

- provide domain advice beyond the evidence
- claim certainty without support
- hide missing data
