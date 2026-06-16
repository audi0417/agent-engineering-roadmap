# Benchmarks

This folder provides a small benchmark layer for the Agent Engineering Roadmap.

The goal is not to compare models. The goal is to check whether the example agents preserve important engineering behaviors.

## Run

```bash
python benchmarks/benchmark_runner.py
```

## Current Checks

| Category | Check | What it protects |
|---|---|---|
| Tool use | Calculator result | Tool call correctness |
| RAG | Grounded approval answer | Retrieval and answer grounding |
| Workflow | Destructive action gate | Approval before high-risk execution |
| Security | Prompt injection blocked | Untrusted retrieval isolation |
| Observability | Guardrail trace exists | Replayable production debugging |

## Why This Helps

Many agent demos look impressive but do not stay reliable after changes.

This benchmark gives contributors a quick signal:

- Did tool behavior break?
- Did retrieval grounding regress?
- Did approval gates still trigger?
- Did prompt injection defenses still work?
- Did traces still capture guardrail decisions?

## Add A Benchmark

Add a new check when you add a new production behavior.

A good benchmark should:

- run without API keys
- test one behavior
- fail loudly
- print a useful detail line
- be stable in GitHub Actions

