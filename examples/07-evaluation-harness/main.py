"""Example 07 - Evaluation Harness.

Run:
    python main.py
"""

from __future__ import annotations

import json
from pathlib import Path

from evaluator import evaluate_case, summarize
from mock_agent import run_agent


BASE_DIR = Path(__file__).resolve().parent
EVAL_PATH = BASE_DIR / "eval_cases.json"


def load_cases() -> list[dict]:
    with EVAL_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)["cases"]


def main() -> None:
    cases = load_cases()
    results = []

    for case in cases:
        output = run_agent(case["input"])
        result = evaluate_case(case, output)
        results.append(result)

    summary = summarize(results)
    print("Evaluation Report")
    print("=================")
    print(f"Passed: {summary['passed']}/{summary['total']}")
    print(f"Pass rate: {summary['pass_rate']:.0%}\n")

    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(f"[{status}] {result.case_id}")
        if result.missing:
            print(f"  missing: {', '.join(result.missing)}")
        if result.forbidden_found:
            print(f"  forbidden: {', '.join(result.forbidden_found)}")
        print(f"  output: {result.output}")


if __name__ == "__main__":
    main()
