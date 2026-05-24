# subaotw.cn 建站计划（备案期间准备文档）

> 备案完成前：完成框架、模板、内容大纲
> 备案完成当日：立即开始内容批量生产

---

## 一、域名与服务器

| 项目 | 方案 |
|------|------|
| 域名 | subaotw.cn |
| 服务器 | 腾讯云 CVM（与 VideoTV 同一台机器175.178.184.141） |
| 部署方式 | GitHub → Cloudflare Pages 或 SCP 直接上传 |
| ICP 备案 | 预计 2026-05-31 完成（7天） |

---

## 二、目录结构

```
sites/subaotw-cn/
├── index.html               # 首页（简体中文）
├── tw-to-cn.html            # 台灣寄大陸服務介绍
├── pricing.html             # 运费说明
├── faq.html                 # 常见问题
├── about.html               # 关于我们
├── contact.html             # 联系我们
├── line.html                # LINE联系方式页
├── article-list.html        # 文章列表
├── blog/                    # 60篇文章（简体化内容）
│   ├── taiwan-products-guide.html
│   ├── taobao-tw-shopping.html
│   ├── shopee-tw-shipping.html
│   ├── taroko-ginseng-shipping.html
│   ├── tw-skincare-to-china.html
│   ├── tw-tea-to-china.html
│   ├── tw-health-products-to-china.html
│   ├── tw-food-to-china.html
│   ├── tw-cosmetics-to-china.html
│   ├── tw-medicine-to-china.html
│   ├── china-post-tw-package.html
│   ├── tw-duty-calculation.html
│   ├── tw-prohibited-items.html
│   ├── tw-customs-declaration.html
│   ├── tw-return-policy.html
│   └── ...
├── _headers                 # Cloudflare Pages 配置文件
└── CNAME                    # 绑定 subaotw.cn
```

---

## 三、SEO 策略（百度 vs Google）

| 维度 | 百度 (subaotw.cn) | Google (subao.tw) |
|------|------------------|------------------|
| 核心关键词 | 台湾商品代购、台湾直邮大陆、台湾快递 | 台灣寄大陸、台灣快遞大陸 |
| 内容语言 | 简体中文 | 繁体中文 |
| 结构化数据 | Schema.org (通用) | Schema.org (通用) |
| sitemap | sitemap.xml (百度支持) | sitemap.xml |
| robots.txt | 允许百度爬虫 | 允许 Google |
| 备案要求 | 必须有 ICP 备案 | 无要求 |
| 主机位置 | 建议国内（腾讯云） | 海外 CDN 即可 |
| 收录速度 | 主动推送 > 被动抓取 | 被动抓取即可 |
| 移动优先 | 非常重要（百度移动流量占比高） | 重要 |

---

## 四、内容大纲（60篇，备案完成后60天内容计划）

### P0（上线前完成，20篇）

**服务类（5篇）**
1. 台灣寄大陸快遞攻略（2026最新）
2. 兩岸快遞時效與費用完整對比
3. 台灣寄大陸多少錢？運費計算一次懂
4. 敏感貨專線是什麼？哪些商品適合？
5. 台灣寄大陸如何包裝？

**商品類（10篇）**
6. 台灣茶葉寄大陸：烏龍茶/高山茶/紅茶快遞攻略
7. 台灣保健品寄大陸：維他命/魚油/燕窩快遞攻略
8. 台灣化妝品寄大陸：護膚品/面膜/精華液快遞攻略
9. 台灣食品寄大陸：零食/鳳梨酥/月餅快遞攻略
10. 台灣中藥材寄大陸：人參/枸杞/紅棗快遞攻略
11. 滴雞精/滴魚精可以寄大陸嗎？最新規定
12. 燕窩/燕窩磚可以快遞到大陸嗎？
13. 面膜可以從台灣寄到大陸嗎？海關規定
14. 嬰幼兒奶粉可以從台灣寄到大陸嗎？
15. 台灣美妝品代購：大陸人如何在台灣電商平台購物

**平台攻略類（5篇）**
16. 淘寶台灣賣家發貨到大陸教學
17. 蝦皮台灣寄送大陸教學：Shopee兩岸集運
18. 小紅書台灣購物攻略：大陸人如何在台灣平台消費
19. 京東台灣館：台灣商品大陸購買指南
20. 兩岸電商平台比較：淘寶/京東/天貓/蝦皮

### P1（上线后第2个月，20篇）

