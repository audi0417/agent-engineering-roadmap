"""Example 08 - Mini RAG With Evaluation.

Run:
    python main.py
"""

from __future__ import annotations

from pathlib import Path

from rag import answer, load_documents, load_eval_cases, retrieve, run_eval


BASE_DIR = Path(__file__).resolve().parent
DOCS_PATH = BASE_DIR / "knowledge_base.json"
EVAL_PATH = BASE_DIR / "eval_cases.json"
DEFAULT_QUESTION = "What should an approval request include before a high-risk tool call?"


def main() -> None:
    documents = load_documents(DOCS_PATH)
    question = input("Question > ").strip() or DEFAULT_QUESTION

    retrieved = retrieve(question, documents)
    print("\n=== Retrieved Documents ===")
    if retrieved:
        for item in retrieved:
            print(f"- {item.document.id} score={item.score} terms={', '.join(item.matched_terms)}")
    else:
        print("- No matching documents")

    print("\n=== Answer ===")
    print(answer(question, retrieved))

    print("\n=== Eval Report ===")
    cases = load_eval_cases(EVAL_PATH)
    results = run_eval(cases, documents)
    passed = sum(1 for result in results if result["passed"])
    print(f"Passed: {passed}/{len(results)}")
    for result in results:
        status = "PASS" if result["passed"] else "FAIL"
        print(
            f"[{status}] {result['id']} "
            f"retrieval={result['retrieval_passed']} answer={result['answer_passed']}"
        )

    if passed != len(results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
