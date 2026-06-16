# 21 Agent Incident Response

## Goal

Learn how to respond when a production agent behaves incorrectly, unsafely, or unexpectedly.

## Why It Matters

Agent incidents are different from ordinary application bugs.

The failure may come from:

- a model decision
- retrieved context
- a tool result
- a memory write
- a permission scope
- a missing approval gate
- a prompt injection
- a broken handoff

Incident response must be trace-driven, not guess-driven.

## Mental Model

```text
detect
   ↓
contain
   ↓
inspect trace
   ↓
disable risky capability
   ↓
ship hotfix + eval
   ↓
write postmortem
```

## Common Failure Modes

### No Kill Switch

The team cannot quickly disable a dangerous tool or agent.

### No Trace

The final answer is visible, but the decision path is invisible.

### No Hotfix Eval

The team patches one incident but breaks another workflow.

### No Owner

Nobody knows who can approve containment.

## Practical Exercise

Use:

```text
incident-response/agent-incident-playbook.md
```

Then replay the incident using:

```bash
python examples/10-observable-agent/main.py
python benchmarks/benchmark_runner.py
```

## Production Checklist

- [ ] Each agent has an owner
- [ ] High-risk tools have kill switches
- [ ] Traces are available for recent runs
- [ ] Security events are searchable
- [ ] Hotfixes require eval updates
- [ ] Postmortems include trace evidence
- [ ] Memory and permission changes are reviewed

