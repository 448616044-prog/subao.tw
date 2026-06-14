# 百度每日API推送 subaotw.cn — 执行记忆

## 运行摘要

- **最近执行**: 2026-06-14 00:05 CST
- **推送脚本**: `baidu-push-runner.py`
- **Sitemap**: `sites/subaotw-cn/sitemap.xml`（60个唯一URL）
- **推送日志**: `baidu-push-log.md`

## 最近一次推送

- 起点索引: 0 → 推送 5 条
- API 返回: `{'remain': 5, 'success': 5}` ✅
- 下次起点: 5

## 注意事项

- 百度API 使用 HTTP（非HTTPS），HTTPS 会导致 SSL 证书验证失败
- 每日限额 10 条，每次推 5 条，remain 显示剩余配额
- 轮转机制：log 文件末尾 `## next_start: N` 记录下次起点；到末尾自动回绕到 0
