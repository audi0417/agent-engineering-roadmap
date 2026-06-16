# Lab 10 Solution Shape - Capstone Prep

## Expected Artifacts

```text
capstone_proposal.md
architecture.md
safety_review.md
eval_plan.md
milestone_plan.md
```

## Capstone Proposal Template

```markdown
# Capstone Proposal

## Domain
Enterprise support workflow.

## User Problem
Support tickets need routing, risk classification, and approval handling.

## Agent Roles
- Supervisor
- Support specialist
- Reviewer

## Tools
- ticket classifier
- mock account lookup

## Memory
Store only stable account workflow preferences. Do not store secrets.

## Safety Boundary
Read-only support is allowed. Destructive operations require approval.

## Evaluation
15 cases: happy path, missing context, unsafe action, tool use, approval path.
```

## Passing Standard

- Scope can be completed in 2-4 weeks.
- At least one tool is defined.
- At least one safety boundary exists.
- Eval plan includes negative cases.
- Capstone can start from `capstone-starter/`.
