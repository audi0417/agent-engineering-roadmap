# Module 03 教案 - Memory Systems

## 本堂課一句話

Memory 不是把所有東西存起來，而是決定什麼值得記、什麼可以用、什麼必須忘。

## 學習目標

學生上完後應該能：

- 區分 context 與 memory
- 設計 memory write policy
- 設計 retrieval policy
- 說明 deletion 與 audit 的必要性
- 修改 Example 04 的 memory rules

## 課前準備

- 閱讀：`curriculum/03-memory-systems_zh.md`
- 範例：`examples/04-memory-agent/README.md`
- 模板：`templates/memory-policy-template.md`

## 90 分鐘課程流程

| 時間 | 活動 |
|---:|---|
| 0-10 | 問：Agent 記住使用者偏好是好事還是壞事？ |
| 10-25 | 講 short-term、semantic、episodic、shared memory |
| 25-40 | 拆 Example 04 的 JSON memory store |
| 40-55 | Live demo：新增 forget 指令 |
| 55-75 | 學生設計一份 memory policy |
| 75-85 | 討論 sensitive data 與 stale memory |
| 85-90 | Recap：memory 是 policy first，database second |

## 板書心智模型

```text
Event
  ↓
Should write?
  ↓
Store with reason
  ↓
Should retrieve?
  ↓
Use only if relevant and safe
  ↓
Audit / update / delete
```

## Live Demo

示範「使用者說 forget my preference」時，系統如何刪掉相關 memory。

## 課堂練習

學生為自己的 agent 寫出：

- should store
- should not store
- retrieve when
- delete when
- audit fields

## 常見誤解

- 誤解：有向量資料庫就等於有 memory。
- 修正：向量資料庫只是 storage/retrieval 技術，memory 的核心是 policy。

## 作業

替 Example 04 加入 update 或 delete memory 的功能。

## 評量標準

| 項目 | 通過標準 |
|---|---|
| Write policy | 不是所有輸入都存 |
| Retrieval | 只取相關記憶 |
| Privacy | 敏感資料預設不存 |
| Deletion | 使用者可要求忘記 |
| Audit | 記錄 why/source/time |
