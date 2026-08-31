# -*- coding: utf-8 -*-
"""生成 taiwan-to-china-duty-tax.html（台灣寄大陸關稅計算與免稅額度權威頁）
模板：pricing-calculator.html（複製後改造 head / schema / main / 計算器 JS）
"""
import re, sys

SRC = 'pricing-calculator.html'
DST = 'taiwan-to-china-duty-tax.html'

html = open(SRC, encoding='utf-8').read()

def rep(old, new, label, count=1):
    global html
    n = html.count(old)
    assert n == count, f'[{label}] 期望 {count} 次匹配，實際 {n} 次'
    html = html.replace(old, new)
    print(f'  ✅ {label}')

# ============ 1. head meta ============
rep('<title>台灣寄大陸運費試算【30秒算好】2026即時報價｜NT$290/kg起 - 速豹集運</title>',
    '<title>台灣寄大陸關稅計算2026｜免稅額度800元＋50元免徵＋行郵稅率13%/20%/50% - 速豹集運</title>',
    'title')

rep(re.search(r'<meta name="description"[^>]*>', html).group(0),
    '<meta name="description" content="台灣寄大陸關稅一次講清：個人包裹單票限值800元、應徵稅額50元以下免徵、行郵稅率13%/20%/50%。輸入貨值即時試算要繳多少關稅，附官方公告依據與稅率對照表。">',
    'description')

rep('<meta property="og:title" content="台灣寄大陸運費試算【30秒算好】2026即時報價｜NT$290/kg起 - 速豹集運">',
    '<meta property="og:title" content="台灣寄大陸關稅計算2026｜免稅額度800元＋50元免徵＋行郵稅率表 - 速豹集運">',
    'og:title')

rep(re.search(r'<meta property="og:description"[^>]*>', html).group(0),
    '<meta property="og:description" content="台灣寄大陸關稅試算：輸入貨值即時算！800元限值、50元免徵、行郵稅率13%/20%/50%，一次講清。">',
    'og:description')

rep('<meta property="og:url" content="https://subao.tw/pricing-calculator">',
    '<meta property="og:url" content="https://subao.tw/taiwan-to-china-duty-tax">',
    'og:url')

rep('<link rel="canonical" href="https://subao.tw/pricing-calculator">',
    '<link rel="canonical" href="https://subao.tw/taiwan-to-china-duty-tax">',
    'canonical')

rep('<meta name="lastmod" content="2026-07-19">',
    '<meta name="lastmod" content="2026-08-31">',
    'lastmod')

# ============ 2. schema 块（按 @type 定位替换） ============
blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, flags=re.S)
assert len(blocks) == 4, f'schema 块数量异常: {len(blocks)}'

# 2a. WebApplication
wa = '''{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "台灣寄大陸關稅試算工具",
  "url": "https://subao.tw/taiwan-to-china-duty-tax",
  "description": "台灣寄大陸個人包裹關稅試算：輸入貨值與商品類別，自動計算應徵稅額，並判斷是否超過800元限值與50元免徵額。",
  "applicationCategory": "FinanceApplication",
  "operatingSystem": "Web",
  "offers": {"@type": "Offer", "price": "0", "priceCurrency": "TWD"},
  "provider": {
    "@type": "Organization",
    "name": "速豹集運",
    "url": "https://subao.tw",
    "contactPoint": {"@type": "ContactPoint", "contactType": "Customer Service", "lineContact": "@734dooky"}
  }
}'''
html = html.replace(blocks[0].strip(), wa, 1)
print('  ✅ WebApplication schema')

