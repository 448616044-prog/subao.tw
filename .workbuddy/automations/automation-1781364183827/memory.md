# 百度每日API推送 subaotw.cn — 执行记忆

## 运行摘要

- **最近执行**: 2026-06-16 23:55 CST
- **推送脚本**: `baidu-push-runner.py`（direct curl 执行）
- **Sitemap**: `sites/subaotw-cn/sitemap.xml`（71个URL，含重复）
- **推送日志**: `baidu-push-log.md`

## 最近一次推送

- 起点索引: 5 → 尝试推送 [5]-[9] 共 5 条
- API 返回: `{"error":400,"message":"over quota"}` ❌
- 原因: 今日百度配额已用完（每日5条，可能已有其他途径消耗）
- 下次起点: **5**（未推进，下次重试同批URL）

## 注意事项

- 百度API 使用 **HTTP**（非HTTPS），HTTPS 会导致 SSL 证书验证失败（exit 60）
- 每日限额 5 条（百度搜索资源平台新站点限制）
- 轮转机制：log 文件末尾 `## next_start: N` 记录下次起点；到末尾自动回绕到 0
- 配额错误 "over quota" 时不推进索引，次日自动重试
