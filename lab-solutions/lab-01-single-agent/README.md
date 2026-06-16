# Lab 01 Solution Shape - Single Agent

## Expected Artifacts

```text
agent_config.json
eval_inputs.md
failure_analysis.md
```

## Example Config Change

```json
{
  "agent": {
    "name": "Decision Extractor Agent",
    "role": "Extract decisions from raw meeting notes.",
    "goal": "Return only decisions, owners, and open questions from provided notes.",
    "rules": [
      "Do not invent decisions.",
      "Mark missing owners as unknown.",
      "Ask for clarification when notes are empty."
    ]
  },
  "summary_sections": ["Decisions", "Owners", "Open Questions"]
}
```

## Eval Inputs

```text
1. Notes with clear decisions.
2. Notes with no decisions.
3. Empty notes.
4. Notes with unclear owner.
5. Notes asking for unrelated financial advice.
```

## Passing Standard

- The agent stays inside one task.
- Output sections are stable.
- Missing information is not invented.
- Out-of-scope input is rejected or redirected.
