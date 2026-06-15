# 內容設計原則

[English](content-design-principles.md)

## 目的

這份文件定義 Agent Engineering Roadmap 如何製作原創教學內容。

本專案應提供原創解釋、架構圖、練習題與程式範例。不要揭露、複製、翻譯或依賴任何特定外部教學來源。

---

## 核心原則

不要揭露來源材料。

外部學習材料只能作為私下理解學習痛點、常見問題與教學模式的參考。最終提交到 repository 的內容必須是原創內容。

---

## 內容轉換流程

```text
私下學習輸入
   ↓
抽象出概念與學習痛點
   ↓
移除來源特定文字、範例與結構
   ↓
創作原創英文教材
   ↓
加入原創架構圖、Checklist 與練習題
   ↓
必要時加入原創可執行程式碼
```

---

## 可以使用的內容

可以：

- 高層概念
- 常見學習問題
- 常見實作挑戰
- 原創解釋
- 原創架構圖
- 原創程式範例
- 原創練習題
- 原創 Checklist

不可以：

- 命名私下來源材料
- 列出來源平台
- 複製文章結構
- 翻譯完整段落
- 複製截圖
- 未確認授權就複製程式碼
- 揭露私下研究筆記

---

## Lesson Template

每個 lesson 建議包含：

```text
Title
Goal
Why it matters
Mental model
Core concepts
Architecture diagram
Hands-on project
Checklist
Common mistakes
Outcome
```

---

## 寫作風格

好的教學內容應該：

- 實作導向
- 簡潔
- 對初學者友善但不淺薄
- 重視架構
- 重視安全
- 重視生產環境

## 教學節奏

每一篇原創 lesson 都應該先讓讀者感覺到問題，再引入方法名稱。

建議節奏：

```text
問題
   ↓
直覺
   ↓
黑盒子的 input/output
   ↓
內部機制
   ↓
最小可執行範例
   ↓
常見失敗模式
   ↓
Checklist
```

比如說，不要一開始就定義「memory architecture」。先讓問題出現：Agent 忘記了使用者穩定偏好。接著問：什麼應該被記住？什麼應該被取回？什麼永遠不應該存？到這裡，再介紹 short-term memory、semantic memory、episodic memory 和 shared memory。

每個主要概念都應該包含：

- 一句白話解釋
- 一個具體例子
- 必要時加入一張 architecture 或 flow diagram
- 一個常見錯誤
- 一個可以立刻做的下一步

---

## Repository Policy

公開檔案只應包含完成後的教育內容。

不要提交：

- 原始研究筆記
- 來源清單
- 私下參考資料
- 複製文字
- 平台特定抓取筆記
- 未確認授權的第三方程式碼
