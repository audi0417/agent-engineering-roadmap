"""A tiny MCP-style client abstraction."""

from __future__ import annotations

from typing import Any

from mcp_server import MCPStyleToolServer


class MCPStyleClient:
    """Client boundary used by the agent runtime."""

    def __init__(self, server: MCPStyleToolServer) -> None:
        self.server = server

    def list_tools(self) -> list[dict[str, Any]]:
        return self.server.list_tools()

    def call_tool(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        return self.server.call_tool(name, arguments)
