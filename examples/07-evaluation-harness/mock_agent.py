"""Deterministic mock agent for Example 07."""

from __future__ import annotations


def run_agent(user_input: str) -> str:
    lowered = user_input.lower()

    if "yesterday" in lowered:
        return "I am missing context. Please clarify what we discussed yesterday."

    if "stock" in lowered or "buy" in lowered:
        return "This is research support, not investment advice. I can help compare risks and assumptions."

    if "diagnose" in lowered or "medicine" in lowered:
        return "This is not medical advice. Please consult a qualified professional for diagnosis or treatment."

    if "12 * 8" in lowered or "12*8" in lowered:
        return "Calculation: 12 * 8 = 96."

    return "Decisions: none provided. Next steps: clarify the goal, identify inputs, and define expected output."
