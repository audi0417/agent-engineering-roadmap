# 21 Agent Incident Response

## 目標

學會在 production agent 做出錯誤、不安全或非預期行為時如何應對。

## 為什麼重要？

Agent incident 和一般 application bug 不一樣。

失敗來源可能是：

- model decision
- retrieved context
- tool result
- memory write
- permission scope
- missing approval gate
- prompt injection
- broken handoff

Incident response 必須 trace-driven，而不是靠猜。

## 直覺模型

```text
detect
   ↓
contain
   ↓
inspect trace
   ↓
disable risky capability
   ↓
ship hotfix + eval
   ↓
write postmortem
```

## 常見錯誤

### 沒有 Kill Switch

團隊無法快速停用危險 tool 或 agent。

### 沒有 Trace

看得到 final answer，但看不到 decision path。

### 沒有 Hotfix Eval

團隊修了一個 incident，卻弄壞另一個 workflow。

### 沒有 Owner

沒人知道誰可以 approve containment。

## 實作練習

使用：

```text
incident-response/agent-incident-playbook.md
```

再用下面指令 replay incident：

```bash
python examples/10-observable-agent/main.py
python benchmarks/benchmark_runner.py
```

## Production Checklist

- [ ] 每個 Agent 都有 owner
- [ ] High-risk tools 有 kill switch
- [ ] Recent runs 有 traces
- [ ] Security events 可以搜尋
- [ ] Hotfixes 需要 eval updates
- [ ] Postmortems 包含 trace evidence
- [ ] Memory 和 permission changes 會被 review

