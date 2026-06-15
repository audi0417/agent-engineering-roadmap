# Example 07 - Evaluation Harness

This example shows how to test an agent with simple regression cases.

好，那 evaluation harness 是什麼？其實就是一組考題而已。你每次改 prompt、換 model、加 tool、改 memory policy，都拿同一組題目考一次。分數變差，你就知道出事了。

This example uses a deterministic mock agent so the evaluation logic is easy to inspect.

## What this example teaches

- how to define expected behavior
- how to separate correctness, format, and safety checks
- how to run a small eval suite
- how to produce a pass/fail report

## Files

| File | Purpose |
|---|---|
| `main.py` | Runs the evaluation suite |
| `evaluator.py` | Scoring logic |
| `mock_agent.py` | Deterministic agent used for tests |
| `eval_cases.yaml` | Test cases |

## Run

```bash
python main.py
```

## Mental model

```text
Eval case
   |
   v
Agent output
   |
   v
Scoring checks
   |
   v
Pass/fail report
```

## Production notes

In production, you can replace the mock agent with real model calls, add judge-model scoring, track historical scores, and block releases when critical cases fail.

Do not start with a giant benchmark. Start with 10 cases that represent real user pain.
