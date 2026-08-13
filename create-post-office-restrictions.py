#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
新建「郵局寄大陸限制」专门页面（恢复「郵局寄大陸限制」排名）
基于 post-office-vs-subao-comparison.html 模板
"""
import re

BASE = "sites/tw-to-cn/blog"
TPL = f"{BASE}/post-office-vs-subao-comparison.html"
OUT = f"{BASE}/post-office-shipping-restrictions.html"

html = open(TPL, encoding="utf-8").read()

NEW_URL = "https://subao.tw/blog/post-office-shipping-restrictions"
NEW_TITLE = "郵局寄大陸限制完整清單【2026】哪些東西郵局不收？敏感貨怎麼寄 | 速豹集運"
NEW_DESC = "郵局寄大陸有哪些限制？2026最新禁運品清單：食品、液體、粉末、含電池、化妝品、藥品郵局通通不收。郵局重量尺寸上限、通關限制一次看懂，敏感貨改走集運專線NT$290/kg起包稅雙清5-7天到府。"
NEW_H1 = "郵局寄大陸限制完整清單2026：這些東西郵局不收、不能寄"

# 1. title
html = re.sub(r"<title>.*?</title>", f"<title>{NEW_TITLE}</title>", html, flags=re.S)

# 2. meta description
html = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{NEW_DESC}"', html)

# 3. canonical
html = html.replace("https://subao.tw/blog/post-office-vs-subao-comparison", NEW_URL)

# 4. H1 + meta
html = re.sub(
    r'<h1 class="blog-title">.*?</h1>\s*<div class="blog-meta">.*?</div>',
    f'<h1 class="blog-title">{NEW_H1}</h1>  <div class="blog-meta">    <span class="blog-category">郵局攻略</span><span>2026年8月13日</span><span>·</span><span>閱讀 7 分鐘</span>  </div>',
    html,
    flags=re.S,
)

# 5. 正文 article 区域替换
article = """
<article>
<h2>🫡 先講結論：郵局寄大陸，限制比你想的多</h2>
<p>很多台灣朋友第一直覺是「寄大陸用郵局最方便」，但實際跑一趟會發現：<strong>郵局（中華郵政）寄大陸有大量品項限制，食品、保健品、化妝品、藥品、液體、粉末、含電池物品，通通不收。</strong>不是櫃檯人員刁難你，是郵局的航空/兩岸郵件規範就是這麼定的。</p>
<p>這篇把郵局寄大陸的「限制」全部攤開講清楚：<strong>哪些東西不能寄、重量尺寸上限、為什麼常被退件，以及郵局不收的敏感貨到底怎麼寄。</strong>看完你就不用白跑一趟郵局。</p>

<h2>📦 郵局寄大陸的「硬限制」：這些東西不能寄</h2>
<table style="width:100%;border-collapse:collapse;margin:16px 0">
<thead><tr style="background:#1E293B;color:#fff"><th style="padding:10px;border:1px solid #334155;text-align:left">品項類別</th><th style="padding:10px;border:1px solid #334155;text-align:center">郵局能否寄</th><th style="padding:10px;border:1px solid #334155;text-align:left">原因</th></tr></thead>
<tbody>
<tr><td style="padding:8px;border:1px solid #E2E8F0">食品（零食/餅乾/泡麵）</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center;color:#DC2626;font-weight:700">❌ 不收</td><td style="padding:8px;border:1px solid #E2E8F0">大陸對進口食品有檢疫要求，郵局不承接</td></tr>
<tr><td style="padding:8px;border:1px solid #E2E8F0">保健品/藥品/中藥材</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center;color:#DC2626;font-weight:700">❌ 不收</td><td style="padding:8px;border:1px solid #E2E8F0">藥品需藥監備案，個人郵寄無法清關</td></tr>
<tr><td style="padding:8px;border:1px solid #E2E8F0">化妝品/保養品（含液體）</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center;color:#DC2626;font-weight:700">❌ 不收</td><td style="padding:8px;border:1px solid #E2E8F0">液體類航空禁運，且需化妝品備案</td></tr>
<tr><td style="padding:8px;border:1px solid #E2E8F0">含電池/充電類3C</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center;color:#DC2626;font-weight:700">❌ 不收</td><td style="padding:8px;border:1px solid #E2E8F0">鋰電池屬航空危險品</td></tr>
<tr><td style="padding:8px;border:1px solid #E2E8F0">液體/粉末/膏狀（醬料/奶粉/茶粉）</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center;color:#DC2626;font-weight:700">❌ 不收</td><td style="padding:8px;border:1px solid #E2E8F0">航空安檢限制</td></tr>
<tr><td style="padding:8px;border:1px solid #E2E8F0">書籍/印刷品/衣物（無敏感成分）</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center;color:#16A34A;font-weight:700">✅ 可寄</td><td style="padding:8px;border:1px solid #E2E8F0">普通貨品，走兩岸郵件</td></tr>
</tbody>
</table>
<p style="font-size:13px;color:#555">註：實際以中華郵政當年度《兩岸郵政業務說明》為準，櫃檯會依內容物逐項判定。</p>

