"""A small MCP gateway teaching tools, resources, prompts, auth, and elicitation."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Request:
    token: str
    capability: str
    name: str
    arguments: dict[str, Any]


class GatewayError(Exception):
    pass


class ModernMCPGateway:
    def __init__(self) -> None:
        self.tokens = {
            "learner-token": {"read:resources", "call:tools", "use:prompts"},
            "readonly-token": {"read:resources"},
        }
        self.resources = {
            "agent://policy/tool-approval": (
                "High-risk tools require approval, reason, expected effect, "
                "and rollback plan."
            )
        }
        self.prompts = {
            "safe-tool-summary": "Summarize tool risk without executing the tool."
        }

    def authorize(self, token: str, capability: str) -> None:
        if capability not in self.tokens.get(token, set()):
            raise GatewayError(f"Unauthorized capability: {capability}")

    def list_capabilities(self, token: str) -> dict[str, list[str]]:
        allowed = self.tokens.get(token, set())
        return {
            "tools": ["risk_score"] if "call:tools" in allowed else [],
            "resources": list(self.resources) if "read:resources" in allowed else [],
            "prompts": list(self.prompts) if "use:prompts" in allowed else [],
        }

    def read_resource(self, request: Request) -> dict[str, Any]:
        self.authorize(request.token, "read:resources")
        if request.name not in self.resources:
            raise GatewayError(f"Unknown resource: {request.name}")
        return {"uri": request.name, "content": self.resources[request.name]}

    def get_prompt(self, request: Request) -> dict[str, Any]:
        self.authorize(request.token, "use:prompts")
        if request.name not in self.prompts:
            raise GatewayError(f"Unknown prompt: {request.name}")
        return {"name": request.name, "template": self.prompts[request.name]}

    def call_tool(self, request: Request) -> dict[str, Any]:
        self.authorize(request.token, "call:tools")
        if request.name != "risk_score":
            raise GatewayError(f"Unknown tool: {request.name}")

        task = str(request.arguments.get("task", ""))
        if not task.strip():
            return {
                "status": "elicitation_required",
                "question": "What task should be risk scored?",
            }

        lowered = task.lower()
        risk = "high" if any(term in lowered for term in ["delete", "production", "external"]) else "low"
        return {"status": "ok", "risk": risk, "task": task}


def run_demo() -> dict[str, Any]:
    gateway = ModernMCPGateway()
    token = "learner-token"
    return {
        "capabilities": gateway.list_capabilities(token),
        "resource": gateway.read_resource(
            Request(token, "read:resources", "agent://policy/tool-approval", {})
        ),
        "prompt": gateway.get_prompt(
            Request(token, "use:prompts", "safe-tool-summary", {})
        ),
        "elicitation": gateway.call_tool(
            Request(token, "call:tools", "risk_score", {"task": ""})
        ),
        "tool_result": gateway.call_tool(
            Request(
                token,
                "call:tools",
                "risk_score",
                {"task": "Delete production records."},
            )
        ),
    }


def run_eval(eval_path: Path) -> dict[str, Any]:
    cases = json.loads(eval_path.read_text(encoding="utf-8"))
    gateway = ModernMCPGateway()
    results = []
    for case in cases:
        try:
            if case["operation"] == "list":
                output = gateway.list_capabilities(case["token"])
            elif case["operation"] == "tool":
                output = gateway.call_tool(
                    Request(
                        case["token"],
                        "call:tools",
                        case["target_name"],
                        case["arguments"],
                    )
                )
            elif case["operation"] == "resource":
                output = gateway.read_resource(
                    Request(case["token"], "read:resources", case["name"], {})
                )
            else:
                raise GatewayError("unknown operation")
            passed = case["expected"] in json.dumps(output)
        except GatewayError as exc:
            output = {"error": str(exc)}
            passed = case["expected"] in str(exc)
        results.append({"name": case["name"], "passed": passed, "output": output})
    return {
        "passed": sum(1 for result in results if result["passed"]),
        "total": len(results),
        "results": results,
    }
