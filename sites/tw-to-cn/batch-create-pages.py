#!/usr/bin/env python3
"""Batch create snack pages + mooncake pages + deploy"""
import os, re

BASE = '/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn/blog'
os.chdir(BASE)
TODAY = '2026-07-31'

# Read a base template
with open('guai-guai-shipping.html', 'r') as f:
    template = f.read()

def create_page(slug, title, desc, h1, meta_kw, content_html, faqs):
    """Create a new page from template"""
    page = template
    
    # Replace title
    page = re.sub(r'<title>[^<]*</title>', f'<title>{title}</title>', page)
    # Replace meta description
    page = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{desc}"', page)
    # Replace keywords
    page = re.sub(r'<meta name="keywords" content="[^"]*"', f'<meta name="keywords" content="{meta_kw}"', page)
    # Replace canonical
    page = re.sub(r'<link rel="canonical" href="[^"]*"', f'<link rel="canonical" href="https://subao.tw/blog/{slug}"', page)
    # Replace lastmod
    page = re.sub(r'<meta name="lastmod" content="[^"]*"', f'<meta name="lastmod" content="{TODAY}"', page)
    # Replace OG title
    page = re.sub(r'<meta property="og:title" content="[^"]*"', f'<meta property="og:title" content="{title}"', page)
    # Replace OG description
    page = re.sub(r'<meta property="og:description" content="[^"]*"', f'<meta property="og:description" content="{desc[:200]}"', page)
    # Replace OG URL
    page = re.sub(r'<meta property="og:url" content="[^"]*"', f'<meta property="og:url" content="https://subao.tw/blog/{slug}"', page)
    # Replace dates in JSON-LD
    page = re.sub(r'"datePublished":\s*"[^"]*"', f'"datePublished": "{TODAY}"', page)
    page = re.sub(r'"dateModified":\s*"[^"]*"', f'"dateModified": "{TODAY}"', page)
    # Replace H1
    page = re.sub(r'<h1[^>]*>.*?</h1>', f'<h1>{h1}</h1>', page, count=1)
    
    # Replace body content (between first <article...> and first <section class="section cta"...)
    art_match = re.search(r'(<article[^>]*>.*?</h1>).*?(<section class="section cta")', page, re.DOTALL)
    if art_match:
        prefix = art_match.group(1)
        suffix = art_match.group(2)
        before = page[:art_match.start()]
        after = page[art_match.end():]
        page = before + prefix + content_html + suffix + after
    
    # Replace FAQ Schema
    faq_json = ','.join([f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a[:300]}"}}}}' for q,a in faqs[:8]])
    old_faq = re.search(r'"@type":"FAQPage","mainEntity":\[.*?\]', page, re.DOTALL)
    if old_faq:
        page = page.replace(old_faq.group(0), f'"@type":"FAQPage","mainEntity":[{faq_json}]')
    
    # Write file
    filepath = os.path.join(BASE, f'{slug}.html')
    with open(filepath, 'w') as f:
        f.write(page)
    return filepath

# ═══════════════ 新建页面 ═══════════════

pages_created = []

# 1. 味味A排骨雞麵
pages_created.append(create_page(
    'weiwie-a-pork-rib-noodles-shipping',
    '味味A排骨雞麵可以寄大陸嗎？2026寄送攻略 NT$290/kg起 | 速豹集運',
    '味味A排骨雞麵可以寄大陸嗎？泡麵類敏感貨專線可寄，NT$290/kg起包稅雙清。含醬料包注意事項、寄送包裝建議、海關通關流程完整教學。',
    '味味A排骨雞麵可以寄大陸嗎？2026完整攻略',
    '味味A排骨雞麵寄大陸,味味A泡麵寄大陸,台灣泡麵寄大陸,排骨雞麵可以寄嗎,味味A寄大陸攻略',
    '''
    <p>味味A排骨雞麵是台灣泡麵界的長青樹，濃郁的排骨雞醬包加上Q彈的麵條，是許多台灣人的心頭好。<strong>想寄味味A排骨雞麵到大陸給親友？答案是可以的！</strong> 但方式和注意事項要搞對。</p>
    
    <h2>味味A排骨雞麵可以寄大陸嗎？</h2>
    <p><strong>✅ 可以寄。</strong>味味A排骨雞麵屬於泡麵類，走敏感貨專線即可寄送。NT$290/kg起，包稅雙清，5-7天到大陸主要城市。</p>
    <p>⚠️ 注意：由於醬包含豬油成分（排骨風味來源），建議走海運或專線空運（非一般航空快遞），避免航空安全管制問題。</p>
    
    <h2>味味A排骨雞麵寄大陸包裝建議</h2>
    <ul>
      <li><strong>保留原包裝</strong>：碗裝或袋裝都行，建議不要拆開</li>
      <li><strong>防壓包裝</strong>：泡麵易碎，建議用氣泡袋包裹再加紙箱</li>
      <li><strong>醬包防漏</strong>：如果擔心醬包破裂，可用夾鏈袋另外包一層</li>
      <li><strong>控制數量</strong>：個人自用建議一次10-20包以內，避免被懷疑商業進口</li>
    </ul>
    
    <h2>味味A全系列寄送對照表</h2>
    <table>
      <tr><th>品項</th><th>可否寄</th><th>注意事項</th></tr>
      <tr><td>排骨雞麵（袋裝）</td><td>✅ 可寄</td><td>醬包含豬油，走專線</td></tr>
      <tr><td>排骨雞麵（碗裝）</td><td>✅ 可寄</td><td>碗裝體積大，建議袋裝省運費</td></tr>
      <tr><td>味味一品牛肉麵</td><td>✅ 可寄</td><td>含牛肉調理包可寄，注意包裝完整</td></tr>
      <tr><td>味味一品原汁珍味牛肉麵</td><td>✅ 可寄</td><td>同上</td></tr>
    </table>
    
    <h2>寄味味A到大陸運費多少？</h2>
    <p>以5包袋裝味味A為例（約0.8kg）：NT$290 × 1kg = NT$290 + NT$100派送費 = <strong>NT$390</strong>（未滿10kg有派送費）。</p>
    <p>以20包為例（約3.2kg）：NT$290 × 4kg = NT$1,160 + NT$100 = <strong>NT$1,260</strong>。</p>
    <p>省錢技巧：湊滿10kg免派送費，或同時寄其他零食一起湊重量。</p>
    
    <h2>味味A vs 其他泡麵品牌寄大陸對比</h2>
    <table>
      <tr><th>品牌</th><th>可否寄</th><th>難度</th></tr>
      <tr><td>味味A排骨雞麵</td><td>✅</td><td>⭐ 簡單（醬包注意）</td></tr>
      <tr><td>統一肉燥麵</td><td>✅</td><td>⭐ 簡單</td></tr>
      <tr><td>維力炸醬麵</td><td>✅</td><td>⭐ 簡單</td></tr>
      <tr><td>滿漢大餐（含肉塊）</td><td>✅</td><td>⭐⭐ 需專線</td></tr>
      <tr><td>花雕雞麵（含料理酒）</td><td>⚠️</td><td>⭐⭐⭐ 酒類注意</td></tr>
    </table>
    
    <p>相關文章：<a href="/blog/noodles-ramen-shipping">台灣泡麵寄大陸品牌對照表</a> | <a href="/blog/tongyi-noodles-shipping">統一麵寄大陸攻略</a> | <a href="/blog/science-noodles-shipping">科學麵寄大陸攻略</a></p>
    ''',
    [
        ('味味A排骨雞麵可以寄大陸嗎？', '✅ 可以。走敏感貨專線，NT$290/kg起包稅雙清，5-7天到大陸。醬包含豬油成分，建議走專線海運或空運（非一般航空快遞），避免安全管制。'),
        ('味味A寄大陸運費多少？', '以5包袋裝為例（約0.8kg），運費約NT$390（NT$290+NT$100派送費）。20包（約3.2kg）約NT$1,260。滿10kg免派送費。'),
        ('味味A碗裝可以寄嗎？', '✅ 可以。碗裝和袋裝都可以寄。碗裝體積較大，建議袋裝更省運費。'),
        ('味味A醬包含豬油會影響寄送嗎？', '會影響選擇運輸渠道。含豬油的泡麵不能走一般航空快遞，需走敏感貨專線的空運或海運。我們有專門的泡麵運輸方案。'),
    ]
))

# 2. 來一客
pages_created.append(create_page(
    'laiyike-cup-noodles-shipping',
    '來一客可以寄大陸嗎？2026杯麵寄送攻略 NT$290/kg起 | 速豹集運',
    '來一客杯麵可以寄大陸嗎？鮮蝦魚板/牛肉蔬菜/京燉肉骨全系列可寄。NT$290/kg起包稅雙清，杯麵寄送包裝技巧與注意事項。',
    '來一客杯麵可以寄大陸嗎？2026完整攻略',
    '來一客寄大陸,來一客杯麵寄大陸,統一來一客可以寄嗎,杯麵寄大陸,台灣泡麵寄大陸',
    '''
    <p>來一客是統一企業旗下的經典杯麵品牌，鮮蝦魚板口味更是許多人從小吃到大的回憶。<strong>想寄來一客到大陸？完全沒問題！</strong></p>
    
    <h2>來一客杯麵可以寄大陸嗎？</h2>
    <p><strong>✅ 可以寄。</strong>來一客杯麵走敏感貨專線即可寄送。NT$290/kg起，包稅雙清，5-7天送到大陸。</p>
    
    <h2>來一客全系列寄送對照表</h2>
    <table>
      <tr><th>口味</th><th>可否寄</th><th>注意事項</th></tr>
      <tr><td>鮮蝦魚板</td><td>✅ 可寄</td><td>最熱門口味，通關順利</td></tr>
      <tr><td>牛肉蔬菜</td><td>✅ 可寄</td><td>含牛肉調味粉，非真實肉塊，可寄</td></tr>
      <tr><td>京燉肉骨</td><td>✅ 可寄</td><td>含調味粉包，可寄</td></tr>
      <tr><td>韓式泡菜</td><td>✅ 可寄</td><td>調味粉包，無真實泡菜塊</td></tr>
    </table>
    
    <h2>杯麵寄大陸包裝建議</h2>
    <ul>
      <li><strong>杯體保護</strong>：來一客杯身較軟，建議每個杯子用氣泡袋單獨包裹</li>
      <li><strong>集中裝箱</strong>：多個杯麵集中放在硬質紙箱，空隙塞滿填充物</li>
      <li><strong>避免擠壓</strong>：杯麵易碎，箱內不要放太重的東西</li>
      <li><strong>乾燥保存</strong>：確認杯麵在乾燥環境包裝，避免受潮</li>
    </ul>
    
    <h2>不同品牌杯麵寄大陸費用參考</h2>
    <table>
      <tr><th>品牌</th><th>單杯重量</th><th>10杯運費</th></tr>
      <tr><td>來一客</td><td>約65g</td><td>約NT$650</td></tr>
      <tr><td>統一肉燥麵（碗裝）</td><td>約90g</td><td>約NT$750</td></tr>
      <tr><td>滿漢大餐（碗裝）</td><td>約200g</td><td>約NT$1,250</td></tr>
    </table>
    
    <p>相關：<a href="/blog/noodles-ramen-shipping">台灣泡麵寄大陸全品牌對照表</a> | <a href="/blog/tongyi-noodles-shipping">統一麵系列攻略</a></p>
    ''',
    [
        ('來一客可以寄大陸嗎？', '✅ 可以。來一客杯麵走敏感貨專線可寄，NT$290/kg起。鮮蝦魚板、牛肉蔬菜、京燉肉骨、韓式泡菜全系列均可。杯體需氣泡袋保護防碎。'),
        ('來一客寄大陸運費多少？', '10杯來一客（約0.65kg）運費約NT$390。30杯（約1.95kg）約NT$680。湊滿10kg以上免NT$100派送費。'),
        ('來一客海鮮口味可以寄嗎？', '✅ 可以。鮮蝦魚板口味不含真實海鮮塊，僅調味粉，通關無問題。'),
    ]
))

# 3. 蝦味先
pages_created.append(create_page(
    'xiaweixian-shipping',
    '蝦味先可以寄大陸嗎？2026寄送攻略 NT$290/kg起 | 速豹集運',
    '蝦味先可以寄大陸嗎？原味/辣味/泡菜口味全系列可寄。NT$290/kg起包稅雙清，台灣經典零食寄大陸包裝建議與海關注意事項。',
    '蝦味先可以寄大陸嗎？2026完整攻略',
    '蝦味先寄大陸,蝦味先可以寄嗎,台灣零食寄大陸,蝦味先泡菜口味,裕榮食品寄大陸',
    '''
    <p>蝦味先是裕榮食品的招牌產品，酥脆的蝦味口感讓它成為台灣最長壽的零食之一。<strong>想寄蝦味先到大陸？答案是：可以！</strong></p>
    
    <h2>蝦味先可以寄大陸嗎？</h2>
    <p><strong>✅ 可以寄。</strong>蝦味先屬於一般零食（非肉製品），走敏感貨專線完全沒問題。NT$290/kg起包稅雙清，5-7天到大陸。</p>
    
    <h2>蝦味先全系列寄送對照</h2>
    <table>
      <tr><th>口味</th><th>可否寄</th><th>備註</th></tr>
      <tr><td>原味</td><td>✅ 可寄</td><td>最經典口味，通關零問題</td></tr>
      <tr><td>辣味</td><td>✅ 可寄</td><td>同上</td></tr>
      <tr><td>泡菜口味</td><td>✅ 可寄</td><td>調味粉包，非真實泡菜</td></tr>
      <tr><td>海苔口味</td><td>✅ 可寄</td><td>海苔調味，非真實海苔片</td></tr>
    </table>
    
    <h2>蝦味先 vs 其他台灣經典零食寄大陸</h2>
    <table>
      <tr><th>零食</th><th>品牌</th><th>可否寄</th><th>難度</th></tr>
      <tr><td>蝦味先</td><td>裕榮食品</td><td>✅</td><td>⭐ 簡單</td></tr>
      <tr><td>可樂果</td><td>聯華食品</td><td>✅</td><td>⭐ 簡單</td></tr>
      <tr><td>乖乖</td><td>乖乖公司</td><td>✅</td><td>⭐ 簡單</td></tr>
      <tr><td>科學麵</td><td>統一企業</td><td>✅</td><td>⭐ 簡單</td></tr>
      <tr><td>真魷味</td><td>華元食品</td><td>✅</td><td>⭐ 簡單</td></tr>
    </table>
    
    <p>相關：<a href="/blog/cola-guo-shipping">可樂果寄大陸攻略</a> | <a href="/blog/guai-guai-shipping">乖乖寄大陸攻略</a> | <a href="/blog/taiwan-snack-recommend">台灣零食寄大陸推薦清單</a></p>
    ''',
    [
        ('蝦味先可以寄大陸嗎？', '✅ 可以。蝦味先原味/辣味/泡菜口味全系列可寄，走敏感貨專線NT$290/kg起，5-7天到大陸。屬一般零食非肉製品，通關沒有問題。'),
        ('蝦味先寄大陸會被海關扣嗎？', '一般不會。蝦味先是調味零食（非真實蝦肉），不屬於海關管制的動物產品。只要數量合理（個人自用），通關順利。'),
    ]
))

# 4. 中秋月餅寄大陸匯總頁 (power page)
pages_created.append(create_page(
    'mid-autumn-mooncake-hub-2026',
    '中秋月餅寄大陸2026完全攻略｜品牌/費用/禁運品一次搞懂 | 速豹集運',
    '2026中秋月餅寄大陸完整攻略：美心/半島/舊振南/奇華等熱門品牌對照、運費試算、禁運品清單、包裝技巧。鳳梨酥/綠豆椪替代方案推薦。NT$290/kg起包稅雙清。',
    '2026中秋月餅寄大陸完全攻略：品牌對照/費用/禁運品一文搞懂',
    '中秋月餅寄大陸,月餅可以寄大陸嗎,台灣月餅寄大陸,中秋節月餅寄送,月餅寄大陸費用,月餅寄大陸品牌',
    '''
    <p>每年中秋節前（7月底-9月初），是台灣月餅寄大陸的高峰期。<strong>但不是所有月餅都能寄——關鍵在於餡料成分。</strong>這篇攻略把品牌對照、費用試算、禁運品和替代方案一次性說清楚。</p>
    
    <h2>月餅寄大陸：一句話結論</h2>
    <p><strong>不含肉類、不含整顆蛋黃的月餅 → ✅ 可寄。含肉餡或整顆蛋黃的傳統月餅 → ❌ 禁運。</strong></p>
    <p>走敏感貨專線，NT$290/kg起包稅雙清，5-7天到大陸主要城市。</p>
    
    <h2>熱門月餅品牌寄大陸對照表</h2>
    <table>
      <tr><th>品牌</th><th>代表產品</th><th>可否寄</th><th>原因</th></tr>
      <tr><td>美心</td><td>流心奶黃月餅</td><td>⚠️ 需確認</td><td>含蛋黃，部分款式不可寄</td></tr>
      <tr><td>半島酒店</td><td>奶黃月餅</td><td>⚠️ 需確認</td><td>同上，需確認成分</td></tr>
      <tr><td>舊振南</td><td>綠豆椪</td><td>✅ 可寄</td><td>純綠豆餡，無肉無蛋黃</td></tr>
      <tr><td>奇華</td><td>蓮蓉月餅</td><td>✅ 可寄</td><td>純蓮蓉餡（無蛋黃版本）</td></tr>
      <tr><td>郭元益</td><td>鳳梨酥/冰沙餡餅</td><td>✅ 可寄</td><td>無肉無蛋黃</td></tr>
      <tr><td>台北犁記</td><td>綠豆小月餅</td><td>✅ 可寄</td><td>純綠豆沙餡</td></tr>
    </table>
    
    <h2>月餅寄大陸費用試算</h2>
    <table>
      <tr><th>月餅數量</th><th>預估重量</th><th>專線運費</th><th>時效</th></tr>
      <tr><td>1-2盒</td><td>約2-3kg</td><td>NT$580-870</td><td>5-7天</td></tr>
      <tr><td>3-5盒</td><td>約4-6kg</td><td>NT$1,160-1,740</td><td>5-7天</td></tr>
      <tr><td>6-10盒</td><td>約7-10kg</td><td>NT$2,030-2,900</td><td>5-7天</td></tr>
    </table>
    <p>⚠️ 以上含稅含清關。10kg以下加收NT$100派送費，滿10kg免收。</p>
    
    <h2>2026中秋月餅寄大陸時間建議</h2>
    <ul>
      <li>🕐 <strong>最佳寄送時間</strong>：9月1日-9月15日（中秋前2-3週）</li>
      <li>🕐 <strong>最後寄送時間</strong>：9月20日前（確保中秋節前到）</li>
      <li>🕐 <strong>尖峰提前</strong>：9月是物流旺季，建議8月底開始準備</li>
    </ul>
    
    <h2>不確定月餅能不能寄？最佳替代方案</h2>
    <p>如果你的月餅含蛋黃或肉餡無法寄送，以下是<strong>100%能寄</strong>的台灣糕點替代方案：</p>
    <table>
      <tr><th>替代方案</th><th>可否寄</th><th>推薦品牌</th></tr>
      <tr><td>鳳梨酥</td><td>✅ 100%可寄</td><td>微熱山丘/佳德/舊振南</td></tr>
      <tr><td>太陽餅</td><td>✅ 100%可寄</td><td>太陽堂/一福堂/如邑堂</td></tr>
      <tr><td>綠豆椪（無蛋黃）</td><td>✅ 100%可寄</td><td>舊振南/台北犁記</td></tr>
      <tr><td>奶油酥餅</td><td>✅ 100%可寄</td><td>裕珍馨</td></tr>
    </table>
    
    <p>深入閱讀：<a href="/blog/mid-autumn-mooncake-shipping">中秋月餅品牌詳細對照</a> | <a href="/blog/mooncake-shipping-cost">月餅寄大陸費用一覽</a> | <a href="/blog/mid-autumn-gift-shipping">中秋禮盒組合方案</a> | <a href="/blog/taiwan-snack-recommend">台灣零食寄大陸推薦清單</a></p>
    ''',
    [
        ('月餅可以寄大陸嗎？', '取決於餡料：不含肉類和整顆蛋黃的月餅✅可寄（如綠豆椪、鳳梨酥）。含肉餡或整顆蛋黃的傳統月餅❌禁運。走敏感貨專線，NT$290/kg起，5-7天到大陸。'),
        ('中秋月餅寄大陸要多久？', '空運專線5-7天到大陸主要城市。建議9月1日-15日寄出，確保中秋節（9月底）前送到。'),
        ('美心月餅可以寄大陸嗎？', '⚠️需確認。美心流心奶黃月餅含蛋黃成分，部分款式不可寄。購買前請查看成分標示，不含肉類和整顆蛋黃的款式可寄。'),
        ('月餅寄大陸最便宜多少錢？', '1-2盒月餅（約2-3kg）走專線約NT$580-870，含稅含清關。如果中秋送禮量大（6盒以上），建議湊滿10kg免派送費。'),
        ('中秋節寄月餅來不及怎麼辦？', '建議用鳳梨酥或太陽餅替代。這兩種糕點不含肉蛋，100%可寄，同樣有台灣特色，是月餅的最佳替代方案。'),
    ]
))

print(f'✅ 已创建 {len(pages_created)} 个新页面:')
for p in pages_created:
    print(f'   {os.path.basename(p)}')
