"""Run the capstone starter colony once."""

from __future__ import annotations

from pathlib import Path
import sys


BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

from tools.mock_tools import lookup_mock_evidence


DEFAULT_TASK = "Route an enterprise support ticket about billing access."


def classify_domain(task: str) -> str:
    lowered = task.lower()
    if any(term in lowered for term in ["stock", "finance", "investment", "buy", "sell", "trade"]):
        return "finance"
    if any(term in lowered for term in ["medicine", "health", "pain", "medical"]):
        return "healthcare"
    return "enterprise"


def risk_level(task: str) -> str:
    lowered = task.lower()
    if any(term in lowered for term in ["delete", "buy", "sell", "trade", "medicine", "chest pain"]):
        return "high"
    return "medium"


def run_colony(task: str) -> str:
    domain = classify_domain(task)
    risk = risk_level(task)
    evidence = lookup_mock_evidence(domain)

    if domain == "finance":
        if any(term in task.lower() for term in ["buy", "sell", "trade"]):
            boundary = (
                "This is research support, not investment advice. "
                "I cannot place trades or provide personalized buy or sell instructions."
            )
        else:
            boundary = "This is research support, not investment advice."
    elif domain == "healthcare":
        boundary = "This is not medical advice. Please consult a qualified professional for high risk symptoms."
    else:
        boundary = "This is support workflow assistance. High-risk operations require approval."

    facts = "\n".join(f"- {fact}" for fact in evidence["facts"])
    missing = "\n".join(f"- {item}" for item in evidence["missing"])
    approval = "required" if risk == "high" else "not required for read-only support"

    return f"""domain: {domain}
risk: {risk}
boundary: {boundary}
approval: {approval}

facts:
{facts}

missing:
{missing}

reviewer: passed with domain boundary and missing information disclosed
"""


def main() -> None:
    task = input("Task > ").strip() or DEFAULT_TASK
    print(run_colony(task))


if __name__ == "__main__":
    main()
