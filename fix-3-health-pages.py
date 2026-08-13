#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量修复 3 个保健品页面的「鞋子内容错配」：
- chicken-essence-shipping.html（雞精/滴雞精）
- collagen-shipping.html（膠原蛋白）
- vitamin-shipping.html（維他命）

问题与 supplement-customs-guide 相同：Article schema 正确，但 title/H1/正文/FAQ 被鞋子模板污染。
"""
import re

BASE = "sites/tw-to-cn/blog"

# 每个页面的定制内容
PAGES = {
    "chicken-essence-shipping": {
        "title": "雞精/滴雞精寄大陸攻略2026｜田原香/白蘭氏/老協珍寄送規定 | 速豹集運",
        "desc": "雞精/滴雞精寄大陸攻略2026：田原香/白蘭氏/老協珍等品牌雞精怎麼寄？液體類保健食品通關注意、包裝防漏教學、運費試算。走敏感貨專線NT$290/kg起包稅雙清5-7天到府，LINE傳照片30秒確認。",
        "h1": "雞精/滴雞精寄大陸攻略 2026：品牌規定、通關注意、運費一次看懂",
        "h2s": [
            ("🫡 先講結論：雞精寄大陸，關鍵在「液體」", "雞精、滴雞精屬<strong>液體類保健食品</strong>，郵局和順豐都不收，要走敏感貨專線。只要原廠密封包裝、玻璃瓶/鋁箔包防漏處理好，通關沒問題。"),
            ("🏷️ 能寄的品牌：田原香/白蘭氏/老協珍", "田原香滴雞精、白蘭氏雞精、老協珍熬雞精等市售品牌均可寄。重點是<strong>原廠密封包裝</strong>，散裝或已開封的不行。"),
            ("📦 液體雞精的包裝防漏教學", "玻璃瓶雞精：每瓶用氣泡紙單獨包裹，瓶口纏防水膠帶，紙箱底部鋪緩衝材。鋁箔包滴雞精：平放勿折，用夾鏈袋分裝防漏。整箱外層再套一層塑膠袋最穩。"),
            ("💰 運費怎麼算？", "雞精通常較重（玻璃瓶+液體），走敏感貨專線 NT$290/kg 起，最低 NT$290，包稅雙清。一次寄 6-12 瓶屬個人自用合理數量。"),
        ],
        "faqs": [
            ("雞精可以寄大陸嗎？", "可以。田原香/白蘭氏/老協珍等市售品牌雞精走敏感貨專線可寄，NT$290/kg起包稅雙清。需原廠密封包裝、防漏處理好。"),
            ("滴雞精寄大陸會被查嗎？", "液體類保健食品海關會抽驗，但只要原廠密封包裝、成分標示完整、個人自用合理數量，通關沒問題。"),
            ("雞精寄大陸運費多少？", "敏感貨專線NT$290/kg起，最低NT$290。玻璃瓶雞精較重，建議先LINE傳照片估重。包稅雙清無隱藏費用。"),
            ("玻璃瓶雞精怎麼包才不會破？", "每瓶氣泡紙單獨包裹、瓶口纏防水膠帶、紙箱底部鋪緩衝材、整箱外層套塑膠袋。這樣5-7天空運也不怕破。"),
            ("雞精寄大陸一次能寄幾瓶？", "個人自用合理數量，單次建議6-12瓶。超過合理數量海關會懷疑商業用途。"),
        ],
        "related": [
            ("/blog/health-products-shipping", "保健品寄大陸完整攻略"),
            ("/blog/health-supplement-shipping", "保健食品寄大陸指南"),
            ("/blog/supplement-customs-guide", "保健品海關指南"),
        ],
    },
    "collagen-shipping": {
        "title": "膠原蛋白寄大陸攻略2026｜膠原蛋白粉/飲/錠寄送規定+運費 | 速豹集運",
        "desc": "膠原蛋白寄大陸攻略2026：膠原蛋白粉/飲/錠怎麼寄？粉末類保健食品通關注意、包裝教學、運費試算。走敏感貨專線NT$290/kg起包稅雙清5-7天到府，LINE傳照片30秒確認。",
        "h1": "膠原蛋白寄大陸攻略 2026：粉/飲/錠寄送規定、通關注意、運費一次看懂",
        "h2s": [
            ("🫡 先講結論：膠原蛋白寄大陸，粉/飲/錠都能寄", "膠原蛋白屬膳食補充劑，粉、飲、錠三種劑型都可寄。關鍵是<strong>原廠密封包裝 + 成分標示完整</strong>，粉末類別散裝裸寄。"),
            ("🏷️ 三種劑型寄送差異", "膠原蛋白粉：最輕最省運費，注意防潮。膠原蛋白飲：液體類，防漏包裝。膠原蛋白錠：最穩，幾乎零風險。三種都走敏感貨專線。"),
            ("📦 粉末類的通關注意", "粉末類保健品海關會抽驗，重點是<strong>原廠包裝 + 成分表可對照</strong>。拆封後用夾鏈袋裝的散粉，海關會想：這是什麼神秘粉末？——容易卡關。"),
            ("💰 運費怎麼算？", "膠原蛋白粉很輕，走敏感貨專線 NT$290/kg 起，最低 NT$290，包稅雙清。一罐粉通常不到 0.5kg，多罐合寄更划算。"),
        ],
        "faqs": [
            ("膠原蛋白可以寄大陸嗎？", "可以。膠原蛋白粉/飲/錠屬膳食補充劑，走敏感貨專線NT$290/kg起包稅雙清。需原廠密封包裝。"),
            ("膠原蛋白粉寄大陸會被查嗎？", "粉末類保健品海關會抽驗，原廠包裝+成分表可對照就沒問題。散裝裸粉容易卡關。"),
            ("膠原蛋白飲寄大陸怎麼防漏？", "液體類飲品每瓶氣泡紙包裹、瓶口防水膠帶、夾鏈袋分裝，整箱外層套塑膠袋。"),
            ("膠原蛋白寄大陸運費多少？", "敏感貨專線NT$290/kg起，最低NT$290。粉劑很輕，多罐合寄更划算。包稅雙清。"),
            ("膠原蛋白錠和粉哪個好寄？", "錠劑最穩（固體、密封、不易碎），粉劑最輕省運費，飲品最重需防漏。三種都可寄。"),
        ],
        "related": [
            ("/blog/health-products-shipping", "保健品寄大陸完整攻略"),
            ("/blog/health-supplement-shipping", "保健食品寄大陸指南"),
            ("/blog/supplement-customs-guide", "保健品海關指南"),
        ],
    },
    "vitamin-shipping": {
        "title": "維他命寄大陸攻略2026｜綜合維他命/B群/維C/鈣片寄送規定+運費 | 速豹集運",
        "desc": "維他命寄大陸攻略2026：綜合維他命/B群/維C/鈣片怎麼寄？保健品通關注意、包裝教學、運費試算。走敏感貨專線NT$290/kg起包稅雙清5-7天到府，LINE傳照片30秒確認。",
        "h1": "維他命寄大陸攻略 2026：綜合維他命/B群/維C/鈣片寄送規定一次看懂",
        "h2s": [
            ("🫡 先講結論：維他命寄大陸，錠劑最穩", "維他命（綜合維他命/B群/維C/鈣片）屬膳食補充劑，錠劑、膠囊、粉劑都可寄。原廠密封包裝、個人自用合理數量，通關沒問題。"),
            ("🏷️ 常見維他命品項", "綜合維他命、維生素B群、維生素C、維生素D、鈣片、葉酸、魚油（嚴格說屬Omega-3）等均可寄。液體維他命（滴劑）需防漏包裝。"),
            ("📦 維他命的通關重點", "維他命通關率很高，重點仍是<strong>原廠包裝 + 成分表可對照 + 個人自用數量</strong>。一次 50 罐同款維他命，海關會懷疑你在進貨。"),
            ("💰 運費怎麼算？", "錠劑/膠囊很輕，走敏感貨專線 NT$290/kg 起，最低 NT$290，包稅雙清。一次寄 6-12 罐屬合理自用範圍。"),
        ],
        "faqs": [
            ("維他命可以寄大陸嗎？", "可以。綜合維他命/B群/維C/鈣片等膳食補充劑走敏感貨專線NT$290/kg起包稅雙清。需原廠密封包裝。"),
            ("維他命寄大陸會被查嗎？", "錠劑/膠囊通關率高，原廠包裝+成分表可對照+個人自用合理數量就沒問題。"),
            ("綜合維他命寄大陸運費多少？", "敏感貨專線NT$290/kg起，最低NT$290。錠劑很輕，6-12罐合寄最划算。包稅雙清。"),
            ("液體維他命可以寄嗎？", "液體維他命滴劑可寄，但需防漏包裝。走敏感貨專線，比錠劑稍重運費略高。"),
            ("維他命一次能寄多少？", "個人自用合理數量，單次建議6-12罐。超過合理數量海關會懷疑商業用途。"),
        ],
        "related": [
            ("/blog/health-products-shipping", "保健品寄大陸完整攻略"),
            ("/blog/health-supplement-shipping", "保健食品寄大陸指南"),
            ("/blog/supplement-customs-guide", "保健品海關指南"),
        ],
    },
}

def build_article(page):
    p = PAGES[page]
    h2s = ""
    for title, body in p["h2s"]:
        h2s += f'<h2>{title}</h2>\n<p>{body}</p>\n'
    faqs = ""
    for q, a in p["faqs"]:
        faqs += (
            '<div style="margin:16px 0">\n'
            f'  <p style="font-weight:700;margin:0 0 4px">Q：{q}</p>\n'
            f'  <p style="margin:0;color:#555">{a}</p>\n'
            '</div>\n'
        )
    related = "".join(
        f'    <a href="{u}" style="color:var(--primary);margin-left:8px">{t}</a>'
        for u, t in p["related"]
    )
    return (
        '<article class="blog-content">\n'
        + h2s
        + '\n<h2>❓ 常見問題</h2>\n'
        + faqs
        + '\n<div class="cta-box" style="background:linear-gradient(135deg,#06C755,#00A650);color:#fff;padding:28px;border-radius:12px;margin:32px 0;text-align:center">\n'
        '  <p style="font-size:20px;font-weight:700;margin:0 0 8px">📱 不確定能不能寄？傳照片問我們</p>\n'
        '  <p style="font-size:15px;margin:0 0 16px;opacity:0.9">LINE @734dooky · 30 秒確認通關機率 · 不收費</p>\n'
        '  <a href="https://line.me/R/ti/p/@734dooky" target="_blank" onclick="gtag(\'event\',\'line_click\',{event_category:\'conversion\',event_label:\'' + page + '_cta\'});gtag(\'event\',\'generate_lead\',{event_category:\'lead\',event_label:\'line\'})" style="display:inline-block;background:#fff;color:#06C755;padding:14px 32px;border-radius:8px;font-weight:700;text-decoration:none;font-size:16px">📸 傳照片問能不能寄 →</a>\n'
        '</div>\n</article>  <div style="margin-top:40px;padding:16px;background:#f9f7f3;border-radius:10px;font-size:14px;color:#666">    <strong>相關文章：</strong>'
        + related
        + '  </div>'
    )

def build_faq_schema(page):
    p = PAGES[page]
    qjson = ",".join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q, a)
        for q, a in p["faqs"]
    )
    return '  {    "@context": "https://schema.org",    "@type": "FAQPage",    "mainEntity": [' + qjson + '    ]  }'

for page, p in PAGES.items():
    path = f"{BASE}/{page}.html"
    html = open(path, encoding="utf-8").read()

    # 1. title（修 20262026 + 球鞋）
    html = re.sub(r"<title>.*?</title>", f"<title>{p['title']}</title>", html, flags=re.S)
    # 2. meta description
    html = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{p["desc"]}"', html)
    # 3. meta keywords（清鞋子）
    kw = p["title"].split("｜")[0] + ",保健品寄大陸,保健食品寄大陸,敏感貨專線,包稅雙清"
    html = re.sub(r'<meta name="keywords" content="[^"]*"', f'<meta name="keywords" content="{kw}"', html)
    # 4. H1 + blog-meta
    html = re.sub(
        r'<h1 class="blog-title">.*?</h1>\s*<div class="blog-meta">.*?</div>',
        f'<h1 class="blog-title">{p["h1"]}</h1>  <div class="blog-meta">    <span class="blog-category">保健品攻略</span><span>2026年8月13日</span><span>·</span><span>閱讀 6 分鐘</span>  </div>',
        html, flags=re.S,
    )
    # 5. 正文（article + 相关文章区）
    html = re.sub(
        r'<article class="blog-content">.*?</div></main>',
        build_article(page) + '</main>',
        html, flags=re.S,
    )
    # 6. Breadcrumb name 乱码+鞋子
    html = re.sub(r'"name":"[^"]*鞋子寄大陸攻略"', f'"name":"{p["title"].split("｜")[0]}"', html)
    # 7. FAQ schema：先移除 @graph 里的 FAQPage，再替换独立 FAQPage script
    html = re.sub(r',\{"@type":"FAQPage","mainEntity":\[.*?\]\}', "", html, flags=re.S)
    html = re.sub(
        r'<script type="application/ld\+json">\s*\{[^<]*?"@type": "FAQPage".*?</script>',
        '<script type="application/ld+json">\n' + build_faq_schema(page) + '\n</script>',
        html, flags=re.S,
    )

    open(path, "w", encoding="utf-8").write(html)
    # 校验
    shoes = html.count("球鞋") + html.count("鞋子寄大陸") + html.count("NIKE")
    print(f"{page}: 鞋子残留={shoes}, 亂碼={html.count(chr(0xfffd))}, FAQPage={html.count('FAQPage')}")
