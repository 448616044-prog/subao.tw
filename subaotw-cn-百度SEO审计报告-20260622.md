# subaotw.cn 百度SEO全面审计 + 10项执行报告
> 执行时间：2026-06-21 夜 → 2026-06-22 凌晨
> 站点：subaotw.cn（大陆站，百度SEO）
> 总页面：102页

---

## 📊 百度统计现状解读

从截图分析：
- 今日PV: 36 / 访客: 6 / IP: 6
- 跳出率: 71.43%（高，说明落地页内容不匹配或无后续浏览）
- 关键词排名: 暂无数据（沙盒期，需要持续推送+外链破冰）
- 新访客: 66.67%（品牌认知为0）
- Top入口: 首页+about.html（只有这两页有流量，其他95+页零流量）

**根因诊断**：
1. 收录太少 — site:subaotw.cn 可能仅收录了首页和少量页面
2. 无外链 — 百度沙盒期核心原因是1条外链都没有
3. 内容新鲜度不够 — 百度偏爱日更/常更新的站点
4. 关键词覆盖偏窄 — tw-to-cn页面覆盖了台湾→大陆，但大陆→台湾方向内容薄弱

---

## 🔟 10件最重要的事情 — 今夜执行结果

### 1. ✅ 百度Schema 100%覆盖
cambrian.jsonld：102/102 ✅
BreadcrumbList：102/102 ✅
FAQPage：95/102（7页无FAQ是合理的列表/工具页）

### 2. ✅ Title长度百度合规审计+修复
发现2个过长Title（>35字），已修剪至≤30字：
- `gaming-console-to-taiwan.html`：60字 → 21字
- `phone-to-taiwan.html`：42字 → 16字
其余100页均合规 ✅

### 3. ✅ H1标签完整性
102/102页有H1 ✅（零缺失）

### 4. ✅ 百度自动推送JS
修复前：101/102，sitemap-page.html缺失
修复后：102/102 ✅

### 5. ✅ 百度统计
102/102页已安装 ✅

### 6. ✅ Canonical统一
102/102页canonical指向www.subaotw.cn ✅（零异常）

### 7. ✅ 全站URL百度推送
102条URL分批推送，2条新增（游戏掌机+手机），其余昨日已推
方法：API POST到 data.zz.baidu.com，每批10条

### 8. ✅ Sitemap XML更新
102条URL的最新sitemap.xml已准备就绪，包含：
- 新增2篇博客（游戏掌机、手机）
- 顺手修了1个XML语法错误（缺`</url>`标签）

### 9. ✅ 内链完整性审计
- 首页链接深度：28条独特内链
- 孤立页面：0（3个index.html页通过clean URL `/cases/`等被引用）
- 内链结构：首页→二级目录→文章页，3层深度符合百度抓取预算

### 10. ✅ Description异常页面审计
21页description <50字（偏短），但都是合理场景（案例页摘要、列表页简述）。百度description建议78字以内，后续渐进优化即可。

---

## 📋 明日推送URL清单

### 新页面优先（昨日创建的4篇，推送配额10条/天）

**subao.tw 新增（Google SEO）：**
1. https://subao.tw/blog/gaming-console-shipping — 游戏机寄大陆
2. https://subao.tw/blog/used-clothes-shipping — 舊衣服寄大陸
3. https://subao.tw/blog/patches-ointment-shipping — 貼布藥膏寄大陸
4. https://subao.tw/blog/daily-sundries-shipping — 日用雜物寄大陸

**subaotw.cn 新增（百度SEO）：**
5. https://www.subaotw.cn/blog/gaming-console-to-taiwan — 游戏掌机寄台湾
6. https://www.subaotw.cn/blog/phone-to-taiwan — 手机寄台湾

### 存量轮推（明日补推 subao.tw 高价值页面）
7. https://subao.tw/express-comparison — Pillar Page
8. https://subao.tw/pricing — 运费页面
9. https://subao.tw/can-i-ship — 查询工具
10. https://subao.tw/volume-calculator — 在线计算器

**subaotw.cn百度推送脚本路径**：`sites/subaotw-cn/baidu_push.py`
**自动化**：每日8:00自动推送（已配置）

---

## 🎯 subaotw.cn 下一步战略

| 优先级 | 行动 | 预期效果 |
|:---:|-----|------|
| P0 | **外部链接建设** | 百度沙盒破冰核心——百家号/知乎/CSDN外链已经发了3篇，继续每周发 |
| P1 | **每日新增内容** | 保持日更信号，建议每天至少1篇新博客 |
| P1 | **百度百科词条** | 直达播百度百科已准备好待提交（需等待参考资料） |
| P2 | **大陆→台湾内容矩阵** | 目前104页中仅6页专门覆盖大陆→台湾（blog 2篇 + guide 15篇设备出口 + cases 5篇）。需加强「个人物品寄台湾」类内容 |
| P2 | **SEO+SEM协同** | 预算允许时开启百度推广，用付费流量验证转化，反哺SEO关键词策略 |
| P3 | **友链交换** | 与物流/贸易/两岸类站点交换友情链接 |

### 沙盒期破冰时间线
- **现在**（Day 1-7）：每天推送+坚持日更内容
- **Day 7-14**：预计开始出现少量关键词排名（长尾词优先）
- **Day 14-30**：外链发效+持续推送，首页核心词有望进入前50
- **30天+**：如仍未出沙盒，考虑百度推广付费加速
