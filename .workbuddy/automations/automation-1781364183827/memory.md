# 百度推送自动化记忆

## 2026-07-06 23:57
- **结果**: ❌ token is not valid（HTTP 401）
- **连续失败天数**: 2天（7/5 + 7/6）
- **待推URL**: 脚本前10条（sitemap.xml, /, /article-list, /tw-to-cn/, 6篇博客）
- **累计推送**: 45/130条 URL（自6/25后无成功，已连续11天无成功推送）
- **Token状态**: `K4kVPs6NwjtWr4ij` 确认失效，需刷新
- **行动建议**:
  1. 登录 [百度搜索资源平台](https://ziyuan.baidu.com/) → 站点管理 → subaotw.cn → 数据引入 → 获取新 API 推送 token
  2. 更新 token 到脚本第5行：`/Users/mac/WorkBuddy/Claw/物流項目/sites/subaotw-cn/baidu-push-priority.sh`
  3. 同时检查站点配额状态（over quota 可能在 token 刷新后仍存在）
  4. 若配额也耗尽，需手动提交 sitemap 作为替代方案

## 2026-07-05 23:56
- **结果**: ❌ token is not valid（HTTP 401）
- 详情同上

## 2026-07-03 23:56
- **结果**: ❌ over quota（HTTP 400）
- 详情见上方

## 2026-06-26 08:06
- **结果**: ❌ over quota
- 详情见历史记录
