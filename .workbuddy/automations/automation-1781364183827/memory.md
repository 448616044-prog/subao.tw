# 百度每日API推送 subaotw.cn — 执行记忆

## 运行摘要

- **最近执行**: 2026-06-18 23:59 CST
- **推送脚本**: `baidu-push-runner.py`
- **Sitemap**: `sites/subaotw-cn/sitemap.xml`（71个唯一URL，含去重）
- **推送日志**: `baidu-push-log.md`

## 最近一次推送

- 起点索引: 11 → 推送 [11]-[15] 共 5 条 ✅
- API 返回: `{"remain":5,"success":5}`（HTTP 200）
- 下次起点: **16**
- 累计推送: 15/71 URL（21.1%）

## 注意事项

- 百度API 使用 **HTTP**（非HTTPS），HTTPS 会导致 SSL 证书验证失败（exit 60）
- 每日限额 5 条（百度搜索资源平台新站点限制）
- 轮转机制：log 文件末尾 `## next_start: N` 记录下次起点；到末尾自动回绕到 0
- 配额错误 "over quota" 时不推进索引，次日自动重试
- sitemap 尾部无 `ns0:` 前缀的 `<url>` 标签不会被解析（已知限制）