<h2>⚖️ 郵局寄大陸的重量、尺寸、金額限制</h2>
<ul>
<li><strong>重量上限</strong>：兩岸郵件單件以 30kg 為上限，但實際郵資會讓重件很不划算。</li>
<li><strong>尺寸上限</strong>：單邊最長 1.5 公尺，長+寬+高合計不超過 3 公尺。</li>
<li><strong>金額限制</strong>：個人郵寄物品價值大陸海關以「自用合理數量」為原則，超過就可能被要求補稅甚至退運。</li>
<li><strong>通關限制</strong>：郵局<strong>不包稅</strong>，大陸海關若課稅，要收件人自己想辦法補稅、跑流程。</li>
</ul>

<h2>🔴🟢 郵局 vs 集運專線：限制對比一次看懂</h2>
<table style="width:100%;border-collapse:collapse;margin:16px 0">
<thead><tr style="background:#1E293B;color:#fff"><th style="padding:10px;border:1px solid #334155;text-align:left">對比項目</th><th style="padding:10px;border:1px solid #334155;text-align:center">中華郵政</th><th style="padding:10px;border:1px solid #334155;text-align:center;background:#166534">速豹集運專線</th></tr></thead>
<tbody>
<tr><td style="padding:8px;border:1px solid #E2E8F0">食品/保健品/化妝品</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center;color:#DC2626">❌ 不收</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center;font-weight:700;color:#166534">✅ 可寄（敏感貨專線）</td></tr>
<tr><td style="padding:8px;border:1px solid #E2E8F0">含電池3C</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center;color:#DC2626">❌ 不收</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center;font-weight:700;color:#166534">✅ 可寄（特貨）</td></tr>
<tr><td style="padding:8px;border:1px solid #E2E8F0">包稅雙清</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center;color:#DC2626">❌ 不包稅</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center;font-weight:700;color:#166534">✅ 包稅雙清</td></tr>
<tr><td style="padding:8px;border:1px solid #E2E8F0">時效</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center">14-21天</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center;font-weight:700;color:#166534">7-12天（空運5-7天）</td></tr>
<tr><td style="padding:8px;border:1px solid #E2E8F0">價格（普貨）</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center">首公斤NT$500-700</td><td style="padding:8px;border:1px solid #E2E8F0;text-align:center;font-weight:700;color:#166534">NT$290/kg起</td></tr>
</tbody>
</table>

<h2>🚫 郵局寄大陸最常被退件的 5 種情況</h2>
<ol>
<li><strong>塞了包零食當伴手禮</strong>——郵局不收食品，當場被擋下。</li>
<li><strong>奶粉、茶葉、咖啡粉</strong>——粉末類航空安檢不過。</li>
<li><strong>護膚品、面膜、精華液</strong>——液體類禁運。</li>
<li><strong>行動電源、藍牙耳機</strong>——含鋰電池，危險品。</li>
<li><strong>申報不實</strong>——寫「日用品」實際是食品，海關查到退件。</li>
</ol>

