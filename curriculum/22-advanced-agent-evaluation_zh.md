# 22 Advanced Agent Evaluation

## 目標

學會建立能 block unsafe 或 low-quality agent release 的 evaluation system。

## 為什麼重要？

簡單 eval 只檢查答案看起來對不對。Production eval 要檢查系統行為是否正確。

Advanced agent evaluation 應該檢查：

- final answer
- tool calls
- retrieval evidence
- guardrail decisions
- approval path
- memory writes
- trace shape
- adversarial behavior

## 直覺模型

```text
eval case
   ↓
agent run
   ↓
answer checks + trace checks + safety checks
   ↓
release gate
```

## Eval Types

| Type | 用途 |
|---|---|
| Regression | 防止已知行為壞掉 |
| Safety | 檢查 refusal、approval、escalation |
| Adversarial | 攻擊 prompt injection 與 policy bypass |
| Golden trace | 檢查 path，而不只檢查 answer |
| Incident replay | 防止修過的 incident 回來 |

## 建議研究的框架

跑完本 repo 的免依賴 examples 之後，建議讀 [DeepEval and RAGAS](../resources/eval-frameworks-deepeval-ragas.md)。

DeepEval 適合用在 pytest-style LLM app tests、custom metrics、safety checks、regression suites 與 CI release gates。

RAGAS 適合用在 RAG evaluation，把 retrieval、grounding、faithfulness、answer relevance 拆開看。

重點是：不要把所有 evaluation 壓成一個分數。Agent evaluation 應該拆開看 answer quality、retrieval quality、trace shape、safety behavior 與 release risk。

## 實作練習

執行：

```bash
python examples/17-advanced-eval-harness/main.py
```

## Production Checklist

- [ ] 每次 release 都跑 regression evals
- [ ] Adversarial cases 會 block release
- [ ] Golden traces 檢查 critical paths
- [ ] Incidents 會變成 eval cases
- [ ] Eval failures 會提供有用 details
- [ ] Benchmarks 在 CI 執行
