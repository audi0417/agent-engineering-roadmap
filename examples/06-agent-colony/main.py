"""Example 06 - Agent Colony.

Run:
    python main.py
"""

from __future__ import annotations

import json
from pathlib import Path

from colony import run_colony


BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "colony_config.json"


def load_config() -> dict:
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    config = load_config()
    task = input("Task > ").strip()
    if not task:
        task = "Build a finance research workflow for comparing two companies."

    result, missing, memory = run_colony(task, config)

    print("\n=== Shared Memory ===")
    for event in memory.events:
        print(f"- {event}")

    print("\n=== Evaluation ===")
    if missing:
        print("Missing fields:")
        for field in missing:
            print(f"- {field}")
    else:
        print("- Passed")

    print("\n=== Colony Output ===")
    print(f"routed_domain: {result['routed_domain']}")
    print(f"disclaimer: {result['disclaimer']}")
    print("recommended_workflow:")
    for step in result["recommended_workflow"]:
        print(f"- {step}")
    print(f"human_review_gate: {result['human_review_gate']}")


if __name__ == "__main__":
    main()
