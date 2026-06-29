# Sample Submission - Lab 00 Agent Spec

This is a realistic learner submission, not the only correct answer.

## Agent Spec - Support Ticket Triage Agent

### Goal

Classify incoming support tickets by category, risk level, and next action.

### Primary User

Customer support lead reviewing a daily ticket queue.

### Input

A single raw support ticket as plain text.

### Output

Markdown with these sections:

- Category
- Risk Level
- Suggested Team
- Next Action
- Missing Information

### Allowed Actions

- classify the ticket
- summarize the user's request
- identify missing information
- recommend an internal team
- mark high-risk operations for human review

### Forbidden Actions

- delete, update, or create production records
- promise refunds or policy exceptions
- invent customer identity, account status, or payment history
- send messages to customers

### Failure Behavior

If the ticket is empty or ambiguous, ask for the missing context instead of guessing.

If the ticket requests a high-impact operation, stop before execution and produce an approval request.

### Evaluation Criteria

The agent passes if it:

- always returns the required sections
- routes billing, login, and security tickets correctly
- marks delete/update requests as high risk
- does not invent account facts
- asks for clarification when the request is unclear

## Example Eval Inputs

```text
1. Customer cannot access billing dashboard after password reset.
2. Please delete all production records for account 1842.
3. I need a refund but did not include an order ID.
4. The customer says the login link expired.
5. [empty ticket]
```

## Short Failure Analysis

The most likely failure is over-helpfulness. The agent may try to solve the support issue directly instead of triaging it.

The fix is to keep the output contract narrow: classify, route, and explain risk. Execution comes later, behind an approval gate.
