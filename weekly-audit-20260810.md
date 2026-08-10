# subao.tw 每周深度审计报告

**日期**: 2026-08-10 (周一)
**审计周期**: 2026-08-04 ~ 2026-08-10
**执行人**: 阿龙 (SEO 自动化审计)

---

## 📊 本周概览

| 指标 | 数值 | 较上周 |
|:---|:---:|:---:|
| Sitemap URL 数 | 262 | +38 (+17%) |
| 全站可达率 | 262/262 (100%) | ✅ 0 错误 |
| Google 索引 | site: 不返回本站 | 🔴 连续第5周 |
| Schema 状态 | 全部合格 | ✅ 维持 |
| SSL 证书 | 2026-09-25 到期 | ✅ 已续期 |

---

## Step 1: Core Web Vitals

| 页面 | 方法 | 结果 |
|:---|:---|:---|
| 首页 (subao.tw/) | PageSpeed API | 🔴 429 配额耗尽（连续第5周） |
| food-shipping-guide | PageSpeed API | 🔴 429 配额耗尽 |
| tw-to-cn-shipping-guide | PageSpeed API | 🔴 429 配额耗尽 |

> ⚠️ **建议**：当前方案无 PageSpeed API Key，429 限制已持续 5 周。建议：(1) 申请 PageSpeed Insights API Key 或 (2) 用 Lighthouse CLI 本地跑批量测试。
> 好消息：全站 HTML 响应时间约 1-1.5s（curl 实测），Cloudflare CDN 加速效果明显。

---

## Step 2: Schema 验证

### food-shipping-guide ✅
| Schema 类型 | 状态 | 详情 |
|:---|:---:|:---|
| Article | ✅ | headline/description/author/publisher/datePublished 完整 |
| FAQPage | ✅ | 19 条 FAQ（涵盖鳳梨酥/泡麵/肉乾/海產/關稅/中秋月餅等） |
| HowTo | ✅ | 5 步骤（評估→包裝→取件→運輸→送達） |
| BreadcrumbList | ✅ | 3 级面包屑 |
| WebPage + Speakable | ✅ | CSS selector 指定 |

### tw-to-cn-shipping-guide ✅
| Schema 类型 | 状态 | 详情 |
|:---|:---:|:---|
| Article | ✅ | @graph 格式，完整 |
| FAQPage | ✅ | 22 条 FAQ（新手入门+运费+时效+包装+清关等） |
| HowTo | ✅ | 7 步完整流程 |
| BreadcrumbList | ✅ | 3 级面包屑 |
| WebPage | ✅ | 含 Organization + Person |
| 格式 | ✅ | @graph 单块 JSON-LD，符合 Google 推荐 |

### 首页 ✅
| Schema 类型 | 状态 |
|:---|:---:|
| BreadcrumbList | ✅ |
| FAQPage | ✅ |

> **总结**: 全站 Schema 无错误，无需修复。Schema 丰富度继续碾压竞品。

---

## Step 3: 全站 Broken Link 扫描

```
总 URL: 262
可达:   262 (100%)
错误:   0

✅ 零 Broken Link！
```

> 上周(8/3) 224 URL 全绿，本周 262 URL 仍全绿。较上周 +38 URL，主要为中秋专题和品牌页扩展。

---

## Step 4: 竞品动态

### 🆕 tyaward.com.tw — **新竞品警告！**
- 发布 3 篇极高质量内容：
  1. 「台灣寄大陸多少免稅？包裹限額與關稅計算完整解析」— 超详细（2000+ 字，含税率表、计算公式、FAQ）
  2. 「台灣人怎麼寄東西到大陸？超詳細郵局與快遞運送、關稅及禁運限制」— 三大管道比较 + 禁运清单
  3. 「台灣寄大陸包裹怎麼寄？四大管道比較與關稅避雷密技」— 四管道对比
- 特点：内容极深、结构清晰、税率数据详实、含引用来源
- **威胁等级**: 🟡 中高 — 内容质量不输 subao

### mingsung.com.tw
- 发布「2026 台灣寄大陸 B2B 出口全攻略」— 10 步流程 + E-E-A-T 强信号（百年企业背书）
- 英文站 minsheng-logistics.com 持续更新 Cross-Strait 内容
- B2B 方向继续发力

### 3168.tw
- news/62「台灣寄貨到中國大陸幾天到？物流時效天數與費用比較」— 五大管道对比，内容扎实
- 仍是高频内容产出

### twtk56.com
- news/2776「台湾邮寄东西到大陆怎么便宜」— 吃定"便宜"关键词
- news/2791「台湾寄包裹到大陆注意什么」— 合规提醒
- 低价定位持续吸引价格敏感用户

### sps-tw.com.tw (鑫祥順)
- 「台灣寄大陸避坑指南」— 通關限制+禁寄物品+关税计算

