# Safety Review

## Domain Boundary

This starter does not perform real medical, finance, or destructive enterprise actions.

## High-Risk Actions

Require human approval for:

- medical symptoms or treatment requests
- personalized investment instructions
- destructive data operations
- messages that could affect legal, financial, or health outcomes

## Refusal Cases

Refuse or redirect when:

- user asks for diagnosis or medication
- user asks for personalized buy/sell decision
- user asks to delete or modify production data without approval
- requested action lacks required context

## Logging

Log:

- user task
- domain route
- risk level
- approval decision
- reviewer result

## Release Gate

Do not ship if:

- eval pass rate is below 100% for critical safety cases
- any high-risk action executes without approval
- output hides missing information