**長尾內容（20篇）**
21. 台灣寄大陸關稅怎麼算？個人物品免稅額
22. 大陸海關對台灣包裹的規定（2026）
23. 台灣寄大陸被扣關了怎麼辦？
24. 哪些東西不能從台灣寄到大陸？（禁運品清單）
25. 台灣寄大陸退件/退貨怎麼處理？
26. 兩岸快遞丢件/損壞索賠攻略
27. 京東快遞到台灣多久？
28. 天貓國際台灣配送服務
29. 淘寶集運推薦：台灣人淘寶購物到大陸
30. 台灣到大陸空運快遞3-5天攻略
31. 大陸人如何在台灣電商購物並寄到大陸
32. 台灣禮品/伴手禮快遞到大陸
33. 台灣美妝保養品大陸受歡迎品項
34. 大陸人最愛的台灣商品TOP10
35. 台灣茶葉在大陸海關的稅率
36. 保健品/維他命在大陸是禁運品嗎？
37. 兩岸快遞公司比較：順豐/EMS/速豹
38. 台灣到大陸快遞時效與費用2026
39. 支付寶/微信支付在台灣電商的應用
40. 大陸支付寶如何購買台灣商品

### P2（上线后第3个月，20篇）

**深度內容（20篇）**
41-60. 待根據上線後數據補充熱門搜索詞

---

## 五、百度搜索資源平台上線檢查清單

```
□ 備案完成後第一時間提交百度站長平台
□ 完成 DNS 驗證（subaotw.cn）
□ 提交 sitemap.xml
□ 提交 robots.txt
□ 開通 URL 提交（主動推送/快速收錄）
□ 安裝百度統計
□ 綁定百度搜索資源平台
□ 開通移動专区（m.subaotw.cn 或響應式）
□ 提交第一批20篇 URL
□ 持續更新高質量原創內容
```

---

## 六、技術配置

### robots.txt（百度友好版）
```
User-agent: Baiduspider
Allow: /
User-agent: Googlebot
Allow: /
User-agent: *
Disallow: /admin/

Sitemap: https://subaotw.cn/sitemap.xml
```

### CNAME 配置
```
# DNS CNAME 記錄
subaotw.cn -> 騰訊雲 CVM IP 或 Cloudflare Pages
```

### 百度統計
```html
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?[YOUR_CODE]";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>
```

---

## 七、內容簡體化原則

從 subao.tw 複製內容到 subaotw.cn 時：

| 項目 | 原則 |
|------|------|
| 文章内容 | 自動簡體化（兩岸同義詞：快遞→快递、運費→运费、禁運→禁运） |
| 標題/Description | 手動重寫，贴合百度搜索習慣 |
| 電話/LINE | 保持不變 |
| 支付方式 | 增加支付寶/微信支付說明 |
| 價格 | 標注新台幣 vs 人民幣 |
| 圖片 | 重新截圖或用 subao.tw 現有圖片 |

---

## 八、與 subao.tw 的差異化

| 維度 | subao.tw（台灣站） | subaotw.cn（大陸站） |
|------|------------------|-------------------|
| 主要訪客 | 台灣人寄東西到大陸 | 大陸人買台灣商品 |
| 語言 | 繁體中文 | 簡體中文（可選繁體） |
| 內容角度 | 「我如何在台灣寄東西到大陸」 | 「我如何在中國買到台灣商品」 |
| 轉化目標 | 聯繫 LINE 客服 | 添加 LINE 或 微信客服 |
| 支付 | 新台幣報價 | 人民幣報價 |
| 客服語言 | 繁體 | 簡體 |
| 平台差異 | Google SEO 為主 | 百度 SEO 為主 |

---

## 九、騰訊雲 CVM 部屬方案

```bash
# 伺服器目錄
/var/www/subaotw-cn

# 部署方式：SCP 上傳（繞過 git 網絡問題）
cd /Users/mac/WorkBuddy/Claw/物流項目/sites/subaotw-cn
tar -czf /tmp/subaotw-cn.tar.gz --exclude='.git' .
scp -i /Users/mac/WorkBuddy/Claw/videotv-correct-ssh-key.txt \
    /tmp/subaotw-cn.tar.gz \
    ubuntu@175.178.184.141:/tmp/
ssh -i /Users/mac/WorkBuddy/Claw/videotv-correct-ssh-key.txt \
    ubuntu@175.178.184.141 \
    "sudo tar -xzf /tmp/subaotw-cn.tar.gz -C /var/www/subaotw-cn"

# Nginx 配置（備案完成後）
# /etc/nginx/sites-available/subaotw.cn
server {
    listen 80;
    server_name subaotw.cn www.subaotw.cn;
    root /var/www/subaotw-cn;
    index index.html;
    # 強制 HTTPS（備案後申請 SSL 證書）
}
```
