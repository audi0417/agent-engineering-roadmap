# Example 12: Cost-Aware Agent

This example teaches model routing with cost and latency constraints.

## Run

```bash
python examples/12-cost-aware-agent/main.py
```

## What It Shows

- Estimate task size
- Decide required quality
- Route to the cheapest model that satisfies constraints
- Fail over to a fallback route when constraints cannot all be met
- Evaluate routing decisions

## Learning Check

- Which tasks need a stronger model?
- Which tasks should use a cheap model?
- What should happen when no model satisfies both cost and latency?

