"""Local tools exposed through the MCP-style server."""

from __future__ import annotations

from typing import Any


KNOWLEDGE_BASE = {
    "mcp": "MCP-style separation keeps tools behind a client/server boundary so agents do not need to import tool code directly.",
    "memory policy": "A memory policy defines what can be stored, who can read or write it, how it is updated, and how it can be deleted.",
    "tool safety": "Tool safety requires clear schemas, argument validation, permission boundaries, and human approval for high-risk actions.",
}

USER_PROFILES = {
    "user_001": {
        "name": "Demo User",
        "care_context": "Tracks nutrition notes, weekly exercise, blood pressure logs, and follow-up reminders.",
        "preferences": ["concise summaries", "action items", "risk flags"],
    },
    "user_002": {
        "name": "Research User",
        "care_context": "Focuses on literature notes, project tasks, and weekly review summaries.",
        "preferences": ["structured output", "citations when available"],
    },
}


def search_knowledge_base(query: str) -> dict[str, Any]:
    """Search a tiny local knowledge base."""
    query_lower = query.lower()
    matches = [
        {"key": key, "content": value}
        for key, value in KNOWLEDGE_BASE.items()
        if query_lower in key.lower() or query_lower in value.lower()
    ]
    return {"query": query, "matches": matches, "match_count": len(matches)}


def get_user_profile(user_id: str) -> dict[str, Any]:
    """Return a demo user profile."""
    profile = USER_PROFILES.get(user_id)
    if not profile:
        return {"user_id": user_id, "error": "User profile not found."}
    return {"user_id": user_id, "profile": profile}


def explain_server_boundary() -> dict[str, Any]:
    """Explain the MCP-style server boundary."""
    return {
        "concept": "MCP-style boundary",
        "explanation": "The agent talks to a client, the client talks to a server, and the server owns the tools. This keeps tool implementation separate from agent reasoning.",
        "benefits": ["replaceable tools", "centralized permissions", "auditability", "reuse across agents"],
    }
