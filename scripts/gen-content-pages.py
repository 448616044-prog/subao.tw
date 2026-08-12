#!/usr/bin/env python3
"""批量生成长尾品类页"""
import os

BASE = '/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn/blog'
TODAY = '2026-08-12'
LINE_ID = '@734dooky'

HEADER = '''<header class="header" id="header"><div class="container"><a href="/" class="logo"><img src="/images/subao-logo-new.png" alt="速豹集運" height="40"></a><nav class="nav"><a href="/tw-to-cn">台灣發大陸</a><a href="/pricing">運費</a><a href="/can-i-ship">可以寄嗎</a><a href="/article-list">文章攻略</a><a href="/about">關於我們</a></nav><div class="header-cta"><a href="https://line.me/R/ti/p/@734dooky" class="btn-line" target="_blank">LINE 咨詢</a></div></div></header>'''

FOOTER = '<footer style="background:#1a1a2e;color:rgba(255,255,255,.7);padding:40px 0;text-align:center;font-size:14px"><div class="container"><p>© 2026 速豹集運 Subao.tw</p></div></footer>'

GA4 = '<script async src="https://www.googletagmanager.com/gtag/js?id=G-X2T4LGTKJ1"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag("js",new Date());gtag("config","G-X2T4LGTKJ1")</script>'

def make_page(filename, title, desc, keywords, h1, subtitle, oneliner, sections, faq_items):
    """Generate a complete SEO page"""
    slug = filename.replace('.html', '')
    
    # Build FAQ JSON
    faq_json = ','.join([
        '{"@type":"Question","name":"' + q.replace('"','\\"') + '","acceptedAnswer":{"@type":"Answer","text":"' + a.replace('"','\\"') + '"}}'
        for q, a in faq_items
    ])
    
    # Build FAQ HTML
    faq_html = ''
    for q, a in faq_items:
        faq_html += f'<details style="margin-bottom:12px;background:#fff;border-radius:8px;padding:16px;box-shadow:0 1px 3px rgba(0,0,0,.08)"><summary style="font-weight:600;cursor:pointer;color:#1565C0">{q}</summary><p style="margin-top:12px;line-height:1.8">{a}</p></details>\n'
    
    # Build sections HTML
    sections_html = ''
    for sec_title, sec_content in sections:
        sections_html += f'<h2>{sec_title}</h2>\n{sec_content}\n'
    
    html = f'''<!DOCTYPE html><html lang="zh-TW"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="lastmod" content="{TODAY}">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<link rel="canonical" href="https://subao.tw/blog/{slug}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://subao.tw/blog/{slug}">
<meta property="og:type" content="article">
<link rel="stylesheet" href="/style.css">
</head><body>
{HEADER}
<main>
<section class="page-hero" style="padding:80px 0 40px;background:linear-gradient(135deg,#0066CC,#004C99);color:#fff">
<div class="container">
<div class="breadcrumb" style="color:rgba(255,255,255,.7);font-size:14px;margin-bottom:16px"><a href="/" style="color:rgba(255,255,255,.7)">首頁</a> › <a href="/article-list" style="color:rgba(255,255,255,.7)">文章攻略</a> › <span>{subtitle.split('·')[0].strip() if '·' in subtitle else subtitle[:20]}</span></div>
<h1 style="font-size:34px;font-weight:800;margin:0 0 12px">{h1}</h1>
<p style="font-size:18px;opacity:.9;max-width:700px">{subtitle}</p>
</div></section>

<section style="padding:50px 0;background:#fff">
<div class="container" style="max-width:900px">

<div style="background:#E3F2FD;border-left:4px solid #1565C0;padding:20px 24px;border-radius:8px;margin-bottom:32px">
<p style="font-size:18px;font-weight:700;color:#0D47A1;margin:0 0 8px">⚡ 一句話結論</p>
<p style="margin:0;line-height:1.8">{oneliner}</p>
</div>

{sections_html}

<h2>常見問題</h2>
{faq_html}

</div></section>

<section style="background:linear-gradient(135deg,#E65100,#CC5200);color:#fff;text-align:center;padding:48px 0">
<div class="container">
<h2 style="font-size:24px;margin:0 0 8px">📦 不確定能不能寄？</h2>
<p style="font-size:16px;opacity:.9;margin:0 0 20px">傳商品照片到LINE @{LINE_ID}，30分鐘內回覆</p>
<a href="https://line.me/R/ti/p/@{LINE_ID}" style="display:inline-block;background:#fff;color:#E65100;padding:14px 40px;border-radius:12px;font-weight:700;font-size:18px;text-decoration:none">LINE 免費估價 →</a>
</div></section>
</main>
{FOOTER}
{GA4}
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_json}]}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"首頁","item":"https://subao.tw/"}},{{"@type":"ListItem","position":2,"name":"文章攻略","item":"https://subao.tw/article-list"}},{{"@type":"ListItem","position":3,"name":"{slug}"}}]}}</script>
</body></html>'''
    
    filepath = os.path.join(BASE, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'✅ {filename} ({len(html)} bytes)')


