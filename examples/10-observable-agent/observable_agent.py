"""A dependency-free observable agent example.

The goal is not to build a clever model. The goal is to make an agent run
inspectable: every decision, tool call, guardrail, and final output becomes a
trace event that can be replayed during debugging.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any
from uuid import uuid4


TracePayload = dict[str, Any]


@dataclass
class TraceEvent:
    run_id: str
    span_id: str
    parent_span_id: str | None
    event_type: str
    name: str
    payload: TracePayload
    timestamp: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "run_id": self.run_id,
            "span_id": self.span_id,
            "parent_span_id": self.parent_span_id,
            "event_type": self.event_type,
            "name": self.name,
            "payload": self.payload,
        }


class TraceRecorder:
    def __init__(self, trace_path: Path) -> None:
        self.trace_path = trace_path
        self.run_id = f"run_{uuid4().hex[:8]}"
        self.events: list[TraceEvent] = []

    def record(
        self,
        event_type: str,
        name: str,
        payload: TracePayload,
        parent_span_id: str | None = None,
    ) -> str:
        span_id = f"span_{len(self.events) + 1:03d}"
        self.events.append(
            TraceEvent(
                run_id=self.run_id,
                span_id=span_id,
                parent_span_id=parent_span_id,
                event_type=event_type,
                name=name,
                payload=payload,
            )
        )
        return span_id

    def write_jsonl(self) -> None:
        self.trace_path.parent.mkdir(parents=True, exist_ok=True)
        with self.trace_path.open("w", encoding="utf-8") as file:
            for event in self.events:
                file.write(json.dumps(event.to_dict(), ensure_ascii=False) + "\n")


class ObservableSupportAgent:
    """Tiny support agent with traceable risk classification and tool calls."""

    def __init__(self, recorder: TraceRecorder) -> None:
        self.recorder = recorder

    def run(self, ticket: str) -> dict[str, Any]:
        root = self.recorder.record(
            "agent.run.start",
            "support_agent",
            {"ticket": ticket},
        )

        risk = self.classify_risk(ticket, root)
        category = self.classify_category(ticket, root)
        approval_required = risk in {"high", "critical"}

        if approval_required:
            self.recorder.record(
                "guardrail.triggered",
                "human_approval_gate",
                {
                    "risk": risk,
                    "reason": "High-impact action requires human approval.",
                },
                parent_span_id=root,
            )
            answer = (
                "Approval required before execution. Prepare requester, reason, "
                "expected effect, rollback plan, and audit owner."
            )
        else:
            lookup = self.lookup_account_status(ticket, root)
            answer = (
                f"Route to {category}. Account status: {lookup['status']}. "
                "Proceed with read-only investigation and document findings."
            )

        self.recorder.record(
            "agent.run.end",
            "support_agent",
            {
                "risk": risk,
                "category": category,
                "approval_required": approval_required,
                "answer": answer,
            },
            parent_span_id=root,
        )
        self.recorder.write_jsonl()

        return {
            "run_id": self.recorder.run_id,
            "risk": risk,
            "category": category,
            "approval_required": approval_required,
            "answer": answer,
            "trace_path": str(self.recorder.trace_path),
        }

    def classify_risk(self, ticket: str, parent_span_id: str) -> str:
        lowered = ticket.lower()
        if any(term in lowered for term in ["delete", "production", "wire", "refund all"]):
            risk = "critical"
        elif any(term in lowered for term in ["billing", "password", "access"]):
            risk = "medium"
        else:
            risk = "low"
        self.recorder.record(
            "llm.decision",
            "classify_risk",
            {"input": ticket, "risk": risk},
            parent_span_id=parent_span_id,
        )
        return risk

    def classify_category(self, ticket: str, parent_span_id: str) -> str:
        lowered = ticket.lower()
        if "billing" in lowered:
            category = "billing_support"
        elif "delete" in lowered or "production" in lowered:
            category = "security_and_data_ops"
        else:
            category = "general_support"
        self.recorder.record(
            "llm.decision",
            "classify_category",
            {"input": ticket, "category": category},
            parent_span_id=parent_span_id,
        )
        return category

    def lookup_account_status(self, ticket: str, parent_span_id: str) -> dict[str, str]:
        result = {"status": "active", "source": "mock_account_tool"}
        self.recorder.record(
            "tool.call",
            "lookup_account_status",
            {"arguments": {"ticket_excerpt": ticket[:80]}},
            parent_span_id=parent_span_id,
        )
        self.recorder.record(
            "tool.result",
            "lookup_account_status",
            result,
            parent_span_id=parent_span_id,
        )
        return result


def load_trace(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as file:
        return [json.loads(line) for line in file]


def summarize_trace(events: list[dict[str, Any]]) -> dict[str, Any]:
    event_counts: dict[str, int] = {}
    for event in events:
        event_counts[event["event_type"]] = event_counts.get(event["event_type"], 0) + 1

    guardrails = [
        event for event in events if event["event_type"] == "guardrail.triggered"
    ]
    final_event = next(
        event for event in reversed(events) if event["event_type"] == "agent.run.end"
    )
    return {
        "run_id": final_event["run_id"],
        "event_counts": event_counts,
        "guardrail_count": len(guardrails),
        "approval_required": final_event["payload"]["approval_required"],
        "risk": final_event["payload"]["risk"],
    }

