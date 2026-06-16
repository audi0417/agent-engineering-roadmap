# 13 Agent Observability

## 目標

學會讓 Agent 系統離開 demo 後，仍然能被檢查、debug、回放與監控。

一個可觀測的 Agent，應該能回答：

- Agent 看到了什麼？
- Agent 做了什麼判斷？
- 呼叫了哪個 tool？
- 哪個 guardrail 被觸發？
- 最後答案為什麼會長這樣？
- 這次 run 花了多少成本？

## 為什麼重要？

Chatbot demo 可以只看最後答案來 debug。Production Agent 不行。

當 Agent 有 tool、memory、retrieval、approval gate、handoff 之後，最後答案只是故事的最後一頁。真正的系統，是答案之前那串決策。

沒有 observability，團隊很難 debug：

- tool 選錯
- retrieval context 不足
- approval gate 漏掉
- prompt injection
- retry 過多
- model call 太貴
- handoff 失敗
- policy violation 被藏起來

## 直覺模型

把 agent trace 想成飛航紀錄器。

Trace 不負責開飛機，但它會記錄足夠的證據。出事之後，團隊可以回放：「剛剛到底發生什麼？」

Agent 最小可用 flight recorder 包含：

- `run_id`：一次使用者請求或背景任務
- `span_id`：run 裡面的一個操作
- `event_type`：model decision、tool call、tool result、guardrail、handoff、memory read
- `payload`：debug 需要的結構化資料
- `parent_span_id`：事件之間的父子關係

## 黑盒視角

```text
user request
   ↓
agent run
   ↓
decisions + tool calls + guardrails + handoffs
   ↓
final answer
```

如果只存 final answer，中間全部都是黑盒。

## 機制視角

```text
Run
├── LLM decision span
├── retrieval span
├── tool call span
├── tool result span
├── guardrail span
├── handoff span
└── final response span
```

每個 span 都要回答一件事：

> 這裡發生了什麼？系統根據什麼證據做判斷？

## 應該 Trace 什麼？

先 trace 這些事件：

| Event | 為什麼重要 |
|---|---|
| run start/end | 把同一次 request 的工作串起來 |
| model request/response metadata | Debug model 選擇、latency、token cost |
| tool call/result | 看 Agent 實際做了什麼 |
| retrieval query/result ids | 解釋答案有沒有 grounded |
| guardrail trigger | 解釋拒答、approval、escalation |
| memory read/write | 找出過期或不安全 context |
| handoff | 看責任如何轉移 |
| final answer | 把可見輸出連回隱藏流程 |

## 不應該盲目記錄什麼？

Observability 也可能變成資料外洩。

不要無腦記錄：

- API keys
- access tokens
- 完整醫療紀錄
- 個人金融資料
- private user memory
- 含敏感資訊的原始文件
- tool 回傳的 credentials

Production traces 需要 redaction 與 retention policy。

## 常見錯誤

### 錯誤 1：只看最後答案 debug

團隊只存 user input 和 final answer。

問題：答案錯了，也不知道是 retrieval、policy、tool use 還是 model reasoning 壞掉。

修正：記錄中間事件。

### 錯誤 2：只寫非結構化 log

團隊只記錄一大段文字。

問題：無法用 tool name、run id、risk level、guardrail type 過濾。

修正：使用 structured JSON events。

### 錯誤 3：什麼都存、永遠不刪

團隊把每個 prompt、document、tool result 都永久保存。

問題：observability 變成 security / compliance 風險。

修正：敏感內容遮蔽，並定義 retention window。

## 實作練習

執行：

```bash
python examples/10-observable-agent/main.py
```

然後檢查：

```bash
cat examples/10-observable-agent/trace.jsonl
```

回答：

- 哪個 event 讓 human approval 變成必要？
- 哪個 event 應該放進 incident review？
- 哪個 payload 欄位在真實 production 需要遮蔽？

## Production Checklist

- [ ] 每次 run 都有 `run_id`
- [ ] tool call 與 tool result 分開記錄
- [ ] guardrail trigger 看得到
- [ ] retrieval trace 存 document ids，而不是只存 raw text
- [ ] 敏感欄位會被 redacted
- [ ] trace retention 有政策
- [ ] incident 可以從 trace replay
- [ ] cost、latency、error rate 可以被量測

## 參考

- [OpenAI Agents SDK Tracing](https://openai.github.io/openai-agents-python/tracing/)
- [OpenTelemetry Generative AI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
- [OpenTelemetry MCP Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/mcp/)

