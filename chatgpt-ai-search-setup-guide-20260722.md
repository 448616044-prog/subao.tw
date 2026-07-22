# ChatGPT AI搜索流量获取 — 3步操作手册

> 目标：Bing收录 → ChatGPT可见 → AI搜索流量增长
> 当前ChatGPT来源：63 session/2.2%（未做任何优化）
> 预计效果：3-4周后ChatGPT流量占比翻倍至4-5%

---

## 第1步：注册 Bing Webmaster Tools 并验证 subao.tw

### 为什么做
ChatGPT搜索底层用的是 **Bing索引**。如果Bing没收录你的页面，ChatGPT就看不到你。这是AI搜索流量的基础设施。

### 操作流程

1. 打开 https://www.bing.com/webmasters
2. 点击「開始使用」→ 用 Microsoft 账号登录（用你的 Hotmail/Outlook 账号，没有就注册一个）
3. 点击「新增網站」→ 输入 `https://subao.tw`
4. 选择验证方式 — **推荐用 DNS 验证**（因为 subao.tw 在 Cloudflare 上，DNS 记录很方便加）：

   **方案A：DNS验证（推荐，Cloudflare操作）**
   - Bing会给你一串验证码，例如：`MS=ms12345678`
   - 去 Cloudflare Dashboard → subao.tw → DNS → Records
   - 添加一条 TXT 记录：名称填 `@`，内容填那串验证码
   - 等待2-5分钟DNS生效后，回到Bing点「驗證」

   **方案B：HTML文件验证（备选）**
   - Bing让你下载一个 `BingSiteAuth.xml` 文件
   - 把文件放到 `sites/tw-to-cn/` 目录下
   - 确认 `https://subao.tw/BingSiteAuth.xml` 可以访问
   - 回到Bing点「驗證」

5. 验证成功后，你会进入Bing Webmaster Tools控制台

---

## 第2步：提交 sitemap 到 Bing

### 操作流程

1. 在 Bing Webmaster Tools 左侧菜单 → 點擊「網站地圖」
2. 點擊「提交網站地圖」
3. 输入 sitemap URL：`https://subao.tw/sitemap.xml`
4. 點擊「提交」

### 提交后检查

等几分钟后：
- 左侧「網站分析」→ 查看收录页面数
- 如果显示「已編製索引的頁面」数量，说明成功
- 第一次收录可能需要1-3天

### 额外操作（建议）

在 Bing Webmaster Tools 里还可以：
- **URL檢查**：手动提交首页和几个核心页面，加速收录
  - `https://subao.tw/`
  - `https://subao.tw/blog/tw-to-cn-shipping-guide`
  - `https://subao.tw/blog/food-shipping-guide`
- **SEO報告**：查看Bing对你网站的SEO评分（通常第一次会有一些建议）

---

## 第3步：注册 Google Merchant Center（可选，电商搜索用）

### 为什么做
Google Merchant Center 的产品数据会被 Google AI Overview 和 Shopping 搜索使用。如果你未来要做电商/代购相关的AI搜索流量，这个很有用。

### 操作流程

1. 打开 https://merchants.google.com
2. 用你的 Google 账号登录（和 GA4/GSC 同一个账号即可）
3. 点击「開始使用」→ 填写商家信息：
   - 商家名称：速豹集運（Subao Logistics）
   - 国家/地区：台湾
   - 时区：(GMT+08:00) 台北
4. 选择「在您的网站上销售」→ 输入 `https://subao.tw`
5. 验证网站所有权（如果同一个Google账号已经在GSC验证过subao.tw，会自动通过）
6. 设置运费和退货政策（可以先填默认值，后面再改）
7. 完成注册

### 注意
- Merchant Center 主要是给实物商品用的，物流服务不一定能直接上传产品feed
- 但注册+验证本身就是一条信任信号
- 如果后续做代购/电商相关的内容，可以直接用

---

## 做完后验证清单

| 检查项 | 方法 |
|:---|:---|
| Bing收录确认 | Bing搜索 `site:subao.tw`，看结果数 |
| ChatGPT可见确认 | 在ChatGPT搜索里问「台湾寄大陆鳳梨酥怎么寄」，看是否引用subao.tw |
| GSC AI流量增长 | 3-4周后在GA4查看 chatgpt.com 来源数据变化 |

---

## 时间线预期

| 时间 | 效果 |
|:---|:---|
| 当天 | Bing Webmaster验证成功，sitemap提交 |
| 1-3天 | Bing开始收录subao.tw页面 |
| 1-2周 | ChatGPT搜索开始出现subao.tw内容 |
| 3-4周 | GA4中 chatgpt.com 来源流量开始增长 |
