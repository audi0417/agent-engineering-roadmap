# Lab Solution Guides

這個資料夾放的是 lab 的解題方向，不是唯一答案。

好，為什麼不要直接給完整答案？因為 Agent Engineering 很多題目沒有唯一解。你做 healthcare agent 和 finance agent，答案當然不一樣。

但完全不給方向也不行。學生會卡在空白頁前面。那怎麼辦呢？

這裡提供的是「解題骨架」：

```text
你應該產出什麼
你應該檢查什麼
常見錯誤是什麼
怎樣算通過
```

## Lab Solution Index

| Lab | Expected Artifact | Key Check |
|---|---|---|
| 00 Agent Spec | `agent_spec.md` | Goal 是否窄、output 是否可驗證 |
| 01 Single Agent | config + eval inputs | Agent 是否拒絕超出範圍任務 |
| 02 Tool Calling | tool policy + wrapper | Unknown tool / unsafe args 是否被拒絕 |
| 03 Memory | memory policy + tests | Sensitive data 是否不會寫入 |
| 04 RAG | KB + eval cases | No-answer case 是否不 hallucinate |
| 05 Workflow | workflow states + retry | Review fail 是否有路徑 |
| 06 Graph Agent | state diagram | 每個 transition 是否有條件 |
| 07 Multi-Agent | routing table | Supervisor 是否能解釋 routing |
| 08 Human Approval | approval spec | High-risk action 是否需要 approval |
| 09 Evaluation | regression suite | 分數下降是否能 block release |
| 10 Capstone Prep | project proposal | Scope 是否能在 2-4 週完成 |

## Example: Lab 04 RAG Solution Shape

```text
knowledge_base.json
  - 5-10 documents

eval_cases.json
  - 3 direct lookup
  - 3 synthesis
  - 2 no-answer
  - 2 adversarial

failure_analysis.md
  - retrieval failure examples
  - answer faithfulness failure examples
```

通過標準：

- retrieved document IDs are visible
- no-answer questions do not produce unsupported answers
- answer quality is judged separately from retrieval quality

## Example: Lab 08 Human Approval Solution Shape

```text
approval_policy.md
  - low-risk actions
  - medium-risk actions
  - high-risk actions
  - refusal cases

approval_request_schema.json
  - action
  - arguments
  - reason
  - risk_level
  - expected_effect
  - rollback_plan
```

通過標準：

- high-impact actions pause before execution
- approval request is auditable
- refusal is explicit when action should never be performed

## Recap

Lab solution 不是標準答案。

它是 guardrail。

學生可以有自己的設計，但不能跳過 scope、safety、evaluation 和 artifact。
