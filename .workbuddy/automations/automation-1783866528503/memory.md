# 自动化执行历史 — subao.tw 每周审计

## 2026-07-13 执行

**结果**：
- Broken Links: 24/24 = 200 OK ✅
- Google 索引: ⚠️ site:subao.tw 未返回有效收录结果（疑似未索引）
- Core Web Vitals: ⚠️ PageSpeed API 429 配额耗尽，Web UI JS 未渲染
- Schema: ⚠️ Rich Results Test JS 渲染未完成
- 竞品: 3168.tw 高频产出（news/193 全攻略、news/167 趋势攻略），mingsung 发布 2026 攻略
- 政策: 中華郵政 2026-01 停航空掛號小包，04-29 EZPost 擴展
- 内容差距: 缺失泛用型「2026 攻略」，但在品类深度上领先

**报告路径**: `weekly-audit-20260713.md`

---

## 2026-07-20 执行

**结果**：
- Broken Links: 147/147 全部可达 ✅（含1个301 redirect widget/index→widget/）
- Google 索引: ⚠️ site:subao.tw 仍未返回本站结果，但 GSC 29,145 展现证明有索引
- Core Web Vitals: 🟡 Lighthouse 实测 — 首页 77/4010ms LCP, food-shipping 70/3758ms, tw-to-cn 84/3245ms。CLS 全绿。PageSpeed API 429 配额耗尽。
- Schema: ✅ food-shipping-guide（Article+FAQPage+BreadcrumbList）和 tw-to-cn-shipping-guide（@graph格式，22条FAQ）均完整有效
- 竞品: 3168.tw 继续高产（193全攻略/155大貿小貿），mingsung 发了 B2B 出口+寄大陸双份2026攻略，spsexpress 稳定
- 内容差距: B2B方向（ECFA/增值稅/大貿小貿/Incoterms）竞品覆盖但subao缺失 — 属战略选择
- 优势保持: 食品品类深度、超具体长尾词排名（凤梨酥#4.3/维力炸酱面#3.7）、FAQ Schema 量级领先
- 下周 P0: 图片性能优化 + 「台灣寄大陸費用對比 2026」Pillar Page

**报告路径**: `weekly-audit-20260720.md`

---

## 2026-07-27 执行

**结果**：
- Broken Links: 156/160 OK，2个404（cross-strait-logistics-guide, baby-formula-milk-powder-shipping），2个timeout
- Google 索引: 🔴 site:subao.tw 仍不返回本站结果（连续3周），但 GSC 有展现证明收录
- Core Web Vitals: ⚠️ PageSpeed API 连续第3周 429 配额耗尽，无法获取
- Schema: ✅ food-shipping-guide（5 block: Article+FAQPage(19)+HowTo+Breadcrumb+WebPage）、tw-to-cn-shipping-guide（@graph: 4类型含FAQPage(22)）、首页（Breadcrumb+FAQPage+meta完整）全部合格
- 竞品: 3168.tw news/193 更新7月全攻略，mingsung 英文站扩展陆运服务，twtk56.com 新站崛起
- 政策: 泉州→台中大三通海运快件进口试点（大陆→台湾方向）
- 内容差距: 「台灣寄大陸費用對比 2026」Pillar Page 连续第3周建议但仍未发布（P0）

**报告路径**: `weekly-audit-20260727.md`

---

## 2026-08-03 执行

**结果**：
- Broken Links: 224/224 = 200 OK ✅（较上周+64 URL，上周2个404已修复）
- Core Web Vitals: 🔴 PageSpeed API 连续第4周 429 配额耗尽
- Google 索引: 🔴 site:subao.tw 连续第4周不返回本站结果
- Schema: ✅ food-shipping-guide（Article+FAQPage(19)+HowTo(5)+BreadcrumbList+WebPage+Speakable）和 tw-to-cn-shipping-guide（@graph格式）均完整有效
- 竞品: mingsung 持续更新2026攻略+B2B出口攻略；3168.tw 发布搬家攻略(197)；twtk56.com 低价路线崛起（"怎么便宜寄"2776）；101jiyun 新食品攻略
- 政策: 泉州→台中大三通海运快件进口试点（大陆→台湾方向）
- 内容亮点: 本周23篇新增（中秋专题8篇+零食品牌12篇+），sitemap 224 URL 创新高
- 内容差距: Pillar Page「費用對比 2026」连续第4周未发布（P0）；tw-to-cn-shipping-cost-ultimate-guide 部分填补缺口
- subao 优势: 食品品类深度+30+品牌专项页+中秋8篇专题+FAQ Schema量级+Schema丰富度 全面碾压竞品
- SSL 证书: ⚠️ 到期日2026-07-28已过，需确认续期状态

**报告路径**: `weekly-audit-20260803.md`
