#!/usr/bin/env python3
"""批量生成食品品牌单品页 ×5"""
import os, json

BASE = '/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn/blog'
TODAY = '2026-08-12'
LINE_ID = '@734dooky'

H = '''<header class="header" id="header"><div class="container"><a href="/" class="logo"><img src="/images/subao-logo-new.png" alt="速豹集運" height="40"></a><nav class="nav"><a href="/tw-to-cn">台灣發大陸</a><a href="/pricing">運費</a><a href="/can-i-ship">可以寄嗎</a><a href="/article-list">文章攻略</a><a href="/about">關於我們</a></nav><div class="header-cta"><a href="https://line.me/R/ti/p/@734dooky" class="btn-line" target="_blank">LINE 咨詢</a></div></div></header>'''
F = '<footer style="background:#1a1a2e;color:rgba(255,255,255,.7);padding:40px 0;text-align:center;font-size:14px"><p>© 2026 速豹集運 Subao.tw</p></footer>'
GA4 = '<script async src="https://www.googletagmanager.com/gtag/js?id=G-X2T4LGTKJ1"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag("js",new Date());gtag("config","G-X2T4LGTKJ1")</script>'

def build_faq(faq_items):
    html = ''
    json_parts = []
    for q, a in faq_items:
        html += f'<details style="margin-bottom:12px;background:#fff;border-radius:8px;padding:16px"><summary style="font-weight:600;cursor:pointer;color:#1565C0">{q}</summary><p style="margin-top:12px;line-height:1.8">{a}</p></details>\n'
        json_parts.append('{"@type":"Question","name":"' + q.replace('"','\\"') + '","acceptedAnswer":{"@type":"Answer","text":"' + a.replace('"','\\"') + '"}}')
    return html, ','.join(json_parts)

