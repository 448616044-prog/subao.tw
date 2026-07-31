#!/usr/bin/env python3
"""Batch create 10 snack brand pages + 2 mooncake pages"""
import os, re

BASE = '/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn/blog'
TODAY = '2026-08-01'

with open(os.path.join(BASE, 'guai-guai-shipping.html'), 'r') as f:
    template = f.read()

def create_page(slug, title, desc, h1, meta_kw, content_html, faqs):
    page = template
    page = re.sub(r'<title>[^<]*</title>', f'<title>{title}</title>', page)
    page = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{desc}"', page)
    page = re.sub(r'<meta name="keywords" content="[^"]*"', f'<meta name="keywords" content="{meta_kw}"', page)
    page = re.sub(r'<link rel="canonical" href="[^"]*"', f'<link rel="canonical" href="https://subao.tw/blog/{slug}"', page)
    page = re.sub(r'<meta name="lastmod" content="[^"]*"', f'<meta name="lastmod" content="{TODAY}"', page)
    page = re.sub(r'<meta property="og:title" content="[^"]*"', f'<meta property="og:title" content="{title}"', page)
    page = re.sub(r'<meta property="og:description" content="[^"]*"', f'<meta property="og:description" content="{desc[:200]}"', page)
    page = re.sub(r'"datePublished":\s*"[^"]*"', f'"datePublished": "{TODAY}"', page)
    page = re.sub(r'"dateModified":\s*"[^"]*"', f'"dateModified": "{TODAY}"', page)
    page = re.sub(r'<h1[^>]*>.*?</h1>', f'<h1>{h1}</h1>', page, count=1)
    
    art_match = re.search(r'(<article[^>]*>.*?</h1>).*?(<section class="section cta")', page, re.DOTALL)
    if art_match:
        prefix, suffix = art_match.group(1), art_match.group(2)
        before, after = page[:art_match.start()], page[art_match.end():]
        page = before + prefix + content_html + suffix + after
    
    faq_json = ','.join([f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a[:300]}"}}}}' for q,a in faqs[:8]])
    old_faq = re.search(r'"@type":"FAQPage","mainEntity":\[.*?\]', page, re.DOTALL)
    if old_faq:
        page = page.replace(old_faq.group(0), f'"@type":"FAQPage","mainEntity":[{faq_json}]')
    
    path = os.path.join(BASE, f'{slug}.html')
    with open(path, 'w') as f:
        f.write(page)
    return path

# ═══ 快捷模板 ═══
def snack_template(brand_cn, brand_file, note=''):
    return create_page(
        f'{brand_file}-shipping',
        f'{brand_cn}可以寄大陸嗎？2026寄送攻略 NT$290/kg起 | 速豹集運',
        f'{brand_cn}可以寄大陸嗎？走敏感貨專線即可寄送，NT$290/kg起包稅雙清。{note}包裝建議、海關注意事項、運費試算一次搞定。',
        f'{brand_cn}可以寄大陸嗎？2026完整攻略',
        f'{brand_cn}寄大陸,{brand_cn}可以寄嗎,台灣零食寄大陸,{brand_cn}快遞大陸',
        f'''
    <p>{brand_cn}是台灣人從小吃到大的經典零食。<strong>想寄{brand_cn}到大陸給親友？答案是：可以！</strong></p>
    
    <h2>{brand_cn}可以寄大陸嗎？</h2>
    <p><strong>✅ 可以寄。</strong>{brand_cn}屬於一般零食（非肉製品），走敏感貨專線完全沒問題。NT$290/kg起包稅雙清，5-7天到大陸。</p>
    
    <h2>{brand_cn}寄大陸費用</h2>
    <p>以5包{brand_cn}為例（約0.5-1kg）：NT$290-390（含NT$100派送費）。滿10kg免派送費，建議和其他零食一起寄更划算。</p>
    
    <h2>台灣經典零食寄大陸對比</h2>
    <table>
      <tr><th>零食</th><th>品牌</th><th>可否寄</th><th>運費/kg</th></tr>
      <tr><td>乖乖</td><td>乖乖公司</td><td>✅</td><td>NT$290起</td></tr>
      <tr><td>可樂果</td><td>聯華食品</td><td>✅</td><td>NT$290起</td></tr>
      <tr><td>科學麵</td><td>統一企業</td><td>✅</td><td>NT$290起</td></tr>
      <tr><td>義美小泡芙</td><td>義美食品</td><td>✅</td><td>NT$290起</td></tr>
      <tr><td>蝦味先</td><td>裕榮食品</td><td>✅</td><td>NT$290起</td></tr>
      <tr><td><strong>{brand_cn}</strong></td><td>—</td><td><strong>✅</strong></td><td><strong>NT$290起</strong></td></tr>
    </table>
    
    <p>相關：<a href="/blog/taiwan-snack-recommend">台灣零食寄大陸推薦清單</a> | <a href="/blog/guai-guai-shipping">乖乖寄大陸</a> | <a href="/blog/cola-guo-shipping">可樂果寄大陸</a></p>
    ''',
        [
            (f'{brand_cn}可以寄大陸嗎？', f'✅ 可以。{brand_cn}屬於一般零食，走敏感貨專線即可寄送。NT$290/kg起包稅雙清，5-7天到大陸主要城市。'),
            (f'{brand_cn}寄大陸運費多少？', f'5包{brand_cn}（約0.5-1kg）運費約NT$290-390。滿10kg免派送費，建議湊重量和其他零食一起寄。'),
            ('台灣零食寄大陸會被海關扣嗎？', '一般零食（餅乾、糖果、泡麵等）只要不含肉類和蛋黃，走專線通關很順利。肉乾、肉鬆、蛋黃酥等含動物成分的不能寄。'),
        ])

# ═══ 10 Brand Pages ═══
brands = [
    ('真魷味', 'zhenyouwei', '華元食品經典零食，醬香味酥脆口感。'),
    ('蚵仔煎洋芋片', 'oyster-omelet-chips', '華元食品出品，台灣味洋芋片經典。'),
    ('孔雀餅乾', 'queque-crackers', '乖乖公司出品，蛋黃甜香酥鬆可口。'),
    ('滿漢大餐', 'manhan-dinner', '統一企業頂級泡麵，含真實肉塊調理包。走敏感貨專線可寄。'),
    ('維力炸醬麵', 'weilih-zhajiang', '台灣經典乾拌泡麵，附炸醬包，走敏感貨專線可寄。'),
    ('花雕雞麵', 'huadiao-chicken-noodles', '台酒出品，含花雕酒調理包。酒精成分需注意，走專線可寄。'),
    ('張君雅小妹妹', 'zhang-junya-snacks', '台灣超人氣點心麵品牌，捏碎吃法風靡全台。'),
    ('新貴派', 'xinguipai', '宏亞食品經典巧克力威化餅，多層次口感。'),
    ('北海鱈魚香絲', 'beihai-xueyu', '台灣最長壽的魚漿零食，一絲一絲超唰嘴。'),
    ('卡哩卡哩', 'kalikali', '台灣古早味螺旋零食，酥脆口感搭配梅粉或糖粉。'),
]

results = []
for brand_cn, brand_file, note in brands:
    path = snack_template(brand_cn, brand_file, note)
    results.append(os.path.basename(path))
    print(f'✅ {path}')

# ═══ 2 Mooncake Pages ═══
create_page(
    'mooncake-vs-pineapple-cake-2026',
    '中秋送禮月餅還是鳳梨酥？2026寄大陸對比攻略 | 速豹集運',
    '2026中秋送禮怎麼選？月餅vs鳳梨酥寄大陸對比：可寄性、費用、受歡迎程度完整PK。鳳梨酥100%可寄，月餅要看餡料。中秋送禮替代方案推薦。',
    '中秋送禮：月餅vs鳳梨酥寄大陸完整對比',
    '中秋送禮,月餅寄大陸,鳳梨酥寄大陸,中秋禮盒寄大陸,月餅鳳梨酥對比',
    '''
    <p>每年中秋節前夕，最多人問的問題就是：「月餅和鳳梨酥，哪個寄大陸比較好？」<strong>答案很明確：鳳梨酥100%可寄，月餅要看餡料。</strong>這篇從三個維度做完整對比。</p>
    
    <h2>月餅 vs 鳳梨酥寄大陸對比表</h2>
    <table>
      <tr><th>比較維度</th><th>月餅</th><th>鳳梨酥</th></tr>
      <tr><td>可寄性</td><td>⚠️ 看餡料（無肉無蛋黃才可）</td><td>✅ 100%可寄</td></tr>
      <tr><td>通關難度</td><td>⭐⭐⭐ 需確認成分</td><td>⭐ 幾乎零問題</td></tr>
      <tr><td>重量/體積</td><td>較重，單顆100-200g</td><td>較輕，單顆約50g</td></tr>
      <tr><td>運費(5盒)</td><td>約NT$1,500-2,500</td><td>約NT$870-1,200</td></tr>
      <tr><td>受歡迎度</td><td>⭐⭐⭐⭐ 季節限定</td><td>⭐⭐⭐⭐⭐ 全年送禮</td></tr>
      <tr><td>保存期限</td><td>較短（1-4週）</td><td>較長（1-3個月）</td></tr>
    </table>
    
    <h2>推薦中秋送禮方案</h2>
    <ol>
      <li><strong>純鳳梨酥禮盒</strong>：100%可寄，無任何通關風險 → 推薦微熱山丘/佳德</li>
      <li><strong>綜合禮盒</strong>：鳳梨酥+太陽餅+綠豆椪 → 多樣化有面子</li>
      <li><strong>月餅（安全款）</strong>：純蓮蓉/純豆沙/綠豆椪（無蛋黃）→ 傳統但不踩雷</li>
    </ol>
    
    <p>相關：<a href="/blog/mid-autumn-mooncake-hub-2026">中秋月餅寄大陸完全攻略</a> | <a href="/blog/mooncake-brands-shipping">月餅品牌對照表</a> | <a href="/blog/mid-autumn-gift-shipping">中秋禮盒組合方案</a></p>
    ''',
    [
        ('中秋送月餅還是鳳梨酥好？', '鳳梨酥更好寄！鳳梨酥100%可寄大陸，不含肉蛋，通關零問題。月餅只有無肉無蛋黃的款式才能寄。送禮安全度：鳳梨酥 > 綠豆椪 > 純蓮蓉月餅 > 含蛋黃月餅。'),
        ('鳳梨酥寄大陸運費多少？', '5盒鳳梨酥（約2-3kg）走專線約NT$580-870。比月餅輕，同樣數量運費便宜30-50%。'),
    ])

create_page(
    'mooncake-gift-packaging-guide',
    '中秋月餅寄大陸包裝攻略2026：怎麼包才不碎？ | 速豹集運',
    '2026中秋月餅寄大陸包裝完整攻略：月餅/鳳梨酥/蛋黃酥包裝材料推薦、防碎技巧、真空包裝vs氣泡袋對比。確保月餅完好送達大陸親友手中。',
    '中秋月餅寄大陸包裝攻略：防碎防壓完整教學',
    '月餅包裝寄大陸,月餅怎麼包裝,中秋送禮包裝,防碎包裝,月餅寄大陸防壓',
    '''
    <p>月餅寄大陸最怕的就是——收到時碎成渣。<strong>包裝決定了月餅的命運。</strong>這篇從材料選擇到具體步驟，教你月餅怎麼包才能完好送達。</p>
    
    <h2>月餅寄大陸包裝材料清單</h2>
    <table>
      <tr><th>材料</th><th>用途</th><th>建議</th></tr>
      <tr><td>氣泡膜</td><td>第一層防震</td><td>每顆月餅單獨包</td></tr>
      <tr><td>硬質紙箱</td><td>外層保護</td><td>雙層瓦楞紙箱</td></tr>
      <tr><td>填充物（報紙/泡棉）</td><td>填滿空隙</td><td>不要留晃動空間</td></tr>
      <tr><td>真空袋（可選）</td><td>防潮保鮮</td><td>適合長途運輸</td></tr>
      <tr><td>膠帶</td><td>封箱</td><td>十字+工字封法</td></tr>
    </table>
    
    <h2>月餅包裝步驟</h2>
    <ol>
      <li>每顆月餅用氣泡膜單獨包裹（2-3層）</li>
      <li>放入原廠禮盒（如有）</li>
      <li>禮盒外再包一層氣泡膜</li>
      <li>放入紙箱，空隙塞滿填充物</li>
      <li>搖一搖確認沒有晃動聲</li>
      <li>十字+工字膠帶封箱</li>
      <li>標註「易碎品」和「向上」</li>
    </ol>
    
    <h2>月餅 vs 鳳梨酥包裝難度對比</h2>
    <table>
      <tr><th>類型</th><th>易碎度</th><th>包裝建議</th></tr>
      <tr><td>廣式月餅</td><td>⭐⭐</td><td>較硬實，氣泡膜+紙箱即可</td></tr>
      <tr><td>蘇式月餅</td><td>⭐⭐⭐</td><td>酥皮易碎，需多層氣泡膜</td></tr>
      <tr><td>冰皮月餅</td><td>⭐</td><td>軟Q不易碎但需低溫</td></tr>
      <tr><td>鳳梨酥</td><td>⭐</td><td>硬實好包，最容易寄送</td></tr>
    </table>
    
    <p>相關：<a href="/blog/mid-autumn-mooncake-hub-2026">中秋月餅寄大陸完全攻略</a> | <a href="/blog/mooncake-shipping-cost">月餅寄大陸費用試算</a></p>
    ''',
    [
        ('月餅寄大陸怎麼包才不會碎？', '關鍵三步：1)每顆月餅用2-3層氣泡膜單獨包裹 2)放入硬質紙箱，空隙全部塞滿填充物 3)搖晃測試無聲音再封箱。標註「易碎」和「向上」標籤。'),
        ('中秋月餅寄大陸包裝需要什麼材料？', '基本材料：氣泡膜、雙層瓦楞紙箱、報紙/泡棉填充物、膠帶。推薦加購：真空袋（防潮）、易碎貼紙。我們提供專業包裝服務，也可自行包裝。'),
    ])

print(f'\n📊 Done: 10品牌 + 2月餅 = 12 new pages')
