# Teaching Layer

這個資料夾放的是「怎麼把這份 repo 教好」。

好，各位同學，教材不是檔案越多越好。檔案很多但學生不知道先看哪裡，其實就像把整個圖書館倒在桌上。很壯觀，但不一定會學會。

這一層的目的，是把 Agent Engineering Roadmap 變成一門有節奏的課：

```text
問題意識
   ↓
直覺模型
   ↓
打開黑盒子
   ↓
跑範例
   ↓
抓常見錯誤
   ↓
完成作業
   ↓
用 eval 證明沒有壞
```

## Files

| File | Purpose |
|---|---|
| `hung-yi-lee-style-audit_zh.md` | 用李宏毅式教學角度檢查目前不足與補強方向 |
| `module-teaching-blueprint_zh.md` | 每個 module 應該具備的固定教學結構 |
| `misconception-map_zh.md` | Agent Engineering 常見誤解與反例 |
| `student-deliverables_zh.md` | 每章學生要交出的具體成果 |

## How To Use

如果你是 self-learner：

1. 先看 `student-deliverables_zh.md`，知道每章要做出什麼。
2. 每讀一章 curriculum，就對照 `module-teaching-blueprint_zh.md`。
3. 做 lab 時，用 `misconception-map_zh.md` 檢查自己有沒有踩坑。
4. 最後用 `scripts/verify_examples.py` 確認範例還能跑。

如果你是 instructor：

1. 用 `hung-yi-lee-style-audit_zh.md` 看課程缺口。
2. 用 `module-teaching-blueprint_zh.md` 準備每堂課。
3. 用 `student-deliverables_zh.md` 當作作業與 grading checklist。

## Teaching Standard

一堂課如果只有名詞，還不算完成。

一堂課至少要讓學生做到：

- 說出問題在哪裡
- 畫出最小架構
- 跑一個例子
- 改一個地方
- 寫一個 eval 或 safety rule
- 說出一個 failure mode

如果做不到，這堂課就是聽起來很厲害而已。
