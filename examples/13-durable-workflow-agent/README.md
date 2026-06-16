# Example 13: Durable Workflow Agent

This example shows checkpoint and resume for long-running agent workflows.

## Run

```bash
python examples/13-durable-workflow-agent/main.py
```

## What It Shows

- Save workflow state after every step
- Stop partway through a run
- Resume from the latest checkpoint
- Preserve artifacts across a restart
- Verify that the resumed run completed safely

## Learning Check

- Which state must be saved to resume safely?
- Which tool calls are safe to retry?
- Which side effects need idempotency keys?

