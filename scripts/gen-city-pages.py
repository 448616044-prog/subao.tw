#!/usr/bin/env python3
"""批量生成台湾寄XX城市专线页面"""
import os, re
from datetime import date

BASE = '/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn/blog'
TODAY = '2026-08-12'

CITIES = [
    {"name": "上海", "region": "華東", "province": "上海", "districts": "浦東/黃浦/靜安/徐匯/長寧",
     "landmark": "陸家嘴", "time": "5-7天", "price": "NT$380/kg", "people": "台商/台幹/留學生"},
    {"name": "深圳", "region": "華南", "province": "廣東", "districts": "福田/南山/羅湖/寶安/龍華",
     "landmark": "科技園", "time": "4-6天", "price": "NT$290/kg", "people": "台商/電子業/創業者"},
    {"name": "廣州", "region": "華南", "province": "廣東", "districts": "天河/越秀/白雲/番禺/海珠",
     "landmark": "珠江新城", "time": "4-6天", "price": "NT$290/kg", "people": "台商/批發貿易/學生"},
    {"name": "廈門", "region": "華南", "province": "福建", "districts": "思明/湖里/集美/海滄/同安",
     "landmark": "鼓浪嶼", "time": "3-5天", "price": "NT$290/kg", "people": "台商/金門/小三通常客"},
    {"name": "成都", "region": "西南", "province": "四川", "districts": "武侯/錦江/青羊/成華/金牛",
     "landmark": "春熙路", "time": "7-9天", "price": "NT$420/kg", "people": "台商/文創/留學生"},
    {"name": "杭州", "region": "華東", "province": "浙江", "districts": "西湖/上城/拱墅/濱江/余杭",
     "landmark": "西湖", "time": "5-7天", "price": "NT$380/kg", "people": "電商創業/阿里員工/學生"},
    {"name": "南京", "region": "華東", "province": "江蘇", "districts": "鼓樓/玄武/秦淮/建鄴/江寧",
     "landmark": "新街口", "time": "6-8天", "price": "NT$390/kg", "people": "台商/學生/學術交流"},
    {"name": "武漢", "region": "華中", "province": "湖北", "districts": "武昌/漢口/漢陽/洪山/江岸",
     "landmark": "光谷", "time": "6-8天", "price": "NT$390/kg", "people": "台商/汽車產業/學生"},
    {"name": "重慶", "region": "西南", "province": "重慶", "districts": "渝中/江北/南岸/九龍坡/沙坪壩",
     "landmark": "解放碑", "time": "7-9天", "price": "NT$420/kg", "people": "台商/火鍋/觀光"},
    {"name": "天津", "region": "華北", "province": "天津", "districts": "和平/河西/南開/河東/濱海新區",
     "landmark": "天津之眼", "time": "5-7天", "price": "NT$410/kg", "people": "台商/製造業/學生"},
]