<h2>💡 郵局不收的敏感貨，到底怎麼寄？</h2>
<p>郵局的限制是「品項」問題，不是「寄大陸」本身的問題。你只需要換一條<strong>收敏感貨的專線</strong>：食品、保健品、化妝品、含電池3C，走集運專線都有對應的通關方案，包稅雙清、不用收件人自己跑海關。</p>
<p>想看郵局和專線的完整對比（價格/時效/品項全PK），參考：<a href="/blog/post-office-vs-subao-comparison">中華郵政vs集運專線2026實測對比 →</a></p>

<h2>❓ 郵局寄大陸限制常見問題</h2>

<div style="margin:16px 0">
  <p style="font-weight:700;margin:0 0 4px">Q：郵局寄大陸可以寄泡麵、餅乾嗎？</p>
  <p style="margin:0;color:#555">不行。食品類（含泡麵、餅乾、零食）郵局一律不收，這是兩岸郵件的固定限制。<a href="/blog/food-shipping-guide">食品寄大陸改走專線攻略 →</a></p>
</div>

<div style="margin:16px 0">
  <p style="font-weight:700;margin:0 0 4px">Q：郵局寄大陸可以寄茶葉、咖啡粉嗎？</p>
  <p style="margin:0;color:#555">茶葉、咖啡粉屬粉末/農產品，郵局不收。真空包裝好走敏感貨專線即可。<a href="/blog/tea-shipping-guide">茶葉寄大陸攻略 →</a></p>
</div>

<div style="margin:16px 0">
  <p style="font-weight:700;margin:0 0 4px">Q：郵局寄大陸可以寄保健品、藥品嗎？</p>
  <p style="margin:0;color:#555">保健食品和藥品郵局都不收，藥品需藥監備案個人無法清關。常見保健品（維他命/魚油/膠原蛋白）走專線可寄。<a href="/blog/health-products-shipping">保健品寄大陸攻略 →</a></p>
</div>

<div style="margin:16px 0">
  <p style="font-weight:700;margin:0 0 4px">Q：郵局寄大陸可以寄化妝品、面膜嗎？</p>
  <p style="margin:0;color:#555">液體類化妝品郵局不收；面膜/乳霜等也受液體膏狀限制。走專線有美妝敏感貨方案。<a href="/blog/cosmetics-shipping">化妝品寄大陸攻略 →</a></p>
</div>

<div style="margin:16px 0">
  <p style="font-weight:700;margin:0 0 4px">Q：郵局寄大陸可以寄手機、行動電源嗎？</p>
  <p style="margin:0;color:#555">含鋰電池的3C郵局不收。手機、藍牙耳機、行動電源走特貨專線，有電池申報方案。<a href="/blog/electronics-shipping">3C電子產品寄大陸攻略 →</a></p>
</div>

<div style="margin:16px 0">
  <p style="font-weight:700;margin:0 0 4px">Q：郵局寄大陸到底能寄什麼？</p>
  <p style="margin:0;color:#555">無敏感成分的普通物品：衣物、書籍、文件、生活雜貨（非液體/粉末/食品/電池）。但要注意郵局不包稅、時效14-21天。若要寄食品/保健品/化妝品，直接走專線最快。<a href="/tw-to-cn">台灣寄大陸完整攻略 →</a></p>
</div>

<div class="cta-box" style="background:linear-gradient(135deg,#06C755,#00A650);color:#fff;padding:28px;border-radius:12px;margin:32px 0;text-align:center">
  <p style="font-size:20px;font-weight:700;margin:0 0 8px">📱 郵局不收的東西，傳照片問我們能不能寄</p>
  <p style="font-size:15px;margin:0 0 16px;opacity:0.9">LINE @734dooky · 每天幫幾十個人確認商品 · 30秒回覆 · 不收費</p>
  <a href="https://line.me/R/ti/p/@734dooky" target="_blank" onclick="gtag('event','line_click',{event_category:'conversion',event_label:'postoffice_restriction_cta'});gtag('event','generate_lead',{event_category:'lead',event_label:'line'})" style="display:inline-block;background:#fff;color:#06C755;padding:14px 32px;border-radius:8px;font-weight:700;text-decoration:none;font-size:16px">📸 傳照片問能不能寄 →</a>