# ============================================================
# Page 1: 面膜寄大陆通用指南
# ============================================================
make_page(
    filename='face-mask-shipping-guide.html',
    title='台灣面膜寄大陸2026｜片狀/泥狀/凍膜能寄嗎？敏感貨專線NT$290起 | 速豹集運',
    desc='台灣面膜寄大陸完整指南：片狀面膜、泥狀面膜、凍膜、眼膜寄送規定一次看懂。含液體面膜需走敏感貨專線，包裝防漏是關鍵。森田藥妝/我的美麗日記/Dr.Wu等品牌均可寄。LINE免費估價。',
    keywords='台灣面膜寄大陸,面膜可以寄大陸嗎,台灣面膜到大陸,片狀面膜寄大陸,泥狀面膜寄大陸',
    h1='台灣面膜寄大陸2026攻略｜片狀/泥狀/凍膜寄送規定一次看懂',
    subtitle='化妝品敏感貨專線 · NT$290/kg起包稅雙清 · 5-7天空運直達',
    oneliner='台灣面膜可以寄大陸！片狀面膜走敏感貨專線NT$290/kg起，泥狀/凍膜/眼膜含液體需加強防漏包裝。台灣面膜品牌（森田藥妝/我的美麗日記/Dr.Wu/提提研）均可寄送，不含違禁成分即可通關。',
    sections=[
        ('台灣面膜寄大陸：哪些可以寄？', '''
<table style="width:100%;border-collapse:collapse;margin:20px 0">
<tr style="background:#E3F2FD"><th style="padding:12px;text-align:left">面膜類型</th><th style="padding:12px;text-align:left">可寄？</th><th style="padding:12px;text-align:left">注意事項</th></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e0e0e0">片狀面膜（精華液浸泡）</td><td style="padding:10px;color:#008A00;font-weight:700">✅ 可寄</td><td style="padding:10px">走敏感貨專線；單片獨立包裝最安全</td></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e0e0e0">泥狀面膜（管狀/罐裝）</td><td style="padding:10px;color:#008A00;font-weight:700">✅ 可寄</td><td style="padding:10px">含液體需加強防漏；蓋子用膠帶加固</td></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e0e0e0">凍膜/晚安面膜</td><td style="padding:10px;color:#008A00;font-weight:700">✅ 可寄</td><td style="padding:10px">凝膠狀需防漏包裝；獨立密封袋</td></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e0e0e0">眼膜/唇膜</td><td style="padding:10px;color:#008A00;font-weight:700">✅ 可寄</td><td style="padding:10px">同片狀面膜處理</td></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e0e0e0">含藥用成分面膜</td><td style="padding:10px;color:#E65100;font-weight:700">⚠️ 需確認</td><td style="padding:10px">含水楊酸/A酸等藥用成分需先LINE確認</td></tr>
</table>'''),
        ('台灣熱門面膜品牌寄送指南', '''
<p>以下台灣常見面膜品牌均可透過速豹敏感貨專線寄送大陸：</p>
<div style="display:flex;flex-wrap:wrap;gap:8px;margin:16px 0">
<span style="background:#E3F2FD;padding:8px 16px;border-radius:20px;font-size:14px">森田藥妝</span>
<span style="background:#E3F2FD;padding:8px 16px;border-radius:20px;font-size:14px">我的美麗日記</span>
<span style="background:#E3F2FD;padding:8px 16px;border-radius:20px;font-size:14px">Dr.Wu</span>
<span style="background:#E3F2FD;padding:8px 16px;border-radius:20px;font-size:14px">提提研</span>
<span style="background:#E3F2FD;padding:8px 16px;border-radius:20px;font-size:14px">霓淨思</span>
<span style="background:#E3F2FD;padding:8px 16px;border-radius:20px;font-size:14px">寵愛之名</span>
<span style="background:#E3F2FD;padding:8px 16px;border-radius:20px;font-size:14px">未來美</span>
<span style="background:#E3F2FD;padding:8px 16px;border-radius:20px;font-size:14px">豐台灣</span>
</div>'''),
        ('面膜寄大陸包裝3原則', '''
<ol style="line-height:2.2">
<li><strong>防漏第一</strong>：含液體面膜（精華液/凍膜）先用密封袋獨立包裝，再放入紙盒</li>
<li><strong>防壓保護</strong>：片狀面膜平整疊放，上下各墊一層氣泡紙，避免運送擠壓破損</li>
<li><strong>外包裝標示</strong>：外箱標註「易碎品-化妝品」，方便物流人員識別處理</li>
</ol>'''),
    ],
    faq_items=[
        ('台灣面膜可以寄大陸嗎？', '可以。片狀面膜、泥狀面膜、凍膜均可走敏感貨專線寄大陸。NT$290/kg起包稅雙清，5-7天空運直達。含藥用成分（水楊酸/A酸）的面膜需先LINE確認。'),
        ('面膜寄大陸運費多少？', '走敏感貨專線NT$290/kg起。例如寄10片面膜約0.5kg，運費約NT$290（含派送費）。精確費用以LINE客服依實際重量報價為準。'),
        ('面膜寄大陸會被扣嗎？', '一般面膜正常申報不會被扣。但含藥用成分或大量同款面膜（超過個人自用數量）可能被海關抽查。建議合理數量寄送，如實申報品名。'),
        ('面膜怎麼包裝寄大陸最安全？', '片狀面膜：保持原包裝→放入密封袋→放入紙盒→放入外箱。泥狀/罐裝面膜：瓶蓋用膠帶加固→密封袋獨立包裝→氣泡紙包裹→外箱。'),
    ],
)

