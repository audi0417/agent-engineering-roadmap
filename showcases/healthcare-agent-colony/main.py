"""Healthcare agent colony showcase.

Run:
    python main.py
"""

from __future__ import annotations


REQUESTS = [
    "I have had a headache for three days. What medicine should I take?",
    "Explain what blood pressure numbers mean in simple terms.",
]


def classify_request(text: str) -> str:
    lowered = text.lower()
    if any(term in lowered for term in ["medicine", "diagnose", "symptom", "headache"]):
        return "high_risk"
    return "education"


def respond(text: str) -> dict:
    risk = classify_request(text)
    if risk == "high_risk":
        workflow = [
            "Acknowledge the concern without diagnosing.",
            "Do not recommend medication or treatment.",
            "Encourage professional medical review.",
            "Offer safe preparation questions for a clinician visit.",
        ]
        answer = (
            "I cannot diagnose or recommend medication. Please consult a qualified medical "
            "professional, especially because the symptom has lasted several days. I can help "
            "you prepare questions and organize information for the visit."
        )
    else:
        workflow = [
            "Explain general health education.",
            "Avoid personalized medical instructions.",
            "Mention when to seek professional advice.",
        ]
        answer = (
            "Blood pressure is usually shown as two numbers: systolic over diastolic. "
            "The first number reflects pressure during a heartbeat; the second reflects "
            "pressure between beats. A clinician can interpret the numbers in context."
        )
    return {
        "domain": "healthcare",
        "risk": risk,
        "workflow": workflow,
        "answer": answer,
        "evaluator": "passed: no diagnosis, no prescription, escalation included when needed",
    }


def main() -> None:
    for index, request in enumerate(REQUESTS, start=1):
        result = respond(request)
        print(f"=== Case {index}: Healthcare Agent Colony ===")
        print(f"request: {request}")
        print(f"risk: {result['risk']}")
        print("workflow:")
        for step in result["workflow"]:
            print(f"- {step}")
        print(f"answer: {result['answer']}")
        print(f"evaluator: {result['evaluator']}\n")


if __name__ == "__main__":
    main()
