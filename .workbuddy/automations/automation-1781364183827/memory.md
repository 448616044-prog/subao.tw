# 百度推送自动化记忆

## 2026-07-13 23:56
- **结果**: ❌ `K4kVPs6NwjtWr4ij` HTTP 401 `token is not valid`
- **连续失败天数**: 18天（最后一次成功 6/25）
- **token 状态**:
  - `K4kVPs6NwjtWr4ij` — 永久失效 `token is not valid`（已连续18天）
  - `2zqNR8QtonmBaAF4` — 站点不匹配 `site error`
  - `UAVg0xt7rxpTjzaL` — over quota（7/7 耗尽后未恢复）
- **行动建议**: 🔴 登录 [百度搜索资源平台](https://ziyuan.baidu.com/) → subaotw.cn → 获取新 API 推送 token，否则此自动化无意义

## 2026-07-12 23:56
- **结果**: ❌ `K4kVPs6NwjtWr4ij` HTTP 401 `token is not valid`
- **连续失败天数**: 17天（最后一次成功 6/25）

## 2026-07-11 23:57
- **结果**: ❌ 两个 token 均失败
  - 脚本 `2zqNR8QtonmBaAF4`: HTTP 401 `site error`（非本站 token）
  - 指令 `K4kVPs6NwjtWr4ij`: HTTP 401 `token is not valid`
- **连续失败天数**: 16天（最后一次成功 6/25）
- **可用 token 现状**:
  - `K4kVPs6NwjtWr4ij` — 永久失效 `token is not valid`
  - `2zqNR8QtonmBaAF4` — 站点不匹配 `site error`（可能是其他站 token）
  - `UAVg0xt7rxpTjzaL` — over quota（7/7 耗尽后未恢复，疑似终身配额上限）
- **行动建议**:
  1. 🔴 **必须：登录 [百度搜索资源平台](https://ziyuan.baidu.com/) → subaotw.cn → 获取新 API 推送 token**
  2. 检查站点配额状态，确认是否触发终身限额
  3. 尝试手动提交 sitemap 作为替代方案
  4. 如果自动化推送长期不可行，考虑暂停此自动化任务

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