# ============================================================
# Page 2: 猫砂寄大陆
# ============================================================
make_page(
    filename='cat-litter-shipping.html',
    title='台灣貓砂寄大陸2026｜豆腐砂/礦砂/木屑砂能寄嗎？運費這樣算 | 速豹集運',
    desc='台灣貓砂寄大陸完整指南：豆腐砂、礦砂、木屑砂寄送規定+運費計算。貓砂重量大，海運比空運省50%以上。寵物用品敏感貨專線，5-7天送達。LINE免費估價。',
    keywords='台灣貓砂寄大陸,貓砂可以寄大陸嗎,豆腐砂寄大陸,礦砂寄大陸,寵物用品寄大陸',
    h1='台灣貓砂寄大陸2026攻略｜豆腐砂/礦砂/木屑砂怎麼寄最省',
    subtitle='寵物用品專線 · 重量大選海運省錢 · 5-7天空運直達',
    oneliner='台灣貓砂可以寄大陸！豆腐砂/礦砂/木屑砂均可走敏感貨專線。貓砂重量大（一包6-7L約2-3kg），建議選海運更省錢（NT$180/kg起）。少量試用裝走空運5-7天到，大量囤貨走海運7-12天。',
    sections=[
        ('貓砂寄大陸：種類與寄送方式', '''
<table style="width:100%;border-collapse:collapse;margin:20px 0">
<tr style="background:#E3F2FD"><th style="padding:12px;text-align:left">貓砂種類</th><th style="padding:12px;text-align:left">可寄？</th><th style="padding:12px;text-align:left">建議運輸</th><th style="padding:12px;text-align:left">注意事項</th></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e0e0e0">豆腐砂</td><td style="padding:10px;color:#008A00;font-weight:700">✅ 可寄</td><td style="padding:10px">空運/海運均可</td><td style="padding:10px">植物成分，通關無問題</td></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e0e0e0">礦砂（膨潤土）</td><td style="padding:10px;color:#008A00;font-weight:700">✅ 可寄</td><td style="padding:10px">建議海運</td><td style="padding:10px">重量大，空運不划算</td></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e0e0e0">木屑砂/松木砂</td><td style="padding:10px;color:#008A00;font-weight:700">✅ 可寄</td><td style="padding:10px">空運/海運均可</td><td style="padding:10px">輕，空運也划算</td></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e0e0e0">水晶砂</td><td style="padding:10px;color:#008A00;font-weight:700">✅ 可寄</td><td style="padding:10px">建議海運</td><td style="padding:10px">重量中等，多包走海運</td></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e0e0e0">混合貓砂</td><td style="padding:10px;color:#008A00;font-weight:700">✅ 可寄</td><td style="padding:10px">依重量決定</td><td style="padding:10px">含豆腐+礦砂混合，同豆腐砂處理</td></tr>
</table>'''),
        ('貓砂運費怎麼算？空運vs海運比一比', '''
<p><strong>貓砂最大的問題是重量</strong>——一包6L貓砂約2-3kg，5包就10kg+。這時候運輸方式的選擇直接影響運費：</p>
<table style="width:100%;border-collapse:collapse;margin:20px 0">
<tr style="background:#FFF3E0"><th style="padding:12px;text-align:left"></th><th style="padding:12px;text-align:left">空運專線</th><th style="padding:12px;text-align:left">海運專線</th></tr>
<tr><td style="padding:10px">單價</td><td style="padding:10px;font-weight:700;color:#E65100">NT$290/kg起</td><td style="padding:10px;font-weight:700;color:#E65100">NT$180/kg起</td></tr>
<tr><td style="padding:10px">10kg貓砂費用</td><td style="padding:10px">約NT$2,900</td><td style="padding:10px">約NT$1,800</td></tr>
<tr><td style="padding:10px">時效</td><td style="padding:10px">5-7天</td><td style="padding:10px">7-12天</td></tr>
<tr><td style="padding:10px">適合</td><td style="padding:10px">少量試用/急用</td><td style="padding:10px">大量囤貨/定期補貨</td></tr>
</table>
<p style="color:#E65100;font-weight:700">💡 省錢建議：貓砂+貓糧+寵物零食一起寄，合併重量更划算！</p>'''),
    ],
    faq_items=[
        ('台灣貓砂可以寄大陸嗎？', '可以。豆腐砂、礦砂、木屑砂、水晶砂均可走敏感貨專線寄大陸。貓砂屬寵物用品，非違禁品，正常申報即可通關。'),
        ('貓砂寄大陸一包多少錢？', '空運NT$290/kg起，海運NT$180/kg起。一包6L豆腐砂約2-3kg，空運約NT$580-870。10kg以下加NT$100派送費。建議多包一起寄走海運更省。'),
        ('貓砂寄大陸會有海關問題嗎？', '一般不會。貓砂是常見寵物用品，非食品非藥品，海關查驗風險低。但建議保留原包裝及購買證明，方便海關核對品名。'),
        ('貓砂和貓糧可以一起寄嗎？', '可以一起寄。貓糧走敏感貨專線（含肉類成分需確認），貓砂走普貨或敏感貨均可。合併寄送可以分攤派送費。'),
    ],
)

