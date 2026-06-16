# Capstone Starter - Agent Colony

This is a runnable starter scaffold for the final project.

It is intentionally small. The goal is not to give you a finished product. The goal is to give you a skeleton you can inspect, modify, and evaluate.

## What You Build From Here

Choose one domain:

- healthcare education
- finance research
- enterprise support
- learning coach
- document operations

Then replace the starter domain logic with your own.

## Files

| File | Purpose |
|---|---|
| `run_demo.py` | Runs the starter colony once |
| `run_eval.py` | Runs regression checks |
| `architecture.md` | Architecture notes to customize |
| `agent_specs/supervisor.md` | Supervisor scope |
| `agent_specs/researcher.md` | Specialist scope |
| `agent_specs/reviewer.md` | Reviewer scope |
| `tools/mock_tools.py` | Safe mock tools |
| `evals/eval_cases.json` | Starter eval cases |
| `safety_review.md` | Safety and approval checklist |

## Run

```bash
python capstone-starter/run_demo.py
python capstone-starter/run_eval.py
```

## Upgrade Path

1. Replace the sample task with your domain task.
2. Add one domain tool.
3. Add a memory policy.
4. Add at least 15 eval cases.
5. Add a human approval gate for high-risk actions.
6. Run evals before every change.

## Passing Standard

Your capstone should be:

- runnable
- inspectable
- evaluated
- safe by default
- honest about limitations
