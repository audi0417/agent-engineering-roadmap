"""Example 02 — Tool-Using Agent.

This script demonstrates a minimal agent that can call approved local tools.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv
from openai import OpenAI

from tools import TOOL_REGISTRY, TOOL_SCHEMAS, ToolError


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_PROMPT = "What is (128 * 42) / 7?"


def load_config() -> dict[str, Any]:
    config_path = BASE_DIR / "agent_config.yaml"
    with config_path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


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
    load_dotenv(BASE_DIR / ".env")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is missing. Copy .env.example to .env and add your API key.")

    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
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


def main() -> None:
    print("Tool-Using Assistant")
    print("Paste a task, or press Enter to use the default example.\n")

    user_input = input("Task: ").strip() or DEFAULT_PROMPT
    result = run_agent(user_input)

    print("\n=== Agent Response ===\n")
    print(result)


if __name__ == "__main__":
    main()
