# Lab 09 - Evaluation

## Objective

Build an evaluation suite that catches regressions.

## Estimated Time

60-90 minutes

## Read First

- `curriculum/09-production-agent-systems.md`
- `examples/07-evaluation-harness/README.md`
- `examples/08-mini-rag/README.md`
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

## Course Verification Challenge

Run:

```bash
python scripts/verify_examples.py
```

Then intentionally break one eval case in `examples/08-mini-rag/eval_cases.json`, run the script again, and observe where the report fails. Restore the case before committing.
