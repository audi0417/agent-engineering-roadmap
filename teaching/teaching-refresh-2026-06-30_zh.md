# Teaching Refresh - 2026-06-30

這份筆記記錄 2026-06-30 的教材更新方向。

一言以蔽之：這次不是加更多名詞，而是補上「初學者怎麼知道自己真的做對了」。

## 為什麼要更新

很多 agent 教材會遇到一個問題。

它講了 tools、memory、RAG、workflow、multi-agent，聽起來很完整。但學生讀完以後會問：

```text
那我現在到底要交什麼？
怎樣算通過？
哪裡是危險邊界？
我的範例有沒有真的跑過？
```

所以這次更新補的是四種東西：

- quickstart：讓第一次進 repo 的人 30 秒內知道怎麼開始
- sample submissions：讓初學者看到可參考的作業品質
- domain safety cases：讓 healthcare / finance 不只是口號，而有具體 eval
- path-level evals：讓 graph agent 測流程，不只測最後文字

## Issue-Driven Updates

| Issue | 更新內容 | 教學意義 |
|---|---|---|
| #1 | Lab 00 / Lab 01 sample learner submissions | 學生不只看解題方向，也看得到可模仿的 artifact |
| #2 | Healthcare casebook 新增 medication interaction 和 emergency triage | 高風險 domain 要教 escalation，不是教模型硬答 |
| #3 | Graph approval agent 新增 permission、read-only、ambiguous destructive evals | Agent workflow 要測路徑，不能只看回答好不好聽 |
| #4 | README 新增三步 quickstart | 新讀者先跑、再學、最後做 capstone |
| #5 | Capstone 新增 finance no-advice evals | Finance agent 要分清楚 research support 和 personalized advice |

## 李宏毅式教學檢查

好，講到這邊我們用課堂視角檢查一下。

一堂 agent 課如果只有「這是 memory」「這是 tool use」，學生很容易以為知道名詞就等於會做。

但 agent engineering 不是背單字。它比較像是蓋一條流水線：

```text
輸入進來
  ↓
判斷風險
  ↓
決定能不能動工具
  ↓
留下 trace
  ↓
用 eval 檢查有沒有壞
```

所以每一章都應該回答三個問題：

1. 這章解決什麼 failure mode？
2. 學生最後要產出什麼 artifact？
3. 哪一個 eval 可以證明它沒有壞？

如果回答不出來，這章就還只是文章，不是教材。

## 下一輪建議

下一輪可以繼續補：

- 每個 lab 的 sample submission
- 每個 showcase 的 eval case 說明
- 每個 curriculum module 的「常見錯誤」小節
- 一份 `RUN_ALL.md`，讓讀者知道所有可執行入口

好，那這次更新的重點就是：讓教材從「內容很多」更靠近「學生真的能完成」。
