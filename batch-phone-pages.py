#!/usr/bin/env python3
"""批量生成手机品类品牌页面"""
import os

SITE_DIR = "/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn/blog"

BRANDS = {
    "iphone-shipping": {
        "title": "iPhone可以寄大陸嗎？台灣買iPhone寄大陸攻略 NT$350/kg起包稅 | 速豹集運",
        "h1": "iPhone可以寄大陸嗎？台灣買iPhone寄大陸完整攻略 2026",
        "desc": "iPhone可以寄大陸嗎？可以！台灣買iPhone比大陸便宜10-15%，走含電池特貨專線NT$350/kg起包稅雙清，最快5-7天。單支iPhone約0.3kg運費NT$350。LINE傳照片30秒確認！",
        "keywords": "iPhone寄大陸,iPhone可以寄大陸嗎,台灣買iPhone寄大陸,蘋果手機寄大陸,iPhone寄大陸運費,台灣iPhone寄大陸",
        "pillar_name": "手機寄大陸",
        "pillar_url": "/blog/phone-shipping-guide",
        "content": """<h2>📱 iPhone 寄大陸全攻略</h2>
<p>台灣買 iPhone 寄大陸，是近期兩岸代購最熱門的生意之一。iPhone 在台灣定價比大陸便宜 10-15%，以 iPhone 17 Pro 256GB 為例：台灣約 NT$38,900 vs 大陸約 ¥9,999（約 NT$44,000），<strong>一支省 NT$5,000+</strong>。走含電池特貨專線 NT$350/kg，單支約 0.3kg，運費 NT$350。包稅雙清、最快 5-7 天送達。</p>
<h3>💰 台灣 vs 大陸 iPhone 價格對比</h3>
<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:14px">
<tr style="background:#e8f0fe"><th style="padding:10px;text-align:left">型號</th><th style="padding:10px">台灣售價</th><th style="padding:10px">大陸售價</th><th style="padding:10px">價差</th></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e2e8f0">iPhone 17 256GB</td><td style="padding:10px;border-bottom:1px solid #e2e8f0">NT$32,900</td><td style="padding:10px;border-bottom:1px solid #e2e8f0">¥7,999 (~NT$35,500)</td><td style="padding:10px;border-bottom:1px solid #e2e8f0;color:#059669;font-weight:700">省 NT$2,600</td></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e2e8f0">iPhone 17 Pro 256GB</td><td style="padding:10px;border-bottom:1px solid #e2e8f0">NT$38,900</td><td style="padding:10px;border-bottom:1px solid #e2e8f0">¥8,999 (~NT$40,000)</td><td style="padding:10px;border-bottom:1px solid #e2e8f0;color:#059669;font-weight:700">省 NT$1,100</td></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e2e8f0">iPhone 17 Pro Max 256GB</td><td style="padding:10px;border-bottom:1px solid #e2e8f0">NT$42,900</td><td style="padding:10px;border-bottom:1px solid #e2e8f0">¥9,999 (~NT$44,000)</td><td style="padding:10px;border-bottom:1px solid #e2e8f0;color:#059669;font-weight:700">省 NT$1,100</td></tr>
</table>
<h3>📦 包裝重點</h3>
<ul>
<li><strong>不要拆封！</strong>原廠封膜完整是通關和保固的關鍵</li>
<li>原廠盒子外層再用氣泡紙包裹 2-3 層</li>
<li>放入紙箱後四周塞填充物，防止晃動</li>
<li>加保價（iPhone 高價值，建議運費×20%），單支保費約 NT$70</li>
<li>購買發票或收據留好，附在包裹裡輔助通關</li>
</ul>
<h3>🛒 購買建議</h3>
<p>推薦購買管道：<strong>Apple Store 直營店（台北101/信義A13）</strong>貨源最穩、可當場驗機。Studio A/燦坤/順發等授權經銷商常有「買手機送配件」活動。Costco 偶有大特價但型號不齊。不要買通訊行水貨——可能有鎖機或翻新機風險。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>iPhone 含鋰電池，走<strong>含電池特貨專線 NT$350/kg</strong>。郵局不收含電池手機。申報時寫「手機/個人自用」，控制在 1-2 支合理自用範圍。台灣版 iPhone 在中國大陸使用完全正常（頻段支援），但 Apple Intelligence AI 功能在兩地版本可能有差異。</p>"""
    },
    "samsung-phone-shipping": {
        "title": "三星手機可以寄大陸嗎？Galaxy S26/Z Fold寄送攻略 NT$350/kg起 | 速豹集運",
        "h1": "三星手機可以寄大陸嗎？台灣買三星寄大陸攻略 2026",
        "desc": "三星手機可以寄大陸嗎？可以！台灣三星旗艦機比大陸便宜，走含電池特貨專線NT$350/kg起包稅雙清，最快5-7天。一支Galaxy S26約0.3kg運費NT$350。LINE傳照片30秒確認！",
        "keywords": "三星手機寄大陸,三星寄大陸,Samsung寄大陸,Galaxy S26寄大陸,Z Fold寄大陸,台灣三星寄大陸",
        "pillar_name": "手機寄大陸",
        "pillar_url": "/blog/phone-shipping-guide",
        "content": """<h2>📱 三星手機寄大陸全攻略</h2>
<p>三星（Samsung）旗艦機型在台灣的定價通常比大陸便宜 5-10%，加上台灣常有通訊行優惠（如傑昇通信 Samsung Galaxy S26 降 NT$4,910），<strong>實際到手價更低</strong>。走含電池特貨 NT$350/kg，一支約 0.3kg，運費 NT$350。</p>
<h3>🔥 台灣三星熱門機型</h3>
<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:14px">
<tr style="background:#e8f0fe"><th style="padding:10px;text-align:left">型號</th><th style="padding:10px">台灣參考價</th><th style="padding:10px">寄送難度</th></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e2e8f0">Galaxy S26 (12G/256G)</td><td style="padding:10px;border-bottom:1px solid #e2e8f0">約 NT$25,000-30,900</td><td style="padding:10px;border-bottom:1px solid #e2e8f0">簡單</td></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e2e8f0">Galaxy Z Fold6</td><td style="padding:10px;border-bottom:1px solid #e2e8f0">約 NT$55,000-60,000</td><td style="padding:10px;border-bottom:1px solid #e2e8f0">建議加保價</td></tr>
<tr><td style="padding:10px">Galaxy Z Flip6</td><td style="padding:10px">約 NT$32,000-35,000</td><td style="padding:10px">簡單</td></tr>
</table>
<h3>📦 包裝重點</h3>
<ul>
<li>原廠盒裝完整寄送，不要拆封膜</li>
<li>摺疊機（Z Fold/Z Flip）螢幕更脆弱，原廠盒外再加一層氣泡紙</li>
<li>建議加保價，尤其是 Z Fold 系列（單價高）</li>
<li>購買發票附在包裹裡</li>
</ul>
<h3>🛒 購買建議</h3>
<p>三星在台灣的通路比 iPhone 更多元：<strong>三星智慧館（官方直營）</strong>貨源最穩；<strong>傑昇通信/地標網通</strong>等通訊行常有比官網低 NT$3,000-5,000 的優惠；Costco 偶有綁約價但需搭門號。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>走含電池特貨 NT$350/kg。三星手機在中國大陸使用需注意：Google 服務在國行版三星被限制，但台灣版三星自帶完整 Google 服務，這反而是優勢。控制在 1-2 支自用範圍。</p>"""
    },
    "google-pixel-shipping": {
        "title": "Google Pixel可以寄大陸嗎？Pixel 10/Pro寄送攻略 NT$350/kg起 | 速豹集運",
        "h1": "Google Pixel可以寄大陸嗎？台灣買Pixel寄大陸攻略 2026",
        "desc": "Google Pixel可以寄大陸嗎？可以！台灣買Pixel比從美國代購更近更快，走含電池特貨NT$350/kg起包稅雙清，5-7天送達。Pixel 10約0.3kg運費NT$350。LINE傳照片30秒確認！",
        "keywords": "Google Pixel寄大陸,Pixel可以寄大陸嗎,台灣Pixel寄大陸,Pixel 10寄大陸,Google手機寄大陸",
        "pillar_name": "手機寄大陸",
        "pillar_url": "/blog/phone-shipping-guide",
        "content": """<h2>📱 Google Pixel 寄大陸全攻略</h2>
<p>Google Pixel 在大陸沒有官方銷售渠道，但<strong>大陸科技圈和開發者對 Pixel 的需求極大</strong>——原生 Android 體驗、最快的系統更新、獨家 AI 功能（Google Gemini）。台灣是亞洲少數有官方銷售 Pixel 的地區，從台灣買 Pixel 寄大陸是最方便的路徑。走含電池特貨 NT$350/kg。</p>
<h3>🔥 為什麼 Pixel 寄大陸這麼熱門？</h3>
<ul>
<li>大陸買不到官方 Pixel，只能靠代購/水貨</li>
<li>台灣 Google Store 定價合理，Pixel 10 約 NT$24,900 起</li>
<li>Pixel 的 AI 功能（Gemini/Circle to Search）在原生系統上體驗最好</li>
<li>開發者需要 Pixel 做 Android 開發測試</li>
</ul>
<h3>📦 包裝重點</h3>
<ul>
<li>Google Store 出貨的原廠包裝已經很安全，外層再加氣泡紙即可</li>
<li>Pixel 的相機模組是橫條設計較突出，包裝時注意不要壓到鏡頭</li>
<li>建議加保價（NT$24,900 保費約 NT$85）</li>
<li>購買發票或 Google Store 訂單截圖附在包裹裡</li>
</ul>
<h3>🛒 購買建議</h3>
<p>Pixel 在台灣的官方渠道：<strong>Google Store 官網（store.google.com/tw）</strong>最穩、常有預購禮；<strong>台灣大哥大</strong>獨家代理，可搭門號或買空機；momo/PChome 也有賣但價格通常跟官網一樣。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>走含電池特貨 NT$350/kg。Pixel 在中國大陸使用需注意：Google 服務在國內被限制，但 Pixel 用戶通常已自備翻牆方案。台灣版 Pixel 支援完整 5G 頻段，電信相容性沒問題。控制在 1-2 支自用範圍。</p>"""
    },
    "asus-phone-shipping": {
        "title": "華碩手機可以寄大陸嗎？Zenfone/ROG Phone寄送攻略 NT$350/kg起 | 速豹集運",
        "h1": "華碩手機可以寄大陸嗎？台灣買華碩寄大陸攻略 2026",
        "desc": "華碩手機可以寄大陸嗎？可以！Zenfone/ROG Phone台灣品牌在地最便宜，走含電池特貨NT$350/kg起包稅雙清，最快5-7天。一支ROG Phone約0.4kg運費NT$350。LINE傳照片30秒確認！",
        "keywords": "華碩手機寄大陸,ASUS手機寄大陸,Zenfone寄大陸,ROG Phone寄大陸,台灣買華碩手機寄大陸",
        "pillar_name": "手機寄大陸",
        "pillar_url": "/blog/phone-shipping-guide",
        "content": """<h2>📱 華碩手機寄大陸全攻略</h2>
<p>華碩（ASUS）是台灣本土品牌，Zenfone 和 ROG Phone 系列在台灣的訂價通常比大陸便宜 10-15%，而且<strong>台灣是首發地區、型號最齊全</strong>。ROG Phone 電競手機在大陸手遊圈極受歡迎，是代購熱門品項。走含電池特貨 NT$350/kg。</p>
<h3>🔥 華碩熱門機型</h3>
<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:14px">
<tr style="background:#e8f0fe"><th style="padding:10px;text-align:left">型號</th><th style="padding:10px">特色</th><th style="padding:10px">台灣參考價</th></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e2e8f0">Zenfone 11 Ultra</td><td style="padding:10px;border-bottom:1px solid #e2e8f0">旗艦拍照手機</td><td style="padding:10px;border-bottom:1px solid #e2e8f0">約 NT$29,990</td></tr>
<tr><td style="padding:10px;border-bottom:1px solid #e2e8f0">ROG Phone 9 Pro</td><td style="padding:10px;border-bottom:1px solid #e2e8f0">電競旗艦，大陸手遊圈最愛</td><td style="padding:10px;border-bottom:1px solid #e2e8f0">約 NT$35,990</td></tr>
<tr><td style="padding:10px">Zenfone 11</td><td style="padding:10px">輕巧小旗艦</td><td style="padding:10px">約 NT$24,990</td></tr>
</table>
<h3>📦 包裝重點</h3>
<ul>
<li>原廠盒裝完整寄送，不要拆封</li>
<li>ROG Phone 盒裝較大，材積重可能超過實重（需注意）</li>
<li>ROG Phone 含散熱風扇配件，原廠盒內已有固定，不用拆出</li>
<li>建議加保價（ROG Phone 高單價尤其需要）</li>
</ul>
<h3>🛒 購買建議</h3>
<p>華碩在台灣的購買管道：<strong>ASUS 官方商城/三創旗艦店</strong>貨源最穩、首發最快；<strong>PChome/momo</strong>常有組合優惠（送保護殼+充電器）；光華商場通訊行價格可能更低但需注意是否為全新公司貨。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>走含電池特貨 NT$350/kg。ROG Phone 是大陸手遊玩家心中的「機皇」，代購需求穩定。台灣版 Zenfone/ROG Phone 支援完整 5G 頻段，在中國大陸使用正常。控制在 1-2 支自用範圍。</p>"""
    },
}

