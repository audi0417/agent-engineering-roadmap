# Module Teaching Blueprint

每個 module 都應該照這個節奏寫。

你可能會想說：「每章格式都一樣，會不會很無聊？」

不會。格式一致不是為了無聊，是為了讓學生不用每章重新猜規則。認知負擔省下來，就可以拿去理解 agent system。

## Standard Flow

```text
1. 開場問題
2. 一句話直覺
3. Black-box view
4. Naive system failure
5. Mechanism
6. Runnable example
7. Common mistakes
8. Eval or safety check
9. Student deliverable
10. Recap
```

## 1. 開場問題

每章先回答：

```text
如果沒有這個東西，agent 會在哪裡壞掉？
```

比如 Tool Calling：

```text
假設使用者問「幫我算 128 * 42 / 7」。
LLM 可以猜，但它不應該猜。
它應該呼叫 calculator。
那問題來了，怎麼安全地呼叫？
```

## 2. 一句話直覺

用一句話抓核心。

| Module | 一句話直覺 |
|---|---|
| 00 Foundations | Agent 其實就是會根據目標反覆觀察、決策、行動的任務系統 |
| 01 Architecture | Architecture 其實就是先決定邊界，再寫程式 |
| 02 Tool Calling | Tool use 其實就是讓 model 不要用猜的，而是去查或去做 |
| 03 Memory | Memory 其實就是決定什麼值得留下來、什麼不該留下來 |
| 04 RAG | RAG 其實就是考試可以翻書，但只能根據書回答 |
| 05 Workflow | Workflow 其實就是不要讓 model 自由奔跑，而是讓它走流程 |
| 06 Graph Agent | Graph 其實就是把流程畫成 state 和 transition |
| 07 Multi-Agent | Multi-agent 其實就是分工，但分工要有交接規則 |
| 08 Human-in-the-loop | Human approval 其實就是把高風險決策交回人類 |
| 09 Production | Production 其實就是出事時你知道哪裡壞、怎麼退 |
| 10 Healthcare | Healthcare agent 其實就是教育和整理資訊，不是診斷 |
| 11 Finance | Finance agent 其實就是研究支援，不是投資指令 |
| 12 Frameworks | Framework 其實就是幫你管理複雜度，不是替你想清楚問題 |

## 3. Black-box View

每章都要寫：

```text
Input:
Output:
Objective:
Failure if missing:
```

比如 Memory：

```text
Input: current user request
Output: answer grounded in current request plus relevant memory
Objective: use useful remembered context without leaking or overusing stale data
Failure if missing: user repeats preferences forever, or agent stores unsafe data
```

## 4. Naive System Failure

先讓錯誤做法撞牆。

比如 Multi-Agent：

```text
錯誤做法：開 5 個 agent，叫它們一起討論。
結果：每個 agent 都講很多，但沒有人負責整合，也沒有人負責驗收。
```

然後問：

```text
怎麼辦呢？
```

這時候才引入 supervisor、routing、artifact contract。

## 5. Mechanism

每章機制只講 3-5 個核心元件。

不要一次塞 20 個名詞。

比如 RAG：

```text
Documents
Chunks
Retriever
Context builder
Grounded answer
Evaluator
```

講完一個元件，就立刻給例子。

## 6. Runnable Example

每章至少要有其中一個：

- runnable example
- showcase
- template filled sample
- lab output sample

如果目前還沒有 runnable example，就要明確說學生要修改哪個 existing example。

## 7. Common Mistakes

每章至少列 3 個常見誤解。

格式：

```text
誤解：
為什麼錯：
正確理解：
如何測：
```

## 8. Eval Or Safety Check

每章都要有一個可測條件。

比如：

| Module | Minimum Check |
|---|---|
| Tool Calling | unknown tool must be rejected |
| Memory | sensitive data must not be stored |
| RAG | no-answer question must not be hallucinated |
| Workflow | failed review must trigger retry or fallback |
| Human Approval | high-risk tool call must pause for approval |

## 9. Student Deliverable

每章最後要交一個 artifact。

比如：

```text
Module 04 deliverable:
- knowledge_base.json
- eval_cases.json
- retrieval report
- one no-answer failure analysis
```

## 10. Recap

最後用三句話收斂。

範例：

```text
好，講到這邊我們知道了。
RAG 不是讓答案自動變真。
RAG 是讓答案有機會根據外部證據。
但你還是要分開測 retrieval 和 answer。
```

## Module Quality Checklist

- [ ] 開場先講問題，不是先丟名詞
- [ ] 有一句話直覺
- [ ] 有 black-box view
- [ ] 有 naive failure
- [ ] 有 mechanism
- [ ] 有 concrete example
- [ ] 有 runnable path
- [ ] 有 common mistakes
- [ ] 有 eval / safety check
- [ ] 有 student deliverable
