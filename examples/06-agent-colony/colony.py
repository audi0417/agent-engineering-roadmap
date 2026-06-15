"""Shared-memory agent colony for Example 06."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SharedMemory:
    events: list[str] = field(default_factory=list)

    def write(self, event: str) -> None:
        self.events.append(event)


def route_domain(task: str, domains: dict) -> str:
    lowered = task.lower()
    scores: dict[str, int] = {}
    for domain, config in domains.items():
        scores[domain] = sum(1 for keyword in config["keywords"] if keyword in lowered)
    best_domain, best_score = max(scores.items(), key=lambda item: item[1])
    return best_domain if best_score > 0 else "enterprise"


def domain_agent(domain: str, task: str, disclaimer: str) -> dict:
    workflows = {
        "healthcare": [
            "Clarify user goal and risk level.",
            "Collect only necessary health context.",
            "Summarize options and uncertainty.",
            "Send high-risk cases to a qualified professional.",
        ],
        "finance": [
            "Define the research question.",
            "Collect comparable data.",
            "Separate facts, assumptions, and opinions.",
            "Review risk before any portfolio action.",
        ],
        "enterprise": [
            "Classify the workflow request.",
            "Retrieve relevant internal context.",
            "Draft a structured action plan.",
            "Ask for approval before writing to systems.",
        ],
    }
    return {
        "routed_domain": domain,
        "task": task,
        "disclaimer": disclaimer,
        "recommended_workflow": workflows[domain],
        "human_review_gate": "Required before high-impact or irreversible actions.",
    }


def evaluate(result: dict, required: list[str]) -> list[str]:
    return [field for field in required if field not in result or not result[field]]


def run_colony(task: str, config: dict) -> tuple[dict, list[str], SharedMemory]:
    memory = SharedMemory()
    domain = route_domain(task, config["domains"])
    memory.write(f"Supervisor routed task to {domain}.")

    disclaimer = config["domains"][domain]["disclaimer"]
    result = domain_agent(domain=domain, task=task, disclaimer=disclaimer)
    memory.write(f"{domain} agent produced recommended workflow.")

    missing = evaluate(result, config["evaluation"]["required"])
    memory.write("Evaluator completed final check.")
    return result, missing, memory
