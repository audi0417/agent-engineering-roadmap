from __future__ import annotations

from pathlib import Path

from observable_agent import ObservableSupportAgent, TraceRecorder, load_trace, summarize_trace


DEFAULT_TICKET = "Please delete all production customer records for account 1842."


def main() -> int:
    print("Observable Agent")
    print("================")
    ticket = input("Ticket > ").strip() or DEFAULT_TICKET

    trace_path = Path(__file__).with_name("trace.jsonl")
    agent = ObservableSupportAgent(TraceRecorder(trace_path))
    result = agent.run(ticket)
    summary = summarize_trace(load_trace(trace_path))

    print("\n=== Agent Output ===")
    print(f"risk: {result['risk']}")
    print(f"category: {result['category']}")
    print(f"approval_required: {result['approval_required']}")
    print(f"answer: {result['answer']}")

    print("\n=== Trace Summary ===")
    print(f"run_id: {summary['run_id']}")
    print(f"events: {summary['event_counts']}")
    print(f"guardrails: {summary['guardrail_count']}")
    print(f"trace_path: {result['trace_path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

