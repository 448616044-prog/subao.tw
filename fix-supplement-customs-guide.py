#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复 supplement-customs-guide.html 内容错配：
- 文件名/URL/canonical = supplement-customs-guide（保健品清关）
- 但正文/H1/FAQ/title 是「鞋子寄大陸」内容（与 shoes-shipping.html 重复）
- title 还有 "20262026" 重复 bug

重写为真正的「保健品寄大陸海關指南」，与已存在的 Article schema 对齐，
补上保健品集群缺失的"清关指南"主题，消除与鞋子页的重复内容。
"""
import re

PATH = "sites/tw-to-cn/blog/supplement-customs-guide.html"
html = open(PATH, encoding="utf-8").read()

NEW_TITLE = "保健品寄大陸海關指南2026｜申報規定/免稅額/成分要求一次看懂 | 速豹集運"
NEW_DESC = "保健品寄大陸海關規定2026完整指南：個人自用合理數量、成分申報要求、含動物/中藥成分禁運紅線。魚油/葉黃素/維他命/膠原蛋白怎麼申報才不會被扣？附常見扣件原因+申報模板，LINE傳成分表30秒確認通關機率。"
NEW_H1 = "保健品寄大陸海關指南 2026：申報規定、免稅額、成分要求一次看懂"

# 1. title（修掉 20262026 重复 + 球鞋）
html = re.sub(r"<title>.*?</title>", f"<title>{NEW_TITLE}</title>", html, flags=re.S)

# 2. meta description
html = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{NEW_DESC}"', html)

# 3. H1 + blog-meta
html = re.sub(
    r'<h1 class="blog-title">.*?</h1>\s*<div class="blog-meta">.*?</div>',
    f'<h1 class="blog-title">{NEW_H1}</h1>  <div class="blog-meta">    <span class="blog-category">保健品攻略</span><span>2026年8月13日</span><span>·</span><span>閱讀 7 分鐘</span>  </div>',
    html,
    flags=re.S,
)

# 4. 正文 article 区域替换
article = """
<article class="blog-content">
<h2>🫡 先講結論：保健品寄大陸，海關看三件事</h2>
<p>保健品寄大陸能不能過關，海關主要看三件事：<strong>① 是不是「個人自用合理數量」；② 成分表有沒有踩紅線（動物成分/中藥材/違禁添加）；③ 申報金額是否在免稅額度內。</strong>三者都合規，走敏感貨專線基本都能通關。</p>
<p>這篇把保健品寄大陸的海關規定一次講清楚：哪些保健品能寄、哪些會被扣、怎麼申報最穩，以及免稅額度和常見扣件原因。看完你就知道自己的保健品能不能寄、要怎麼準備。</p>

<h2>📦 能寄大陸的保健品（常見品項）</h2>
<ul>
<li><strong>魚油 / 磷蝦油</strong>：軟膠囊類，成分單純，通關率高。</li>
<li><strong>葉黃素 / 花青素</strong>：護眼類，屬膳食補充劑，可寄。</li>
<li><strong>維他命 / 綜合維生素</strong>：常見保健品，可寄。</li>
<li><strong>膠原蛋白 / 玻尿酸</strong>：口服美容類，可寄（粉末/膠囊皆可）。</li>
<li><strong>益生菌 / 乳酸菌</strong>：可寄，注意常溫保存標示。</li>
</ul>

<h2>🚫 不能寄 / 高風險的保健品</h2>
<table style="width:100%;border-collapse:collapse;margin:16px 0">
<thead><tr style="background:#1E293B;color:#fff"><th style="padding:10px;border:1px solid #334155;text-align:left">品項</th><th style="padding:10px;border:1px solid #334155;text-align:center">判定</th><th style="padding:10px;border:1px solid #334155;text-align:left">原因</th></tr></thead>
<tbody>
<tr><td style="padding:8px;border:1px solid #E2E8F0">處方藥（需醫師處方）</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center;color:#DC2626;font-weight:700">❌ 禁運</td><td style="padding:8px;border:1px solid #E2E8F0">藥品需藥監備案，個人無法清關</td></tr>
<tr><td style="padding:8px;border:1px solid #E2E8F0">注射劑 / 針劑</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center;color:#DC2626;font-weight:700">❌ 禁運</td><td style="padding:8px;border:1px solid #E2E8F0">屬醫療用品，禁止個人郵寄</td></tr>
<tr><td style="padding:8px;border:1px solid #E2E8F0">含動物成分（鹿茸/牛鞭/蛇膽等）</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center;color:#DC2626;font-weight:700">❌ 禁運</td><td style="padding:8px;border:1px solid #E2E8F0">動植物檢疫紅線，海關直接扣</td></tr>
<tr><td style="padding:8px;border:1px solid #E2E8F0">含中藥材（人參/當歸/黃芪等）</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center;color:#D97706;font-weight:700">⚠️ 高風險</td><td style="padding:8px;border:1px solid #E2E8F0">需單獨確認，部分中藥材屬管控品</td></tr>
<tr><td style="padding:8px;border:1px solid #E2E8F0">含興奮劑/違禁添加成分</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center;color:#DC2626;font-weight:700">❌ 禁運</td><td style="padding:8px;border:1px solid #E2E8F0">違反兩岸藥品監管法規</td></tr>
</tbody>
</table>

