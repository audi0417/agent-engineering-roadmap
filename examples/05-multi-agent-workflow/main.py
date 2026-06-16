"""Example 05 - Multi-Agent Workflow.

Run:
    python main.py
"""

from __future__ import annotations

import json
from pathlib import Path

from workflow import run_workflow


BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "agent_config.json"


def load_config() -> dict:
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    config = load_config()
    task = input("Task > ").strip()
    if not task:
        task = "Create a lesson plan for teaching tool-using agents."

    artifact = run_workflow(
        task=task,
        required_items=config["rubric"]["must_include"],
        max_rounds=int(config["workflow"]["max_review_rounds"]),
    )

    print("\n=== Plan ===")
    for step in artifact.plan:
        print(f"- {step}")

    print("\n=== Review ===")
    if artifact.feedback:
        for item in artifact.feedback:
            print(f"- {item}")
    else:
        print("- Passed")

    print("\n=== Final Draft ===")
    print(artifact.draft)


if __name__ == "__main__":
    main()
