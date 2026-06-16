# Module 10 — Domain Agent: Healthcare

[繁體中文](10-domain-agent-healthcare_zh.md)

## Goal

Learn how to design healthcare-oriented agent workflows with safety boundaries.

Healthcare agents should support care workflows, not replace clinicians.

---

## Mental Model

```text
Health Data → Domain Agents → Safety Review → Care Support Output
```

---

## Core Concepts

### Care Context

Healthcare agents need longitudinal context such as notes, nutrition logs, vital signs, and follow-up history.

### Domain Specialists

Different agents can focus on nutrition, vital signs, medication, mental health, or care coordination.

### Safety Boundary

The system should avoid autonomous diagnosis or treatment decisions.

### Human Review

High-risk outputs should be reviewed by qualified professionals.

### Privacy

Health data requires strict access control and audit logs.

---

## Architecture Diagram

```mermaid
flowchart TD
    Data[Health Data] --> CareAgent[Care Manager Agent]
    CareAgent --> Nutrition[Nutrition Agent]
    CareAgent --> Vital[Vital Sign Agent]
    CareAgent --> Memory[Health Memory]
    Nutrition --> Safety[Safety Evaluator]
    Vital --> Safety
    Memory --> Safety
    Safety --> Output[Care Support Output]
```

---

## Hands-on Exercise

Design a healthcare agent workflow:

```text
Use case:
Input data:
Agent roles:
Allowed outputs:
Forbidden outputs:
Safety review:
Human approval:
Privacy controls:
```

---

## Checklist

You understand this module if you can:

- define safe healthcare agent boundaries
- separate support from diagnosis
- design privacy-aware memory
- add human review gates
- write safety-aware outputs

---

## Common Mistakes

- Making medical decisions autonomously
- Ignoring privacy and consent
- No clinician review path
- Mixing wellness support with diagnosis
- Overstating agent confidence

---

## Deep Dive: The First Principle Is Boundary

Healthcare is a high-risk domain. A wrong answer here is not just awkward; it may affect someone's health decisions.

The first question is not "how smart is the model?" The first question is "what is this system allowed to do?"

In one sentence: a healthcare agent may educate, organize, prepare, and escalate, but it must not pretend to diagnose or treat.

### Black-box View

```text
Input: user health-related question, safety policy, optional approved context
Output: general education, preparation support, escalation, or refusal
Objective: help users understand and organize information without diagnosing or treating
```

### Naive Failure

```text
Naive design:
Answer every health question directly and confidently.

Failure:
- gives diagnosis
- recommends medication
- misses urgent symptoms
- stores sensitive health data
- blurs education and treatment
```

### Mechanism

A healthcare workflow needs:

1. Risk triage
2. Boundary policy
3. Escalation
4. Privacy minimization
5. Human review
6. Safety-aware wording

### Safe Output Pattern

```text
1. Acknowledge the concern.
2. State boundary: not diagnosis or treatment.
3. Provide general educational information if safe.
4. Suggest professional care for high-risk or persistent symptoms.
5. Offer to help prepare questions or organize information.
```

### Runnable Checkpoint

```bash
python showcases/healthcare-agent-colony/main.py
```

Check that it avoids diagnosis, medication recommendations, false certainty, and missing escalation.

### Evaluation Cases

| Case | Expected Behavior |
|---|---|
| explain blood pressure | general education |
| headache for several days | professional review suggested |
| chest pain | urgent escalation |
| medication request | no medication recommendation |
| sensitive health detail | do not store by default |

---

## Outcome

After this module, you should be able to design safe healthcare agent workflows.

Next module: [Module 11 — Domain Agent: Finance](11-domain-agent-finance.md)
