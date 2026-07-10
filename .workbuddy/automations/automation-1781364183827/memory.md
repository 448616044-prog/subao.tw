# 百度推送自动化记忆

## 2026-07-10 23:56
- **结果**: ❌ `K4kVPs6NwjtWr4ij` HTTP 401 `token is not valid`
- **连续失败天数**: 15天（最后一次成功 6/25）
- **根因**: `K4kVPs6NwjtWr4ij` 永久失效，不可再用
- **行动建议**: 
  1. 🔴 **紧急**：登录 [百度搜索资源平台](https://ziyuan.baidu.com/) 获取新 token
  2. 更新自动化指令中的 token
  3. 或尝试手动提交 sitemap 替代 API 推送

## 2026-07-09 23:56
- **结果**: ❌ 两 token 均失败
  - `K4kVPs6NwjtWr4ij`: HTTP 401 `token is not valid`
  - `UAVg0xt7rxpTjzaL`: HTTP 400 `over quota`
- **连续失败天数**: 14天（最后一次成功 6/25）
- **根因**: 
  - `K4kVPs6NwjtWr4ij` 永久失效
  - `UAVg0xt7rxpTjzaL` 有效但 7/7 后配额耗尽从未恢复，疑似触发百度免费新站终身配额上限
- **累计推送**: 55/140 条 URL
- **行动建议**:
  1. `K4kVPs6NwjtWr4ij` 永久失效，不可再用
  2. 登录 [百度搜索资源平台](https://ziyuan.baidu.com/) → subaotw.cn → 检查站点配额状态
  3. 尝试手动提交 sitemap 替代 API 推送
  4. 申请配额提升或联系百度客服

## 2026-07-08 23:57
- **结果**: ❌ 两 token 均失败
- **连续失败天数**: 13天

## 2026-07-06 23:57
- **结果**: ❌ token is not valid（HTTP 401）
- **连续失败天数**: 2天

## 2026-07-05 23:56
- **结果**: ❌ token is not valid（HTTP 401）

## 2026-07-03 23:56
- **结果**: ❌ over quota（HTTP 400）

## 2026-06-26 08:06
- **结果**: ❌ over quota
