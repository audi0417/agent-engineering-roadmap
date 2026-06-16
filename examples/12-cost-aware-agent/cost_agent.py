"""Cost and latency aware routing for agent tasks."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path


@dataclass(frozen=True)
class ModelOption:
    name: str
    quality: int
    cost_per_1k_tokens: float
    latency_ms: int


MODELS = [
    ModelOption("fast-small", quality=2, cost_per_1k_tokens=0.05, latency_ms=180),
    ModelOption("balanced-medium", quality=4, cost_per_1k_tokens=0.35, latency_ms=650),
    ModelOption("deep-large", quality=5, cost_per_1k_tokens=1.2, latency_ms=1800),
]


def estimate_tokens(task: str) -> int:
    return max(80, len(task.split()) * 12)


def required_quality(task: str) -> int:
    lowered = task.lower()
    if any(term in lowered for term in ["legal", "medical", "finance", "production"]):
        return 5
    if any(term in lowered for term in ["compare", "analyze", "debug", "plan"]):
        return 4
    return 2


def choose_model(task: str, max_latency_ms: int, max_cost: float) -> dict[str, object]:
    tokens = estimate_tokens(task)
    quality = required_quality(task)
    candidates = []

    for model in MODELS:
        estimated_cost = round((tokens / 1000) * model.cost_per_1k_tokens, 4)
        if (
            model.quality >= quality
            and model.latency_ms <= max_latency_ms
            and estimated_cost <= max_cost
        ):
            candidates.append((estimated_cost, model.latency_ms, model))

    if not candidates:
        fallback = min(MODELS, key=lambda item: item.cost_per_1k_tokens)
        return {
            "selected_model": fallback.name,
            "tokens": tokens,
            "estimated_cost": round((tokens / 1000) * fallback.cost_per_1k_tokens, 4),
            "latency_ms": fallback.latency_ms,
            "quality_required": quality,
            "fallback": True,
            "reason": "No model satisfied all constraints; routed to cheapest safe fallback.",
        }

    estimated_cost, latency_ms, model = sorted(candidates)[0]
    return {
        "selected_model": model.name,
        "tokens": tokens,
        "estimated_cost": estimated_cost,
        "latency_ms": latency_ms,
        "quality_required": quality,
        "fallback": False,
        "reason": "Selected the cheapest model that satisfies quality, latency, and cost.",
    }


def answer(task: str, budget: dict[str, float | int]) -> dict[str, object]:
    route = choose_model(
        task,
        max_latency_ms=int(budget["max_latency_ms"]),
        max_cost=float(budget["max_cost"]),
    )
    return {
        "task": task,
        "route": route,
        "response": (
            f"Use `{route['selected_model']}` for this task. "
            f"Estimated cost: ${route['estimated_cost']}. "
            f"Estimated latency: {route['latency_ms']}ms."
        ),
    }


def run_eval(eval_path: Path) -> dict[str, object]:
    cases = json.loads(eval_path.read_text(encoding="utf-8"))
    results = []
    for case in cases:
        output = answer(case["task"], case["budget"])
        route = output["route"]
        passed = (
            route["selected_model"] == case["expected_model"]
            and route["estimated_cost"] <= case["budget"]["max_cost"]
            and route["latency_ms"] <= case["budget"]["max_latency_ms"]
        )
        results.append({"name": case["name"], "passed": passed, "output": output})
    return {
        "passed": sum(1 for result in results if result["passed"]),
        "total": len(results),
        "results": results,
    }