# ============================================================
# Page 3: 两岸快递对比
# ============================================================
make_page(
    filename='cross-strait-express-comparison.html',
    title='台灣寄大陸快遞哪家便宜2026｜郵局vs順豐vs集運vs速豹終極比較 | 速豹集運',
    desc='2026台灣寄大陸快遞終極對比：郵局、順豐、新竹物流、集運平台、速豹專線五大渠道價格/時效/可寄品類全PK。一張表看懂哪家最適合你。附常見品牌對比+省錢技巧。',
    keywords='台灣寄大陸哪家便宜,台灣寄大陸快遞比較,郵局寄大陸vs順豐,兩岸快遞推薦,台灣寄大陸最便宜',
    h1='台灣寄大陸快遞哪家便宜？2026五大渠道終極比較',
    subtitle='郵局 · 順豐 · 新竹物流 · 集運平台 · 速豹專線 — 價格/時效/品類全PK',
    oneliner='寄台灣到大陸，選對渠道運費差3倍！郵局最便宜但不收敏感貨（食品/保健品/化妝品）；順豐快但貴且限制多；集運平台便宜但時效慢；速豹專線走敏感貨NT$290/kg起包稅雙清。一張表看懂你的貨該走哪家。',
    sections=[
        ('五大渠道價格時效總表', '''
<table style="width:100%;border-collapse:collapse;margin:20px 0;font-size:15px">
<tr style="background:#E3F2FD"><th style="padding:12px;text-align:left">管道</th><th style="padding:12px">價格</th><th style="padding:12px">時效</th><th style="padding:12px">敏感貨</th><th style="padding:12px">適合</th></tr>
<tr><td style="padding:10px;font-weight:700">中華郵政</td><td style="padding:10px;color:#008A00">最便宜<br>約NT$100-300/件</td><td style="padding:10px;color:#E65100">10-21天<br>不穩定</td><td style="padding:10px;color:#D32F2F">❌ 不收</td><td style="padding:10px">文件/衣物/書籍</td></tr>
<tr><td style="padding:10px;font-weight:700">順豐速運</td><td style="padding:10px;color:#E65100">較貴<br>NT$200-450/kg</td><td style="padding:10px;color:#008A00">3-5天<br>最快</td><td style="padding:10px;color:#E65100">⚠️ 限制多</td><td style="padding:10px">文件/新品/3C</td></tr>
<tr><td style="padding:10px;font-weight:700">新竹物流</td><td style="padding:10px">中等<br>NT$150-350/kg</td><td style="padding:10px">5-10天</td><td style="padding:10px;color:#E65100">⚠️ 部分收</td><td style="padding:10px">一般包裹</td></tr>
<tr><td style="padding:10px;font-weight:700">集運平台</td><td style="padding:10px;color:#008A00">便宜<br>NT$90-180/kg</td><td style="padding:10px;color:#E65100">7-15天<br>慢</td><td style="padding:10px;color:#008A00">✅ 可收</td><td style="padding:10px">大批量/不急</td></tr>
<tr style="background:#FFF8E1"><td style="padding:10px;font-weight:700">速豹專線</td><td style="padding:10px;color:#E65100;font-weight:700">NT$290/kg起<br>包稅雙清</td><td style="padding:10px;color:#008A00;font-weight:700">5-7天空運</td><td style="padding:10px;color:#008A00;font-weight:700">✅ 專收敏感貨</td><td style="padding:10px">食品/保健品/化妝品</td></tr>
</table>'''),
        ('選哪家？看你的貨品類型', '''
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;margin:20px 0">
<div style="background:#E8F5E9;padding:20px;border-radius:8px"><strong>📄 文件/書籍/衣物</strong><br><span style="color:#666">→ 郵局最便宜</span></div>
<div style="background:#FFF3E0;padding:20px;border-radius:8px"><strong>📱 3C/電子/有發票新品</strong><br><span style="color:#666">→ 順豐最快（但限制多）</span></div>
<div style="background:#E3F2FD;padding:20px;border-radius:8px"><strong>🍪 食品/零食/伴手禮</strong><br><span style="color:#666">→ 郵局不收，順豐不一定收 → 速豹專線</span></div>
<div style="background:#F3E5F5;padding:20px;border-radius:8px"><strong>💊 保健品/化妝品/茶葉</strong><br><span style="color:#666">→ 郵局不收 → 速豹專線NT$290起</span></div>
<div style="background:#FCE4EC;padding:20px;border-radius:8px"><strong>📦 大量/貓砂/液體</strong><br><span style="color:#666">→ 海運NT$180/kg起最省</span></div>
<div style="background:#ECEFF1;padding:20px;border-radius:8px"><strong>🔄 退貨/返修</strong><br><span style="color:#666">→ 返修專線NT$350/kg起</span></div>
</div>'''),
    ],
    faq_items=[
        ('台灣寄大陸最便宜的快遞是哪家？', '看貨品：寄文件/衣物選郵局（NT$100-300/件）；寄食品/保健品/化妝品郵局不收，速豹專線NT$290/kg起是敏感貨最便宜的選擇。大量貨物選海運NT$180/kg起。'),
        ('郵局vs順豐vs速豹哪個好？', '郵局便宜但不收敏感貨；順豐快但貴（NT$200-450/kg）且對食品/保健品限制多；速豹專線專收敏感貨（食品/保健品/化妝品/茶葉），NT$290/kg起包稅雙清，是敏感貨最佳選擇。'),
        ('台灣寄大陸運費怎麼省？', '1) 不趕時間選海運（NT$180/kg起）；2) 多件合併寄（攤派送費）；3) 滿10kg免派送費；4) 避開節假日（春節/雙11運費漲20-50%）；5) 壓縮體積（衣物用真空袋）。'),
        ('寄大陸會被收關稅嗎？', '個人自用物品價值800人民幣以內通常免稅。速豹專線NT$290/kg起已含清關費用（包稅雙清），一般不用額外繳稅。高價值物品需如實申報。'),
    ],
)

