# Example 10: Observable Agent

This example shows how to make an agent run inspectable.

The agent writes a JSONL trace with:

- run start and end events
- risk and category decisions
- tool calls and tool results
- guardrail triggers
- a replayable trace summary

## Run

```bash
python examples/10-observable-agent/main.py
```

Press Enter to use the default high-risk ticket.

## Why This Matters

A production agent can fail in many places: model decision, tool call, memory retrieval, policy gate, or handoff. Without traces, debugging becomes guesswork.

This example teaches the minimum useful trace shape:

- `run_id`: groups all events from one agent run
- `span_id`: identifies each operation
- `parent_span_id`: connects child work to the run
- `event_type`: makes filtering possible
- `payload`: records the decision or observation

## Learning Check

After running the example, inspect `trace.jsonl` and answer:

- Which event caused human approval to be required?
- Which events would you show in an incident review?
- What payload fields should be redacted before sending traces to a vendor?

