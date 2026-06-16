# 範例 14：Modern MCP Gateway

這個範例示範 modern MCP-style gateway 的形狀。

它不是完整 MCP 實作，而是教學用的概念模型：

- tools
- resources
- prompts
- authorization
- required arguments 缺少時的 elicitation

## 執行

```bash
python examples/14-modern-mcp-gateway/main.py
```

## 學習檢查

- 哪個 token 可以 call tools？
- 哪個操作需要 elicitation？
- 為什麼 resources 和 tools 應該有不同權限？

