# Paper Notes 論文導讀

這裡放短版工程導讀。內容刻意精簡，而且是原創整理；完整細節請讀官方論文。

## ReAct

- Link: https://arxiv.org/abs/2210.03629
- PDF: https://arxiv.org/pdf/2210.03629
- Organizations: Google Research, Princeton
- Related modules: 01, 02, 05, 06
- Related examples: `examples/02-tool-using-agent`, `examples/09-graph-approval-agent`

一句話：ReAct 讓 agent 交錯進行 reasoning 與 action，先想、呼叫工具、觀察結果，再更新下一步。

工程啟發：tool-using agent 不應該是一個巨大 prompt，而是一個明確 loop：reason、act、observe、update。

限制：reasoning trace 有助 debug，但不能取代 tool validation、trace 或 eval。

練習：新增一個 eval case，讓工具結果推翻原本計畫，agent 必須修正下一步。

## Toolformer

- Link: https://arxiv.org/abs/2302.04761
- PDF: https://arxiv.org/pdf/2302.04761
- Organization: Meta AI
- Related modules: 02, 03, 15
- Related examples: `examples/02-tool-using-agent`, `examples/12-cost-aware-agent`

一句話：Toolformer 研究模型如何學會何時呼叫工具，以及如何把工具結果整合回回答。

工程啟發：tool call 需要 schema、呼叫時機、結果整合與成本控制。

限制：paper 裡學會呼叫 API，不等於 production 環境中安全地呼叫工具。

練習：加入 bad-tool-choice eval，測試 agent 是否能避免不必要的高成本工具。

## WebGPT

- Link: https://arxiv.org/abs/2112.09332
- PDF: https://cdn.openai.com/WebGPT.pdf
- Organization: OpenAI
- Related modules: 00, 02, 04, 08, 13
- Related examples: `examples/08-mini-rag`, `examples/10-observable-agent`

一句話：WebGPT 訓練模型瀏覽網頁、收集引用，並用 human feedback 改善長答案。

工程啟發：grounded answer 需要 evidence collection，而不是只靠流暢文字。

限制：瀏覽能幫助 factuality，但 source selection 與 citation quality 仍然需要評估。

練習：替 RAG 或 browsing-style agent 加上 citation-quality check。

## RAG

- Link: https://arxiv.org/abs/2005.11401
- PDF: https://arxiv.org/pdf/2005.11401
- Organizations: Meta AI, UCL, NYU, FAIR
- Related modules: 04, 09, 22
- Related examples: `examples/08-mini-rag`

一句話：RAG 把模型內部知識與外部檢索記憶結合。

工程啟發：retrieval 不是 chatbot 的附加功能，而是一個需要 indexing、ranking、grounding、no-answer behavior 的系統元件。

限制：檢索變好不代表生成一定 faithful。

練習：加入 irrelevant retrieval、missing answer、conflicting sources 的 eval cases。

## Lost in the Middle

- Link: https://arxiv.org/abs/2307.03172
- PDF: https://arxiv.org/pdf/2307.03172
- Organizations: Stanford, UC Berkeley, Samaya AI
- Related modules: 03, 04, 18
- Related examples: `examples/08-mini-rag`, `examples/15-memory-governance-agent`

一句話：長 context 模型在相關資訊位於中段時，可能無法穩定使用該資訊。

工程啟發：巨大 context window 不等於 memory system；retrieval order、compression、evaluation 都很重要。

限制：不同模型與任務的失敗模式不同，所以團隊需要自己的 eval。

練習：做一個相關記憶被夾在無關 chunks 中間的測試。

## Generative Agents

- Link: https://arxiv.org/abs/2304.03442
- PDF: https://arxiv.org/pdf/2304.03442
- Organizations: Stanford, Google
- Related modules: 03, 07, 18
- Related examples: `examples/04-memory-agent`, `examples/06-agent-colony`

一句話：Generative Agents 展示由 observation、memory、reflection、planning 組成的 believable agents。

工程啟發：agent memory 應該有 retrieval 與 reflection policy，而不是只存 raw chat history。

限制：believable simulation 不等於可靠的 production automation。

練習：在 memory example 裡加入 reflection step，把重複觀察摘要後再存長期記憶。

## Reflexion

- Link: https://arxiv.org/abs/2303.11366
- PDF: https://arxiv.org/pdf/2303.11366
- Organizations: Princeton, Northeastern
- Related modules: 03, 05, 16, 18
- Related examples: `examples/05-multi-agent-workflow`, `examples/13-durable-workflow-agent`

一句話：Reflexion 透過把 verbal feedback 存進 episodic memory，改善 agent 下一次表現。

工程啟發：feedback 只有在具體、已驗證、安全時，才應該變成 reusable memory。

限制：錯誤 reflection 會把錯誤傳遞到後續任務。

練習：替 evaluator feedback 加 memory governance rule。

## Self-Refine

- Link: https://arxiv.org/abs/2303.17651
- PDF: https://arxiv.org/pdf/2303.17651
- Organizations: Allen AI, CMU, University of Washington, others
- Related modules: 05, 07, 22
- Related examples: `examples/05-multi-agent-workflow`, `examples/17-advanced-eval-harness`

一句話：Self-Refine 用 generate、feedback、refine loop 讓輸出在不額外訓練下改進。

工程啟發：reviewer agent 應該有明確 review criteria 與 stop condition。

限制：self-feedback 可能強化模型自己的盲點。

練習：要求 reviewer 說明是哪一條 rubric 觸發 revision。

## Tree of Thoughts

- Link: https://arxiv.org/abs/2305.10601
- PDF: https://arxiv.org/pdf/2305.10601
- Organizations: Princeton, Google DeepMind
- Related modules: 05, 06, 07
- Related examples: `examples/09-graph-approval-agent`

