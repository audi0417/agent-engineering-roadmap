# Benchmarks

這個資料夾提供 Agent Engineering Roadmap 的小型 benchmark layer。

目標不是比較模型，而是檢查範例 Agent 是否保留重要工程行為。

## 執行

```bash
python benchmarks/benchmark_runner.py
```

## 目前檢查項目

| 類別 | Check | 保護什麼 |
|---|---|---|
| Tool use | Calculator result | Tool call correctness |
| RAG | Grounded approval answer | Retrieval 與 answer grounding |
| Workflow | Destructive action gate | 高風險執行前需要 approval |
| Security | Prompt injection blocked | 隔離不可信 retrieved content |
| Observability | Guardrail trace exists | 可 replay 的 production debugging |
| Cost-latency | Model route respects budget | 依成本與延遲 route task |
| Runtime | Checkpoint resume completes | Durable long-running workflows |
| MCP | Read-only token cannot call tools | Capability-scoped authorization |

## 為什麼有幫助？

很多 Agent demo 看起來很酷，但改一點東西就壞。

這個 benchmark 給 contributor 一個快速訊號：

- tool behavior 有沒有壞？
- retrieval grounding 有沒有退化？
- approval gate 還會不會觸發？
- prompt injection defense 還有效嗎？
- trace 是否仍然記錄 guardrail decision？
- cost-aware routing 是否仍選到預期模型？
- durable workflow 是否仍能 resume？
- MCP gateway permissions 是否仍會拒絕不安全存取？

## 新增 Benchmark

新增 production behavior 時，也應該新增 benchmark。

好的 benchmark 應該：

- 不需要 API key
- 一次測一個行為
- 失敗時明確報錯
- 印出有用的 detail line
- 在 GitHub Actions 穩定執行