<h2>🧾 海關申報：三條黃金規則</h2>
<ol>
<li><strong>個人自用合理數量</strong>：單次建議 6-12 瓶/罐，總量別像在進貨。一次 50 罐同款魚油，海關合理懷疑你在賣。</li>
<li><strong>成分表留好</strong>：原廠包裝 + 成分標示完整，海關查驗時能對得上。拆封、無標示的散裝最容易被扣。</li>
<li><strong>申報如實</strong>：品名寫「保健食品（魚油軟膠囊）」而非籠統的「日用品」，如實申報反而不容易被盯上。</li>
</ol>

<h2>💰 免稅額度與稅費</h2>
<p>大陸對個人郵寄物品設有免稅額度（行郵稅），<strong>個人自用合理數量、總值在免稅額度內通常免稅放行</strong>。走速豹敏感貨專線是<strong>包稅雙清</strong>——運費已含關稅+增值稅，收件人不用自己跑海關補稅。NT$290/kg 起，空運 5-7 天到府。</p>

<h2>⚖️ 保健品 vs 藥品：海關怎麼判定？</h2>
<p>關鍵看<strong>外包裝標示</strong>：標「保健食品」「膳食補充劑」「食品」→ 走敏感貨專線可寄；標「藥品」「國藥準字」→ 屬藥品，個人郵寄基本過不了。台灣的「健康食品認證」產品大多屬保健食品範疇，可寄。<a href="/blog/health-products-shipping">保健品寄大陸完整攻略 →</a></p>

<h2>❓ 保健品寄大陸海關常見問題</h2>

<div style="margin:16px 0">
  <p style="font-weight:700;margin:0 0 4px">Q：魚油、葉黃素寄大陸會被扣嗎？</p>
  <p style="margin:0;color:#555">成分單純的膳食補充劑（魚油/葉黃素/維他命）通關率高。個人自用合理數量、原廠密封包裝、成分標示完整，基本不會被扣。<a href="/blog/health-products-shipping">保健品寄大陸攻略 →</a></p>
</div>

<div style="margin:16px 0">
  <p style="font-weight:700;margin:0 0 4px">Q：台灣的保健食品可以寄到大陸嗎？</p>
  <p style="margin:0;color:#555">可以。標示為「保健食品/膳食補充劑」的產品走敏感貨專線可寄，NT$290/kg起包稅雙清。標示為「藥品」的不行。</p>
</div>

<div style="margin:16px 0">
  <p style="font-weight:700;margin:0 0 4px">Q：含中藥成分的保健品能寄嗎？</p>
  <p style="margin:0;color:#555">看成分。純草本萃取（如葉黃素、花青素）可寄；含人參、當歸、黃芪等中藥材的需單獨確認，部分屬管控品。傳成分表到 LINE 30 秒確認。</p>
</div>

<div style="margin:16px 0">
  <p style="font-weight:700;margin:0 0 4px">Q：一次可以寄多少保健品？</p>
  <p style="margin:0;color:#555">個人自用合理數量，單次建議 6-12 瓶/罐，總值在免稅額度內。超過合理數量海關會懷疑商業用途，要求補稅或退運。</p>
</div>

<div style="margin:16px 0">
  <p style="font-weight:700;margin:0 0 4px">Q：保健品寄大陸要申報成分嗎？</p>
  <p style="margin:0;color:#555">要。原廠包裝 + 成分標示完整是通關關鍵。拆封、無標示的散裝保健品最容易被扣。申報品名寫清楚（如「魚油軟膠囊」）。</p>