一句話：Tree of Thoughts 把解題視為多條 reasoning path 的搜尋。

工程啟發：困難 planning task 適合明確 branching、scoring、backtracking。

限制：search 很花成本，簡單任務不一定需要。

練習：替 graph agent 加入兩個 plan 分支，先評分再執行。

## Voyager

- Link: https://arxiv.org/abs/2305.16291
- PDF: https://arxiv.org/pdf/2305.16291
- Organizations: NVIDIA, Caltech, UT Austin, Stanford, ASU
- Related modules: 06, 07, 16, 18
- Related examples: `examples/06-agent-colony`, `examples/13-durable-workflow-agent`

一句話：Voyager 用 automatic curriculum、executable skill library、environment feedback、self-verification 做 open-ended learning。

工程啟發：skill 如果是 executable、reusable、tested，才會真正變成 agent 能累積的能力。

限制：遊戲環境和企業系統不同；企業系統還要處理 permission 與 safety。

練習：替 colony example 加一個小型 skill library 並測試 skill reuse。

## AgentBench

- Link: https://arxiv.org/abs/2308.03688
- PDF: https://arxiv.org/pdf/2308.03688
- Organizations: Tsinghua, Ohio State, UC Berkeley
- Related modules: 09, 22
- Related examples: `examples/17-advanced-eval-harness`, `benchmarks/benchmark_runner.py`

一句話：AgentBench 在互動環境中評估 LLM-as-agent。

工程啟發：agent eval 需要包含 action、state、多輪錯誤與 recovery。

限制：benchmark 是信號，不是 production domain eval 的替代品。

練習：新增一個測試 agent 在中間步驟錯誤後能否 recovery 的 benchmark。

## AutoGen

- Link: https://arxiv.org/abs/2308.08155
- PDF: https://arxiv.org/pdf/2308.08155
- Organization: Microsoft Research
- Related modules: 07, 08, 12, 25
- Related examples: `examples/05-multi-agent-workflow`, `examples/06-agent-colony`

一句話：AutoGen 把 LLM app 視為多個 customizable agents 之間的 conversation，並可結合 model、tool、human。

工程啟發：multi-agent system 需要明確 conversation pattern、role boundary、human/tool integration rules。

限制：conversation-based orchestration 如果沒有 trace、turn limit、eval，會很難 debug。

練習：把 multi-agent workflow example 改寫成 supervisor、worker、human proxy 的 conversation protocol。

## RAGAS

- Link: https://arxiv.org/abs/2309.15217
- PDF: https://arxiv.org/pdf/2309.15217
- Organizations: Exploding Gradients, CardiffNLP
- Related modules: 04, 22
- Related examples: `examples/08-mini-rag`, `examples/17-advanced-eval-harness`

一句話：RAGAS 為 RAG pipeline 提供自動化評估維度。

工程啟發：RAG eval 要拆開 retrieval quality、grounding、answer quality。

限制：自動化指標仍然要和真實使用者需求校準。

練習：把 RAG eval 拆成 retrieval pass、grounding pass、answer pass。

## SWE-agent

- Link: https://arxiv.org/abs/2405.15793
- PDF: https://arxiv.org/pdf/2405.15793
- Organization: Princeton
- Related modules: 09, 13, 16, 25
- Related examples: `examples/10-observable-agent`, `examples/13-durable-workflow-agent`

一句話：SWE-agent 說明 agent-computer interface 會大幅影響 software engineering agent 表現。

工程啟發：interface 是 agent system 的一部分；檔案編輯、導覽、測試、錯誤回饋都要為 agent 設計。

限制：coding-agent 結果不會自動轉移到所有企業 workflow。

練習：加入記錄 file operation、test command、failure、retry 的 trace format。

## Prompt Injection

- Link: https://arxiv.org/abs/2306.05499
- PDF: https://arxiv.org/pdf/2306.05499
- Organizations: NTU, Zhejiang University, others
- Related modules: 03, 14, 21
- Related examples: `examples/11-prompt-injection-defense`

一句話：Prompt injection 利用 LLM 很難區分 instruction 與 untrusted data 的弱點。

工程啟發：retrieved docs、tool results、web pages、user files 都要視為 untrusted input。

限制：filter 不夠；還需要 permission、least privilege、logging、eval。

練習：替每個 RAG 或 MCP example 加 indirect prompt injection cases。

## Constitutional AI

- Link: https://arxiv.org/abs/2212.08073
- PDF: https://arxiv.org/pdf/2212.08073
- Organization: Anthropic
- Related modules: 08, 14, 22
- Related examples: `examples/11-prompt-injection-defense`, `examples/17-advanced-eval-harness`

一句話：Constitutional AI 用 principles、critique、revision、AI feedback 訓練 helpful and harmless behavior。

工程啟發：safety policy 要明確到可以 review、test、revise。

限制：principle list 不是完整 operational safety system。

練習：把 safety policy 轉成 eval cases 與 refusal tests。

## Sleeper Agents

- Link: https://arxiv.org/abs/2401.05566
- PDF: https://arxiv.org/pdf/2401.05566
- Organization: Anthropic and collaborators
- Related modules: 14, 21, 22
- Related examples: `examples/11-prompt-injection-defense`, `examples/17-advanced-eval-harness`

一句話：Sleeper Agents 研究 hidden deceptive behavior 如何在標準 safety training 後仍然保留。

工程啟發：safety testing 應該包含 hidden trigger、distribution shift、adversarial release gate。

限制：paper 使用 proof-of-concept 設定，production risk 仍要看 domain context。

練習：把 hidden-trigger adversarial eval cases 加進 advanced eval harness。
