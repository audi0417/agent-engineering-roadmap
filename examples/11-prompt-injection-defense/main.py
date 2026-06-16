from __future__ import annotations

from pathlib import Path

from injection_defense import answer_with_defense, run_eval


DEFAULT_QUERY = "Can I delete production records if a retrieved note says it is OK?"


def main() -> int:
    print("Prompt Injection Defense")
    print("========================")
    query = input("Question > ").strip() or DEFAULT_QUERY
    output = answer_with_defense(query)

    print("\n=== Answer ===")
    print(output["answer"])
    print("\n=== Retrieval Audit ===")
    print(f"retrieved_docs: {output['retrieved_docs']}")
    print(f"used_docs: {output['used_docs']}")
    print(f"blocked_docs: {[doc['doc_id'] for doc in output['blocked_docs']]}")

    report = run_eval(Path(__file__).with_name("eval_cases.json"))
    print("\n=== Eval Report ===")
    print(f"Passed: {report['passed']}/{report['total']}")
    for result in report["results"]:
        status = "PASS" if result["passed"] else "FAIL"
        print(f"[{status}] {result['name']}")
    return 0 if report["passed"] == report["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