# 复用 v1 模板生成函数
def generate_brand_page(key, data):
    title, h1, desc, keywords, content = data["title"], data["h1"], data["desc"], data["keywords"], data["content"]
    pillar_name, pillar_url = data["pillar_name"], data["pillar_url"]
    
    page = f'''<!DOCTYPE html><html lang="zh-TW"><head>
  <meta charset="UTF-8"><link rel="icon" href="/favicon.ico"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{keywords}">
  <meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
  <meta property="og:image" content="https://subao.tw/images/subao-logo-new.webp">
  <meta property="og:url" content="https://subao.tw/blog/{key}"><meta property="og:type" content="article"><meta property="og:locale" content="zh_TW">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="canonical" href="https://subao.tw/blog/{key}"><meta name="lastmod" content="2026-08-06">
  <style>:root{{--primary:#1a56db;--primary-light:#e8f0fe;--text-dark:#1a1a2e;--text-light:#64748b;--bg:#f8fafc;--white:#fff;--border:#e2e8f0;--green:#059669;--amber:#d97706;--radius:12px;--shadow:0 2px 8px rgba(0,0,0,.08)}}*{{margin:0;padding:0;box-sizing:border-box}}body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang TC","Microsoft JhengHei",sans-serif;color:var(--text-dark);background:var(--bg);line-height:1.7}}.container{{max-width:800px;margin:0 auto;padding:0 20px}}header{{background:var(--white);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100}}nav{{display:flex;align-items:center;justify-content:space-between;max-width:1200px;margin:0 auto;padding:12px 20px}}.logo{{font-size:22px;font-weight:800;color:var(--primary);text-decoration:none}}.nav-links{{display:flex;gap:20px;align-items:center}}.nav-links a{{color:var(--text-light);text-decoration:none;font-size:14px;font-weight:500}}.nav-links a:hover{{color:var(--primary)}}.btn-line{{background:var(--green);color:var(--white)!important;padding:8px 16px;border-radius:20px;font-weight:600;text-decoration:none;display:inline-flex;align-items:center;gap:6px;font-size:14px}}.top-promo{{background:linear-gradient(135deg,#1a56db,#2563eb);color:var(--white);text-align:center;padding:8px 16px;font-size:13px;position:relative;display:flex;align-items:center;justify-content:center;gap:12px;flex-wrap:wrap}}.top-promo a{{color:var(--white);background:rgba(255,255,255,.2);padding:4px 14px;border-radius:16px;text-decoration:none;font-weight:600;font-size:12px}}.top-promo-close{{position:absolute;right:12px;background:none;border:none;color:var(--white);font-size:20px;cursor:pointer}}.article-header{{background:var(--white);padding:40px 0 30px;border-bottom:1px solid var(--border);margin-bottom:30px}}.article-header h1{{font-size:28px;line-height:1.4;margin-bottom:12px}}.article-meta{{color:var(--text-light);font-size:13px}}.article-body{{background:var(--white);padding:30px 0;border-radius:var(--radius);box-shadow:var(--shadow);margin-bottom:30px}}.article-body .container{{padding:0 24px}}.article-body h2{{font-size:22px;margin:30px 0 14px;padding-bottom:8px;border-bottom:2px solid var(--primary-light)}}.article-body h3{{font-size:18px;margin:22px 0 10px}}.article-body p{{margin:10px 0;color:#334155}}.article-body ul{{margin:10px 0;padding-left:24px}}.article-body li{{margin:6px 0;color:#334155}}.article-body li strong{{color:var(--text-dark)}}.cta-box{{background:linear-gradient(135deg,#eff6ff,#dbeafe);border:2px solid var(--primary);border-radius:var(--radius);padding:24px;margin:30px 0;text-align:center}}.cta-box p{{font-size:16px;margin-bottom:14px}}.cta-box .btn{{display:inline-block;background:var(--green);color:var(--white);padding:12px 28px;border-radius:24px;text-decoration:none;font-weight:700;font-size:16px}}.pillar-nav{{background:var(--white);border-radius:var(--radius);box-shadow:var(--shadow);padding:20px 24px;margin-bottom:30px}}.pillar-nav strong{{display:block;margin-bottom:10px;color:var(--primary)}}.pillar-nav a{{color:var(--primary);text-decoration:none;font-size:14px;font-weight:500}}.internal-links{{background:var(--white);border-radius:var(--radius);box-shadow:var(--shadow);padding:20px 24px;margin-bottom:30px}}.internal-links p{{margin:0 0 10px;font-weight:700;font-size:15px}}.internal-links a{{display:inline-block;background:var(--primary-light);color:var(--primary);padding:6px 12px;border-radius:6px;text-decoration:none;font-size:13px;margin:4px 6px 4px 0;font-weight:500}}.internal-links a:hover{{background:var(--primary);color:var(--white)}}.faq-section{{background:var(--white);border-radius:var(--radius);box-shadow:var(--shadow);padding:24px;margin-bottom:30px}}.faq-section h2{{margin-top:0!important;border-bottom:none!important}}.faq-item{{border-bottom:1px solid var(--border);padding:14px 0}}.faq-item:last-child{{border-bottom:none}}.faq-question{{font-weight:700;font-size:15px;margin-bottom:6px}}.faq-answer{{color:#475569;font-size:14px}}footer{{background:var(--text-dark);color:var(--white);padding:40px 0 20px;margin-top:40px}}footer a{{color:#94a3b8;text-decoration:none;font-size:13px;display:block;margin:4px 0}}footer a:hover{{color:var(--white)}}.footer-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:24px;max-width:1200px;margin:0 auto;padding:0 20px}}footer h3{{font-size:16px;margin-bottom:10px;color:var(--white)}}.footer-bottom{{text-align:center;padding-top:20px;margin-top:20px;border-top:1px solid #334155;color:#64748b;font-size:13px;max-width:1200px;margin:0 auto;padding:20px 20px 0}}.float-bar{{position:fixed;bottom:0;left:0;right:0;background:var(--white);border-top:2px solid var(--primary);padding:12px 20px;display:flex;align-items:center;justify-content:space-between;z-index:200;box-shadow:0 -4px 16px rgba(0,0,0,.08);flex-wrap:wrap;gap:8px}}.float-bar-text{{font-size:13px;line-height:1.4}}.float-bar-text strong{{color:var(--primary)}}.float-bar-text small{{display:block;color:var(--text-light);font-size:11px}}.float-bar-close{{position:absolute;top:4px;right:12px;background:none;border:none;font-size:18px;cursor:pointer;color:var(--text-light)}}table{{width:100%;border-collapse:collapse;margin:16px 0;font-size:14px}}th{{background:var(--primary-light);color:var(--primary);padding:10px 12px;text-align:left;font-weight:600}}td{{padding:10px 12px;border-bottom:1px solid var(--border)}}tr:hover td{{background:#f8fafc}}</style>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-X2T4LGTKJ1"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-X2T4LGTKJ1');</script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"首頁","item":{{"@id":"https://subao.tw/","name":"首頁"}}}},{{"@type":"ListItem","position":2,"name":"{pillar_name}","item":{{"@id":"https://subao.tw{pillar_url}","name":"{pillar_name}"}}}},{{"@type":"ListItem","position":3,"name":"{h1}"}}]}}</script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"{h1}","acceptedAnswer":{{"@type":"Answer","text":"可以寄！走含電池特貨專線 NT$350/kg 起包稅雙清，最快5-7天送達。單支手機約0.3kg運費NT$350。需注意原廠封膜完整、含購買發票、控制在1-2支合理自用範圍。"}}}},{{"@type":"Question","name":"運費怎麼算？一支手機寄大陸多少錢？","acceptedAnswer":{{"@type":"Answer","text":"含電池特貨 NT$350/kg，最低收費 NT$350。一支手機約0.3kg，運費 NT$350。包稅雙清、無隱藏費用。建議加保價（運費×20%），一支iPhone保費約NT$70。"}}}},{{"@type":"Question","name":"寄手機到大陸會被課稅嗎？","acceptedAnswer":{{"@type":"Answer","text":"走包稅專線關稅已含在運費內。個人自用1-2支手機走行郵稅通常免稅（稅額NT$50以下免徵），但包稅專線直接幫你處理好，不用擔心補稅通知。"}}}},{{"@type":"Question","name":"手機寄大陸要多久？包裝要注意什麼？","acceptedAnswer":{{"@type":"Answer","text":"含電池特貨空運 5-7 天送達。包裝關鍵：原廠封膜不要拆、盒裝完整寄送、外層加氣泡紙、建議加保價。郵局不收含電池手機，必須走特貨專線。"}}}}]}}</script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{h1}","description":"{desc}","datePublished":"2026-08-06","dateModified":"2026-08-06","author":{{"@type":"Organization","name":"速豹集運","url":"https://subao.tw"}},"publisher":{{"@type":"Organization","name":"速豹集運","url":"https://subao.tw","logo":{{"@type":"ImageObject","url":"https://subao.tw/images/subao-logo-new.webp"}}}},"image":"https://subao.tw/images/subao-logo-new.webp","mainEntityOfPage":{{"@type":"WebPage","@id":"https://subao.tw/blog/{key}"}}}}</script>
</head><body>
<header><nav><a href="/" class="logo">速豹集運</a><div class="nav-links"><a href="/tw-to-cn">台灣寄大陸</a><a href="/pricing">運費說明</a><a href="/article-list">文章攻略</a><a href="/faq">常見問題</a><a href="https://line.me/R/ti/p/@734dooky" class="btn-line" target="_blank" onclick="gtag('event','line_click',{{event_category:'conversion',event_label:'nav'}});gtag('event','generate_lead',{{event_category:'lead',event_label:'line'}})">💬 LINE 咨詢</a></div></nav></header>
<div class="top-promo" id="topPromo"><span>📦 不確定能不能寄？</span><a href="https://line.me/R/ti/p/@734dooky" target="_blank" onclick="gtag('event','line_click',{{event_category:'conversion',event_label:'top_promo'}});gtag('event','generate_lead',{{event_category:'lead',event_label:'line'}})">LINE 免費估價 →</a><button class="top-promo-close" onclick="this.parentElement.style.display='none'" aria-label="關閉">×</button></div>
<div class="article-header"><div class="container"><h1>{h1}</h1><div class="article-meta">📅 2026-08-06 更新 · 速豹集運 · 5-7天送達</div></div></div>
<div class="article-body"><div class="container">
<div class="pillar-nav"><strong>📌 返回主題總覽：</strong><a href="{pillar_url}">{pillar_name}完整攻略 →</a></div>
{content}
<div class="cta-box"><p>📱 <strong>要寄手機了？傳照片給我們確認運費和包裝</strong></p><p style="font-size:14px;color:var(--text-light)">LINE @734dooky · 含電池特貨 NT$350/kg · 包稅雙清</p><a href="https://line.me/R/ti/p/@734dooky" class="btn" target="_blank" onclick="gtag('event','line_click',{{event_category:'conversion',event_label:'cta_box'}});gtag('event','generate_lead',{{event_category:'lead',event_label:'line'}})">💬 LINE 立即咨詢</a></div>
<div class="internal-links"><p>🔗 相關寄送指南</p><a href="{pillar_url}">{pillar_name}</a><a href="/blog/electronics-shipping">電子產品寄大陸</a><a href="/pricing">運費查詢</a><a href="/blog/tw-to-cn-customs">海關通關指南</a></div>
</div></div>
<div class="faq-section"><div class="container"><h2>❓ 常見問題</h2>
<div class="faq-item"><div class="faq-question">Q: {h1}</div><div class="faq-answer">A: 可以寄！走含電池特貨專線 NT$350/kg 起包稅雙清，最快5-7天送達。郵局不收含電池手機，必須走特貨。控制在1-2支合理自用範圍，附購買發票。</div></div>
<div class="faq-item"><div class="faq-question">Q: 運費怎麼算？最低多少？</div><div class="faq-answer">A: 含電池特貨 NT$350/kg，最低收費 NT$350（不滿1kg以1kg計）。一支手機約0.3kg，運費 NT$350。建議加保價（運費×20%），iPhone保費約NT$70。</div></div>
<div class="faq-item"><div class="faq-question">Q: 寄手機到大陸會被海關扣嗎？</div><div class="faq-answer">A: 走包稅專線基本上不會。手機申報為「個人自用」，附購買發票更穩。1-2支合理自用範圍通關順暢。</div></div>
<div class="faq-item"><div class="faq-question">Q: 台灣版手機在大陸能正常使用嗎？</div><div class="faq-answer">A: iPhone/三星/華碩台版在中國大陸使用完全正常，頻段和電信相容性沒問題。Pixel因Google服務需自備翻牆。台灣版三星自帶完整Google服務反而是優勢。</div></div>
</div></div>
<footer><div class="footer-grid"><div><h3>速豹集運</h3><p style="font-size:13px;color:#94a3b8">台灣寄大陸專家，專營敏感貨兩岸快遞服務。</p><p style="font-size:13px;color:#94a3b8">LINE：<a href="https://line.me/R/ti/p/@734dooky" target="_blank" style="color:#60a5fa;display:inline">@734dooky</a></p></div><div><h3>服務項目</h3><a href="/tw-to-cn">台灣發大陸</a><a href="/pricing">運費說明</a><a href="/article-list">文章攻略</a><a href="/pickup-service">上門取貨</a><a href="/faq">常見問題</a></div><div><h3>寄送指南</h3><a href="/blog/tea-shipping-guide">茶葉寄送</a><a href="/blog/cosmetics-shipping">化妝品寄送</a><a href="/blog/health-products-shipping">保健品寄送</a><a href="/blog/food-shipping-guide">食品寄送</a></div><div><h3>幫助中心</h3><a href="/about">關於我們</a><a href="/pricing">運費查詢</a><a href="https://line.me/R/ti/p/@734dooky" target="_blank">LINE 客服</a></div></div><div class="footer-bottom"><p>© 2026 速豹集運 Subao.tw All rights reserved.</p></div></footer>
<div class="float-bar" id="floatBar"><button class="float-bar-close" onclick="this.parentElement.style.display='none'" aria-label="關閉">×</button><div class="float-bar-text"><p>📦 不確定能不能寄？<strong>傳照片免費評估</strong></p><small>LINE：@734dooky　平均30分鐘內回覆</small></div><a href="https://line.me/R/ti/p/@734dooky" class="btn-line" target="_blank" onclick="gtag('event','line_click',{{event_category:'conversion',event_label:'float_bar'}});gtag('event','generate_lead',{{event_category:'lead',event_label:'line'}})">💬 LINE 咨詢</a></div>
</body></html>'''
    return page

if __name__ == "__main__":
    for key, data in BRANDS.items():
        filepath = os.path.join(SITE_DIR, f"{key}.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(generate_brand_page(key, data))
        print(f"✅ {key}.html")
    print(f"\n🎉 共生成 {len(BRANDS)} 个手机品牌页")
