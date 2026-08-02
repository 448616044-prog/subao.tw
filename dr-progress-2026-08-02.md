# subao.tw DR 外链进度报告 (2026-08-02)

**报告周期**: 7/14 - 8/2 (约 2.5 周)
**报告人**: WorkBuddy SEO Expert

---

## ✅ 累计可追踪外链目录 (14个)

| # | 目录 | 类型 | 预估 DR | 状态 | 提交日 |
|:--|:---|:---|:---:|:--|:--|
| 1 | forwarderspn.com | 货代专业 | 35+ | ✅ 审核通过 | 7/14 |
| 2 | freightnet.com | 货代目录（28,000+会员）| 40+ | 🟢 Member 275376 (待邮箱验证+审核，30天) | **8/2** |
| 3 | webmulu.com | 通用目录 | - | ✅ 已提交 | 7/14 |
| 4 | allproducts.com | 通用目录 | - | ✅ 已提交 | 7/14 |
| 5 | ruzave.com | 货代目录 | 35+ | ✅ 已有账号 | 7/15 |
| 6 | freightengage.com | 货代专业 | - | ✅ 注册成功 | 7/15 |
| 7 | somuch.com | 通用目录 | 57 | ✅ 队列中 | 7/15 |
| 8 | jayde.com | B2B Search | 59 | ✅ 提交成功 | 7/15 |
| 9 | 1websdirectory.com | 通用目录 | 40 | ✅ 提交成功 | 7/15 |
| 10 | alovair-sea.com | 货代专业 | 35+ | ✅ 提交成功 | 7/15 |
| 11 | viesearch.com | 通用目录 | 35+ | ✅ 已提交 | 7/16 |
| 12 | freightpages.org | 货代专业 | - | ✅ CF7确认 | 7/16 |

## 🟡 阿龙手动完成队列

| 目录 | 类型 | 状态 | 行动 |
|:---|:---|:---:|:---|
| **freightnet.com 邮箱验证** | 货代联盟 | 🟢 Member 275376 已注册 | **阿龙去 mailbox business@subao.tw 收验证邮件 → 点链接** |
| tranznova.com | 货代联盟 | 🟡 OTP待填 | 查邮箱 → 填6位码 |
| forwarderfocusdirectory.com | 货代联盟 | 🟡 邮件草稿就绪 | 阿龙发送 |

## ❌ 本次失败 (5个)

| 目录 | 失败原因 |
|:---|:---|
| freightcue.com | Cloudflare Turnstile |
| forwardingcompanies.com | 无公开提交入口 |
| shippingscout.com | 域名parked |
| freedirectory.com | 域名parked |
| foreign-trade.com | Google reCAPTCHA |

## 🚀 8月新增目标 (8/2 调研更新)

### 🟢 已验证可提交（无 captcha，需要 agent-browser）
| # | 目录 | 预估DR | 表单类型 | 优先级 | 备注 |
|:--|:---|:---:|:---|:---:|:---|
| 1 | forwardingcompanies.com | 30+ | TYPO3 Powermail | 🔴 | "world's largest" 150国，无captcha！ |
| 2 | cargolinked.com | 25+ | React SPA | 🔴 | 免费tier forever，新平台竞争少 |
| 3 | shippingsail.com | 20+ | WPForms (需JS) | 🟡 | 简单4字段，agent-browser快速 |
| 4 | freightshipping.ca | 15+ | 传统表单 | 🟡 | 加拿大货运目录，可扩展 |

### 🟡 待验证
| 目录 | 预估DR | 备注 |
|:---|:---:|:---|
| cargotrax.com | 10+ | 经典ASP，2000年建站，可能已死 |
| worldfreightdirect.com | 25+ | 待验证 |
| forwardingdirectory.com | 20+ | 待验证 |
| directory.freightcaviar.com | 30+ | 待验证 |

### 🔴 被拒但可重试
| 目录 | 原失败原因 | 新方案 |
|:---|:---|:---|
| forwardingcompanies.com | 之前标记为"无公开提交入口" | **8/2发现：有get-listed表单！** 需要agent-browser提交 |

## 📊 关键经验汇总

### ✅ 可复制打法（freightnet.com 8/2 实战）
1. **agent-browser + eval 组合** 处理 JS 渲染 + 后端表单：
   - `eval` 函数包裹 `(function(){...})()` 解决 "Illegal return statement"
   - `el.dispatchEvent(new Event('change',{bubbles:true}))` 触发 select 事件
   - `f.requestSubmit()` 比 `click()` 更可靠（直接走 form submit）
2. **hidden fields 必填**：表单可能有 `signup1`、`is_manual_entry`、`latitude`、`longitude` 等 hidden input，requestSubmit 自动带
3. **"Enter manually" 触发 manual address fields**：Google Maps autocomplete 必填，否则卡住
4. **page 状态保持**：snapshot 后 ref 可能失效，每步重新 snapshot 更安全
5. **select 动态国家**：218 个国家，ref 索引不稳定；用 `eval` 按文本找最稳

### ❌ Hard Blockers 仍存在
- Cloudflare Turnstile / reCAPTCHA / PHPLD 付费墙 / Badge 回链 / 域 parked

## 🎯 8月预期

- **DR**: 当前=2 → 预期=3-4（如果 freightnet 通过审核）
- **引用域名**: 当前=276 → 预期=+3-5
- **下一步**: 8月底前再攻 5-8 个新货代目录

## 🔗 重要新发现

**Yandex IndexNow 工作流**：
- Bing 的 `api.indexnow.org/indexnow` 直接拒绝（403 "UserForbiddedToAccessSite"），因为 key 未注册
- Yandex 的 `yandex.com/indexnow` **接受**无注册 key 的提交（HTTP 202）
- 12 个核心 URL 已全部提交（首页 + 11 个月饼 + 零食 power page）
- Bing 不会立即收到，但 Yandex 会处理
- Google 已弃用 IndexNow，但仍可能从其他渠道重新发现