PAGES = [
    {
        "slug": "sun-cake-shipping",
        "title": "台灣太陽餅寄大陸2026｜台中名產能寄嗎？運費NT$290起 | 速豹集運",
        "desc": "台灣太陽餅寄大陸完整指南：太陽堂/一福堂/如邑堂等台中太陽餅品牌均可寄送。太陽餅屬糕餅類走敏感貨專線NT$290/kg起，5-7天空運直達。包裝防碎技巧+海關注意事項一次看懂。",
        "kw": "太陽餅寄大陸,太陽餅可以寄大陸嗎,台中太陽餅寄大陸,太陽餅可以帶去大陸嗎,台灣太陽餅到大陸",
        "h1": "台灣太陽餅寄大陸2026攻略｜台中名產怎麼寄最安全",
        "sub": "台中糕餅名產 · NT$290/kg起包稅雙清 · 5-7天空運直達",
        "oneliner": "台灣太陽餅可以寄大陸！太陽堂、一福堂、如邑堂、陳允寶泉等台中名店太陽餅均可走敏感貨專線寄送。NT$290/kg起包稅雙清，5-7天門到門送達。關鍵是包裝防碎（太陽餅酥皮容易碎裂），建議原廠禮盒+氣泡紙+外箱三重保護。",
        "brands": "太陽堂|一福堂|如邑堂|陳允寶泉|阿明師|自由路太陽餅",
        "faq": [
            ("太陽餅可以寄大陸嗎？", "可以。太陽餅屬於糕餅類，走敏感貨專線NT$290/kg起包稅雙清，5-7天空運直達。台中太陽堂、一福堂、如邑堂等品牌均可寄送。"),
            ("太陽餅寄大陸運費多少？", "敏感貨專線NT$290/kg起。例如一盒太陽餅約0.5kg，運費約NT$290（含派送費）。多盒可合併寄送攤運費，滿10kg免派送費。"),
            ("太陽餅怎麼包裝不會碎？", "太陽餅酥皮極脆，包裝重點：1) 保留原廠禮盒 2) 盒外用氣泡紙包裹至少2層 3) 外箱空隙填滿報紙或緩衝材 4) 外箱標註「易碎品-糕餅」。"),
            ("太陽餅寄大陸會被扣嗎？", "一般不會。太陽餅是純植物性糕點（麵粉+麥芽糖+奶油），不含肉類/蛋黃成分，通關無問題。含蛋黃/肉鬆的變體（如蛋黃酥）需另外確認。"),
        ],
    },
    {
        "slug": "nougat-candy-shipping",
        "title": "台灣牛軋糖寄大陸2026｜糖村/櫻桃爺爺/大黑松小倆口能寄嗎 | 速豹集運",
        "desc": "台灣牛軋糖寄大陸完整指南：糖村、櫻桃爺爺、大黑松小倆口等台灣一線牛軋糖品牌寄送攻略。牛軋糖走敏感貨專線NT$290/kg起，夏天寄送注意防融化。包裝方法+運費參考。",
        "kw": "牛軋糖寄大陸,牛軋糖可以寄大陸嗎,糖村牛軋糖寄大陸,台灣牛軋糖到大陸,牛軋糖可以帶去大陸",
        "h1": "台灣牛軋糖寄大陸2026攻略｜糖村/櫻桃爺爺怎麼寄",
        "sub": "台灣經典糖果 · NT$290/kg起包稅雙清 · 5-7天空運直達",
        "oneliner": "台灣牛軋糖可以寄大陸！糖村、櫻桃爺爺、大黑松小倆口等品牌均可走敏感貨專線寄送。NT$290/kg起包稅雙清，5-7天送達。夏天寄送建議加冰袋或選空運（避免海運高溫導致融化）。軟質牛軋糖比硬質更耐運送。",
        "brands": "糖村|櫻桃爺爺|大黑松小倆口|聖保羅|舊振南",
        "faq": [
            ("牛軋糖可以寄大陸嗎？", "可以。糖村、櫻桃爺爺、大黑松小倆口等台灣牛軋糖品牌均可走敏感貨專線寄送。NT$290/kg起包稅雙清，5-7天空運直達。"),
            ("牛軋糖寄大陸會融化嗎？", "夏天寄送有融化風險。建議：1) 選空運（5-7天）而非海運（7-12天）2) 軟質牛軋糖比硬質耐高溫 3) 加冰袋/保冷劑包裝 4) 避開7-8月最熱時段寄送。"),
            ("牛軋糖運費怎麼算？", "敏感貨專線NT$290/kg起。一盒牛軋糖約300-500g，運費約NT$290（含派送費）。多盒合併寄可攤運費，滿10kg免派送費。"),
            ("哪些牛軋糖品牌最受歡迎？", "糖村（法式牛軋糖）、櫻桃爺爺（多口味牛軋糖）、大黑松小倆口（經典牛軋糖）是台灣三大牛軋糖品牌。包裝精美，非常適合作為伴手禮寄送大陸親友。"),
        ],
    },
    {
        "slug": "315-milk-tea-shipping",
        "title": "台灣三點一刻奶茶寄大陸2026｜沖泡奶茶能寄嗎？NT$290起 | 速豹集運",
        "desc": "台灣三點一刻奶茶寄大陸完整指南：三點一刻/三點一刻3點1刻即溶奶茶、各式口味（原味/伯爵/炭燒/玫瑰）均可寄送。速豹敏感貨專線NT$290/kg起包稅雙清，5-7天空運直達。",
        "kw": "三點一刻寄大陸,三點一刻可以寄大陸嗎,三點一刻奶茶寄大陸,台灣沖泡奶茶寄大陸,三點一刻可以帶去大陸",
        "h1": "台灣三點一刻奶茶寄大陸2026攻略｜沖泡奶茶寄送完整指南",
        "sub": "台灣沖泡奶茶第一品牌 · NT$290/kg起包稅雙清 · 5-7天空運直達",
        "oneliner": "台灣三點一刻（3:15 PM）奶茶可以寄大陸！原味、伯爵、炭燒、玫瑰等口味均可走敏感貨專線寄送。NT$290/kg起包稅雙清，5-7天送達。三點一刻是大陸遊客最愛買的台灣伴手禮之一，奶茶粉屬食品類走敏感貨專線完全沒問題。",
        "brands": "三點一刻|3點1刻|三點一刻原味|三點一刻伯爵|三點一刻炭燒|三點一刻玫瑰",
        "faq": [
            ("三點一刻奶茶可以寄大陸嗎？", "可以。三點一刻（3:15 PM）即溶奶茶屬於食品類，走敏感貨專線NT$290/kg起包稅雙清，5-7天空運直達。原味/伯爵/炭燒/玫瑰等口味均可寄送。"),
            ("三點一刻寄大陸運費多少？", "NT$290/kg起。一盒三點一刻（10-15包）約0.3-0.5kg，運費約NT$290。10kg以下加NT$100派送費，滿10kg免派送費。多盒合併寄更划算。"),
            ("三點一刻哪些口味最暢銷？", "原味奶茶（藍色包裝）最經典，伯爵奶茶（紫色包裝）和炭燒奶茶（咖啡色包裝）最受大陸朋友歡迎。建議各口味混搭寄送，體驗感更豐富。"),
            ("沖泡飲品寄大陸有特殊規定嗎？", "一般沖泡飲品（奶茶粉/咖啡粉/可可粉）走敏感貨專線即可。含奶精/奶粉成分不影響通關。液體飲品（瓶裝/罐裝）需注意防漏包裝。"),
        ],
    },
    {
        "slug": "egg-yolk-pastry-shipping",
        "title": "台灣蛋黃酥寄大陸2026｜中秋送禮能寄嗎？蛋黃限制一次看懂 | 速豹集運",
        "desc": "台灣蛋黃酥寄大陸完整指南：蛋黃酥含蛋黃能寄大陸嗎？2026海關對含蛋製品的最新規定。不二緻果/舊振南/郭元益蛋黃酥寄送攻略。中秋送禮必看，包裝+時效+關稅一次搞懂。",
        "kw": "蛋黃酥寄大陸,蛋黃酥可以寄大陸嗎,蛋黃酥可以帶去大陸,中秋蛋黃酥寄大陸,台灣蛋黃酥到大陸",
        "h1": "台灣蛋黃酥寄大陸2026攻略｜含蛋製品寄送規定一次搞懂",
        "sub": "中秋送禮必看 · NT$290/kg起包稅雙清 · 5-7天空運直達",
        "oneliner": "台灣蛋黃酥寄大陸需注意蛋黃成分！2026年大陸海關對含蛋製品查驗較嚴，但合理自用範圍內的蛋黃酥仍可走敏感貨專線寄送。NT$290/kg起，關鍵是保留原廠包裝+如實申報成分。中秋節前建議提前2週寄出避開高峰期。",
        "brands": "不二緻果|舊振南|郭元益|李鵠|佳德|小潘",
        "faq": [
            ("蛋黃酥可以寄大陸嗎？", "可以，但有限制。蛋黃酥含蛋黃成分，大陸海關對含蛋製品查驗較嚴。合理自用數量（2-3盒）正常申報可通關。保留原廠包裝+成分標籤，走敏感貨專線NT$290/kg起。"),
            ("蛋黃酥寄大陸會被扣嗎？", "有被抽查風險。含蛋製品是大陸海關重點查驗品類。降低風險的方法：1) 少量寄送（2-3盒）2) 保留完整商業包裝 3) 如實申報「蛋黃酥（糕點）」4) 避開中秋前1週高峰期。"),
            ("蛋黃酥中秋節前多久寄？", "建議提前2週寄出。中秋節前1週是兩岸物流最擁堵時期，清關時間可能延長至5-7天。提前寄不僅時效更穩，也能避開海關高峰期查驗。"),
            ("蛋黃酥和鳳梨酥可以一起寄嗎？", "可以一起寄。但建議蛋黃酥和鳳梨酥分開申報品名，方便海關辨識。純鳳梨酥（不含蛋）通關比蛋黃酥順暢。合併寄送可攤運費。"),
        ],
    },
    {
        "slug": "chiade-pineapple-cake-shipping",
        "title": "佳德鳳梨酥寄大陸2026｜佳德vs微熱山丘能寄嗎？運費NT$290起 | 速豹集運",
        "desc": "佳德鳳梨酥寄大陸完整指南：佳德vs微熱山丘vs小潘鳳梨酥三大品牌寄送比較。鳳梨酥走敏感貨專線NT$290/kg起包稅雙清，5-7天空運直達。排隊名店代購寄送攻略，包裝+保存+時效全解析。",
        "kw": "佳德鳳梨酥寄大陸,佳德可以寄大陸嗎,佳德鳳梨酥可以帶去大陸,微熱山丘鳳梨酥寄大陸,佳德vs微熱山丘鳳梨酥",
        "h1": "佳德鳳梨酥寄大陸2026攻略｜排隊名店怎麼寄最划算",
        "sub": "鳳梨酥排隊名店 · NT$290/kg起包稅雙清 · 5-7天空運直達",
        "oneliner": "佳德鳳梨酥可以寄大陸！佳德、微熱山丘、小潘是台灣三大鳳梨酥排隊名店，均可走敏感貨專線寄送。NT$290/kg起包稅雙清，5-7天送達。佳德鳳梨酥（冬瓜餡）甜度適中，微熱山丘（土鳳梨餡）偏酸，小潘（鳳凰酥）含蛋黃需注意。",
        "brands": "佳德|微熱山丘|小潘|鳳凰酥|土鳳梨酥|冬瓜餡",
        "faq": [
            ("佳德鳳梨酥可以寄大陸嗎？", "可以。佳德鳳梨酥走敏感貨專線NT$290/kg起包稅雙清，5-7天空運直達。保留原廠禮盒包裝+成分標籤，如實申報即可通關。建議寄2-3盒最安全。"),
            ("佳德vs微熱山丘哪個好？", "口味差異：佳德（冬瓜餡）甜味溫和接受度最高；微熱山丘（土鳳梨餡）纖維感強、酸甜明顯，有人愛有人不愛。寄送方面兩者均可走敏感貨專線。佳德位於南京東路排隊時間長，建議平日一早前往。"),
            ("鳳梨酥寄大陸運費多少？", "NT$290/kg起。一盒鳳梨酥約0.5-0.6kg，運費約NT$290。兩盒約NT$450，三盒約NT$650。滿10kg免派送費，大批量寄送走海運NT$180/kg起更省。"),
            ("鳳梨酥保存期限短怎麼辦？", "鳳梨酥保存期限通常2-4週。寄送建議：1) 選空運（5-7天）非海運 2) 購買時確認生產日期 3) 購買後24小時內寄出 4) 提醒收件人收到後冷藏保存。"),
        ],
    },
]

