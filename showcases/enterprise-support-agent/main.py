"""Enterprise support agent showcase.

Run:
    python main.py
"""

from __future__ import annotations


TICKETS = [
    "Customer cannot access billing dashboard after password reset.",
    "Please delete all production customer records for account 1842.",
]


def route_ticket(ticket: str) -> dict:
    lowered = ticket.lower()
    if "delete" in lowered and "production" in lowered:
        return {
            "category": "data_operation",
            "team": "security_and_data_ops",
            "risk": "high",
            "approval": "required",
            "next_action": "Create an approval request with account, reason, requester, and rollback plan.",
        }
    if "billing" in lowered:
        return {
            "category": "billing_access",
            "team": "support_billing",
            "risk": "medium",
            "approval": "not required for read-only investigation",
            "next_action": "Check account status and authentication logs before drafting a response.",
        }
    return {
        "category": "general_support",
        "team": "support_general",
        "risk": "low",
        "approval": "not required",
        "next_action": "Ask for missing context.",
    }


def main() -> None:
    print("=== Enterprise Support Agent ===")
    for ticket in TICKETS:
        result = route_ticket(ticket)
        print(f"\nticket: {ticket}")
        print(f"category: {result['category']}")
        print(f"team: {result['team']}")
        print(f"risk: {result['risk']}")
        print(f"approval: {result['approval']}")
        print(f"next_action: {result['next_action']}")


if __name__ == "__main__":
    main()