</div>

<div style="margin:16px 0">
  <p style="font-weight:700;margin:0 0 4px">Q：藥品可以寄大陸嗎？</p>
  <p style="margin:0;color:#555">處方藥、注射劑不能寄，需藥監備案個人無法清關。常見保健品（魚油/維他命/膠原蛋白）走專線可寄。<a href="/blog/chronic-disease-medicine-shipping">藥品/慢病用藥寄大陸說明 →</a></p>
</div>

<div class="cta-box" style="background:linear-gradient(135deg,#06C755,#00A650);color:#fff;padding:28px;border-radius:12px;margin:32px 0;text-align:center">
  <p style="font-size:20px;font-weight:700;margin:0 0 8px">📱 不確定保健品能不能寄？傳成分表問我們</p>
  <p style="font-size:15px;margin:0 0 16px;opacity:0.9">LINE @734dooky · 30 秒確認通關機率 · 不收費</p>
  <a href="https://line.me/R/ti/p/@734dooky" target="_blank" onclick="gtag('event','line_click',{event_category:'conversion',event_label:'supplement_customs_cta'});gtag('event','generate_lead',{event_category:'lead',event_label:'line'})" style="display:inline-block;background:#fff;color:#06C755;padding:14px 32px;border-radius:8px;font-weight:700;text-decoration:none;font-size:16px">📸 傳成分表問能不能寄 →</a>
</div>
</article>
"""

html = re.sub(r'<article class="blog-content">.*?</article>', article.strip(), html, flags=re.S)

# 5. Breadcrumb name 修正（鞋子 → 保健品清关）
html = html.replace("台灣鞋子寄大陸攻略", "保健品寄大陸海關指南")

# 6. 替换 FAQPage schema（鞋子 FAQ → 保健品清关 FAQ）
new_faq = """  {    "@context": "https://schema.org",    "@type": "FAQPage",    "mainEntity": [      {"@type":"Question","name":"魚油、葉黃素寄大陸會被扣嗎？","acceptedAnswer":{"@type":"Answer","text":"成分單純的膳食補充劑（魚油/葉黃素/維他命）通關率高。個人自用合理數量、原廠密封包裝、成分標示完整，基本不會被扣。"}},{"@type":"Question","name":"台灣的保健食品可以寄到大陸嗎？","acceptedAnswer":{"@type":"Answer","text":"可以。標示為保健食品/膳食補充劑的產品走敏感貨專線可寄，NT$290/kg起包稅雙清。標示為藥品的不行。"}},{"@type":"Question","name":"含中藥成分的保健品能寄嗎？","acceptedAnswer":{"@type":"Answer","text":"看成分。純草本萃取（如葉黃素、花青素）可寄；含人參、當歸、黃芪等中藥材的需單獨確認，部分屬管控品。"}},{"@type":"Question","name":"一次可以寄多少保健品？","acceptedAnswer":{"@type":"Answer","text":"個人自用合理數量，單次建議6-12瓶/罐，總值在免稅額度內。超過合理數量海關會懷疑商業用途。"}},{"@type":"Question","name":"保健品寄大陸要申報成分嗎？","acceptedAnswer":{"@type":"Answer","text":"要。原廠包裝+成分標示完整是通關關鍵。拆封、無標示的散裝保健品最容易被扣。申報品名寫清楚。"}},{"@type":"Question","name":"藥品可以寄大陸嗎？","acceptedAnswer":{"@type":"Answer","text":"處方藥、注射劑不能寄，需藥監備案個人無法清關。常見保健品（魚油/維他命/膠原蛋白）走專線可寄。"}}    ]  }  """

# FAQPage 是独立的 <script type="application/ld+json"> 块
html = re.sub(
    r'<script type="application/ld\+json">\s*\{[^<]*?"@type": "FAQPage".*?</script>',
    '<script type="application/ld+json">\n' + new_faq + '\n</script>',
    html,
    flags=re.S,
)

open(PATH, "w", encoding="utf-8").write(html)
print("重写完成:", PATH, "len=", len(html))
print("校验 title 20262026 残留:", html.count("20262026"))
print("校验 球鞋 残留:", html.count("球鞋"))
print("校验 FAQPage:", html.count("FAQPage"))
