"""Tiny inspectable RAG pipeline for teaching retrieval evaluation."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "be",
    "before",
    "for",
    "from",
    "how",
    "is",
    "of",
    "should",
    "the",
    "to",
    "what",
    "which",
}


@dataclass(frozen=True)
class Document:
    id: str
    title: str
    text: str


@dataclass(frozen=True)
class RetrievalResult:
    document: Document
    score: int
    matched_terms: list[str]


def load_documents(path: Path) -> list[Document]:
    raw_docs = json.loads(path.read_text(encoding="utf-8"))
    return [Document(**item) for item in raw_docs]


def load_eval_cases(path: Path) -> list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def tokenize(text: str) -> list[str]:
    tokens = re.findall(r"[a-z0-9-]+", text.lower())
    return [token for token in tokens if token not in STOPWORDS and len(token) > 2]


def retrieve(question: str, documents: list[Document], limit: int = 2) -> list[RetrievalResult]:
    query_terms = set(tokenize(question))
    results: list[RetrievalResult] = []

    for document in documents:
        doc_terms = set(tokenize(f"{document.title} {document.text}"))
        matched = sorted(query_terms & doc_terms)
        if matched:
            results.append(
                RetrievalResult(
                    document=document,
                    score=len(matched),
                    matched_terms=matched,
                )
            )

    return sorted(results, key=lambda item: (-item.score, item.document.id))[:limit]


def answer(question: str, retrieved: list[RetrievalResult]) -> str:
    if not retrieved or retrieved[0].score < 1:
        return "I do not have enough information in the knowledge base to answer that."

    evidence = retrieved[0].document
    if is_secret_question(question):
        return "I do not have enough information in the knowledge base to answer that."

    return (
        f"Based on `{evidence.id}`: {evidence.text} "
        f"Retrieved terms: {', '.join(retrieved[0].matched_terms)}."
    )


def is_secret_question(question: str) -> bool:
    lowered = question.lower()
    return any(term in lowered for term in ["password", "secret", "guaranteed", "best for every"])


def evaluate_case(case: dict[str, Any], documents: list[Document]) -> dict[str, Any]:
    retrieved = retrieve(case["question"], documents)
    output = answer(case["question"], retrieved)
    retrieved_ids = [item.document.id for item in retrieved]

    if case["expected_doc"] is None:
        retrieval_passed = not retrieved or case["expected_doc"] not in retrieved_ids
    else:
        retrieval_passed = case["expected_doc"] in retrieved_ids

    lowered_output = output.lower()
    answer_passed = all(term.lower() in lowered_output for term in case["expected_terms"])

    return {
        "id": case["id"],
        "passed": retrieval_passed and answer_passed,
        "retrieval_passed": retrieval_passed,
        "answer_passed": answer_passed,
        "retrieved_ids": retrieved_ids,
        "output": output,
    }


def run_eval(cases: list[dict[str, Any]], documents: list[Document]) -> list[dict[str, Any]]:
    return [evaluate_case(case, documents) for case in cases]