</div>
</article>
"""

html = re.sub(r'<article class="blog-content">.*?</article>', article.strip(), html, flags=re.S)

# 6. 替换 JSON-LD：Breadcrumb name + Article headline/description
html = html.replace("中華郵政vs速豹集運對比", "郵局寄大陸限制清單")
html = html.replace("中華郵政vs速豹集運2026實測對比：台灣寄大陸選哪個？", "郵局寄大陸限制完整清單2026：哪些東西郵局不收")
html = html.replace(
    "台灣寄大陸選中華郵政還是集運專線？5大維度全面PK：價格、時效、可寄品類、通關率、客服質量。郵局不收的敏感貨（食品/保健品/化妝品），集運專線5-7天雙清包稅送達。",
    "郵局寄大陸有哪些限制？2026最新禁運品清單：食品、液體、粉末、含電池、化妝品、藥品郵局通通不收。敏感貨改走集運專線NT$290/kg起包稅雙清。",
)

# 7. 替换 FAQPage schema
new_faq = """{    "@context": "https://schema.org",    "@type": "FAQPage",    "mainEntity": [      {"@type":"Question","name":"郵局寄大陸可以寄泡麵、餅乾嗎？","acceptedAnswer":{"@type":"Answer","text":"不行。食品類（含泡麵、餅乾、零食）郵局一律不收，這是兩岸郵件的固定限制。食品寄大陸改走集運專線，NT$290/kg起包稅雙清。"}},{"@type":"Question","name":"郵局寄大陸可以寄茶葉、咖啡粉嗎？","acceptedAnswer":{"@type":"Answer","text":"茶葉、咖啡粉屬粉末/農產品，郵局不收。真空包裝好走敏感貨專線即可，空運5-7天到府。"}},{"@type":"Question","name":"郵局寄大陸可以寄保健品、藥品嗎？","acceptedAnswer":{"@type":"Answer","text":"保健食品和藥品郵局都不收，藥品需藥監備案個人無法清關。常見保健品（維他命/魚油/膠原蛋白）走專線可寄。"}},{"@type":"Question","name":"郵局寄大陸可以寄化妝品、面膜嗎？","acceptedAnswer":{"@type":"Answer","text":"液體類化妝品郵局不收，面膜/乳霜等也受液體膏狀限制。走專線有美妝敏感貨方案。"}},{"@type":"Question","name":"郵局寄大陸可以寄手機、行動電源嗎？","acceptedAnswer":{"@type":"Answer","text":"含鋰電池的3C郵局不收。手機、藍牙耳機、行動電源走特貨專線，有電池申報方案。"}},{"@type":"Question","name":"郵局寄大陸到底能寄什麼？","acceptedAnswer":{"@type":"Answer","text":"無敏感成分的普通物品：衣物、書籍、文件、生活雜貨（非液體/粉末/食品/電池）。但郵局不包稅、時效14-21天。若要寄食品/保健品/化妝品，直接走專線最快。"}}    ]  }"""

html = re.sub(
    r'<script type="application/ld\+json">\s*\{[^<]*?"@type": "FAQPage".*?</script>',
    '<script type="application/ld+json">\n' + new_faq + '\n</script>',
    html,
    flags=re.S,
)

# 8. 更新"相關評測"内链块（指向郵局系列 + 限制页自身不在内）
html = html.replace(
    '<a href="/blog/post-office-vs-subao-comparison"',
    '<a href="/blog/post-office-vs-subao-comparison"',
)

open(OUT, "w", encoding="utf-8").write(html)
print("created:", OUT, "len=", len(html))
print("校验: title 出现次数", html.count(NEW_TITLE))
print("校验: canonical", html.count(NEW_URL))
print("校验: FAQPage", html.count('"@type": "FAQPage"'))
