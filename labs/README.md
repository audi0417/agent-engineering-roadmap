# Labs

Guided exercises for the Agent Engineering course.

Each lab has:

- objective
- estimated time
- files to read
- task
- acceptance criteria
- extension challenge

## Lab Sequence

| Lab | Topic | Output |
|---|---|---|
| 00 | Agent Specification | A complete agent spec |
| 01 | Single Agent | A task-focused agent prompt and output schema |
| 02 | Tool Calling | A tool policy and validation wrapper |
| 03 | Memory | A memory write/retrieve/delete policy |
| 04 | RAG | A retrieval test set and mini RAG eval |
| 05 | Workflow | A planner-executor-reviewer workflow |
| 06 | Graph Agent | A state machine design |
| 07 | Multi-Agent | A supervisor routing policy |
| 08 | Human Approval | A risk-based approval gate |
| 09 | Evaluation | A regression eval suite |
| 10 | Capstone Prep | A production readiness review |

## How To Use

Do not only read the labs. Run the matching examples and modify one thing.

Learning agents by reading only is like learning swimming by looking at water. It feels reasonable until the first wave arrives.

## Verification

Before opening a PR or sharing your fork, run:

```bash
python scripts/verify_examples.py
```

This checks the examples and showcases that are designed to work without API keys.
