# Hung-Yi Lee Style Teaching Audit

## 一言以蔽之

這個 repo 現在已經不是空的教材。它有 roadmap、curriculum、examples、labs、showcases、templates、eval 和 GitHub Pages。

但是如果用「一門會讓學生真的學會」的標準來看，還有三個缺口：

```text
概念有了，但每章的教學節奏不夠一致。
範例有了，但每章的交付成果不夠明確。
評量有了，但錯誤觀念與反例還不夠集中。
```

白話文就是：材料很多，但老師上課的手勢還要更清楚。

## Audit 기준

這份 audit 用五個問題檢查每個 module：

1. 有沒有先講「沒有這個東西會怎麼壞」？
2. 有沒有一個不用術語也能懂的 intuition？
3. 有沒有 black-box view：輸入、輸出、目標？
4. 有沒有 runnable example 或明確 lab？
5. 有沒有 misconception、eval、交付成果？

你可能會想說：「每章都有 README 和 checklist，這樣不夠嗎？」

不夠。Checklist 是結尾。教學還需要中間那段「怎麼從不懂走到懂」。

## What Is Already Strong

| Area | Why It Works |
|---|---|
| Roadmap | 從 single agent 到 production，有清楚 progression |
| Examples | 01-08 都能免 API key 跑，這點很重要 |
| Showcases | healthcare、finance、enterprise 讓 repo 不是純玩具 |
| Visual assets | 已經有 course map 和 architecture diagrams |
| CI | `Verify Runnable Examples` 讓範例不會偷偷壞掉 |
| Templates | agent spec、memory policy、eval、safety gate 都有起點 |

好，這些是優點。接下來我們看不足。

## Gap 1: Some Modules Are Too Definition-First

有些章節一開始就列核心概念，比如 memory、embedding、workflow。這沒錯，但容易變成名詞表。

更好的節奏是：

```text
先讓 naive chatbot 撞牆
   ↓
問：怎麼辦呢？
   ↓
再引入 memory / RAG / workflow
```

比如 Memory 不要一開始說 Short-term Memory、Episodic Memory、Semantic Memory。

可以先說：

```text
假設你昨天跟 agent 說你想用繁體中文學習。
今天你再問一次，它完全忘記。
那這個 agent 聰明嗎？
也許單次回答很聰明，但作為長期助教，它其實不可靠。
怎麼辦呢？
這時候才需要 memory policy。
```

## Gap 2: Assignments Need More Concrete Outputs

現在 labs 有 task 和 acceptance criteria，但學生交什麼，有時還不夠明確。

每章應該都要有一個 artifact：

```text
不是「理解 tool calling」
而是「交出 tool_policy.json + 3 個負例 eval」
```

因為作品集 repo 需要可展示成果。Stars 也常常來自這種東西：別人 fork 以後知道自己要改哪裡。

## Gap 3: Misconceptions Need A Central Map

Agent 領域最容易壞的地方，不是完全不懂。

是懂一半。

比如：

- 以為 tool use 就是把 function 丟給 model
- 以為 memory 就是 vector database
- 以為 multi-agent 會自動變聰明
- 以為 eval 是最後看一下 output 順不順

這些誤解要集中列出來，因為教學上最有價值的往往是「把錯的直覺扭回來」。

## Gap 4: Capstone Needs A Starter Scaffold

Capstone project 的要求是完整的，但對學生來說，空白 repo 壓力很大。

比較好的方式是給 starter：

```text
capstone-starter/
  README.md
  architecture.md
  agent_specs/
  tools/
  evals/
  run_demo.py
  run_eval.py
```

這樣學生不是從零開始，而是從一個可以跑的骨架開始改。

## Gap 5: Evaluation Should Be A Habit, Not A Chapter

現在 Example 07 和 08 都有 eval，這很好。

但整門課要一直提醒：

```text
每加一個能力，就加一個 eval。
每修一個 bug，就加一個 regression case。
每碰高風險工具，就加一個 approval test。
```

不然 evaluation 會變成 Module 09 才出現的東西。那就太晚了。

## What This Patch Adds

這次補上：

- `teaching/module-teaching-blueprint_zh.md`
- `teaching/misconception-map_zh.md`
- `teaching/student-deliverables_zh.md`
- `capstone-starter/`
- `lab-solutions/README_zh.md`
- curriculum / directory / README 的索引更新

## Recap

好，講到這邊我們知道了。

這個 repo 最大的不足，不是沒有內容。

是要把內容變成「可教、可練、可交、可測」。

所謂可教，就是每章都有問題意識和直覺。

所謂可練，就是每章都有 runnable example 或 lab。

所謂可交，就是每章有明確 artifact。

所謂可測，就是每章都能寫 eval 或 safety check。

這樣才像一門課，不只是很多 Markdown 檔案而已。