# 2b. HowTo
howto = '''{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "如何計算台灣寄大陸關稅",
  "description": "依序判斷商品類別稅率、申報貨值是否超過800元限值、應徵稅額是否超過50元免徵額，即可估算台灣寄大陸個人包裹要繳多少關稅。",
  "step": [
    {"@type": "HowToStep", "name": "確認商品類別與稅率", "text": "行郵稅分三檔：食品/保健品/奶粉等13%、衣服/鞋/箱包/普通化妝品等20%、高檔化妝品/香水/菸酒/珠寶/電池等50%。"},
    {"@type": "HowToStep", "name": "輸入申報貨值", "text": "輸入包裹申報價值（人民幣）。個人寄自台灣的包裹單票限值800元人民幣。"},
    {"@type": "HowToStep", "name": "判斷是否超過限值", "text": "貨值≤800元且自用合理可放行；超過800元需退運或改按貨物報關（單件不可分割除外）。"},
    {"@type": "HowToStep", "name": "計算應徵稅額", "text": "應徵稅額 = 完稅價格 × 稅率。系統用「貨值 × 稅率」作參考估算。"},
    {"@type": "HowToStep", "name": "判斷是否免徵", "text": "應徵稅額在人民幣50元（含）以下免徵；超過50元才需繳稅。"},
    {"@type": "HowToStep", "name": "加 LINE 確認", "text": "速豹敏感貨專線包稅雙清，關稅由速豹處理，實際以海關審定完稅價格為準。"}
  ],
  "totalTime": "PT5M"
}'''
html = html.replace(blocks[1].strip(), howto, 1)
print('  ✅ HowTo schema')

# 2c. BreadcrumbList
bc = '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"首頁","item":{"@id":"https://subao.tw/","name":"首頁"}},{"@type":"ListItem","position":2,"name":"關稅試算","item":{"@id":"https://subao.tw/taiwan-to-china-duty-tax","name":"關稅試算"}}]}'
html = html.replace(blocks[2].strip(), bc, 1)
print('  ✅ BreadcrumbList schema')

# 2d. FAQPage
faq = '''{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"台灣寄大陸關稅多少？","acceptedAnswer":{"@type":"Answer","text":"個人行郵稅分三檔：13%（食品/保健品/奶粉/書刊/家具）、20%（衣服/鞋/箱包/普通化妝品/小家電）、50%（高檔化妝品/香水/菸酒/珠寶/高檔手錶/電池）。應徵稅額在50元以下免徵。"}},
{"@type":"Question","name":"台灣寄大陸免稅額度是多少？","acceptedAnswer":{"@type":"Answer","text":"個人寄自台灣的包裹單票限值800元人民幣（海關總署2010年第43號公告）。貨值在800元以內且自用合理即可放行；超過800元需退運或改按貨物報關。"}},
{"@type":"Question","name":"台灣寄大陸要繳關稅嗎？","acceptedAnswer":{"@type":"Answer","text":"不一定。若貨值≤800元且應徵稅額≤50元則免徵；只有超過800元限值或應徵稅額>50元才需要繳稅。用上方試算器可快速判斷。"}},
{"@type":"Question","name":"台灣寄大陸關稅怎麼算？","acceptedAnswer":{"@type":"Answer","text":"應徵稅額 = 完稅價格 × 稅率。完稅價格以海關審定為準；實際購買價是完稅價格表2倍以上或1/2以下時，海關可依發票重新核定。"}},
{"@type":"Question","name":"速豹包稅雙清是什麼意思？","acceptedAnswer":{"@type":"Answer","text":"包稅雙清指關稅與進出口清關手續都由速豹處理，你只需付運費，不用自己面對海關補稅或退運風險。速豹敏感貨專線NT$290/kg起，食品/保健品/茶葉/3C含電池全收。"}}
]}'''
html = html.replace(blocks[3].strip(), faq, 1)
print('  ✅ FAQPage schema')

