# subaotw.cn 百度主动推送日志

> 每天5条URL，轮转式推送
> 
> API: data.zz.baidu.com
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
