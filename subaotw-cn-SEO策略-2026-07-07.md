# subaotw.cn 百度SEO全面诊断 + 执行路线图
>
> 分析日期：2026-07-07
> 站点定位：大陆→台湾大件物流专线（百度SEO，简体中文）

---

## 一、站点现状快照

| 指标 | 数值 |
|:---|:---:|
| 总页面数 | 140 页 |
| 首页定位 | 大陆寄台湾大件物流（家具/搬家/设备/建材） |
| ICP备案 | 湘ICP备2026016030号-2 ✅ |
| 百度站长验证 | codeva-K4kVPs6NwjtWr4ij ✅ |
| 百度统计 | 全站已覆盖（130/130）✅ |
| 自动推送JS | 全站已覆盖 ✅ |
| API推送 | ❌ Token 失效（401），仅成功推45条 |
| 百度收录(site:) | 未查（需登录百度站长平台） |
| CSS | 引用外部 `/style.css`（非自包含）|

### 页面分布

| 目录 | 数量 | 方向 | 说明 |
|:---|:---:|:---:|:---|
| 根目录 | 21 | cn→tw | about/contact/pricing-calculator 等 |
| blog/ | 29 | 混合 | 8篇 cn→tw + ~10篇 tw→cn + 其他 |
| tw-to-cn/ | 37 | tw→cn | 台湾零食/茶葉/化妝品等寄大陆 |
| equipment/ | 20 | cn→tw | CNC/注塑/印刷等设备出口台湾（含1篇index）|
| guide/ | 21 | cn→tw | 出口指南/海关/保险/问答 |
| cases/ | 6 | cn→tw | 东莞/昆山/佛山等设备出口案例 |

---

## 二、🔴 核心问题诊断

### 问题 1：内容方向严重混搭 → 主题权威性零散

```
subaotw.cn 首页定位: "大陆→台湾大件物流"
    ├── 博客层: 8篇 cn→tw + 10篇 tw→cn ← 方向分裂！
    ├── tw-to-cn/: 37篇 台湾寄大陆 ← 与首页定位完全相反！
    ├── equipment/: 20篇 设备出口 ← 符合定位 ✅
    ├── guide/: 21篇 出口指南   ← 符合定位 ✅
    └── cases/: 6篇 设备案例   ← 符合定位 ✅
```

**Baidu 视角**：一个网站同时讲「大陆寄台湾」和「台湾寄大陆」两个完全相反的方向，搜索引擎无法判断这个站到底在哪个方向上"专"。

**后果**：
- Baiduspider 爬取时看到两个方向的内容，站点主题模糊
- 「大陆寄台湾」类关键词难以获得权威排名
- 37 篇 tw-to-cn 内容在百度站内没有最佳归宿（这些关键词用简体在百度搜不如在 Google 用繁体搜 subao.tw）

### 问题 2：tw-to-cn 内容与 subao.tw 高度重叠

| subaotw.cn (简体) | subao.tw (繁体) | 重叠判定 |
|:---|:---|:---:|
| tw-to-cn/food-shipping | blog/food-shipping-guide | ✅ 内容重叠 |
| tw-to-cn/tea-shipping | blog/tea-shipping-guide | ✅ 内容重叠 |
| tw-to-cn/cosmetics-shipping | blog/cosmetics-shipping | ✅ 内容重叠 |
| tw-to-cn/electronics-shipping | blog/electronics-shipping | ✅ 内容重叠 |
| tw-to-cn/prohibited-items | blog/tw-to-cn-prohibited-items | ✅ 内容重叠 |

**这些内容是 duplicated across domains**。Baidu 和 Google 都不会给重复内容排名。

### 问题 3：Baidu API 推送已断

- Token `K4kVPs6NwjtWr4ij` 7/5 起返回 401
- 仅 45/140 页被主动推送过
- 自动推送 JS 仍在运行但覆盖面不可控

---

## 三、关键词策略

### 确认方向：只做 大陆→台湾

放弃 tw→cn 方向的百度SEO（这个方向的主力战场是 Google + subao.tw）。37篇 tw-to-cn 内容要么归档/重定向，要么静默（noindex）。

### 短词（头词）— 高难度，需积累权重

