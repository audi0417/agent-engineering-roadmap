"""Example 03 — MCP-style Agent.

This script demonstrates how an agent can access tools through a client/server boundary.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from mcp_client import MCPStyleClient
from mcp_server import MCPStyleToolServer


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_PROMPT = "Use available tools to explain what MCP-style separation means."


def load_config() -> dict[str, Any]:
    config_path = BASE_DIR / "agent_config.json"
    with config_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def build_system_prompt(config: dict[str, Any]) -> str:
    agent = config["agent"]
    rules = "\n".join(f"- {rule}" for rule in agent.get("rules", []))

    return f"""
You are {agent['name']}.

Role:
{agent['role']}

Goal:
{agent['goal']}

Rules:
{rules}

You can request tools that are exposed by the MCP-style client.
Use tool results as observations. Do not invent server results.
""".strip()


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

    tool_server = MCPStyleToolServer()
    mcp_client = MCPStyleClient(tool_server)
    tool_schemas = mcp_client.list_tools()

    messages: list[dict[str, Any]] = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input},
    ]

    first_response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tool_schemas,
        tool_choice="auto",
        temperature=0.2,
    )

    assistant_message = first_response.choices[0].message
    messages.append(assistant_message.model_dump())

    if assistant_message.tool_calls:
        for tool_call in assistant_message.tool_calls:
            tool_name = tool_call.function.name
            try:
                arguments = json.loads(tool_call.function.arguments or "{}")
            except json.JSONDecodeError as exc:
                tool_result = {"error": f"Invalid JSON arguments: {exc}"}
            else:
                tool_result = mcp_client.call_tool(tool_name, arguments)

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
    """Deterministic MCP-style path for API-key-free demos."""
    tool_server = MCPStyleToolServer()
    mcp_client = MCPStyleClient(tool_server)
    tools = [tool["function"]["name"] for tool in mcp_client.list_tools()]
    boundary = mcp_client.call_tool("explain_server_boundary", {})
    search = mcp_client.call_tool("search_knowledge_base", {"query": "mcp"})

    return f"""Mock mode: OPENAI_API_KEY not set, so the local MCP-style client/server path was used.

User task:
{user_input}

Available server tools:
{format_bullets(tools)}

Tool observation: explain_server_boundary
{json.dumps(boundary["result"], indent=2, ensure_ascii=False)}

Tool observation: search_knowledge_base
{json.dumps(search["result"], indent=2, ensure_ascii=False)}

Final answer:
MCP-style separation means the agent talks to a client, the client talks to a server, and the server owns the tools. This keeps permissions, auditing, and tool implementation outside the agent runtime.
"""


def format_bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def main() -> None:
    print("MCP-style Agent")
    print("Paste a task, or press Enter to use the default example.\n")

    user_input = input("Task: ").strip() or DEFAULT_PROMPT
    result = run_agent(user_input)

    print("\n=== Agent Response ===\n")
    print(result)


if __name__ == "__main__":
    main()