TEMPLATE = '''<!DOCTYPE html><html lang="zh-TW"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="lastmod" content="{date}">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<link rel="canonical" href="https://subao.tw/blog/{slug}">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:url" content="https://subao.tw/blog/{slug}">
<meta property="og:type" content="article">
{style_ref}
{script_ref}
</head><body>
{header}
<main>
<section class="page-hero" style="padding:80px 0 40px;background:linear-gradient(135deg,#0066CC,#004C99);color:#fff">
<div class="container">
<div class="breadcrumb" style="color:rgba(255,255,255,.7);font-size:14px;margin-bottom:16px"><a href="/" style="color:rgba(255,255,255,.7)">首頁</a> › <a href="/tw-to-cn" style="color:rgba(255,255,255,.7)">台灣發大陸</a> › <span>寄{name}</span></div>
<h1 style="font-size:36px;font-weight:800;margin:0 0 12px">{h1}</h1>
<p style="font-size:18px;opacity:.9;max-width:700px">{subtitle}</p>
</div></section>

<section style="padding:50px 0;background:#fff">
<div class="container" style="max-width:900px">

<div style="background:#E3F2FD;border-left:4px solid #1565C0;padding:20px 24px;border-radius:8px;margin-bottom:32px">
<p style="font-size:18px;font-weight:700;color:#0D47A1;margin:0 0 8px">⚡ 台灣寄{name}一句話</p>
<p style="margin:0;line-height:1.8">{oneliner}</p>
</div>

<h2>台灣寄{name}費用一覽</h2>
<table style="width:100%;border-collapse:collapse;margin:24px 0">
<tr style="background:#E3F2FD"><th style="padding:12px;text-align:left">運輸方式</th><th style="padding:12px;text-align:left">參考價格</th><th style="padding:12px;text-align:left">時效</th><th style="padding:12px;text-align:left">適合</th></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e0e0e0">空運專線</td><td style="padding:10px;border-bottom:1px solid #e0e0e0;color:#E65100;font-weight:700">{price}起</td><td style="padding:10px;border-bottom:1px solid #e0e0e0">{time}</td><td style="padding:10px;border-bottom:1px solid #e0e0e0">食品/保健品/化妝品/茶葉</td></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e0e0e0">海運專線</td><td style="padding:10px;border-bottom:1px solid #e0e0e0;color:#E65100;font-weight:700">NT$180/kg起</td><td style="padding:10px;border-bottom:1px solid #e0e0e0">最快5-7天</td><td style="padding:10px;border-bottom:1px solid #e0e0e0">大宗/不急件/衣物書籍</td></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e0e0e0">敏感貨專線</td><td style="padding:10px;border-bottom:1px solid #e0e0e0;color:#E65100;font-weight:700">{price}起</td><td style="padding:10px;border-bottom:1px solid #e0e0e0">{time}</td><td style="padding:10px;border-bottom:1px solid #e0e0e0">含液體/粉末/電池類</td></tr>
</table>
<p style="font-size:13px;color:#999">※ 以上為參考價格，10kg以下加收NT$100派送費。實際費用以LINE客服報價為準。</p>

<h2>台灣寄{name}可以寄什麼？</h2>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin:20px 0">
{items_grid}
</div>

<h2>寄{name}流程</h2>
<ol style="line-height:2.2;font-size:16px">
<li><strong>LINE傳照片估價</strong>：加LINE @734dooky，傳商品照片+目的地地址</li>
<li><strong>預約上門取件</strong>：台灣本島多數地區取件費NT$100起，預約後次日上門</li>
<li><strong>專業打包+出口報關</strong>：速豹代辦出口報關手續</li>
<li><strong>空運/海運直送</strong>：{time}門到門送達{name}</li>
<li><strong>大陸清關+派送</strong>：{name}全區派送（含{districts}）</li>
</ol>

<h2>台灣寄{name}常見問題</h2>
{faq_html}

</div></section>

<section style="background:linear-gradient(135deg,#E65100,#CC5200);color:#fff;text-align:center;padding:48px 0">
<div class="container">
<h2 style="font-size:24px;margin:0 0 8px">📦 準備寄{name}？</h2>
<p style="font-size:16px;opacity:.9;margin:0 0 20px">傳商品照片到LINE，30分鐘內回覆運費+時效</p>
<a href="https://line.me/R/ti/p/@734dooky" style="display:inline-block;background:#fff;color:#E65100;padding:14px 40px;border-radius:12px;font-weight:700;font-size:18px;text-decoration:none">LINE 免費估價 →</a>
</div></section>

<section style="padding:40px 0;background:#f5f7fa">
<div class="container" style="max-width:900px">
<p style="font-size:14px;color:#999;text-align:center">🔗 更多城市專線：<a href="/blog/beijing-shipping-guide" style="color:#1565C0">寄北京</a> · <a href="/blog/shanghai-shipping-guide" style="color:#1565C0">寄上海</a> · <a href="/blog/shenzhen-shipping-guide" style="color:#1565C0">寄深圳</a> · <a href="/city-shipping-guide" style="color:#1565C0">全部城市專線 →</a></p>
</div></section>
</main>
{footer}
{scripts}
</body></html>'''

# Simplified header/footer/style references - assume they exist in the site
STYLE_REF = '<link rel="stylesheet" href="/style.css">'
SCRIPT_REF = ''

# We'll use a stripped-down approach: minimal but functional inline styles
# since the site uses inline CSS for blog posts

HEADER = '''<header class="header" id="header">
<div class="container">
<a href="/" class="logo"><img src="/images/subao-logo-new.png" alt="速豹集運" height="40"></a>
<nav class="nav"><a href="/tw-to-cn">台灣發大陸</a><a href="/pricing">運費</a><a href="/can-i-ship">可以寄嗎</a><a href="/article-list">文章攻略</a><a href="/about">關於我們</a></nav>
<div class="header-cta"><a href="https://line.me/R/ti/p/@734dooky" class="btn-line" target="_blank">LINE 咨詢</a></div>
</div></header>'''

FOOTER = '''<footer style="background:#1a1a2e;color:rgba(255,255,255,.7);padding:40px 0;text-align:center;font-size:14px">
<div class="container"><p>© 2026 速豹集運 Subao.tw</p></div></footer>'''

SCRIPTS = '''<script async src="https://www.googletagmanager.com/gtag/js?id=G-X2T4LGTKJ1"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag('js',new Date());gtag('config','G-X2T4LGTKJ1')</script>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_json}]}</script>'''