for p in PAGES:
    faq_html, faq_json = build_faq(p['faq'])
    
    html = f'''<!DOCTYPE html><html lang="zh-TW"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="lastmod" content="{TODAY}">
<title>{p['title']}</title>
<meta name="description" content="{p['desc']}">
<meta name="keywords" content="{p['kw']}">
<link rel="canonical" href="https://subao.tw/blog/{p['slug']}">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:url" content="https://subao.tw/blog/{p['slug']}">
<meta property="og:type" content="article">
<link rel="stylesheet" href="/style.css">
</head><body>
{H}
<main>
<section class="page-hero" style="padding:80px 0 40px;background:linear-gradient(135deg,#0066CC,#004C99);color:#fff">
<div class="container">
<div class="breadcrumb" style="color:rgba(255,255,255,.7);font-size:14px;margin-bottom:16px"><a href="/" style="color:rgba(255,255,255,.7)">首頁</a> › <a href="/article-list" style="color:rgba(255,255,255,.7)">文章攻略</a> › <a href="/blog/food-shipping-guide" style="color:rgba(255,255,255,.7)">食品寄大陸</a></div>
<h1 style="font-size:34px;font-weight:800;margin:0 0 12px">{p['h1']}</h1>
<p style="font-size:18px;opacity:.9">{p['sub']}</p>
</div></section>

<section style="padding:50px 0;background:#fff"><div class="container" style="max-width:900px">

<div style="background:#E3F2FD;border-left:4px solid #1565C0;padding:20px 24px;border-radius:8px;margin-bottom:32px">
<p style="font-size:18px;font-weight:700;color:#0D47A1;margin:0 0 8px">⚡ 一句話結論</p>
<p style="margin:0;line-height:1.8">{p['oneliner']}</p></div>

<h2>運費參考</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0">
<tr style="background:#E3F2FD"><th style="padding:12px;text-align:left">運輸方式</th><th style="padding:12px;text-align:left">參考價格</th><th style="padding:12px;text-align:left">時效</th><th style="padding:12px;text-align:left">適合場景</th></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e0e0e0">空運專線</td><td style="padding:10px;color:#E65100;font-weight:700">NT$290/kg起</td><td style="padding:10px">5-7天</td><td style="padding:10px">少量自用、送禮急件</td></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e0e0e0">海運專線</td><td style="padding:10px;color:#E65100;font-weight:700">NT$180/kg起</td><td style="padding:10px">7-12天</td><td style="padding:10px">大量寄送、不趕時間</td></tr>
</table>
<p style="font-size:13px;color:#999">※ 10kg以下加收NT$100派送費，滿10kg免派送費。取件費另計NT$100起。</p>

<h2>熱門品牌推薦</h2>
<div style="display:flex;flex-wrap:wrap;gap:8px;margin:16px 0 24px">
{" ".join(f'<span style="background:#FFF3E0;padding:8px 16px;border-radius:20px;font-size:14px">{b}</span>' for b in p['brands'].split('|'))}
</div>

<h2>常見問題</h2>
{faq_html}

<p style="margin:24px 0;padding:16px;background:#FFF3E0;border-radius:8px;font-size:14px;color:#666">
📌 延伸閱讀：<a href="/blog/food-shipping-guide" style="color:#1565C0">台灣食品寄大陸全攻略</a> · <a href="/pricing" style="color:#1565C0">查看完整運費表</a> · <a href="/can-i-ship" style="color:#1565C0">你的東西能不能寄？</a>
</p>

</div></section>

<section style="background:linear-gradient(135deg,#E65100,#CC5200);color:#fff;text-align:center;padding:48px 0">
<div class="container"><h2 style="font-size:24px;margin:0 0 8px">📦 準備寄送？</h2>
<p style="font-size:16px;opacity:.9;margin:0 0 20px">傳商品照片到LINE @{LINE_ID}，30分鐘內回覆運費+時效</p>
<a href="https://line.me/R/ti/p/@{LINE_ID}" style="display:inline-block;background:#fff;color:#E65100;padding:14px 40px;border-radius:12px;font-weight:700;font-size:18px;text-decoration:none">LINE 免費估價 →</a></div></section>
</main>
{F}
{GA4}
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_json}]}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"首頁","item":"https://subao.tw/"}},{{"@type":"ListItem","position":2,"name":"文章攻略","item":"https://subao.tw/article-list"}},{{"@type":"ListItem","position":3,"name":"{p['slug']}"}}]}}</script>
</body></html>'''
    
    filepath = os.path.join(BASE, p['slug'] + '.html')
    with open(filepath, 'w') as f:
        f.write(html)
    print(f'✅ {p["slug"]}.html ({len(html)} bytes)')

print('\nDone! 5 food brand pages generated.')
