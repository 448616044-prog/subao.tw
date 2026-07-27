# subao.tw 每周深度审计报告

**日期**: 2026-07-27（周一）
**审计范围**: 全站技术 / Schema / Broken Link / 竞品 / 内容差距
**上次审计**: 2026-07-20

---

## 一、执行摘要

| 维度 | 状态 | 变化 |
|------|------|------|
| Core Web Vitals | ⚠️ 无数据 | API 连续第3周 429 |
| Google 索引 | 🔴 site: 不返回 | 与上周相同 |
| Schema | ✅ 全部合格 | 维持 |
| Broken Links | 🟡 2个404 | 上周0个 |
| 竞品动态 | 🟡 3168/mingsung 活跃 | 无重大变动 |
| 内容覆盖 | 🟢 品类领先 | 维持 |

---

## 二、Core Web Vitals

**⚠️ 无法获取数据** — PageSpeed API 连续第3周返回 429 Quota Exceeded。

- 原因：`project_number:583797351490` 的每日配额为 0
- 影响：无法追踪性能变化趋势
- 上周 Lighthouse 实测参考：首页 77分/LCP 4010ms，food-shipping 70分/LCP 3758ms，tw-to-cn 84分/LCP 3245ms
- **建议**: 考虑更换 PageSpeed API key 或使用 CrUX API 获取真实用户数据

---

## 三、Google 索引状态

**🔴 site:subao.tw 仍未返回本站结果**

Google 搜索 `site:subao.tw` 返回的结果全部是不相关域名（sobute.com, subaonet.com 等），Google 进行了模糊匹配。

但有 GSC 数据（上周 29,145 展现）证明页面实际已被索引。这是 Google 的 site: 操作符行为问题，不是索引问题。

**行动**: 继续依赖 GSC 数据监控索引状态，不必过度担心 site: 结果。

---

## 四、Schema 结构化数据验证

### food-shipping-guide ✅
| Schema 类型 | 状态 | 详情 |
|-------------|------|------|
| Article | ✅ | 含 headline, datePublished, author |
| FAQPage | ✅ | **19条** FAQ，结构化完整 |
| HowTo | ✅ | 完整步骤指引 |
| BreadcrumbList | ✅ | 面包屑路径正确 |
| WebPage | ✅ | 含 @id, name, description |

⚠️ 注意：5个独立 JSON-LD block（非 @graph 格式），Google 支持多 block 但不如 @graph 优雅。

### tw-to-cn-shipping-guide ✅
| Schema 类型 | 状态 | 详情 |
|-------------|------|------|
| BreadcrumbList | ✅ | |
| Article | ✅ | |
| FAQPage | ✅ | **22条** FAQ |
| HowTo | ✅ | |

✅ @graph 格式，1个 block 包含全部，最规范。

### 首页 ✅
| 元素 | 状态 |
|------|------|
| BreadcrumbList | ✅ |
| FAQPage | ✅ |
| title | ✅ 含品牌词+品类词+价格锚点 |
| meta description | ✅ 含 CTA + 痛点 |
| canonical | ✅ |
| hreflang (zh-Hans → subaotw.cn) | ✅ |
| meta keywords | ✅ |

**结论**: Schema 全部健康，无错误。本周无 Schema 修改需求。

---

## 五、Broken Link 扫描

**扫描范围**: sitemap.xml 全部 160 个 URL

| 状态 | 数量 | 占比 |
|------|------|------|
| ✅ 2xx/3xx | 156 | 97.5% |
| ❌ 404 | 2 | 1.25% |
| ⚠️ Timeout | 2 | 1.25% |

### 404 错误（需修复）

| URL | 问题 |
|-----|------|
| `https://subao.tw/blog/cross-strait-logistics-guide` | 返回 404 |
| `https://subao.tw/blog/baby-formula-milk-powder-shipping` | 返回 404 |

### Timeout（需排查）

| URL | 问题 |
|-----|------|
| `https://subao.tw/blog/post-office-rejected-parcel-solution` | 读取超时 |
| `https://subao.tw/blog/skincare-products-shipping` | 读取超时 |

**行动建议**:
1. **P0**: 修复 2 个 404 — 检查页面是否已删除，若删除则设置 301 跳转
2. **P1**: 排查 2 个 timeout 页面 — 可能是页面过重或服务器响应慢
3. **P1**: 从 sitemap 中移除 404 URL，避免向 Google 提交死链

---

## 六、竞品监控

### 3168.tw（宸弘全球聯運）
- 高频产出，每周至少 1-2 篇新内容
- 最新文章：`news/193` "2026 最新！台灣寄包裹到大陸全攻略"（7月更新）
- 其他活跃页面：news/62（时效费用对比）、news/69（寄文件）、news/175（一站式方案）
- BRAND: "台灣到大陸海運第一品牌"
- 策略：用 news 目录做 SEO 内容矩阵，覆盖面广但深度一般

