"""Finance research agent showcase.

Run:
    python main.py
"""

from __future__ import annotations


COMPANIES = {
    "Atlas AI": {
        "business": "AI infrastructure tools",
        "driver": "enterprise demand for agent observability",
        "risk": "high competition and cloud cost pressure",
    },
    "Nova Health": {
        "business": "digital health workflow software",
        "driver": "hospital automation budgets",
        "risk": "regulatory and procurement delays",
    },
}


def compare_companies() -> dict:
    rows = []
    for name, data in COMPANIES.items():
        rows.append(
            {
                "company": name,
                "business": data["business"],
                "growth_driver": data["driver"],
                "key_risk": data["risk"],
            }
        )
    return {
        "boundary": "Research support only. Not investment advice.",
        "comparison": rows,
        "missing_data": [
            "valuation multiples",
            "revenue growth",
            "gross margin trend",
            "customer concentration",
        ],
        "next_questions": [
            "Which company has more durable distribution?",
            "Which risk is already priced in?",
            "What assumptions would change the conclusion?",
        ],
        "evaluator": "passed: no buy/sell instruction, assumptions separated from facts",
    }


def main() -> None:
    result = compare_companies()
    print("=== Finance Research Agent ===")
    print(result["boundary"])
    print("\ncomparison:")
    for row in result["comparison"]:
        print(f"- {row['company']}: {row['business']}")
        print(f"  growth driver: {row['growth_driver']}")
        print(f"  key risk: {row['key_risk']}")
    print("\nmissing data:")
    for item in result["missing_data"]:
        print(f"- {item}")
    print("\nnext questions:")
    for question in result["next_questions"]:
        print(f"- {question}")
    print(f"\nevaluator: {result['evaluator']}")


if __name__ == "__main__":
    main()