# ============ 3. main 内容（page-hero + calculator-section） ============
s = html.find('<section class="page-hero">')
e = html.find('<div style="background:linear-gradient(135deg,#E3F2FD,#BBDEFB)')
assert s != -1 and e != -1, 'main 定位失败'
main_new = '''<section class="page-hero">    <div class="container">      <h1>台灣寄大陸關稅計算與免稅額度</h1>      <p>2026最新規則一次講清：個人包裹單票限值 800 元、應徵稅額 50 元以下免徵、行郵稅率 13%/20%/50%</p>    </div>  </section>  <section class="calculator-section">    <div class="container">      <div class="calc-card">        <div class="calc-title">🧮 關稅試算器</div>        <div class="calc-subtitle">輸入商品申報貨值（人民幣）與商品類別，立即估算是否要繳關稅、要繳多少</div>        <div class="calc-grid">          <div class="calc-group">            <label>商品類別</label>            <select id="dutyCategory">              <option value="0.13">🍜 食品/零食/茶葉/保健品/奶粉（13%）</option>              <option value="0.20">👕 衣服/鞋/箱包/普通化妝品/小家電（20%）</option>              <option value="0.50">💎 高檔化妝品/香水/菸酒/珠寶/高檔手錶/電池（50%）</option>            </select>          </div>          <div class="calc-group">            <label>申報貨值（人民幣 ¥）</label>            <input type="number" id="dutyValue" placeholder="例如：300" min="1" max="100000" step="1">            <span class="hint">個人寄自台灣包裹單票限值 800 元</span>          </div>        </div>        <div id="resultPanel" class="result-panel">          <div class="result-label">關稅試算結果（參考）</div>          <div class="result-price" id="resultPrice">—</div>          <div class="result-delivery" id="resultDelivery"></div>          <div class="result-note">※ 以上為個人行郵渠道參考估算，實際以海關審定完稅價格為準。<a href="https://line.me/R/ti/p/@734dooky" target="_blank" style="color:#008A00;font-weight:700;text-decoration:underline" onclick="gtag('event','line_click',{event_category:'conversion',event_label:'duty_note'});gtag('event','generate_lead',{event_category:'lead',event_label:'duty_note'})">加 LINE 讓速豹幫你包稅雙清，不用自己面對關稅</a></div>        </div>        <div class="info-box">          <h3>📌 2026 台灣寄大陸關稅核心規則</h3>          <p>① <strong>限值 800 元</strong>：個人寄自台灣的包裹單票限值 800 元人民幣（海關總署 2010 年第 43 號公告），超限需退運或改按貨物報關，單件不可分割除外。② <strong>50 元免徵</strong>：應徵稅額在人民幣 50 元（含）以下免徵。③ <strong>三檔稅率</strong>：行郵稅 13%／20%／50%（2019 年第 63 號《進境物品完稅價格表》）。完整清關流程請看 <a href="/customs-guide" style="color:#0066CC;font-weight:700">大陸海關清關攻略</a>，寄送費用看 <a href="/pricing" style="color:#0066CC;font-weight:700">運費價格表</a>。</p>        </div>        <div class="cta-box">          <h3>不想自己算關稅？</h3>          <p>速豹敏感貨專線「包稅雙清」，關稅與清關手續都由我們處理，你只需付運費，食品/保健品/茶葉/3C含電池全收</p>          <a href="https://line.me/R/ti/p/@734dooky" class="btn" target="_blank" onclick="gtag('event','line_click',{event_category:'conversion',event_label:'line_consult',value:1});gtag('event','generate_lead',{event_category:'lead',event_label:'line'})"><svg class="icon" aria-hidden="true" ><use href="#line"/></svg> 立即LINE咨詢</a>        </div>        <table class="pricing-table">          <thead>            <tr>              <th>稅率檔</th>              <th>適用商品</th>              <th>常見例子</th>            </tr>          </thead>          <tbody>            <tr class="recommended">              <td><span class="badge">13%</span></td>              <td>食品、飲料（不含酒精）、書刊、家具、玩具、金銀、藥品、計算機等資訊產品</td>              <td>零食/泡麵/茶葉/奶粉/保健品</td>            </tr>            <tr>              <td><span class="badge">20%</span></td>              <td>運動用品、紡織品、服裝、箱包、鞋、手錶(1萬以下)、普通化妝品、小家電</td>              <td>衣服/球鞋/包包/洗面乳</td>            </tr>            <tr>              <td><span class="badge">50%</span></td>              <td>菸、酒、高檔手錶(≥1萬)、高檔化妝品、香水、珠寶、高爾夫球具、電池</td>              <td>香水/名錶/菸酒</td>            </tr>          </tbody>        </table>        <p style="font-size:13px;color:#888;text-align:center;margin-top:12px;">          ※ 個人行郵渠道限值 800 元人民幣｜應徵稅額 ≤50 元免徵｜速豹專線為包稅雙清，實際以海關審定為準        </p>      </div>    </div>  </section>  '''
html = html[:s] + main_new + html[e:]
print('  ✅ main 内容')

