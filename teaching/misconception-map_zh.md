# Agent Engineering Misconception Map

這份文件專門整理學生最容易誤解的地方。

好，為什麼要有這個？因為 Agent Engineering 最危險的地方不是完全不懂。完全不懂的人會慢慢學。最危險的是懂一半，然後很有自信地把系統推到 production。你沒有看錯，這種事情真的很常發生。

## Foundations

### 誤解：Agent 就是比較長的 chatbot prompt

為什麼錯：

Chatbot 主要是回應。Agent 是任務系統。它要管理 context、tools、memory、workflow、evaluation 和 safety。

正確理解：

Agent 不是一句 prompt。Agent 是一個 loop。

如何測：

要求學生畫出 input、state、tool、observation、output。畫不出來，就還只是 prompt。

## Tool Calling

### 誤解：把 function schema 給 model 就等於安全

為什麼錯：

Schema 只能限制參數形狀，不能判斷行動風險。比如 `delete_user(id)` schema 很漂亮，但刪錯人還是很慘。

正確理解：

Tool use 需要 validation、risk classification、approval、logging。

如何測：

加入一個 high-risk request，確認 agent 不會直接執行。

## MCP

### 誤解：MCP 的重點是 protocol 名字

為什麼錯：

Protocol 當然重要，但教學上第一個要懂的是 boundary。Agent 不應該到處 import tool code。

正確理解：

MCP-style separation 其實就是 client/server boundary。Agent reason，server own tools。

如何測：

要求學生替同一個 tool 寫 direct-call version 和 MCP-style version，說出差異。

## Memory

### 誤解：Memory 就是 vector database

為什麼錯：

Vector database 只是 retrieval infrastructure。Memory 真正困難的是 policy。

正確理解：

Memory 先問能不能存、該不該存、誰能看、何時刪，再問用哪個資料庫。

如何測：

給一段含敏感資訊的 input，確認 memory policy 會拒存。

## RAG

### 誤解：RAG 會讓答案自動變正確

為什麼錯：

RAG 只是把資料拿進 context。拿錯資料，答案還是錯。拿對資料，模型也可能亂講。

正確理解：

RAG 要分開測 retrieval quality 和 answer faithfulness。

如何測：

使用 `examples/08-mini-rag`，加入一題 no-answer case，確認答案不會硬掰。

## Workflow

### 誤解：讓 model 自己決定下一步最聰明

為什麼錯：

完全自由的 agent 很難 debug。出錯時你不知道是 planning 錯、tool 錯、memory 錯，還是 review 沒擋。

正確理解：

Workflow 是把自由度收斂成可觀測步驟。

如何測：

要求每個 step 都產生 artifact，並讓 reviewer 只看 artifact 做判斷。

## Multi-Agent

### 誤解：Agent 越多越聰明

為什麼錯：

很多 agent 如果沒有分工和交接規則，只是很多聲音同時出現而已。蠻熱鬧，但不一定有用。

正確理解：

Multi-agent 的重點是 role boundary、routing、artifact contract、conflict resolution。

如何測：

把其中一個 specialist 關掉，看 supervisor 能不能 graceful fallback。

## Human-in-the-loop

### 誤解：Human approval 會讓 agent 不自動，所以不好

為什麼錯：

高風險任務不該追求完全自動。能停下來問人，是能力，不是缺陷。

正確理解：

Human-in-the-loop 是 risk control layer。

如何測：

設計一個 high-impact action，確認系統產生 approval request 而不是直接執行。

## Evaluation

### 誤解：Eval 就是看答案順不順

為什麼錯：

順不代表對。更不代表安全。LLM 最會寫看起來合理的錯答案。

正確理解：

Eval 要分 correctness、format、safety、retrieval、tool behavior、memory behavior。

如何測：

每次修 prompt 或改 tool，都新增 regression case。

## Production

### 誤解：Demo 跑得動，就可以上線

為什麼錯：

Demo 只證明 happy path。Production 要處理錯誤、攻擊、成本、資料外洩、rollback。

正確理解：

Production readiness 其實就是「出事時你知道怎麼辦」。

如何測：

要求學生回答：哪裡會壞、怎麼知道、誰處理、怎麼回復。

## Recap

好，這張 misconception map 的重點很簡單。

每個 agent concept 都有一個聽起來很合理、但其實不夠完整的版本。

教學要做的事情，就是把這些「懂一半」的直覺拆掉，重新組成可測、可控、可上線的工程判斷。