def generate():
    for city in CITIES:
        name = city['name']
        slug = f"{name.lower()}-shipping-guide"
        region = city['region']
        
        # Build SEO fields
        title = f"台灣寄{name}2026｜運費NT$290起最快{city['time']}到｜{city['districts'].split('/')[0]}等全區派送 - 速豹集運"
        desc = f"台灣寄{name}包裹全攻略：NT$290/kg起包稅雙清，最快{city['time']}空運到。{region}地區食品/保健品/化妝品/3C敏感貨寄送規定+運費+時效一表看懂，{city['districts']}等全區派送。LINE免費估價。"
        keywords = f"台灣寄{name},台灣寄{name}運費,台灣寄{name}多久,寄{city['province']},{city['province']}快遞"
        og_title = f"台灣寄{name}2026實戰手冊｜NT$290/kg起{city['time']}包稅雙清"
        og_desc = f"台灣寄{name}快遞全攻略。{city['districts']}等全區派送。食品/保健品/化妝品/茶葉均可寄。"
        h1 = f"台灣寄{name}2026實戰手冊｜運費、時效、禁運一次看懂"
        subtitle = f"{region}地區專線 · {city['time']}送達 · {city['districts']}全區派送"
        oneliner = f"台灣寄{name}走敏感貨專線，{city['price']}起包稅雙清，{city['time']}門到門送達{city['districts']}等全區。食品/保健品/化妝品/茶葉/3C均可寄。適合{city['people']}。"
        
        # FAQ questions
        faq_items = [
            {"q": f"台灣寄{name}要多久？", "a": f"空運專線{city['time']}門到門送達{name}{city['districts']}等全區。海運約7-12天。具體時效依商品類型及海關查驗速度而定，請加LINE確認。"},
            {"q": f"台灣寄{name}運費多少？", "a": f"空運專線{city['price']}起包稅雙清，海運NT$180/kg起。10kg以下加收NT$100派送費，滿10kg免派送費。取件費NT$100起另計。精確費用以LINE客服依商品類型報價為準。"},
            {"q": f"台灣寄{name}食品/保健品可以寄嗎？", "a": f"可以。台灣食品（零食/泡麵/鳳梨酥/伴手禮）、保健品（維他命/膠原蛋白/葉黃素）均可走敏感貨專線寄{name}。含肉類/動物成分的產品需額外確認。茶葉、咖啡豆也可正常寄送。"},
            {"q": f"台灣寄{name}有上門取件嗎？", "a": f"有。台灣本島多數地區提供上門取件服務，取件費NT$100起。預約後次日上門。加LINE @734dooky提供地址即可確認是否在取件範圍內。"},
        ]
        
        # Build FAQ HTML
        faq_html = ""
        for item in faq_items:
            faq_html += f'<details style="margin-bottom:12px;background:#fff;border-radius:8px;padding:16px;box-shadow:0 1px 3px rgba(0,0,0,.08)"><summary style="font-weight:600;cursor:pointer;color:#1565C0">{item["q"]}</summary><p style="margin-top:12px;line-height:1.8">{item["a"]}</p></details>\n'
        
        # Build FAQ JSON
        faq_json_parts = []
        for item in faq_items:
            faq_json_parts.append('{"@type":"Question","name":"' + item['q'] + '","acceptedAnswer":{"@type":"Answer","text":"' + item['a'].replace('"','\\"') + '"}}')
        faq_json = ','.join(faq_json_parts)
        
        # Items grid
        items_grid = f'''
<div style="background:#E8F5E9;padding:16px;border-radius:8px;text-align:center"><strong>✅ 食品類</strong><br><span style="font-size:14px;color:#666">零食/泡麵/伴手禮/鳳梨酥</span></div>
<div style="background:#E8F5E9;padding:16px;border-radius:8px;text-align:center"><strong>✅ 保健品</strong><br><span style="font-size:14px;color:#666">維他命/膠原蛋白/葉黃素</span></div>
<div style="background:#E8F5E9;padding:16px;border-radius:8px;text-align:center"><strong>✅ 化妝品</strong><br><span style="font-size:14px;color:#666">面膜/精華液/乳液/防曬</span></div>
<div style="background:#E8F5E9;padding:16px;border-radius:8px;text-align:center"><strong>✅ 茶葉/咖啡</strong><br><span style="font-size:14px;color:#666">高山茶/咖啡豆/茶包</span></div>
<div style="background:#FFF3E0;padding:16px;border-radius:8px;text-align:center"><strong>⚠️ 3C電子</strong><br><span style="font-size:14px;color:#666">含電池走敏感貨</span></div>
<div style="background:#FFEBEE;padding:16px;border-radius:8px;text-align:center"><strong>❌ 禁運品</strong><br><span style="font-size:14px;color:#666">肉製品/新鮮水果/藥品</span></div>'''
        
        # Build page using simple string replace
        html = TEMPLATE
        for key, val in {
            '{date}': TODAY, '{title}': title, '{desc}': desc,
            '{keywords}': keywords, '{slug}': slug,
            '{og_title}': og_title, '{og_desc}': og_desc,
            '{style_ref}': STYLE_REF, '{script_ref}': SCRIPT_REF,
            '{header}': HEADER, '{footer}': FOOTER,
            '{name}': name, '{h1}': h1, '{subtitle}': subtitle,
            '{oneliner}': oneliner, '{time}': city['time'],
            '{price}': city['price'], '{districts}': city['districts'],
            '{items_grid}': items_grid, '{faq_html}': faq_html,
        }.items():
            html = html.replace(key, val)
        
        # FAQ Schema (separate to avoid brace conflicts)
        html = html.replace('{faq_json}', faq_json)
        # Remove remaining unused template vars  
        html = html.replace('{scripts}', SCRIPTS)
        
        filepath = os.path.join(BASE, f'{slug}.html')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f'✅ {slug}.html ({len(html)} bytes)')

if __name__ == '__main__':
    generate()
    print(f'\nDone! {len(CITIES)} city pages generated.')
