# 範例 12：Cost-Aware Agent

這個範例示範如何依照成本與延遲限制做 model routing。

## 執行

```bash
python examples/12-cost-aware-agent/main.py
```

## 展示重點

- 估算任務大小
- 判斷需要的品質等級
- 選擇符合限制的最便宜模型
- 無法同時滿足限制時使用 fallback route
- 評估 routing decisions

## 學習檢查

- 哪些任務需要更強模型？
- 哪些任務適合便宜模型？
- 沒有模型同時滿足成本與延遲時，系統應該怎麼做？