# ============ 4. 计算器 JS ============
js_old_start = html.find('const pricingData')
js_old_end = html.find("['productType', 'weight', 'region', 'serviceType'].forEach", js_old_start)
assert js_old_start != -1 and js_old_end != -1, 'JS 定位失败'
# 找到该 forEach 语句结束（含括号）
js_old_end = html.find('});', js_old_end) + 3
js_new = '''const LIMIT = 800;    const EXEMPT = 50;    function calculateDuty() {      const rate = parseFloat(document.getElementById('dutyCategory').value);      const value = parseFloat(document.getElementById('dutyValue').value);      if (!value || value <= 0) {        document.getElementById('resultPanel').classList.remove('show');        return;      }      const overLimit = value > LIMIT;      const tax = Math.round(value * rate * 100) / 100;      const exempt = tax <= EXEMPT;      const payable = exempt ? 0 : tax;      document.getElementById('resultPrice').textContent = exempt ? '✅ 免徵關稅' : ('應繳關稅 ≈ ¥' + Math.round(payable));      let detail = '貨值 ¥' + value.toLocaleString() + ' × 稅率 ' + (rate * 100) + '% = 應徵稅額 ¥' + tax.toFixed(2);      detail += overLimit ? '｜⚠️ 貨值超 800 元限值，需退運或改按貨物報關（單件不可分割除外）' : '｜✅ 貨值在 800 元限值內';      detail += exempt ? '｜✅ 應徵稅額 ≤50 元，免徵' : ('｜實繳 ¥' + Math.round(payable));      document.getElementById('resultDelivery').textContent = detail;      document.getElementById('resultPanel').classList.add('show');      if (typeof gtag === 'function') {        gtag('event', 'duty_calc_result', { event_category: 'engagement', event_label: (rate * 100) + '%', value: Math.round(payable) });      }    }    ['dutyCategory', 'dutyValue'].forEach(function(id) {      document.getElementById(id).addEventListener('change', calculateDuty);      document.getElementById(id).addEventListener('input', calculateDuty);    });'''
html = html[:js_old_start] + js_new + html[js_old_end:]
print('  ✅ 计算器 JS')

# ============ 5. 工具矩阵内链：加「關稅速查」链接到 customs-guide ============
tm_old = '<a href="/volume-calculator" style="display:inline-block;background:#fff;color:#1565C0;padding:10px 20px;border-radius:8px;font-weight:700;font-size:14px;box-shadow:0 2px 8px rgba(0,0,0,0.08);text-decoration:none">📐 材積計算機</a>'
tm_new = tm_old + '        <a href="/customs-guide" style="display:inline-block;background:#fff;color:#1565C0;padding:10px 20px;border-radius:8px;font-weight:700;font-size:14px;box-shadow:0 2px 8px rgba(0,0,0,0.08);text-decoration:none">📋 關稅速查</a>'
rep(tm_old, tm_new, '工具矩阵加關稅速查链接')

open(DST, 'w', encoding='utf-8').write(html)
print(f'\n🎉 生成完成: {DST}（{len(html)} 字符）')