### mingsung.com.tw（民生國際物流）
- 2026年5月更新 "2026寄大陸全攻略"，内容极为详尽
- 定位 B2B：ECFA 早收清单、正式报关、增值税发票抵扣
- 新增英文站 `minsheng-logistics.com`，推陆运服务（FTL/LTL/冷链/跨境）
- 策略：B2B 高端路线，强调 40 年经验

### spsexpress.com.tw（鑫祥順）/ amituo.com.tw（鼎运）
- 稳定运营，2026 更新价格表
- 策略：传统物流公司，SEO 内容少，靠品牌+线下口碑

### 新进入者
- `twtk56.com` — 新站点，有多篇寄大陆文章，内容偏搬运/聚合
- `upbuygo.com` — 禁运说明页，有一定 SEO 价值

### 政策动态
- 泉州启动对台海运快件进口业务试点（泉州→台中大三通航线），7月24日发布
- 方向是大陆→台湾（非 subao 主营的台湾→大陆），但对整体两岸物流格局有影响

### 对比 subao 的竞争位置
| 维度 | subao.tw | 3168.tw | mingsung | spsexpress |
|------|----------|---------|----------|------------|
| 内容深度 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐ |
| 内容频率 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐ |
| Schema SEO | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐ |
| B2C 定位 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| 工具/互动 | ⭐⭐⭐⭐ | ⭐ | ⭐ | ⭐ |

**结论**: subao 在内容深度、Schema SEO、工具矩阵上明显领先。竞品的优势在于产出频率（3168）和 B2B 深度（mingsung）。

---

## 七、内容差距分析

### subao 已覆盖（竞品缺失或薄弱）
- ✅ 品类级深度（食品下分 22 种单品，每品独立页）
- ✅ FAQ Schema 量级（19-22 条/页，竞品大多 5-8 条或不规范）
- ✅ 工具矩阵（能不能寄/运费试算/材积计算/价格指数）
- ✅ 城市级寄送指南（北京/上海/深圳/广州/成都/重庆等）
- ✅ 返修退货系列（手机/笔电/设备返修）

### 竞品覆盖（subao 缺失或薄弱）
| 内容缺口 | 竞品代表 | 优先级 |
|----------|----------|--------|
| 「2026 寄大陸費用對比」Pillar Page | 3168/news/62, mingsung 全攻略 | 🔴 P0 |
| 寄文件到大陸指南 | 3168/news/69 | 🟡 P1 |
| 大陆→台湾 反向物流 | — | 🟢 P2 |
| B2B 正式报关/增值稅发票 | mingsung | 🟢 P2（战略选择） |
| 英文版 / 多语言 | mingsung 新英文站 | 🟢 P2 |

### 本周新发现的关键词缺口
- 「台灣寄大陸運費比較 2026」→ 竞品 twtk56.com 和 3168/news/62 都在抢
- 「台灣寄快遞到大陸最便宜」→ 多个竞品有专门的价格对比页
- 「台灣寄大陸海運」→ subao 有 sea-freight 页但可强化

---

## 八、本周流量变化

⚠️ 无 GSC 实时数据（自动化环境无 API 接入）

基于上周（7/20）基准：
- GSC 展现：29,145
- 点击：估算 1,200-1,500
- CTR：约 4-5%

**本周推测**: 7月下旬暑假寄件潮，食品/伴手礼相关搜索量可能上升。

---

## 九、下周行动建议

### P0 — 本周必须做
1. **修复 2 个 404 页面** — cross-strait-logistics-guide、baby-formula-milk-powder-shipping
2. **清理 sitemap** — 移除 404 URL，提交 GSC Indexing API
3. **发布「台灣寄大陸費用對比 2026」Pillar Page** — 汇总所有渠道价格+时效+适用场景（连续第三周建议，不能再拖）

### P1 — 本周尽量做
4. **排查 2 个 timeout 页面** — post-office-rejected-parcel-solution、skincare-products-shipping
5. **更新 food-shipping-guide meta** — 7 月食品搜索量上升，测试新标题
6. **写一篇「寄文件到大陸」** — 竞品 3168/news/69 排名不错，我们缺这个

### P2 — 有时间就做
7. **监控 3168.tw 新文章频率** — 如果他们在 7 月底有暑假寄件潮内容，及时反应
8. **考虑更新 tw-to-cn-shipping-guide 的 2026 年时效/价格数据** — 保持 freshness 信号

---

## 十、历史趋势追踪

| 指标 | 7/13 | 7/20 | 7/27 |
|------|------|------|------|
| Broken Link | 0 | 0 | 2 ⚠️ |
| Schema 错误 | — | 0 | 0 |
| PageSpeed 得分 | — | 77/70/84 | N/A |
| site: 索引 | ⚠️ | ⚠️ | ⚠️ |
| 3168 新文章 | +2 | +1 | ~+1 |
| mingsung 更新 | 2026攻略 | B2B出口+寄大陸 | 英文站扩展 |
| GSC 展现 | — | 29,145 | 待下周 |

---

*报告生成: 2026-07-27 09:50 | 自动化审计 @subao-tw-seo*
