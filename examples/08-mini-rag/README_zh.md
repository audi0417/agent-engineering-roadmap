# Example 08 - Mini RAG With Evaluation

[English](README.md)

這個範例會建立課程中最小、可檢查的 RAG pipeline。

好，各位同學看到 RAG 很容易覺得它是一個很大的系統。其實把它打開來看，最小版本就是三步而已：找資料、根據資料回答、檢查有沒有亂講。就這樣子。

## 這個範例教什麼？

- 如何把 retrieval 和 answer generation 分開看
- 如何檢查到底取回哪些 documents
- 如何處理 no-answer questions
- 如何評估 retrieval hit rate 和 answer faithfulness
- 為什麼 RAG eval 不能只看最後答案順不順

## 檔案

| File | Purpose |
|---|---|
| `main.py` | 執行單次 query 與 eval suite |
| `rag.py` | Keyword retriever、grounded answerer、evaluator |
| `knowledge_base.json` | 小型本地知識庫 |
| `eval_cases.json` | Retrieval 與 answer 測試案例 |

## 執行

```bash
python main.py
```

可以試：

```text
How should tool calls be approved?
```

```text
What is the database password?
```

## 心智模型

```text
使用者問題
   |
   v
Retriever 選出候選文件
   |
   v
Answerer 只能根據取回證據回答
   |
   v
Evaluator 檢查 retrieval hit 和 grounded answer
```

## 生產環境提醒

這裡故意用 keyword scoring，因為它很好檢查。Production 裡你可以換成 embeddings、reranking、hybrid search 或 vector database。

重點不是 keyword search 很厲害。重點是 eval shape：你要分別檢查「有沒有找對資料」和「答案有沒有根據資料」。這兩件事常常不是同一件事。
