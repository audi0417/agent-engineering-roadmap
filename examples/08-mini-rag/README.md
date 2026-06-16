# Example 08 - Mini RAG With Evaluation

This example builds the smallest inspectable RAG pipeline in the course.

好，那 RAG 聽起來很神奇，但最小版本其實就是三件事：先找資料、再根據資料回答、最後檢查有沒有亂講。沒有向量資料庫，沒有 LLM，也沒有 API key。先把核心看懂，再換成 production stack。

## What this example teaches

- how to separate retrieval from answer generation
- how to inspect which documents were retrieved
- how to handle no-answer questions
- how to evaluate retrieval hit rate and answer faithfulness
- why RAG eval should test both "found the right document" and "answered from the document"

## Files

| File | Purpose |
|---|---|
| `main.py` | Runs one query and the eval suite |
| `rag.py` | Keyword retriever, grounded answerer, and evaluator |
| `knowledge_base.json` | Small local document set |
| `eval_cases.json` | Retrieval and answer test cases |

## Run

```bash
python main.py
```

Try:

```text
How should tool calls be approved?
```

```text
What is the database password?
```

## Mental model

```text
User question
   |
   v
Retriever selects candidate documents
   |
   v
Answerer uses only retrieved evidence
   |
   v
Evaluator checks retrieval hit and grounded answer
```

## Production notes

This example uses keyword scoring because it is transparent. In production, you can replace the retriever with embeddings, reranking, hybrid search, or a vector database.

The important point is the test shape. Do not only check whether the final answer sounds good. Check whether the system retrieved the right evidence and whether the answer stayed inside that evidence.
