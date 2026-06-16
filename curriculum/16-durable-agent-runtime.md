# 16 Durable Agent Runtime

## Goal

Learn how to design agent workflows that can survive crashes, restarts, retries, and long-running tasks.

## Why It Matters

Many useful agent tasks are not one-shot chat completions.

They may:

- call slow tools
- wait for approval
- process many documents
- run in the background
- resume tomorrow
- retry after failure

If the process crashes halfway through, the agent should not forget what happened or repeat dangerous side effects.

## Mental Model

Durable execution means:

```text
do one step
   ↓
save checkpoint
   ↓
do next step
   ↓
save checkpoint
   ↓
resume safely after interruption
```

The checkpoint is the system's memory of workflow state, not the model's memory.

## Core Mechanisms

| Mechanism | Purpose |
|---|---|
| Checkpoint | Save workflow state after each step |
| Resume | Continue from the latest safe state |
| Idempotency key | Prevent repeating external side effects |
| Retry policy | Decide what can be retried and how often |
| Human wait state | Pause while waiting for approval |
| Event log | Preserve evidence of what happened |
| Compensation | Define rollback or repair action |

## Common Failure Modes

### No Checkpoint

A crash loses the workflow state.

### Blind Retry

The agent repeats a payment, email, delete, or external write.

### Hidden Wait State

The agent is waiting for approval, but the system cannot show why.

### Model Memory Confusion

The team assumes model context is durable state. It is not.

## Practical Exercise

Run:

```bash
python examples/13-durable-workflow-agent/main.py
```

The example stops after two steps, writes a checkpoint, then resumes from that checkpoint.

## Production Checklist

- [ ] Each workflow step has a stable name
- [ ] State is checkpointed after each step
- [ ] External writes use idempotency keys
- [ ] Approval waits are explicit states
- [ ] Retryable and non-retryable failures are separated
- [ ] Resume logic is tested
- [ ] Checkpoints avoid sensitive raw data when possible

