from __future__ import annotations

from pathlib import Path
import json

from permission_system import run_demo, run_eval


def main() -> int:
    print("Agent Permission System")
    print("=======================")
    print(json.dumps(run_demo(), indent=2))

    report = run_eval(Path(__file__).with_name("eval_cases.json"))
    print("\n=== Eval Report ===")
    print(f"Passed: {report['passed']}/{report['total']}")
    for result in report["results"]:
        status = "PASS" if result["passed"] else "FAIL"
        print(f"[{status}] {result['name']}")
    return 0 if report["passed"] == report["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

