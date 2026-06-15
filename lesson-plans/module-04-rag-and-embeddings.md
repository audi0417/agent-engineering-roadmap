# Module 04 教案 - RAG And Embeddings

## 本堂課一句話

RAG 不是讓模型變聰明，而是把可檢索的外部知識放進它當下看得到的 context。

## 學習目標

學生上完後應該能：

- 解釋 embedding 與 similarity search
- 設計 chunking strategy
- 建立 retrieval eval cases
- 區分 retrieval failure 與 generation failure
- 設計 no-answer behavior

## 課前準備

- 閱讀：`curriculum/04-rag-and-embeddings_zh.md`
- Roadmap：`roadmap/level-0-ai-llm-fundamentals.md`
- Lab：`labs/lab-04-rag.md`

## 90 分鐘課程流程

| 時間 | 活動 |
|---:|---|
| 0-10 | 問：為什麼模型知道很多事還需要 RAG？ |
| 10-25 | 講 embedding、vector search、top-k |
| 25-40 | 講 chunking 與 metadata |
| 40-55 | Live demo：用小知識庫設計 10 個問題 |
| 55-75 | 學生建立 RAG eval set |
| 75-85 | 討論 no-answer 與 citation |
| 85-90 | Recap：RAG 要分開評估 retrieve 和 answer |

## 板書心智模型

```text
Question
  ↓
Embed query
  ↓
Search chunks
  ↓
Rank context
  ↓
Generate answer
  ↓
Check citation and faithfulness
```

## Live Demo

給 5 段文件，要求學生設計：

- direct lookup question
- synthesis question
- no-answer question
- ambiguous question

## 課堂練習

完成 `labs/lab-04-rag.md` 的 10 題 eval set。

## 常見誤解

- 誤解：RAG 一定會減少 hallucination。
- 修正：如果 retrieve 錯文件，模型只是拿錯 context 很流暢地回答。

## 作業

為你的 RAG agent 定義 retrieval precision 與 answer faithfulness 評分規準。

## 評量標準

| 項目 | 通過標準 |
|---|---|
| Chunks | 有合理切分與 metadata |
| Eval cases | 包含 no-answer 與 ambiguous |
| Citation | 答案能指回來源 |
| Faithfulness | 不編造文件外資訊 |
| Failure | 找不到答案時會承認 |
