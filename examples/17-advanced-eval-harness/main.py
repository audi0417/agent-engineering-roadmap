from __future__ import annotations

from pathlib import Path

from advanced_eval import run_suite


def main() -> int:
    print("Advanced Eval Harness")
    print("=====================")
    report = run_suite(Path(__file__).with_name("eval_cases.json"))
    print(f"Passed: {report['passed']}/{report['total']}")
    print(f"Pass rate: {report['pass_rate']:.0%}")
    print(f"Release gate: {'passed' if report['release_gate_passed'] else 'failed'}")

    print("\n=== By Type ===")
    for case_type, score in report["by_type"].items():
        print(f"{case_type}: {score['passed']}/{score['total']}")

    print("\n=== Cases ===")
    for result in report["results"]:
        status = "PASS" if result["passed"] else "FAIL"
        print(f"[{status}] {result['id']} trace={' -> '.join(result['output']['trace'])}")
    return 0 if report["release_gate_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

