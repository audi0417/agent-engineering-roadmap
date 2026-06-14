"""A tiny MCP-style tool server abstraction.

This is not a full MCP implementation. It teaches the separation pattern:
Agent -> Client -> Server -> Tools.
"""

from __future__ import annotations

from typing import Any, Callable

from tools import explain_server_boundary, get_user_profile, search_knowledge_base


class MCPStyleToolServer:
    """A local server-like boundary that owns tools and schemas."""

    def __init__(self) -> None:
        self._tools: dict[str, Callable[..., dict[str, Any]]] = {
            "search_knowledge_base": search_knowledge_base,
            "get_user_profile": get_user_profile,
            "explain_server_boundary": explain_server_boundary,
        }

    def list_tools(self) -> list[dict[str, Any]]:
        return [
            {
                "type": "function",
                "function": {
                    "name": "search_knowledge_base",
                    "description": "Search the local knowledge base for a topic.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "The topic to search for.",
                            }
                        },
                        "required": ["query"],
                        "additionalProperties": False,
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_user_profile",
                    "description": "Get a demo user profile by user_id.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "user_id": {
                                "type": "string",
                                "description": "The user id, such as user_001.",
                            }
                        },
                        "required": ["user_id"],
                        "additionalProperties": False,
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "explain_server_boundary",
                    "description": "Explain the MCP-style client/server boundary.",
                    "parameters": {
                        "type": "object",
                        "properties": {},
                        "additionalProperties": False,
                    },
                },
            },
        ]

    def call_tool(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        if name not in self._tools:
            return {"error": f"Unknown tool: {name}"}

        try:
            result = self._tools[name](**arguments)
            return {"tool": name, "arguments": arguments, "result": result}
        except TypeError as exc:
            return {"tool": name, "arguments": arguments, "error": f"Invalid arguments: {exc}"}
        except Exception as exc:
            return {"tool": name, "arguments": arguments, "error": f"Unexpected server error: {exc}"}
