"""Example 09 - Graph Approval Agent.

Run:
    python main.py
"""

from __future__ import annotations

import json
from pathlib import Path

from graph_agent import format_state, run_graph


BASE_DIR = Path(__file__).resolve().parent
EVAL_PATH = BASE_DIR / "eval_cases.json"
DEFAULT_TASK = "Delete production customer records for account 1842."


def run_eval() -> list[dict]:
    cases = json.loads(EVAL_PATH.read_text(encoding="utf-8"))
    results = []
    for case in cases:
        state = run_graph(case["task"])
        output = format_state(state)
        path_passed = state.path == case["expected_path"]
        terms_passed = all(term.lower() in output.lower() for term in case["expected_terms"])
        results.append(
            {
                "id": case["id"],
                "passed": path_passed and terms_passed,
                "path_passed": path_passed,
                "terms_passed": terms_passed,
                "path": state.path,
                "output": output,
            }
        )
    return results


def main() -> None:
    task = input("Task > ").strip() or DEFAULT_TASK
    state = run_graph(task)

    print("\n=== Graph Run ===")
    print(format_state(state))

    print("=== Eval Report ===")
    results = run_eval()
    passed = sum(1 for result in results if result["passed"])
    print(f"Passed: {passed}/{len(results)}")
    for result in results:
        status = "PASS" if result["passed"] else "FAIL"
        print(
            f"[{status}] {result['id']} "
            f"path={result['path_passed']} terms={result['terms_passed']}"
        )

    if passed != len(results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
