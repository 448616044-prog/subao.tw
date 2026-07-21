# 全站定价合规审计报告
**日期**: 2026-07-18
**范围**: subao.tw 全站
**背景**: P1-6/7 完成后的终扫发现大量遗漏

---

## 📊 违规汇总

| 违规类型 | 旧价格 | 铁律价格 | 涉及文件 | 总处数 | 优先级 |
|:---|:---:|:---:|:---:|:---:|:---:|
| NT$360 用于敏感货经济专线 | NT$360 | NT$290 | 15个文件 | 41处 | P0 |
| NT$380 用于特货/含电池 | NT$380 | NT$350 | ~6个文件 | ~60处 | P1 |
| NT$500 用于电器(含电池) | NT$500 | NT$350 | pricing.html + 3 blog | ~6处 | P0 |
| NT$780 用于中西药 | NT$780 | NT$290 | pricing.html | 4处 | P0 |

---

## 🔴 P0-A: NT$360 → NT$290（敏感货经济专线）

### pricing.html（主定价页，3处）
| 行号 | 位置 | 当前值 | 修改为 |
|:---|:---|:---|:---|
| L316 | 华南 B類 | NT$360/kg | NT$290/kg |
| L347 | 华东 B類 | NT$360/kg | NT$290/kg |
| L497 | 西北 A類 | NT$360/kg | NT$290/kg |

> ⚠️ pricing.html 还使用 A/B/C/D 区域定价体系。B類=NT$360、C類=NT$500、D類=NT$780 全部违反铁律。**需阿龙确认：是统一改为铁律价格，还是保留区域定价但更新各档位？**

### Blog 页面（38处 / 14个文件）
| 文件 | 处数 | 主要问题 |
|:---|:---:|:---|
| patches-ointment-shipping.html | 7 | 貼布/藥膏 敏感貨專線 NT$360 |
| health-products-shipping.html | 6 | 保健品/貼布 敏感貨 NT$360 |
| tw-to-cn-cost.html | 5 | 運費比較頁 B類 NT$360 |
| jewelry-crystal-shipping.html | 4 | 水晶首飾 B類 NT$360 |
| daily-sundries-shipping.html | 4 | 日用品 敏感貨 NT$360 |
| shopee-shipping.html | 2 | 蝦皮 敏感貨 NT$360 |
| food-shipping-guide.html | 2 | 食品寄送 A類 NT$360 |
| first-aid-shipping.html | 2 | 急救藥品 NT$360 |
| battery-products-shipping.html | 1 | 藍牙耳機 NT$360 (应为特货NT$350) |
| perfume-shipping.html | 1 | 香水/香膏 NT$360 |
| consolidation-shipping.html | 1 | 集運 敏感貨 NT$360 |
| hair-care-shipping.html | 1 | 洗護髮 B類 NT$360 |
| thermos-kettle-shipping.html | 1 | 充電式保溫杯 NT$360 (应为特货NT$350) |
| taiwan-to-china-guide.html | 1 | 總覽頁 敏感貨 NT$360 |

---

## 🔴 P0-B: pricing.html A/B/C/D 体系与铁律冲突

pricing.html 当前使用区域定价体系（华南/华东/华中/华北/西北 × A/B/C/D四档），与铁律的统一价格体系直接冲突：

### 经济专线（当前值 vs 铁律）
| 类别 | 华南 | 华东 | 华中 | 华北 | 西北 | 铁律 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| A(普货) | 290 ✅ | 290 ✅ | 300 ❌ | 320 ❌ | 360 ❌ | 290 |
| B(敏感货) | 360 ❌ | 360 ❌ | 370 ❌ | 390 ❌ | 440 ❌ | 290 |
| C(电器含电池) | 500 ❌ | 500 ❌ | 510 ❌ | 540 ❌ | 570 ❌ | 350 |
| D(中西药) | 780 ❌ | 780 ❌ | 790 ❌ | 840 ❌ | 1080 ❌ | 290 |

### 快件专线（当前值 vs 铁律）
| 类别 | 华南 | 华东 | 铁律 |
|:---|:---:|:---:|:---:|
| A(普货) | 380 ✅ | 380 ✅ | 380 ✅ |
| B(敏感货) | 450 ✅ | 450 ✅ | 450 ✅ |
| C(电器含电池) | 590 ❌ | 590 ❌ | 450 ❌ |
| D(中西药) | 870 ❌ | 870 ❌ | 450 ❌ |

> **决策点**：铁律是统一价格（不分区域），但 pricing.html 有区域差价。两个方案：
> - **方案A**：全站统一铁律价格，删除区域差价体系
> - **方案B**：保留区域定价，但 B→290、C→350、D→290（仅华南），其他区域按比例调整

---

## 🟡 P1: NT$380 → NT$350（特货/含电池产品）

以下页面将 NT$380 用于含锂电池产品（特货），应为 NT$350：

| 文件 | 处数 | 产品类型 |
|:---|:---:|:---|
| gaming-console-shipping.html | 14 | Switch/PS5/Steam Deck (含锂电池) |
| bluetooth-earphones-watch-shipping.html | 12 | AirPods/Apple Watch (含锂电池) |
| small-appliances-shipping.html | ~10 | 无线吸尘器/电动牙刷 (含锂电池) |
| ecommerce-platform-return.html | 3 | 含电池商品退货 |
| tw-to-cn-repair-return-hub.html | 3 | 手机/笔电维修 |
| tw-to-cn-cheapest-shipping.html | ~5 | 含电池产品引用 |

> 注：城市页中的 "快件線一般貨NT$380/kg" 是合法的（快件普货=NT$380），不需要改。

---

## ✅ 已完成

| 项目 | 状态 |
|:---|:---|
| 7个城市页敏感货 NT$360→NT$290 (P1-6) | ✅ 已部署 |
| 上海页敏感货 NT$360→NT$290 (P1-6遗漏) | ✅ 已部署 (commit 2845d41) |
| used-phone-tablet 特货 NT$380→NT$350 (P1-7) | ✅ 已部署 |
| 10个城市页案例研究时效+价格重算 | ✅ 已部署 |
| /blog/blog/ 错误内链 | ✅ 已清零 |
| pricing.html 导航404链接 | ✅ 已清零 |

---

## 📋 待阿龙确认

1. **pricing.html A/B/C/D 体系**：方案A（统一铁律）还是方案B（保留区域差价）？
2. **NT$360 → NT$290**：15个文件41处，涉及 Schema + body，确认后立即执行
3. **NT$380 → NT$350**：6个文件~50处特货价格，确认后立即执行
4. **NT$500/NT$780**：pricing.html C/D类价格，取决于方案A/B选择
