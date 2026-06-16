# Student Deliverables

這份文件定義每個 module 學生要交什麼。

一言以蔽之：學完 Agent Engineering，不應該只留下筆記。應該留下一個可以放進 portfolio 的 artifact。

## Deliverable Matrix

| Module | Topic | Student Deliverable | Verification |
|---|---|---|---|
| 00 | Foundations | `agent_spec.md` | Scope 是否明確、output 是否可測 |
| 01 | Agent Architecture | Modified Example 01 config + 5 eval inputs | Agent 是否保持窄任務 |
| 02 | Tool Calling | `tool_policy.json` + validation wrapper | Unknown/high-risk tools 是否被擋 |
| 03 | Memory | `memory_policy.md` + memory test cases | Sensitive data 是否拒存 |
| 04 | RAG | `knowledge_base.json` + `eval_cases.json` | Retrieval 和 answer 是否分開測 |
| 05 | Workflow | workflow diagram + retry policy | Review fail 是否會 retry/fallback |
| 06 | Graph Agent | state machine spec | 每個 edge 是否有條件 |
| 07 | Multi-Agent | supervisor routing table | Specialist conflict 是否可處理 |
| 08 | Human-in-the-loop | approval gate spec | High-risk action 是否暫停 |
| 09 | Production | release checklist + regression suite | 低於 threshold 是否 block release |
| 10 | Healthcare | domain safety policy | 不診斷、不開藥、有 escalation |
| 11 | Finance | research boundary policy | 不給個人化買賣建議 |
| 12 | Frameworks | framework decision memo | 選型是否根據需求，不是流行 |
| Capstone | Agent Colony | runnable project + eval report | `run_eval.py` 全過 |

## Minimum Portfolio Standard

學生最後至少要有：

- 1 個 single-agent example
- 1 個 tool-using example
- 1 個 memory or RAG example
- 1 個 workflow or multi-agent example
- 1 個 eval suite
- 1 份 safety review

這樣才不是「我讀過 agent」，而是「我做過 agent system」。

## Review Questions For Every Deliverable

每個 artifact 都要回答：

```text
這個系統解決什麼問題？
它不做什麼？
輸入是什麼？
輸出是什麼？
哪裡會壞？
怎麼測？
什麼情況要交給人？
```

## Submission Format

建議學生每章交一個資料夾：

```text
submissions/module-04-rag/
  README.md
  knowledge_base.json
  eval_cases.json
  run_eval.py
  failure_analysis.md
```

## Recap

好，講到這邊我們知道了。

如果一章沒有 deliverable，學生很容易以為自己懂了。

但 agent system 是工程。工程要有 artifact，要能跑，要能測，要能被別人 review。

這就是 deliverables 的目的。
