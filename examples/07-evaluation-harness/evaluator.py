"""Simple string-based evaluator for Example 07."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CaseResult:
    case_id: str
    passed: bool
    missing: list[str]
    forbidden_found: list[str]
    output: str


def evaluate_case(case: dict, output: str) -> CaseResult:
    expected = case["expected"]
    lowered = output.lower()

    missing = [
        phrase
        for phrase in expected.get("must_include", [])
        if phrase.lower() not in lowered
    ]
    forbidden_found = [
        phrase
        for phrase in expected.get("must_not_include", [])
        if phrase.lower() in lowered
    ]

    return CaseResult(
        case_id=case["id"],
        passed=not missing and not forbidden_found,
        missing=missing,
        forbidden_found=forbidden_found,
        output=output,
    )


def summarize(results: list[CaseResult]) -> dict:
    passed = sum(1 for result in results if result.passed)
    total = len(results)
    return {
        "passed": passed,
        "failed": total - passed,
        "total": total,
        "pass_rate": passed / total if total else 0.0,
    }
