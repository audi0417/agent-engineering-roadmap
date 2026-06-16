# Assessment Rubrics

## Agent Specification Rubric

| Dimension | Excellent | Needs Work |
|---|---|---|
| Goal | Specific, observable, bounded | Vague or too broad |
| Scope | Allowed and prohibited actions are clear | Scope is implied |
| Inputs | Types and required fields are defined | Inputs are informal |
| Outputs | Format and validation are defined | Output is free-form |
| Tools | Purpose, risk, approval are specified | Tools are listed without policy |
| Memory | Write, retrieve, delete rules are clear | Memory is treated as storage only |
| Evaluation | Testable criteria exist | "Looks good" is the only standard |

## Runnable Example Rubric

| Dimension | Excellent | Needs Work |
|---|---|---|
| Setup | Runs with documented commands | Setup is implicit |
| Simplicity | Minimal but meaningful | Too much framework noise |
| Inspectability | Intermediate artifacts are visible | Everything is hidden in model calls |
| Safety | Risky actions are bounded | Tools are unrestricted |
| Extensibility | Clear next modification | Hard to adapt |
| Verification | Included in `scripts/verify_examples.py` or documented why not | No repeatable check |

## RAG Evaluation Rubric

| Dimension | Excellent | Needs Work |
|---|---|---|
| Retrieval | Expected evidence is explicitly checked | Only final answer is judged |
| No-answer | Missing-evidence cases are included | Agent always tries to answer |
| Faithfulness | Answer must use retrieved evidence | Answer can add unsupported claims |
| Coverage | Includes lookup, synthesis, ambiguous, and adversarial cases | Only happy-path lookup questions |
| Inspectability | Retrieved document IDs and scores are visible | Retrieval is hidden |

## Production Readiness Rubric

| Dimension | Excellent | Needs Work |
|---|---|---|
| Evaluation | Regression suite blocks unsafe releases | No evals |
| Observability | Logs model, tools, memory, cost, errors | Logs final answer only |
| Security | Prompt injection and permissions considered | Trusts all input |
| Privacy | Sensitive data minimized and auditable | Stores everything |
| Human Control | Approval gates exist for high impact actions | Fully autonomous by default |
| Recovery | Rollback and failure handling defined | No recovery path |
