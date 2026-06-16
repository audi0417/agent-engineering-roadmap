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

## Solution Guides

Use [Lab Solution Guides](../lab-solutions/README_zh.md) after attempting the lab.

The guide does not give one fixed answer. It tells you what artifact should exist, what failure modes to check, and how to know whether your solution is good enough.

| Lab | Solution Guide |
|---|---|
| 00 | [Agent Spec](../lab-solutions/lab-00-agent-spec/README.md) |
| 01 | [Single Agent](../lab-solutions/lab-01-single-agent/README.md) |
| 02 | [Tool Calling](../lab-solutions/lab-02-tool-calling/README.md) |
| 03 | [Memory](../lab-solutions/lab-03-memory/README.md) |
| 04 | [RAG](../lab-solutions/lab-04-rag/README.md) |
| 05 | [Workflow](../lab-solutions/lab-05-workflow/README.md) |
| 06 | [Graph Agent](../lab-solutions/lab-06-graph-agent/README.md) |
| 07 | [Multi-Agent](../lab-solutions/lab-07-multi-agent/README.md) |
| 08 | [Human-in-the-loop](../lab-solutions/lab-08-human-in-the-loop/README.md) |
| 09 | [Evaluation](../lab-solutions/lab-09-evaluation/README.md) |
| 10 | [Capstone Prep](../lab-solutions/lab-10-capstone-prep/README.md) |

## How To Use

Do not only read the labs. Run the matching examples and modify one thing.

Learning agents by reading only is like learning swimming by looking at water. It feels reasonable until the first wave arrives.

## Verification

Before opening a PR or sharing your fork, run:

```bash
python scripts/verify_examples.py
```

This checks the examples and showcases that are designed to work without API keys.
