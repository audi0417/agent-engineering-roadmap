# Agent Deployment Review Template

Use this template before promoting an agent to production.

## Release

- Agent:
- Version:
- Owner:
- Date:
- Reviewer:

## Changes

- New tools:
- New data sources:
- New memory behavior:
- New workflows:
- New user-facing behavior:

## Verification

```bash
python scripts/verify_examples.py
python benchmarks/benchmark_runner.py
```

## Release Gate

- [ ] Regression evals passed
- [ ] Safety evals passed
- [ ] Adversarial evals passed
- [ ] Golden trace checks passed
- [ ] Incident replay cases passed
- [ ] Cost and latency budget accepted

## Operational Readiness

- [ ] Owner confirmed
- [ ] Kill switch tested
- [ ] Trace logging enabled
- [ ] Approval UX reviewed
- [ ] Rollback plan documented
- [ ] Support path documented

## Decision

- [ ] Approved
- [ ] Approved with conditions
- [ ] Blocked

Notes:

