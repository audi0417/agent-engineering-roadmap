"""Safe deterministic tools for the capstone starter."""

from __future__ import annotations


def lookup_mock_evidence(topic: str) -> dict:
    evidence = {
        "enterprise": {
            "facts": [
                "Support tickets should be routed by category and risk.",
                "High-risk data operations require approval.",
            ],
            "missing": ["account status", "requester identity"],
        },
        "finance": {
            "facts": [
                "Research support should separate facts from assumptions.",
                "Personalized buy or sell instructions are out of scope.",
            ],
            "missing": ["valuation", "revenue growth", "risk tolerance"],
        },
        "healthcare": {
            "facts": [
                "Healthcare education can explain general concepts.",
                "Diagnosis and treatment recommendations are out of scope.",
            ],
            "missing": ["clinician review", "patient-specific context"],
        },
    }
    return evidence.get(topic, {"facts": [], "missing": ["domain evidence"]})
