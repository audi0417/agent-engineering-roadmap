"""Agent identity and permission system example."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class AgentIdentity:
    agent_id: str
    owner: str
    risk_tier: str
    scopes: set[str]


class PermissionDenied(Exception):
    pass


class PermissionSystem:
    def __init__(self) -> None:
        self.agents = {
            "researcher": AgentIdentity(
                "researcher",
                "ai-platform",
                "low",
                {"read:docs", "write:draft"},
            ),
            "ops_agent": AgentIdentity(
                "ops_agent",
                "platform-ops",
                "high",
                {"read:docs", "write:draft", "read:tickets", "request:approval"},
            ),
        }
        self.audit_log: list[dict[str, Any]] = []

    def authorize(self, agent_id: str, scope: str, action: str) -> dict[str, Any]:
        identity = self.agents[agent_id]
        allowed = scope in identity.scopes
        requires_review = identity.risk_tier == "high" or scope.startswith("delete:")
        decision = {
            "agent_id": agent_id,
            "owner": identity.owner,
            "scope": scope,
            "action": action,
            "allowed": allowed,
            "requires_review": requires_review,
        }
        self.audit_log.append(decision)
        if not allowed:
            raise PermissionDenied(f"{agent_id} lacks scope {scope}")
        return decision

    def access_review(self) -> list[dict[str, Any]]:
        return [
            {
                "agent_id": identity.agent_id,
                "owner": identity.owner,
                "risk_tier": identity.risk_tier,
                "scope_count": len(identity.scopes),
                "high_risk": identity.risk_tier == "high",
            }
            for identity in self.agents.values()
        ]


def run_demo() -> dict[str, Any]:
    system = PermissionSystem()
    allowed = system.authorize("researcher", "read:docs", "summarize policy")
    denied = None
    try:
        system.authorize("researcher", "read:tickets", "inspect customer ticket")
    except PermissionDenied as exc:
        denied = str(exc)
    return {
        "allowed": allowed,
        "denied": denied,
        "access_review": system.access_review(),
        "audit_log": system.audit_log,
    }


def run_eval(eval_path: Path) -> dict[str, Any]:
    cases = json.loads(eval_path.read_text(encoding="utf-8"))
    results = []
    for case in cases:
        system = PermissionSystem()
        try:
            output = system.authorize(case["agent_id"], case["scope"], case["action"])
            passed = case["expected"] == "allowed" and output["allowed"]
        except PermissionDenied as exc:
            output = {"error": str(exc)}
            passed = case["expected"] == "denied"
        results.append({"name": case["name"], "passed": passed, "output": output})
    return {
        "passed": sum(1 for result in results if result["passed"]),
        "total": len(results),
        "results": results,
    }

