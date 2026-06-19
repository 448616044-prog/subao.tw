# subao.tw SEO 框架总览 v2.0

> 更新：2026-06-19 | 状态：Phase 3 执行中

---

## 一、技术健康基线

| 指标 | 当前值 | 目标 | 状态 |
|:---|:---|:---|:---:|
| 总 URL | 104 | — | — |
| Blog 文章 | 80 | 100+ | 🟡 |
| Sitemap URL | 89 | 103 | 🟡 |
| 已索引 (GSC) | 58 | 85+ | 🔴 |
| 索引率 | 65% | 85%+ | 🔴 |
| DR | 0 | 15+ | 🔴 |
| 标准快递残留 | 0 | 0 | ✅ |
| GSC 结构化数据错误 | 3 (缓存) | 0 | 🟡 |

### Schema 覆盖
| Schema 类型 | 页数 | 覆盖率 |
|:---|:---:|:---:|
| BreadcrumbList | 98 | 94% |
| FAQPage | 92 | 88% |
| Article | 22 | 21% |
| HowTo | 5 | 5% |
| VideoObject | 3 | 3% |
| Organization | 1 | 1% |

### 内容深度
| 大小 | 数量 | 评价 |
|:---|:---:|:---|
| >50KB (深度) | 15 | 好 — 核心页面内容充实 |
| 30-50KB (标准) | 45 | 好 — 大部分页面达标 |
| 15-30KB (偏薄) | 20 | 🟡 — 9个城市页+11个轻量页需加厚 |

---

## 二、信息架构

### URL 层级
```
subao.tw/
├── index.html              (首页)
├── pricing.html            (定价 — 359内链)
├── about.html              (关于 — 234内链)
├── faq.html                (FAQ — 221内链)
├── tw-to-cn.html           (台湾发大陆 — 233内链)
├── article-list.html       (文章列表 — 238内链)
├── express-comparison.html (快递对比 — 206内链)
├── can-i-ship.html         (可以寄吗 — 157内链)
├── customs-guide.html      (关税速查 — 134内链)
├── partners.html           (合作伙伴 — 125内链)
├── pricing-calculator.html (运费计算器 — 191内链)
├── volume-calculator.html  (体积计算器 — 128内链)
├── contact-form.html       (留言表单 — 51内链)
└── blog/
    ├── *-shipping-guide.html     (物品/城市寄送指南 x25)
    ├── tw-to-cn-*.html           (台湾→大陆专题 x20)
    ├── *-repair-return*.html     (返修退貨 x6)
    ├── *-shipping.html           (寄送品类 x15)
    ├── case-*.html               (案例 x1)
    └── 其他                       (x13)
```

### 内链健康
| 评估项 | 状态 |
|:---|:---:|
| 孤立页面 | 1 (contact-form 仅 header/footer 链接) |
| 未入 article-list | 0 ✅ |
| 内链集中度 | 根页面占 70%+ 内链，blog 页互链偏弱 |
| 城市页互链 | 9 个城市页之间互链少 |

---

## 三、关键词覆盖矩阵

### 整体覆盖
| 层级 | 目标词数 | 已覆盖 | 待建 |
|:---|:---:|:---:|:---:|
| 短词 (1-2词) | 10 | 8 | 2 |
| 中词 (3-4词) | 40 | 35 | 5 |
| 长尾词 (5词+) | 100+ | 55 | 45+ |
| **合计** | **150+** | **98 (65%)** | **52+** |

### 短词覆盖详情
| 关键词 | 目标页 | 状态 |
|:---|:---|:---:|
| 台灣寄大陸 | 首页 | ✅ |
| 台灣快遞 | tw-express-service | ✅ 新上线 |
| 台灣物流 | 首页 | ✅ |
| 寄大陸 | 首页 | ✅ |
| 大陸快遞 | tw-express-service | ✅ |
| 台灣郵寄 | post-office-vs-subao | ✅ |
| 國際快遞 | express-comparison | ✅ |
| 跨境物流 | 首页 | ✅ |
| 台灣集運 | consolidation-shipping | ✅ 新上线 |
| 兩岸物流 | 首页 | ✅ |