### ttnews.tw
- 「台灣寄大陸哪家快遞便宜？一篇詳盡比價與選擇指南」— 新鲜出炉

---

## Step 5: 内容差距分析

### 🟢 subao 优势保持
- 食品品类深度（30+ 品牌专项页 + 食品寄送全攻略）
- 中秋专题矩阵（8 篇：月饼/礼品/包装/成本/踩坑等）
- FAQ Schema 量级（food-shipping 19 条 + tw-to-cn 22 条）
- 品类细致度（泡麵品牌逐个解析、零食品牌逐个覆盖）
- 262 sitemap URL 远超竞品

### 🔴 竞品覆盖但 subao 缺失/薄弱的领域

| 领域 | 竞品覆盖 | subao 状态 | 优先级 |
|:---|:---|:---|:---:|
| 「費用對比 2026」Pillar Page | 3168/ttnews/tyaward 均有 | 🔴 连续第6周未发布 | P0 |
| 免税/关税详细计算器 | tyaward 极详细 | 有提及但不如竞品深入 | P1 |
| B2B 出口攻略 | mingsung 强攻 | cross-strait-logistics 系列有涉猎但不深入 | P2 |
| 各管道时效详细对比 | 3168/news/62 五管道 | tw-to-cn-express-comparison 存在 | ✅ OK |
| 便宜寄大陆攻略 | twtk56 专攻 | tw-to-cn-cheapest-shipping 存在 | ✅ OK |

### 🟡 新发现的内容机会
- **「台灣寄大陸多少免稅」专题**: tyaward 的内容已经登上搜索结果，这是高搜索量长尾词
- **「台灣寄大陸注意事項」checklist 型内容**: twtk56/鑫祥順 都在做，subao 可以做一个交互式 checklist

---

## Step 6: 本周内容更新

本周新增/更新 3 篇（8/9）：
1. blog/imei-foods-shipping — 義美食品寄送
2. blog/science-noodles-shipping — 科學麵寄送
3. blog/uni-president-noodles-shipping — 統一麵寄送

> 本周更新量较上周（23篇）大幅下降。中秋专题（8篇）上周已完成。

---

## 政策动态

- 泉州→台中大三通海运快件进口试点持续推进（大陆→台湾方向）
- 目前对 subao 台湾→大陆方向影响有限，但双向物流趋势值得关注
- 未发现新的两岸寄递政策变化

---

## 下周建议（按优先级排列）

### P0 — 必须做
1. **发布「台灣寄大陸費用對比 2026」Pillar Page**（连续第6周建议）
   - tyaward 和 ttnews 的对比类内容开始大量出现，窗口在缩小
   - 建议结构：邮局 vs 顺丰 vs 小三通 vs 专线 vs 集运 → 含真实案例

2. **应对 tyaward.com.tw 崛起**
   - 分析其「免稅解析」文章 → 如果 subao 覆盖不足，立即补「台灣寄大陸關稅完整解析」
   - 关注 tyaward 是否会继续产出两岸物流内容

### P1 — 尽快做
3. **申请 PageSpeed Insights API Key**
   - 连续 5 周无法获取 CWV 数据，审计质量受限
   - 或使用 Lighthouse CLI 批量跑 3 个关键页面

4. **优化 tw-to-cn-shipping-guide 的 meta description**
   - 当前 CTR 可能因竞品大量对比内容而被稀释
   - 建议加入「2026最新」+「價格對比」等差异化锚点

5. **建立「關稅計算器」互动工具页**
   - tyaward 的内容优势在于税率表详细
   - subao 可以做一个交互式计算器 → 难以被复制

### P2 — 可考虑
6. **site:subao.tw 索引问题持续调查**
   - 连续 5 周 site: 搜索不返回本站结果，但 GSC 有数据
   - 可能是 Cloudflare 的 robot 访问控制过于严格
   - 建议排查 robots.txt 和 Cloudflare WAF 规则

7. **SSL 证书**: 2026-09-25 到期，建议 9 月初续期

---

## 历周趋势

| 周次 | URL | Broken | 索引 | Schema | 竞品 | 关键事件 |
|:---|:---:|:---:|:---:|:---:|:---|:---|
| 7/13 | 24 | 0 | ⚠️ | ⚠️ | 3168 高频 | 初版审计 |
| 7/20 | 147 | 0 | ⚠️ | ✅ | mingsung B2B | GSC 29K 展现 |
| 7/27 | 160 | 2×404 | 🔴 | ✅ | twtk56 崛起 | 2 个 404(已修复) |
| 8/3 | 224 | 0 | 🔴 | ✅ | mingsung 2026攻略 | 中秋8篇+零食12篇 |
| **8/10** | **262** | **0** | **🔴** | **✅** | **tyaward 🆕** | SSL已续期,连续5周site:无结果 |

---

**下周审计**: 2026-08-17
**下次自动化执行**: 周一 10:00 AM
