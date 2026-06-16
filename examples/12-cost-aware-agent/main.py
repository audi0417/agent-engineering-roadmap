from __future__ import annotations

from pathlib import Path

from cost_agent import answer, run_eval


DEFAULT_TASK = "Summarize this support ticket and suggest the next safe action."


def main() -> int:
    print("Cost-Aware Agent")
    print("================")
    try:
        task = input("Task > ").strip() or DEFAULT_TASK
    except EOFError:
        task = DEFAULT_TASK
    output = answer(task, {"max_latency_ms": 800, "max_cost": 0.05})

    print("\n=== Route ===")
    for key, value in output["route"].items():
        print(f"{key}: {value}")
    print("\n=== Response ===")
    print(output["response"])

    report = run_eval(Path(__file__).with_name("eval_cases.json"))
    print("\n=== Eval Report ===")
    print(f"Passed: {report['passed']}/{report['total']}")
    for result in report["results"]:
        status = "PASS" if result["passed"] else "FAIL"
        print(f"[{status}] {result['name']}")
    return 0 if report["passed"] == report["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
