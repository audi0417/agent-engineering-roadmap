# 22 Advanced Agent Evaluation

## Goal

Learn how to build evaluation systems that can block unsafe or low-quality agent releases.

## Why It Matters

Simple evals check whether an answer looks right. Production evals check whether the system behaved correctly.

Advanced agent evaluation should inspect:

- final answer
- tool calls
- retrieval evidence
- guardrail decisions
- approval path
- memory writes
- trace shape
- adversarial behavior

## Mental Model

```text
eval case
   ↓
agent run
   ↓
answer checks + trace checks + safety checks
   ↓
release gate
```

## Eval Types

| Type | Purpose |
|---|---|
| Regression | Prevent known behavior from breaking |
| Safety | Check refusal, approval, and escalation |
| Adversarial | Attack prompt injection and policy bypass |
| Golden trace | Verify the path, not only the answer |
| Incident replay | Prevent a fixed incident from returning |

## Practical Exercise

Run:

```bash
python examples/17-advanced-eval-harness/main.py
```

## Production Checklist

- [ ] Every release runs regression evals
- [ ] Adversarial cases block release
- [ ] Golden traces check critical paths
- [ ] Incidents become eval cases
- [ ] Eval failures include useful details
- [ ] Benchmarks run in CI

