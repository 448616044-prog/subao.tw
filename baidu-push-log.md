## 2026-07-19 00:08 — 凌晨推送（自动化）
- **Token `K4kVPs6NwjtWr4ij`**: ❌ HTTP 401 `token is not valid`
- **推送URL数**: 10（尝试：sitemap.xml, /, /article-list, /tw-to-cn/, 6篇博客）
- **状态**: ❌ 连续第23天失败
- **根因**: token 永久失效；需登录 [百度搜索资源平台](https://ziyuan.baidu.com/) 获取新 token

## 2026-07-18 01:00 — 凌晨推送（自动化）
- **Token `UAVg0xt7rxpTjzaL`**: ❌ HTTP 401 `site error`
- **推送URL数**: 10（尝试：blog/* 10篇）
- **状态**: ❌ 连续失败，token 需更新

## 2026-07-17 23:56 — 凌晨推送（自动化）
- **Token `K4kVPs6NwjtWr4ij`**: ❌ HTTP 401 `token is not valid`
- **推送URL数**: 10（尝试：sitemap.xml, /, /article-list, /tw-to-cn/, 6篇博客）
- **状态**: ❌ 连续第21天失败
- **根因**: token 永久失效；需登录 [百度搜索资源平台](https://ziyuan.baidu.com/) 获取新 token

## 2026-07-16 23:56 — 凌晨推送（自动化）
- **Token `K4kVPs6NwjtWr4ij`** (指令指定): ❌ HTTP 401 `token is not valid`
- **Token `UAVg0xt7rxpTjzaL`** (脚本默认): ❌ HTTP 401 `site error`
- **推送URL数**: 10（尝试：sitemap.xml, /, /article-list, /tw-to-cn/, 6篇博客）
- **状态**: ❌ 双 token 均失败，连续第20天失败
- **根因**: 三个已知 token 全部失效，无可用 token；需登录百度搜索资源平台获取新 token

## 2026-07-15 23:56 — 凌晨推送（自动化）
- **Token `UAVg0xt7rxpTjzaL`** (脚本默认): ❌ HTTP 401 `site error`
- **Token `K4kVPs6NwjtWr4ij`** (指令指定): ❌ HTTP 401 `token is not valid`
- **推送URL数**: 10（尝试：sitemap.xml, /, /article-list, /tw-to-cn/, 6篇博客）
- **状态**: ❌ 双 token 均失败，连续第19天失败
- **根因**:
  - `K4kVPs6NwjtWr4ij` → 永久失效
  - `UAVg0xt7rxpTjzaL` → 站点不匹配
  - `2zqNR8QtonmBaAF4` → 站点不匹配（历史验证）
- **行动建议**: 🔴 登录 [百度搜索资源平台](https://ziyuan.baidu.com/) → subaotw.cn → 获取新 token

## 2026-07-13 23:56 — 凌晨推送（自动化）
- **Token**: K4kVPs6NwjtWr4ij ❌ HTTP 401 `token is not valid`
- **推送URL数**: 10（尝试：sitemap.xml, /, /article-list, /tw-to-cn/, 6篇博客）
- **状态**: ❌ 连续第18天失败
- **根因**: `K4kVPs6NwjtWr4ij` 永久失效，不可再用

# subaotw.cn 百度主动推送日志

> 每天10条URL，轮转式推送
> 
> API: data.zz.baidu.com
> Token: 全部失效 — 见下方分析

## 2026-07-12 23:56 — 凌晨推送（自动化）
- **Token K4kVPs6NwjtWr4ij**: ❌ HTTP 401 `token is not valid`
- **推送URL数**: 10（尝试：sitemap.xml, /, /article-list, /tw-to-cn/, 6篇博客）
- **状态**: ❌ 连续第17天失败
- **根因**: `K4kVPs6NwjtWr4ij` 永久失效，不可再用

## 2026-07-11 23:57 — 凌晨推送（自动化）
- **Token 2zqNR8QtonmBaAF4（脚本内置）**: ❌ HTTP 401 `site error`
- **Token K4kVPs6NwjtWr4ij（用户指令）**: ❌ HTTP 401 `token is not valid`
- **推送URL数**: 10（尝试：sitemap.xml, /, /article-list, /tw-to-cn/, 6篇博客）
- **状态**: ❌ 两个 token 均永久失效，连续第16天失败
- **根因**: 
  - `K4kVPs6NwjtWr4ij`：永久失效 `token is not valid`
  - `2zqNR8QtonmBaAF4`：站点不匹配 `site error`（非本站 token）
  - `UAVg0xt7rxpTjzaL`：over quota（已在 7/7 耗尽，从未恢复）

## 2026-07-10 23:56 — 凌晨推送（自动化）
- **Token K4kVPs6NwjtWr4ij**: ❌ HTTP 401 `token is not valid`
- **推送URL数**: 10（尝试：sitemap.xml, /, /article-list, /tw-to-cn/, 6篇博客）
- **状态**: ❌ token 永久失效，连续第15天失败
- **根因**: `K4kVPs6NwjtWr4ij` 已确认永久失效，不可再用

## 2026-07-08 23:57 — 凌晨推送（自动化）
- **Token K4kVPs6NwjtWr4ij**: ❌ HTTP 401 `token is not valid`
- **Token UAVg0xt7rxpTjzaL（脚本内）**: ❌ HTTP 400 `over quota`
- **推送URL数**: 10（尝试：sitemap.xml, /, /article-list, /tw-to-cn/, 6篇博客）
- **状态**: ❌ 两 token 均不可用。全天2次尝试（00:01 + 23:57）均失败
- **根因**: `UAVg0xt7rxpTjzaL` 有效但 7/7 22:45 的 10 条推送耗尽配额后未曾恢复

## 2026-07-09 23:56 — 凌晨推送（自动化）
- **Token K4kVPs6NwjtWr4ij**: ❌ HTTP 401 `token is not valid`
- **Token UAVg0xt7rxpTjzaL**: ❌ HTTP 400 `over quota`
- **推送URL数**: 10（尝试：sitemap.xml, /, /article-list, /tw-to-cn/, 6篇博客）
- **状态**: ❌ 两个 token 均不可用
- **连续失败**: 14天（最后一次成功 6/25）

## 2026-07-08 00:01 — 凌晨推送
- **Token K4kVPs6NwjtWr4ij**: ❌ HTTP 401 `token is not valid`
- **Token UAVg0xt7rxpTjzaL（脚本内）**: ❌ HTTP 400 `over quota`
- **推送URL数**: 10（尝试：sitemap.xml, /, /article-list, /tw-to-cn/, 6篇博客）
- **状态**: ❌ 两个 token 均不可用。指定 token 失效；脚本 token 有效但日配额已耗尽
- **建议**: 
  1. `K4kVPs6NwjtWr4ij` 确认失效，不可再使用
  2. `UAVg0xt7rxpTjzaL` 是当前有效 token，但需等次日配额恢复
  3. 自动化脚本应更新为使用 `UAVg0xt7rxpTjzaL` 作为唯一 token

## 2026-07-07 22:45 — Token更新 + 首日10条推送
- **Token更新**: K4kVPs6NwjtWr4ij → UAVg0xt7rxpTjzaL（旧账号恢复）
- **批次1**: 5条 → remain=5, success=5
  - https://www.subaotw.cn/
  - https://www.subaotw.cn/tw-to-cn/
  - https://www.subaotw.cn/equipment/
  - https://www.subaotw.cn/guide/
  - https://www.subaotw.cn/blog/cn-to-tw-shipping-guide
- **批次2**: 5条 → remain=0, success=5
  - https://www.subaotw.cn/blog/cn-to-tw-furniture-shipping
  - https://www.subaotw.cn/blog/cn-to-tw-moving-guide
  - https://www.subaotw.cn/blog/cn-to-tw-appliance-shipping
  - https://www.subaotw.cn/blog/cn-to-tw-building-materials-shipping
  - https://www.subaotw.cn/blog/cn-to-tw-equipment-shipping
- **状态**: ✅ 全部成功，日配额用完
- **累计推送**: 45 + 10 = 55/140

## 2026-07-05 23:56 — 凌晨推送
- **推送URL数**: 10（尝试，取脚本前10条：sitemap.xml, /, /article-list, /tw-to-cn/, /blog/cn-to-tw-shipping-guide, /blog/food-shipping-guide, /blog/noodles-ramen-shipping, /blog/tea-shipping-guide, /blog/cosmetics-shipping, /blog/electronics-shipping）
- **API返回**: `{"error":401,"message":"token is not valid"}`
- **状态**: ❌ Token 失效
- **对比上次(7/3)**: 上次为 HTTP 400 over quota，本次变为 HTTP 401 token is not valid
- **结论**: Token `K4kVPs6NwjtWr4ij` 已过期或被撤销，需登录[百度搜索资源平台](https://ziyuan.baidu.com/)重新获取推送 token
> Token: K4kVPs6NwjtWr4ij

## 2026-06-14 00:05
- **推送URL数**: 5
- **起点索引**: 0
- [0] https://www.subaotw.cn/
- [1] https://www.subaotw.cn/equipment/
- [2] https://www.subaotw.cn/tw-to-cn/
- [3] https://www.subaotw.cn/tw-to-cn/complete-guide
- [4] https://www.subaotw.cn/guide/
- **API返回**: `{'remain': 5, 'success': 5}`

## 2026-06-16 23:55
- **推送URL数**: 5（尝试）
- **起点索引**: 5
- [5] https://www.subaotw.cn/faq
- [6] https://www.subaotw.cn/pricing-calculator
- [7] https://www.subaotw.cn/volume-calculator
- [8] https://www.subaotw.cn/about
- [9] https://www.subaotw.cn/contact
- **API返回**: `{"error":400,"message":"over quota"}`
- **状态**: ⚠️ 配额已满，索引未推进

## 2026-06-17 23:55
- **推送URL数**: 5 ✅
- **起点索引**: 5（重试上轮因配额未推的URL）
- [5] https://www.subaotw.cn/faq
- [6] https://www.subaotw.cn/pricing-calculator
- [7] https://www.subaotw.cn/volume-calculator
- [8] https://www.subaotw.cn/about
- [9] https://www.subaotw.cn/contact
- **API返回**: `{"remain":5,"success":5}`
- **状态**: ✅ 全部推送成功


## 2026-06-18 23:59
- **推送URL数**: 5
- **起点索引**: 11
- [11] https://www.subaotw.cn/tw-to-cn
- [12] https://www.subaotw.cn/tw-to-cn/food-shipping
- [13] https://www.subaotw.cn/guide/equipment-export-process
- [14] https://www.subaotw.cn/equipment/cnc-export-taiwan
- [15] https://www.subaotw.cn/equipment/injection-molding
- **API返回**: `{'remain': 5, 'success': 5}`


## 2026-06-20 00:01
- **推送URL数**: 5
- **起点索引**: 17
- [17] https://www.subaotw.cn/equipment/cnc-export-taiwan
- [18] https://www.subaotw.cn/equipment/construction-machinery
- [19] https://www.subaotw.cn/equipment/food-processing
- [20] https://www.subaotw.cn/equipment/injection-molding
- [21] https://www.subaotw.cn/equipment/mechanical-parts
- **API返回**: `{'remain': 5, 'success': 5}`


## 2026-06-20 00:11 batch
- **推送URL数**: 5
- **起点索引**: 22
- [22] https://www.subaotw.cn/equipment/mining-equipment
- [23] https://www.subaotw.cn/equipment/mold-tooling
- [24] https://www.subaotw.cn/equipment/packaging-equipment
- [25] https://www.subaotw.cn/equipment/plastic-machinery
- [26] https://www.subaotw.cn/equipment/press-machine
- **API返回**: {"remain": 0, "success": 5}


## 2026-06-20 08:07 batch (继续)
- **推送**: 5
- **起点**: 22
- **返回**: {"error": 400, "message": "over quota"}
- [22] https://www.subaotw.cn/equipment/mining-equipment
- [23] https://www.subaotw.cn/equipment/mold-tooling
- [24] https://www.subaotw.cn/equipment/packaging-equipment
- [25] https://www.subaotw.cn/equipment/plastic-machinery
- [26] https://www.subaotw.cn/equipment/press-machine


## 06-20 auto
- **27**: 5 URLs
- **return**: {"error": 400, "message": "over quota"}
- https://www.subaotw.cn/equipment/printing-equipment
- https://www.subaotw.cn/equipment/textile-machinery
- https://www.subaotw.cn/equipment/woodworking
- https://www.subaotw.cn/faq
- https://www.subaotw.cn/furniture-shipping


## 2026-06-21 00:03
- **推送URL数**: 5
- **起点索引**: 27
- [27] https://www.subaotw.cn/equipment/mining-equipment.html
- [28] https://www.subaotw.cn/equipment/mold-tooling.html
- [29] https://www.subaotw.cn/equipment/ningbo-export-taiwan.html
- [30] https://www.subaotw.cn/equipment/packaging-equipment.html
- [31] https://www.subaotw.cn/equipment/plastic-machinery.html
- **API返回**: `{'remain': 5, 'success': 5}`
- **状态**: ✅ 推送成功

## 2026-06-21 23:55
- **推送URL数**: 5（尝试）
- **起点索引**: 32
- [32] https://www.subaotw.cn/equipment/press-machine.html
- [33] https://www.subaotw.cn/equipment/printing-equipment.html
- [34] https://www.subaotw.cn/equipment/qingdao-export-taiwan.html
- [35] https://www.subaotw.cn/equipment/shenzhen-export-taiwan.html
- [36] https://www.subaotw.cn/equipment/suzhou-export-taiwan.html
- **API返回**: `{"error":400,"message":"over quota"}`
- **状态**: ⚠️ 今日配额已用（00:03已推5条），索引保持32不变

## next_start: 32

## 2026-06-22 23:32
- **推送URL数**: 5（尝试）
- **起点索引**: 32（注意：与 txt 文件行号已不一致，本次实际取到 textile/tianjin/woodworking/wuhan/xiamen）
- [32] https://www.subaotw.cn/equipment/textile-machinery.html
- [33] https://www.subaotw.cn/equipment/tianjin-export-taiwan.html
- [34] https://www.subaotw.cn/equipment/woodworking.html
- [35] https://www.subaotw.cn/equipment/wuhan-export-taiwan.html
- [36] https://www.subaotw.cn/equipment/xiamen-export-taiwan.html
- **API返回**: `{"error":400,"message":"over quota"}`
- **状态**: ⚠️ 配额异常——6/22 全天仍未恢复（上次成功 6/21 00:03），索引保持 32 不变

## 2026-06-23 07:55
- **推送URL数**: 5（队列模式，取文件前5行）
- **队列首行**: 1
- [1] https://www.subaotw.cn/blog/shipping-fee-guide.html
- [2] https://www.subaotw.cn/building-materials-taiwan.html
- [3] https://www.subaotw.cn/bulk-cargo-taiwan.html
- [4] https://www.subaotw.cn/cases/case-cnc-dongguan.html
- [5] https://www.subaotw.cn/cases/case-injection-shenzhen.html
- **API返回**: `{"error":400,"message":"over quota"}`
- **状态**: ❌ 配额已满——连续4次失败（6/21 23:55, 6/22 23:32, 6/23 07:55）。切换为队列模式后 API 仍然拒绝。

## next_start: 队列模式（不适用）

---

## ⚠️ 配额诊断 (2026-06-23)
- **连续失败**: 4次（6/20 ~ 6/23）
- **累计成功推送**: 35条
- **结论**: 百度免费新站推送配额已耗尽（≈35条上限）
- **建议**: 登录 [百度搜索资源平台](https://ziyuan.baidu.com/) 检查站点 **subaotw.cn** 配额状态：
  1. 查看「数据引入 → 普通收录」额度
  2. 尝试提交 sitemap 替代 API 推送
  3. 提交配额提升申请
  4. 或将推送频率降为每周2-3次，观察配额重置周期
- **清理**: 本次同时修复了 baidu-push-urls.txt 中合并行(第95行)和3条重复URL

---

## ⚠️ 配额诊断（历史 2026-06-22）

- 连续2天（6/21 23:55、6/22 23:32）返回 `over quota`，单条测试也失败
- 累计成功推送：**35条**
- 可能原因：百度新站免费推送总量有上限（推测~30-50条），已耗尽
- 建议：登录 [百度搜索资源平台](https://ziyuan.baidu.com/) 检查站点配额状态，或联系百度申请提额

## 2026-06-25 00:05 — 配额恢复+10条推送

**推送批次1**: remain=6 → 成功4
- furniture-shipping, commercial-cargo, moving-cost, sitemap.xml

**推送批次2**: remain=1 → 成功5
- tw-to-cn/, equipment/, blog/ezway-tutorial, blog/complete-guide, cases/

**推送批次3**: remain=0 → 成功1
- pricing-calculator

**累计**: 35 + 10 = 45/120 URL 已推送到百度

## 2026-06-26 08:06
- **推送URL数**: 5（队列模式，取文件前5行）
- **队列序号**: 第1-5行
- [1] https://www.subaotw.cn/
- [2] https://www.subaotw.cn/about
- [3] https://www.subaotw.cn/appliance-shipping
- [4] https://www.subaotw.cn/article-list
- [5] https://www.subaotw.cn/blog/clothes-to-taiwan
- **API返回**: `{"error":400,"message":"over quota"}`
- **状态**: ❌ 配额已满——6/26 仍未恢复。上次成功推送 6/25 00:05（10条），推测免费新站日配额当天已用完或总量近上限。
## 2026-07-03 23:56:23 — 凌晨推送
- **推送URL数**: 10（尝试）
- **API返回**: {"error":400,"message":"over quota"}

## 2026-07-04 — 全站技术修复后推送尝试
- **推送URL数**: 5（sitemap+首页+核心入口）
- **API返回**: {"error":400,"message":"over quota"}
- **状态**: ❌ 连续10天 over quota，最后一次成功6/25
- **结论**: 免费新站推送总量上限已触发（≈45条后永久锁定），需手动登录[百度搜索资源平台](https://ziyuan.baidu.com/)：
  1. 查看站点配额状态
  2. 手动提交 sitemap（非API方式）
  3. 申请配额提升
- **副作用**: subaotw.cn 130页中仍有85页未被推送，Baiduspider 缺乏入口

## 2026-07-04 — 技术修复清单
- P0-1: ✅ 清除6页GA/gtag代码
- P0-2: ✅ 全量百度统计覆盖（130/130）
- P0-3: ✅ 全量自动推送JS覆盖（130/130）
- P0-4: ⚠️ API推送配额耗尽，需手动提交sitemap
- **状态**: ❌ 配额已满或失败

## 2026-07-05 23:56:40 — 凌晨推送
- **推送URL数**: 10（尝试）
- **API返回**: {"error":401,"message":"token is not valid"}
- **状态**: ❌ 配额已满或失败

## 2026-07-06 23:57:38 — 凌晨推送
- **推送URL数**: 10（尝试）
- **API返回**: {"error":401,"message":"token is not valid"}
- **状态**: ❌ 配额已满或失败

## 2026-07-08 23:57:05 — 凌晨推送
- **推送URL数**: 10（尝试）
- **API返回**: {"error":401,"message":"site error"}
- **状态**: ❌ 配额已满或失败

## 2026-07-11 23:57:08 — 凌晨推送
- **推送URL数**: 10（尝试）
- **API返回**: {"error":401,"message":"site error"}
- **状态**: ❌ 配额已满或失败

## 2026-07-15 23:56:43 — 凌晨推送
- **推送URL数**: 10（尝试）
- **API返回**: {"error":401,"message":"site error"}
- **状态**: ❌ 配额已满或失败


## 2026-07-16 22:54
- 提交sitemap.xml: 400
- 批量URL推送: 10个高优先URL
- 剩余quota: 9-10
