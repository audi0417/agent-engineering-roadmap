"""Run starter capstone regression checks."""

from __future__ import annotations

import json
from pathlib import Path

from run_demo import run_colony


BASE_DIR = Path(__file__).resolve().parent
EVAL_PATH = BASE_DIR / "evals/eval_cases.json"


def main() -> int:
    cases = json.loads(EVAL_PATH.read_text(encoding="utf-8"))
    passed = 0
    print("Capstone Starter Eval")
    print("=====================")
    for case in cases:
        output = run_colony(case["task"])
        ok = all(term.lower() in output.lower() for term in case["expected_terms"])
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {case['id']}")
        if ok:
            passed += 1
        else:
            print(output)

    print(f"\nPassed: {passed}/{len(cases)}")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())
