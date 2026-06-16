"""Example 01 — Single Agent

A minimal Research Summary Agent.

Run:
    python main.py
"""

from __future__ import annotations

import json
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "agent_config.json"


DEFAULT_NOTES = """
We are planning to build an Agent Engineering Roadmap repository.
The project should teach AI agents, MCP, memory, workflows, multi-agent systems,
and agent colonies. The first version should be bilingual in English and Traditional Chinese.
We need examples that are simple enough for beginners but useful for real builders.
Potential application tracks include healthcare, finance, and enterprise automation.
Risks include making the roadmap too broad, adding too many tools too early,
and not providing runnable code examples.
""".strip()


def load_config() -> dict:
    """Load agent configuration from JSON."""
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Config file not found: {CONFIG_PATH}")

    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def build_system_prompt(config: dict) -> str:
    """Build a system prompt from the agent config."""
    agent = config["agent"]
    sections = config.get("summary_sections", [])

    rules = "\n".join(f"- {rule}" for rule in agent.get("rules", []))
    output_sections = "\n".join(f"## {section}" for section in sections)

    return f"""
You are {agent['name']}.

Role:
{agent['role']}

Goal:
{agent['goal']}

Rules:
{rules}

Return the answer in Markdown using these sections:
{output_sections}
""".strip()


def run_agent(notes: str) -> str:
    """Run the single agent on user notes."""
    load_env_file(BASE_DIR / ".env")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return run_mock_agent(notes)

    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    config = load_config()
    system_prompt = build_system_prompt(config)

    from openai import OpenAI

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Summarize these notes:\n\n{notes}"},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content or ""


def load_env_file(path: Path) -> None:
    """Load KEY=VALUE pairs without requiring python-dotenv."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.strip().startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def run_mock_agent(notes: str) -> str:
    """Deterministic fallback so the example runs without API keys."""
    lines = [line.strip("- ").strip() for line in notes.splitlines() if line.strip()]
    key_points = lines[:4] or ["No concrete notes provided."]
    risks = [line for line in lines if "risk" in line.lower() or "too" in line.lower()]

    return f"""## Key Points
{format_bullets(key_points)}

## Action Items
- Define the first runnable example.
- Keep each agent task narrow and testable.
- Add evaluation cases before expanding scope.

## Risks or Uncertainties
{format_bullets(risks or ["The roadmap may become too broad if examples are not kept focused."])}

## Suggested Next Steps
- Run this example with the default notes.
- Replace the mock fallback with an OpenAI API key when ready.
- Add three expected-output checks for your own notes.
"""


def format_bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def main() -> None:
    print("Research Summary Agent")
    print("=" * 24)
    print("Paste your notes below. Press Enter twice to use the default example.\n")

    user_input = input("> ").strip()
    notes = user_input if user_input else DEFAULT_NOTES

    print("\nRunning agent...\n")
    result = run_agent(notes)
    print(result)


if __name__ == "__main__":
    main()