# ============================================================
# Page 4: 集运推荐合集
# ============================================================
make_page(
    filename='tw-to-cn-consolidation-recommend.html',
    title='台灣集運到大陸推薦2026｜兩岸集運平台怎麼選？5大重點一次懂 | 速豹集運',
    desc='台灣集運到大陸推薦指南：集運是什麼？怎麼選集運商？價格/時效/服務/理賠/客服5大評估重點。附台灣寄大陸集運流程圖+常見陷阱避雷。敏感貨集運推薦速豹專線。',
    keywords='台灣集運推薦,台灣到大陸集運,兩岸集運平台,集運怎麼選,台灣寄大陸集運價格',
    h1='台灣集運到大陸推薦2026｜集運平台怎麼選才不踩雷',
    subtitle='兩岸集運入門 · 5大評估重點 · 敏感貨集運首選',
    oneliner='台灣集運到大陸就是把多家買的東西集中到台灣集運倉，統一打包寄往大陸。選集運商要看5點：價格是否透明、敏感貨能不能收、時效穩不穩定、丟件怎麼賠、客服找不找得到人。速豹集運專收敏感貨，NT$290/kg起包稅雙清，5-7天空運直達。',
    sections=[
        ('集運是什麼？3分鐘看懂', '''
<ol style="line-height:2.2">
<li><strong>註冊集運帳號</strong>：選擇集運平台，獲取專屬倉庫地址</li>
<li><strong>購物寄到集運倉</strong>：在台灣各電商/實體店購買，寄到集運倉地址</li>
<li><strong>合併打包</strong>：所有包裹到齊後，集運商統一打包、秤重、計算運費</li>
<li><strong>支付運費出貨</strong>：付款後，集運商安排空運/海運送往大陸</li>
<li><strong>大陸清關+派送</strong>：到港清關後，快遞派送到大陸收件地址</li>
</ol>'''),
        ('選集運商的5大重點', '''
<table style="width:100%;border-collapse:collapse;margin:20px 0">
<tr style="background:#E3F2FD"><th style="padding:12px;text-align:left">評估點</th><th style="padding:12px;text-align:left">怎麼判斷</th><th style="padding:12px;text-align:left">速豹表現</th></tr>
<tr><td style="padding:10px"><strong>1. 價格透明</strong></td><td style="padding:10px">有公開價格表？隱藏費用？</td><td style="padding:10px;color:#008A00">✅ NT$290/kg起，官網公開</td></tr>
<tr><td style="padding:10px"><strong>2. 敏感貨能力</strong></td><td style="padding:10px">食品/保健品/化妝品能寄？</td><td style="padding:10px;color:#008A00">✅ 專收敏感貨，包稅雙清</td></tr>
<tr><td style="padding:10px"><strong>3. 時效穩定</strong></td><td style="padding:10px">實際時效 vs 宣稱時效</td><td style="padding:10px;color:#008A00">✅ 空運5-7天，海運7-12天</td></tr>
<tr><td style="padding:10px"><strong>4. 理賠政策</strong></td><td style="padding:10px">丟件/破損怎麼賠？</td><td style="padding:10px;color:#008A00">✅ 可購買運輸保險</td></tr>
<tr><td style="padding:10px"><strong>5. 客服響應</strong></td><td style="padding:10px">找得到人？回覆速度？</td><td style="padding:10px;color:#008A00">✅ LINE @734dooky 30分鐘回</td></tr>
</table>'''),
        ('集運常見陷阱避雷', '''
<ul style="line-height:2.2">
<li>❌ <strong>低價誘餌</strong>：廣告寫NT$50/kg，實際加一堆手續費</li>
<li>❌ <strong>敏感貨偷跑</strong>：說可以寄食品，結果走非法管道被海關扣</li>
<li>❌ <strong>體積重灌水</strong>：故意用大箱子裝小東西，材積重暴增</li>
<li>❌ <strong>客服消失</strong>：出問題找不到人，LINE已讀不回</li>
<li>✅ <strong>速豹對策</strong>：價格官網公開、正規報關、實際重量計費、LINE 30分鐘回</li>
</ul>'''),
    ],
    faq_items=[
        ('台灣集運到大陸推薦哪家？', '看你的貨品類型：寄一般衣物書籍選郵局或一般集運平台；寄食品/保健品/化妝品/茶葉等敏感貨推薦速豹集運（NT$290/kg起包稅雙清，5-7天空運直達）。'),
        ('集運運費怎麼算？', '空運約NT$290/kg起，海運NT$180/kg起。部分平台按實際重量或體積重量取大值計費。速豹按實際重量計費，10kg以下加NT$100派送費，滿10kg免派送費。'),
        ('集運可以寄食品/保健品嗎？', '一般集運平台和郵局不收敏感貨。速豹專線專收食品/保健品/化妝品/茶葉等敏感貨，正規報關包稅雙清，是敏感貨集運的最佳選擇。'),
        ('集運東西丟了怎麼辦？', '選擇有理賠政策的集運商很重要。速豹提供運輸保險（可選購），確認保價後如有丟失按保價金額賠償。建議高價值物品購買保險。'),
    ],
)

print('\nDone! 4 content pages generated.')