| 关键词 | 预估难度 | 当前排名 | 策略 |
|:---|:---:|:---:|:---|
| 大陆寄台湾 | ⭐⭐⭐⭐⭐ | 未知 | 首页承载，靠整站权重拉升 |
| 海运到台湾 | ⭐⭐⭐⭐ | 未知 | 首页+海运专题页 |
| 大件物流台湾 | ⭐⭐⭐⭐ | 未知 | 首页+大件专题页 |
| 寄东西到台湾 | ⭐⭐⭐⭐ | 未知 | 首页承载 |
| 集运台湾 | ⭐⭐⭐ | 未知 | 首页+FAQ |

### 中词（品类词）— 核心战场

| 关键词 | 目标页面 | 优先级 |
|:---|:---|:---:|
| 大陆寄家具到台湾 | /blog/cn-to-tw-furniture-shipping | P0 |
| 大陆搬家到台湾 | /blog/cn-to-tw-moving-guide | P0 |
| 设备出口台湾 | /equipment/ | P0 |
| 大陆寄家电到台湾 | /blog/cn-to-tw-appliance-shipping | P0 |
| 大陆寄建材到台湾 | /blog/cn-to-tw-building-materials-shipping | P0 |
| 大陆寄大件到台湾 | /blog/cn-to-tw-large-items-shipping | P0 |
| 大陆寄钢琴到台湾 | /blog/cn-to-tw-special-large-items | P1 |
| 大陆食品寄台湾 | /blog/food-to-taiwan | P1 |
| 大陆衣服寄台湾 | /blog/clothes-to-taiwan | P1 |
| 大陆日用品寄台湾 | /blog/daily-items-to-taiwan | P1 |
| 手机寄台湾 | /blog/phone-to-taiwan | P1 |
| 游戏机寄台湾 | /blog/gaming-console-to-taiwan | P1 |

### 长尾词 — 设备/搬家/大件的大金矿

| 关键词模式 | 举例 | 承载页面 |
|:---|:---|:---|
| 大陆寄XX到台湾怎么运 | 大陆寄跑步机到台湾怎么运 | cn-to-tw-special-large-items |
| XX出口台湾手续 | CNC出口台湾手续 | equipment/cnc-export-taiwan |
| XX海运到台湾多少钱 | 家具海运到台湾多少钱 | blog/cn-to-tw-furniture-shipping |
| 大陆到台湾海运专线 | — | blog/cn-to-tw-shipping-guide |
| 从XX寄大件到台湾 | 从深圳寄大件到台湾 | blog/cn-to-tw-large-items-shipping |
| 搬家到台湾要多少钱 | — | blog/cn-to-tw-moving-guide |

---

## 四、执行路线图

### 🔴 P0 — 本周必做（不依赖数据）

#### P0-1：修复 Baidu API 推送 Token

```
当前状态: Token K4kVPs6NwjtWr4ij → 401 已失效
修复方式: 登录百度搜索资源平台 → 数据引入 → 普通收录 → 重新获取推送Token
影响: 85页未被主动推送，修复后可将未推送页面批量提交
```

#### P0-2：确定 tw-to-cn 37 页的处理方案

| 方案 | 操作 | 对SEO影响 |
|:---|:---|:---:|
| A. 静默 | 给37页加 `<meta name="robots" content="noindex,follow">` | 保留页面但不出现在搜索结果 |
| B. 删除 | 直接删文件 | 会丢页面，但百度本来也没收多少 |
| C. 重定向 | 301→subao.tw 对应页面 | 流失到台湾站，百度不认跨域301 |

**推荐方案 A**：静默 tw-to-cn 目录，保留页面但不参与百度排名。这些内容在 Google 才是好归宿（subao.tw）。

#### P0-3：首页 title/meta 优化（缩到 30 字以内）

Baidu title 显示长度 ≤ 30 汉字：

| 项 | 当前 | 优化后 |
|:---|:---|:---|
| Title | 大陆寄台湾大件物流专线_家具搬家设备建材海运门到门 — 速豹集运 | **大陆寄台湾大件物流_家具海运搬家设备专线门到门 | 速豹集运**（26字）|

#### P0-4：csrf/cn→tw blog 页面 title 优化

当前 blog 标题普遍太长，需缩到 30 字以内：

