"""Small graph-based agent with a human approval gate."""

from __future__ import annotations

from dataclasses import dataclass, field


START = "START"
END = "END"


@dataclass
class GraphState:
    task: str
    current_node: str = START
    risk: str = "unknown"
    approval: str = "unknown"
    executed: bool = False
    team: str = "unassigned"
    output: str = ""
    path: list[str] = field(default_factory=lambda: [START])


def classify_risk(state: GraphState) -> GraphState:
    lowered = state.task.lower()
    if any(
        term in lowered
        for term in [
            "delete",
            "remove",
            "production",
            "permission",
            "grant access",
            "revoke access",
            "records",
            "customer data",
        ]
    ):
        state.risk = "critical"
    elif any(term in lowered for term in ["send", "email", "external", "customer"]):
        state.risk = "high"
    elif any(term in lowered for term in ["billing", "ticket", "classify", "support"]):
        state.risk = "medium"
    else:
        state.risk = "low"

    if "billing" in lowered:
        state.team = "support_billing"
    elif "security" in lowered or "permission" in lowered:
        state.team = "security"
    else:
        state.team = "support_general"

    return state


def execute_read_only(state: GraphState) -> GraphState:
    state.approval = "not_required"
    state.executed = True
    state.output = (
        f"Read-only workflow completed for team `{state.team}`. "
        "No state-changing tool was executed."
    )
    return state


def request_approval(state: GraphState) -> GraphState:
    state.approval = "required"
    state.executed = False
    state.output = (
        "Approval required before execution. "
        f"Proposed task: {state.task} "
        f"Risk level: {state.risk}. "
        "Include requester, reason, expected effect, and rollback plan."
    )
    return state


def review(state: GraphState) -> GraphState:
    if state.risk in {"high", "critical"} and state.executed:
        state.output = "Reviewer blocked unsafe execution."
        state.executed = False
        state.approval = "required"
    return state


def next_node(state: GraphState) -> str:
    if state.current_node == START:
        return "classify_risk"
    if state.current_node == "classify_risk":
        return "request_approval" if state.risk in {"high", "critical"} else "execute_read_only"
    if state.current_node in {"execute_read_only", "request_approval"}:
        return "review"
    if state.current_node == "review":
        return END
    return END


def run_graph(task: str) -> GraphState:
    state = GraphState(task=task)
    while state.current_node != END:
        node = next_node(state)
        state.current_node = node
        state.path.append(node)

        if node == "classify_risk":
            state = classify_risk(state)
        elif node == "execute_read_only":
            state = execute_read_only(state)
        elif node == "request_approval":
            state = request_approval(state)
        elif node == "review":
            state = review(state)

    return state


def format_state(state: GraphState) -> str:
    return f"""path: {' -> '.join(state.path)}
risk: {state.risk}
approval: {state.approval}
executed: {str(state.executed).lower()}
team: {state.team}
output: {state.output}
"""
