# 速豹集运 网站SEO技术规范（给TRAE）

**项目**：速豹集运 两岸物流网站
**用途**：TRAE生成网站时必须遵循的SEO技术标准
**更新时间**：2026-04-23

---

## 一、URL结构规范

```
首页：/
台湾寄大陆：/tw-to-cn/
大陆寄台湾：/cn-to-tw/
运费报价：/pricing/
常见问题：/faq/
关于我们：/about/

文章（博客形式）：
/blog/taiwan-to-china-guide/
/blog/health-products-shipping/
/blog/tea-shipping-guide/
/blog/shopee-shipping-to-china/
```

### URL命名规则
- 全小写
- 用连字符 `-` 分隔词（不用下划线）
- 避免参数URL
- 最多3层目录深度

---

## 二、每个页面必须包含的SEO元素

### TDK标准

**首页**：
- title：台灣寄大陸快遞首選｜速豹集運 兩岸物流專家
- description：速豹集運專業提供台灣寄大陸，大陸寄台灣物流服務，敏感貨專線，3-7天必達，LINE一對一客服
- keywords：台灣寄大陸,大陸寄台灣,兩岸物流,台灣快遞到大陸

**台湾寄大陆页面**：
- title：台灣寄大陸｜速豹集運 敏感貨專線 3-5天到貨
- description：專業台灣寄大陸物流，處理保健品、茶葉、化妝品等敏感貨，3-5個工作天送達

### 必须标签

```html
<link rel="canonical" href="标准URL">
<meta property="og:title" content="标题">
<meta property="og:description" content="描述">
<meta property="og:image" content="图片URL">
<meta property="og:locale" content="zh_TW">
<meta name="twitter:card" content="summary_large_image">
```

---

## 三、结构化数据（Schema）

### Organization（首页）
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "速豹集運",
  "url": "https://www.subaotw.com",
  "logo": "https://www.subaotw.com/images/logo.png"
}
```

### FAQPage（FAQ页面）
每页FAQ都要加对应Schema

### LocalBusiness
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "速豹集運",
  "addressCountry": "TW"
}
```

---

## 四、技术SEO清单

### 必做
- [ ] XML站点地图（sitemap.xml）
- [ ] Robots.txt
- [ ] 移动端响应式
- [ ] HTTPS
- [ ] 页面速度 < 3秒
- [ ] 图片WebP格式 + ALT文字
- [ ] 面包屑导航

### 性能目标
- LCP < 2.5秒
- CLS < 0.1
- INP < 200毫秒

---

## 五、内容SEO要求

### 正文结构
- H1：1个，页面主题
- H2：3-5个，主要分段
- H3：子分段
- 前100字包含关键词
- 内部链接3-5个
- 外部权威链接2-3个

### 内部链接策略
- 每页 → 首页
- 每页 → 相关服务页
- 文章 → 相关文章（至少3条）
- 锚文字用描述性（不用"点击这里"）

---

## 六、台湾本地化

### 繁體中文全站
- 不用简繁切换，一套繁体
- 词汇：大陆≠大陸、快递≠快遞
- 客服：LINE（不用微信）
- 电话格式：+886-XXXX-XXXX-XXXX

### 双搜索平台
- Google繁体（台湾用户主力）
- 百度（大陆用户辅助）

---

## 七、分析配置

- Google Analytics 4（安装 + 转化目标）
- 百度统计
- Google Search Console（繁体站）
- 百度搜索资源平台（简体站）
