"""Example 02 — Tool-Using Agent.

This script demonstrates a minimal agent that can call approved local tools.
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any

from tools import TOOL_REGISTRY, TOOL_SCHEMAS, ToolError


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_PROMPT = "What is (128 * 42) / 7?"


def load_config() -> dict[str, Any]:
    config_path = BASE_DIR / "agent_config.json"
    with config_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def build_system_prompt(config: dict[str, Any]) -> str:
    agent = config["agent"]
    rules = "\n".join(f"- {rule}" for rule in agent.get("rules", []))
    tools = ", ".join(config.get("tools", []))

    return f"""
You are {agent['name']}.

Role:
{agent['role']}

Goal:
{agent['goal']}

Available tools:
{tools}

Rules:
{rules}

When a tool result is provided, use it as an observation and produce a clear final answer.
Do not invent tool results.
""".strip()


def execute_tool_call(tool_call: Any) -> dict[str, Any]:
    tool_name = tool_call.function.name
    raw_arguments = tool_call.function.arguments or "{}"

    if tool_name not in TOOL_REGISTRY:
        return {"error": f"Unknown tool: {tool_name}"}

    try:
        arguments = json.loads(raw_arguments)
    except json.JSONDecodeError as exc:
        return {"error": f"Invalid JSON arguments: {exc}"}

    try:
        result = TOOL_REGISTRY[tool_name](**arguments)
        return {"tool": tool_name, "arguments": arguments, "result": result}
    except ToolError as exc:
        return {"tool": tool_name, "arguments": arguments, "error": str(exc)}
    except Exception as exc:  # Defensive boundary for teaching purposes.
        return {"tool": tool_name, "arguments": arguments, "error": f"Unexpected tool error: {exc}"}


def run_agent(user_input: str) -> str:
    load_env_file(BASE_DIR / ".env")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return run_mock_agent(user_input)

    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    from openai import OpenAI

    client = OpenAI(api_key=api_key)
    config = load_config()
    system_prompt = build_system_prompt(config)

    messages: list[dict[str, Any]] = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input},
    ]

    first_response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=TOOL_SCHEMAS,
        tool_choice="auto",
        temperature=0.2,
    )

    assistant_message = first_response.choices[0].message
    messages.append(assistant_message.model_dump())

    if assistant_message.tool_calls:
        for tool_call in assistant_message.tool_calls:
            tool_result = execute_tool_call(tool_call)
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(tool_result, ensure_ascii=False),
                }
            )

        final_response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.2,
        )
        return final_response.choices[0].message.content or ""

    return assistant_message.content or ""


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.strip().startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def run_mock_agent(user_input: str) -> str:
    """Deterministic local mode that demonstrates tool use without an API key."""
    expression = extract_expression(user_input) or "(128 * 42) / 7"
    tool_result = TOOL_REGISTRY["calculator"](expression=expression)
    return f"""Mock mode: OPENAI_API_KEY not set, so the local tool path was used.

Tool called: calculator
Arguments: {{"expression": "{expression}"}}
Result: {tool_result["result"]}

Final answer:
The expression `{expression}` evaluates to `{tool_result["result"]}`. In the real API mode, the model decides whether to call this tool; in mock mode, the example calls it deterministically so the demo always runs.
"""


def extract_expression(text: str) -> str | None:
    candidates = re.findall(r"[\d\s+\-*/().%]+", text)
    for candidate in sorted(candidates, key=len, reverse=True):
        expression = candidate.strip()
        has_number = any(char.isdigit() for char in expression)
        has_operator = any(char in "+-*/%" for char in expression)
        if has_number and has_operator:
            return expression
    return None


def main() -> None:
    print("Tool-Using Assistant")
    print("Paste a task, or press Enter to use the default example.\n")

    user_input = input("Task: ").strip() or DEFAULT_PROMPT
    result = run_agent(user_input)

    print("\n=== Agent Response ===\n")
    print(result)


if __name__ == "__main__":
    main()
