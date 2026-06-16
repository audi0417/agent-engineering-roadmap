# 15 Agent Cost And Latency Engineering

## 目標

學會讓 Agent 系統在 production 中夠快、夠便宜，同時仍然可靠。

## 為什麼重要？

Demo 裡跑得動的 Agent，如果太慢或太貴，仍然不能成為產品。

成本與延遲不只是 infra 問題，它們會影響 Agent 設計：

- 哪個任務用哪個模型
- retrieval 要拿多少 context
- 什麼時候 call tool
- 什麼時候 cache
- 什麼時候 fallback
- 什麼時候該問使用者，而不是繼續花 token

## 直覺模型

把每次 agent run 想成有預算的路線選擇。

```text
task
   ↓
估算 difficulty + token size + risk
   ↓
選擇 model + retrieval budget + tool timeout
   ↓
run
   ↓
量測 cost, latency, quality
```

最好的 route 不一定是最強模型，而是能滿足品質與安全需求的最便宜 route。

## 核心機制

| 機制 | 用途 |
|---|---|
| Model routing | 簡單任務用小模型，高風險任務用強模型 |
| Token budgeting | 限制 context 與 output size |
| Retrieval budgeting | 拿足夠證據，但不要淹沒 context |
| Tool timeout | 避免單一慢工具卡住 workflow |
| Caching | 重用穩定結果 |
| Fallback | model 或 tool 失敗時恢復 |
| Cost telemetry | 追蹤每次 run、user、workflow、feature 的成本 |

## 常見錯誤

### 永遠用最強模型

品質可能只提升一點，但成本和 latency 會爆炸。

### 永遠用最便宜模型

Agent 變快了，但複雜或高風險任務會不可靠。

### Retrieve Everything

模型拿到太多 context，答案變吵，token cost 也上升。

### 沒有 Timeout

一個慢 tool 就能卡住整個 workflow。

## 實作練習

執行：

```bash
python examples/12-cost-aware-agent/main.py
```

然後修改 task 和 budget：

- 讓 task 變成 high-risk
- 降低 `max_cost`
- 降低 `max_latency_ms`
- 觀察 routing 如何改變

## Production Checklist

- [ ] 每個 workflow 有 latency target
- [ ] 每個 workflow 有 cost budget
- [ ] model choice 是明確的
- [ ] retrieval limit 是明確的
- [ ] tool timeout 是明確的
- [ ] fallback behavior 有被測試
- [ ] 每次 run 都 trace cost 和 latency
- [ ] high-risk tasks 可以在合理情況下使用更多 budget