| 页面 | 当前 title | 优化后 |
|:---|:---|:---|
| cn-to-tw-furniture-shipping | 大陆买家具海运到台湾全攻略：费用流程关税 | **大陆寄家具到台湾_海运费用流程门到门 | 速豹集运** |
| cn-to-tw-moving-guide | 大陆搬家到台湾全攻略：海运流程费用门到门 | **大陆搬家到台湾_海运搬家流程费用全攻略 | 速豹集运** |
| cn-to-tw-appliance-shipping | 大陆寄家电到台湾：冰箱洗衣机电视海运怎么运 | **大陆寄家电到台湾_冰箱洗衣机电视海运专线 | 速豹集运** |

### 🟡 P1 — 本周推进

#### P1-1：新建「大陆寄台湾百科」pillar page

当前内容分散在 blog/ 里，缺少一个统合页面：

```
新页面: /cn-to-tw-guide
H1: 大陆寄台湾全攻略_海运/空运/专线怎么选
内容: 整合流程/费用/禁运品/时效 → 链接到所有子页面
```

#### P1-2：百度站长平台查 site: 收录

手动查 `site:subaotw.cn` 确认百度实际收录了多少页。这是制定后续内容策略的基础数据。

#### P1-3：百度百科/百度知道内容投放

已有 `baidu-zhidao-content.md` 和 `baidu-baike-draft.md`，可以开始发布。百度自有产品在搜索结果中优先级极高。

### ⏳ P2 — 1个月内

#### P2-1：CSS 自包含化

当前 subaotw.cn 引用 `/style.css`（不满足 subao.tw 的工程规范），但百度访问站点的 CSS 不受 GFW 影响，且百度对 CSS 包容度比 Google 高。**暂不高于 P0/P1 优先级处理**。

#### P2-2：设备出口页 Schema 补强

equipment/ 目录的 20 页是最高价值的内容集群，应补 `Product` Schema（含设备参数/品牌/型号）而非仅有 `Article`。

#### P2-3：跨站协同（subaotw.cn ↔ subao.tw）

两个站互相链接对 SEO 无效（Google≠Baidu），但可在两站 footer 加「友情链接」式的互链，增加品牌联想。

---

## 五、短词/中词/长尾漏斗

```
    短词（头词）
大陆寄台湾 / 海运到台湾
    ├── 竞争激烈，需6+个月积累
    └── 首页承载 + 整站权重
          ↓
    中词（品类词）
大陆寄家具到台湾 / 搬家到台湾 / 设备出口台湾
    ├── 核心战场，用专门页面承接
    └── cn→tw blog pages + equipment pages
          ↓
    长尾（问句/场景词）
大陆寄跑步机到台湾怎么运 / CNC出口台湾需要什么手续
    ├── 流量小但转化率高
    └── 每个设备页就是一个长尾答案
```

---

## 六、第一优先级执行清单

| # | 动作 | 类型 | 耗时 | 影响 |
|:---:|:---|:---|:---:|:---|
| 1 | 修 Baidu API Token | 技术 | 5分钟 | 🔴 阻塞85页推送 |
| 2 | tw-to-cn 37页加 noindex | 修改 | 30分钟 | 🟡 清主题模糊 |
| 3 | 首页 title 优化 | 修改 | 2分钟 | 🟡 百度显示改善 |
| 4 | 8篇 cn→tw blog title 优化 | 修改 | 20分钟 | 🟡 CTR提升 |
| 5 | 查 site:subaotw.cn | 调研 | 2分钟 | 📊 基准数据 |
| 6 | 新建 /cn-to-tw-guide pillar page | 新建 | 半天 | 🟢 内容整合 |

---

## 七、与 subao.tw 的分工

| 维度 | subao.tw | subaotw.cn |
|:---|:---|:---|
| 方向 | 台湾→大陆 | 大陆→台湾 |
| 搜尋引擎 | Google | Baidu |
| 目标用户 | 台湾用户 | 大陆用户 |
| 语言 | 繁体中文 | 简体中文 |
| 核心品类 | 敏感货（食品/化妆品/保健品）| 大件（家具/搬家/设备/建材）|
| 内容策略 | 长尾为主，中短词靠权重积累 | 中词为主，短词靠百度生态积累 |

**关键原则：两个站各做各的方向，不交叉、不重复。subaotw.cn 不碰 tw→cn 内容。**

---

*需要我从 P0-1（修 Baidu Token）开始依次执行吗？*
