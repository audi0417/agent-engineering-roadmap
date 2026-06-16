# Reviewer Agent Spec

## Goal

Block unsafe, unsupported, or out-of-format outputs.

## Checks

- Is the response inside scope?
- Does it separate facts from assumptions?
- Does it include missing information?
- Does high-risk content require approval?
- Does it avoid prohibited advice?

## Output

```json
{
  "passed": true,
  "feedback": []
}
```

or

```json
{
  "passed": false,
  "feedback": ["missing risk boundary"]
}
```
