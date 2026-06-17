# subao.tw 内容保鲜机制 SOP

## 核心原则
- **改实质，不改表面**：每次刷新必须添加 10-15% 新内容，绝不只改日期
- **流量导向**：优先刷新高流量页面（top 10），投入产出比最高
- **案例驱动**：用真实客户咨询作为更新素材，天然去 AI 味且独一无二

---

## 保鲜频率

| 页面类型 | 数量 | 刷新频率 | 每次改动量 |
|:---|:---:|:---|:---|
| Top 10 流量页 | 10 | **每 2 个月** | 10-15% 新内容 |
| Top 11-20 | 10 | **每 3 个月** | 5-10% 新内容 |
| 其余 blog 页 | ~37 | **每 6 个月** | 1 段新内容 |
| 核心页（首页/运费/关于）| 5 | **每 3 个月** | 视情况 |

---

## Top 10 核心页面清单（按 GSC 流量）

| # | 页面 | GSC 点击 | 上次刷新 |
|:---:|:---|:---:|:---:|
| 1 | food-shipping-guide | 66 | 2026-06-17 ✅ |
| 2 | prohibited-items | 14 | 待刷新 |
| 3 | cosmetics-shipping | 11 | 2026-06-17 ✅ |
| 4 | battery-products-shipping | 9 | 2026-06-17 ✅ |
| 5 | electronics-shipping | 8 | 2026-06-17 ✅ |
| 6 | tea-shipping-guide | 7 | 待刷新 |
| 7 | health-products-shipping | 5 | 待刷新 |
| 8 | ezway-tutorial | 5 | 待刷新 |
| 9 | shopee-shipping | 5 | 待刷新 |
| 10 | taiwan-medicine-to-china | 5 | 待刷新 |

---

## 标准刷新动作清单

每次刷新页面时，至少完成以下 **3 项中的 2 项**：

### 1. 加「最新咨询回馈」板块
```
<h2>🆕 2026年X月最新諮詢回饋</h2>
<ul>
  <li><strong>物品名称 寄目的地</strong>：具体描述，运费，时效，注意事项。</li>
  <li>... 至少 2-3 条</li>
</ul>
```
素材来源：LINE 客服真实问题、GSC 搜索词

### 2. 加 1-2 条新 FAQ
- 从 GSC 数据中找用户实际搜索的问题
- 同时更新 Schema FAQPage
- FAQ 是 Google PAA（People Also Ask）的主要来源

### 3. 加内链 + 交叉推荐
- 链接到 1-2 个新发布的关联页面
- 示例：health-products → baby-products、electronics → car-parts

---

## 更新后必检清单

- [ ] 实际添加了新内容（不少于 3 段/3 条）
- [ ] 更新 `<meta name="lastmod">` 为当天日期
- [ ] 更新 Schema `dateModified` 为当天日期
- [ ] 页面在浏览器中打开验证无排版问题
- [ ] Git commit message 注明具体改动（不写"刷新"）

---

## 下一轮刷新时间
- **2026年8月**：Top 10 全量刷新
- **2026年7月**：prohibited-items + tea-shipping + health-products（本轮未完成的）

---

## 避坑指南

| ❌ 不要 | ✅ 要 |
|:---|:---|
| 只改日期不改内容 | 每次至少加 3 段新文字 |
| 批量全站改 lastmod | 差异化管理，每页单独评估 |
| 用 AI 生成的泛泛文字 | 用真实客户案例 + GSC 搜索词 |
| 改 Title/URL 结构（SEO 动作需确认）| 只在 body 内加新内容板块 |
| 刷新频率过密（<1个月） | 最少间隔 2 个月 |
