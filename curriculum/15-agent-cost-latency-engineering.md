# 15 Agent Cost And Latency Engineering

## Goal

Learn how to make agent systems fast enough, cheap enough, and still reliable enough for production.

## Why It Matters

An agent that works once in a demo can still fail as a product if it is too slow or too expensive.

Cost and latency are not only infrastructure concerns. They shape agent design:

- which model handles which task
- how much context is retrieved
- when tools should be called
- when to cache
- when to fallback
- when to ask the user for clarification instead of spending more tokens

## Mental Model

Think of every agent run as a budgeted route.

```text
task
   ↓
estimate difficulty + token size + risk
   ↓
choose model + retrieval budget + tool timeout
   ↓
run
   ↓
measure cost, latency, quality
```

The best route is not always the strongest model. The best route is the cheapest route that meets the quality and safety requirement.

## Core Mechanisms

| Mechanism | Purpose |
|---|---|
| Model routing | Use small models for simple work and stronger models for risky work |
| Token budgeting | Limit context and output size |
| Retrieval budgeting | Retrieve enough evidence without flooding context |
| Tool timeout | Avoid long waits from unreliable services |
| Caching | Reuse stable results |
| Fallback | Recover when a model or tool fails |
| Cost telemetry | Track cost per run, user, workflow, and feature |

## Common Failure Modes

### Always Use The Strongest Model

Quality may improve slightly, but cost and latency explode.

### Always Use The Cheapest Model

The agent becomes fast but unreliable on complex or high-risk tasks.

### Retrieve Everything

The model receives too much context, answers become noisy, and token cost rises.

### No Timeout

One slow tool can freeze the whole workflow.

## Practical Exercise

Run:

```bash
python examples/12-cost-aware-agent/main.py
```

Then change the task and budget:

- make the task high-risk
- reduce `max_cost`
- reduce `max_latency_ms`
- observe how routing changes

## Production Checklist

- [ ] Each workflow has a latency target
- [ ] Each workflow has a cost budget
- [ ] Model choice is explicit
- [ ] Retrieval limit is explicit
- [ ] Tool timeout is explicit
- [ ] Fallback behavior is tested
- [ ] Cost and latency are traced per run
- [ ] High-risk tasks can spend more budget when justified