### 未覆盖关键词 Gap
| 优先级 | 关键词 | 类型 | 建议 |
|:---:|:---|:---|:---|
| 🔴 | 台湾寄大陆推荐 | 中词 | 需专题对比页 |
| 🔴 | 台湾寄大陆哪家好 | 中词 | 竞品对比页 |
| 🟡 | 台湾寄大陆海运价格 | 长尾 | 扩展 tw-to-cn-sea-freight |
| 🟡 | 台湾寄大陆药物 | 中词 | 已有部分，需独立页 |
| 🟡 | 台湾寄大陆文件 | 中词 | 快速文档寄送 |
| 🟢 | 50+ 城市+物品组合长尾 | 长尾 | 模板批量 |

---

## 四、内容矩阵

### 品类覆盖（敏感货为核心优势）
| 品类 | 独立页 | FAQ覆盖 | 搜索量信号 |
|:---|:---:|:---:|:---:|
| 食品 | ✅ food-shipping-guide | 强 | 高 (52%点击) |
| 茶葉 | ✅ tea-shipping-guide | 强 | 中 |
| 保健品 | ✅ health-products-shipping | 强 | 中 |
| 化妝品 | ✅ cosmetics-shipping | 强 | 中 |
| 3C/電子 | ✅ electronics-shipping | 强 | 中 |
| 電池 | ✅ battery-products-shipping | 中 | 低 |
| 書籍/文化 | ✅ books-culture-shipping | 中 | 低 |
| 衣服/鞋子 | ✅ clothing-shoes-shipping | 中 | 低 |
| 首飾/水晶 | ✅ jewelry-crystal-shipping | 中 | 低 |
| 中藥 | ✅ chinese-medicine-shipping | 中 | 低 |
| 醫療用品 | ✅ medical-supplies-shipping | 中 | 低 |
| 嬰兒用品 | ✅ baby-products-shipping | 中 | 低 |
| 燕窩/人參 | ✅ birds-nest-ginseng-shipping | 中 | 低 |
| 個人行李 | ✅ personal-belongings-shipping | 低 | 低 |

### 城市覆盖（Programmatic SEO 模板）
| 城市 | 页面 | 区域定价 | 时效 | 区名 |
|:---|:---|:---|:---|:---|
| 上海 | ✅ | 華東 A290/B360 | 5-6天 | ✅ |
| 深圳 | ✅ | 華南 A290/B360 | 4-5天 | ✅ |
| 廣州 | ✅ | 華南 A290/B360 | 5-6天 | ✅ |
| 廈門 | ✅ | 華南 A290/B360 | 4-5天 | ✅ |
| 北京 | ✅ | 華北 A320/B390 | 5-6天 | ✅ |
| 成都 | ✅ | 西南 A330/B410 | 5-6天 | ✅ |
| 重慶 | ✅ | 西南 A330/B410 | 5-6天 | ✅ |
| 南京 | ✅ | 華東 A290/B360 | 5-7天 | ✅ |
| 武漢 | ✅ | 華中 A300/B380 | 5-6天 | ✅ |
| 杭州 | ✅ | 已有 (hangzhou) | — | 需审核 |
| 東莞 | ❌ | — | — | 待建 |
| 蘇州 | ❌ | — | — | 待建 |

### 返修/退貨 Cluster
| 场景 | 页面 | 状态 |
|:---|:---|:---:|
| Hub 页 | tw-to-cn-repair-return-hub | ✅ |
| 手机/笔电 返修 | phone-laptop-repair-return | ✅ |
| 电商退貨 | ecommerce-platform-return | ✅ |
| 设备返修 | equipment-machinery-repair-return | ✅ |
| 电子产品返修 | electronics-repair-return-shipping | ✅ |
| 二手电子产品返修 | used-electronics-repair-shipping | ✅ |
| 一般商品退貨 | product-return-shipping | ✅ |
| 双向物流 | cross-strait-bidirectional-logistics | ✅ |

