"""Minimal MCP-style tool server template.

This file is intentionally framework-light. Replace the registry with your MCP
framework of choice when moving to production.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


ToolHandler = Callable[[dict[str, Any]], dict[str, Any]]


@dataclass
class Tool:
    name: str
    description: str
    input_schema: dict[str, Any]
    handler: ToolHandler


class ToolRegistry:
    def __init__(self) -> None:
        self.tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        self.tools[tool.name] = tool

    def call(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        if name not in self.tools:
            raise KeyError(f"Unknown tool: {name}")
        return self.tools[name].handler(arguments)


def echo_tool(arguments: dict[str, Any]) -> dict[str, Any]:
    text = str(arguments.get("text", ""))
    return {"text": text, "length": len(text)}


def build_registry() -> ToolRegistry:
    registry = ToolRegistry()
    registry.register(
        Tool(
            name="echo",
            description="Return text and its length.",
            input_schema={
                "type": "object",
                "properties": {"text": {"type": "string"}},
                "required": ["text"],
            },
            handler=echo_tool,
        )
    )
    return registry


if __name__ == "__main__":
    server = build_registry()
    print(server.call("echo", {"text": "hello agent engineering"}))
