# 範例 17：Advanced Eval Harness

這個範例示範 release-oriented agent evaluation。

## 執行

```bash
python examples/17-advanced-eval-harness/main.py
```

## 展示重點

- regression cases
- safety cases
- adversarial cases
- golden trace checks
- release gate pass/fail
- 依 case type 拆解分數

## 學習檢查

- 哪些 cases 應該 block release？
- 哪些 trace steps 可以證明 guardrail 有觸發？
- 每次 incident 後應該新增什麼 eval？