---

## 五、外链建设进度

### 当前状态
| 指标 | 值 |
|:---|:---:|
| DR | 0 |
| Referring Domains | 0 |
| 外链速查卡 | 已生成 (28个目标 x 5梯队) |
| 第一梯队提交 | 待确认 |
| FB 粉丝页 | 被锁，待恢复 |

### 外链策略
| 梯队 | 目标 | 数量 | 状态 |
|:---:|:---|:---:|:---:|
| T1 目录提交 | 台湾商业目录 | 8 | 待执行 |
| T2 本地平台 | Dcard/PTT/Medium | 5 | 待注册 |
| T3 博客/论坛 | Pixnet/Blogger | 5 | 待注册 |
| T4 行业站点 | 物流/贸易相关 | 5 | 待研究 |
| T5 内容分发 | 文章转载/引用 | 5 | 待规划 |

---

## 六、待执行优先级

### 🔴 P0 — 立即（本周）
| 任务 | 说明 | 负责 |
|:---|:---|:---:|
| GSC URL 提交 | 剩余 10 个新页 (6/20) | 阿龙 |
| 结构化数据验证 | 确认 3 个 GSC 报错已清除 | 待重抓 |
| 城市页加厚 | 9 个城市页补充 500-1000 字场景内容 | AI |
| 杭州页审核 | 价格/区名/时效对齐 | AI |

### 🟡 P1 — 下周
| 任务 | 说明 | 负责 |
|:---|:---|:---:|
| 外链第一梯队 | 8 个目录提交 | 阿龙 |
| 外链平台注册 | Dcard/PTT/Medium 账号 | 阿龙 |
| 文章内链加固 | 城市页互链 + 品类页互链 | AI |
| 对比评测页 | "台湾寄大陆哪家好" pillar | AI |
| 药物独立页 | 台湾寄大陆药物专题 | AI |

### 🟢 P2 — 两周内
| 任务 | 说明 | 负责 |
|:---|:---|:---:|
| 返修 cluster 扩展 | +2-3 个场景页 | AI |
| 城市页扩展 | 东莞/苏州/天津/西安 | AI |
| 长尾 FAQ 批量 | 50 个 Q&A 嵌入相关页 | AI |
| Schema Rich Result 监控 | 追踪 FAQ/HowTo 展现 | 观察 |

### 🔵 P3 — 月度
| 任务 | 说明 |
|:---|:---|
| GSC 数据月报 | 排名变化分析 |
| 竞品监测 | 75sea/yilinyi 内容动向 |
| 内容分发 | Dcard/PTT/Medium 发文 |
| 视频 SEO | YouTube 视频优化（标题/描述/标签） |

---

## 七、风险监控

| 风险 | 概率 | 影响 | 缓解措施 |
|:---|:---:|:---:|:---|
| DR=0 长期不涨 | 高 | 高 | 外链建设必须启动 |
| 食品季後流量下降 | 中 | 中 | 扩大品类覆盖，不依赖单品 |
| Cloudflare 缓存旧版 | 低 | 中 | 每次部署后 curl 验证 |
| GSC 索引速度慢 | 中 | 中 | 每日提交 + sitemap 刷新 |
| 结构化数据错误 | 低 | 低 | 每次发新页前验证 JSON-LD |
| SSL 证书到期 | 低 | 高 | 7/21 提醒续期 (到期 7/28) |

---

## 八、核心 KPI 追踪

| KPI | 当前 | 30天目标 | 90天目标 |
|:---|:---:|:---:|:---:|
| 有机点击/月 | 73 | 150 | 500 |
| 已索引页 | 58 | 80 | 100 |
| DR | 0 | 5-8 | 15+ |
| 首页转化率 | 10.6% | 保持 | 12%+ |
| 回访率 | 9% | 15% | 25% |
| Featured Snippet | 0 | 2-3 | 10+ |
| 非品牌流量占比 | 100% (DR=0) | 100% | 95%+ |

---

*文档版本：v2.0 | 更新：2026-06-19*
