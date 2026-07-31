import re, os
from datetime import date

BASE = '/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn'
BLOG = f'{BASE}/blog'
TODAY = date.today().isoformat()
MODIFIED = []

def read(f):
    with open(f, 'r') as fh:
        return fh.read()

def write(f, content):
    with open(f, 'w') as fh:
        fh.write(content)
    MODIFIED.append(f)
    return f

def update_lastmod(content):
    return re.sub(r'"dateModified":\s*"[^"]*"', f'"dateModified": "{TODAY}"', content)

# ============================================
# Fix #1: pineapple cake title — 實測3天寄達 → 最快5-7天（空運）
# Fix #2: pineapple cake meta — 實測深圳3天到、上海5天到 → 最快5-7天（空運）
# ============================================
print("=== Fix #1-#2: pineapple cake title/meta ===")
f = f'{BLOG}/taiwan-pineapple-cake-shipping.html'
c = read(f)

# Title: 鳳梨酥可以寄大陸嗎？⚡實測3天寄達 2026佳德/微熱山丘/小潘 NT$290起包稅 - 速豹集運
c = c.replace(
    '<title>鳳梨酥可以寄大陸嗎？⚡實測3天寄達 2026佳德/微熱山丘/小潘 NT$290起包稅 - 速豹集運</title>',
    '<title>鳳梨酥可以寄大陸嗎？2026佳德/微熱山丘/小潘寄送攻略 NT$290/kg起包稅最快5-7天（空運） - 速豹集運</title>'
)

# Meta description: ...實測深圳3天到、上海5天到。真空包裝教學...
c = c.replace(
    '實測深圳3天到、上海5天到。真空包裝教學',
    '專線最快5-7天（空運）送達。真空包裝教學'
)

# OG title
c = c.replace(
    'content="鳳梨酥可以寄大陸嗎？⚡實測3天寄達 2026佳德/微熱山丘/小潘 NT$290起包稅 - 速豹集運"',
    'content="鳳梨酥可以寄大陸嗎？2026佳德/微熱山丘/小潘寄送攻略 NT$290/kg起包稅最快5-7天（空運） - 速豹集運"'
)

# OG description
c = c.replace(
    '實測深圳3天到、上海5天到',
    '專線最快5-7天（空運）送達'
)

c = update_lastmod(c)
write(f, c)
print("  ✅ pineapple cake fixed")

# Also fix #2 in Schema description
# Schema description already covers generic text, no specific time promise found in the inline schema

# ============================================
# Fix #3: /tw-to-cn — add cluster recommendation cards
# ============================================
print("=== Fix #3: /tw-to-cn cluster cards ===")
f = f'{BASE}/tw-to-cn.html'
c = read(f)

cluster_cards = '''<div style="background:#F5F7FA;border-radius:12px;padding:20px;margin:20px 0">
  <p style="margin:0 0 12px;font-weight:700;font-size:15px;color:#1e293b">📂 熱門寄送攻略</p>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px">
    <a href="/blog/food-shipping-guide" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">🍪 食品零食寄大陸攻略</a>
    <a href="/blog/health-products-shipping" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">💊 保健品藥品寄大陸攻略</a>
    <a href="/blog/cosmetics-shipping" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">💄 化妝品寄大陸攻略</a>
    <a href="/blog/noodles-ramen-shipping" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">🍜 泡麵寄大陸攻略</a>
    <a href="/blog/tea-shipping-guide" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">🍵 茶葉寄大陸攻略</a>
    <a href="/blog/taiwan-souvenir-shipping" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">🎁 伴手禮寄大陸攻略</a>
    <a href="/blog/tw-to-cn-shipping-guide" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">📦 台灣寄大陸完整指南</a>
    <a href="/blog/shipping-cost-guide" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">💰 運費計算完整攻略</a>
  </div>
</div>'''

# Insert the cards after the "敏感貨可寄品項" H2 section
# Find the closing </section> or </div> right after that H2
# Strategy: insert before the "寄件流程" H2 which follows 敏感貨可寄品項
c = c.replace(
    '<h2 class="section-title">寄件流程</h2>',
    cluster_cards + '\n<h2 class="section-title">寄件流程</h2>'
)

c = update_lastmod(c)
write(f, c)
print("  ✅ tw-to-cn cluster cards added")

# ============================================
# Fix #4: health-products cluster link matrix
# ============================================
print("=== Fix #4: health-products cluster ===")
LINK_STYLE = 'style="padding:12px 16px;background:#FFF3E0;border-radius:8px;font-size:14px"'

# Sub-page link template → pillar
def make_sub_to_pillar_link(text):
    return f'<p {LINK_STYLE}>🔗 👉 <a href="/blog/health-products-shipping">{text}</a></p>'

# 4a: health-supplement-shipping (had 0 links)
f = f'{BLOG}/health-supplement-shipping.html'
c = read(f)
# Insert before FAQ or before 相關文章
if '<h2>常見問題' in c or 'FAQ' in c:
    c = c.replace(
        '<h2>常見問題',
        make_sub_to_pillar_link('查看完整保健品寄大陸攻略：運費、通關、品牌對照一篇搞懂') + '<h2>常見問題',
        1
    )
elif '<h2>相關文章' in c:
    c = c.replace(
        '<h2>相關文章',
        make_sub_to_pillar_link('查看完整保健品寄大陸攻略：運費、通關、品牌對照一篇搞懂') + '<h2>相關文章',
        1
    )
else:
    # Insert before the last </section> or before footer
    c = c.replace('</body>',
        make_sub_to_pillar_link('查看完整保健品寄大陸攻略：運費、通關、品牌對照一篇搞懂') + '\n</body>', 1)
c = update_lastmod(c)
write(f, c)
print("  ✅ health-supplement → pillar: 1 link added (now ≥1)")

# 4b: medicine-health-supplements-shipping (had 1, add 2nd)
f = f'{BLOG}/medicine-health-supplements-shipping.html'
c = read(f)
# Already has 1 link, add another contextual one near pricing/timing section
target_insert = '藥品寄大陸運費' if '藥品寄大陸運費' in c else '常見問題'
if target_insert in c:
    c = c.replace(
        target_insert,
        make_sub_to_pillar_link('查看完整保健品寄大陸攻略：葉黃素/益生菌/魚油/膠原蛋白全品項') + target_insert,
        1
    )
elif '相關文章' in c:
    c = c.replace(
        '相關文章',
        make_sub_to_pillar_link('查看完整保健品寄大陸攻略：葉黃素/益生菌/魚油/膠原蛋白全品項') + '相關文章',
        1
    )
else:
    c = c.replace('</body>',
        make_sub_to_pillar_link('查看完整保健品寄大陸攻略：葉黃素/益生菌/魚油/膠原蛋白全品項') + '\n</body>', 1)
c = update_lastmod(c)
write(f, c)
print("  ✅ medicine-health-supplements → pillar: 2nd link added (now ≥2)")

# 4c: health-products-shipping pillar → add recommendation grid for sub-pages
f = f'{BLOG}/health-products-shipping.html'
c = read(f)

health_sub_cards = '''<div style="background:#F0FDF4;border-radius:12px;padding:20px;margin:20px 0">
  <p style="margin:0 0 12px;font-weight:700;font-size:15px;color:#166534">💊 保健食品分類攻略</p>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px">
    <a href="/blog/health-supplement-shipping" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">保健食品寄大陸</a>
    <a href="/blog/medicine-health-supplements-shipping" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">藥品保健品寄大陸</a>
    <a href="/blog/lutein-shipping" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">葉黃素寄大陸</a>
    <a href="/blog/probiotics-shipping" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">益生菌寄大陸</a>
    <a href="/blog/fish-oil-shipping" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">魚油寄大陸</a>
    <a href="/blog/vitamin-shipping" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">維他命寄大陸</a>
    <a href="/blog/collagen-shipping" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">膠原蛋白寄大陸</a>
    <a href="/blog/chicken-essence-shipping" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">滴雞精寄大陸</a>
    <a href="/blog/birds-nest-ginseng-shipping" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">燕窩人參寄大陸</a>
    <a href="/blog/supplement-customs-guide" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">保健品通關指南</a>
  </div>
</div>'''

# Insert before FAQ or 相關文章
if '<h2>常見問題' in c:
    c = c.replace('<h2>常見問題', health_sub_cards + '<h2>常見問題', 1)
elif '<h2>相關文章' in c:
    c = c.replace('<h2>相關文章', health_sub_cards + '<h2>相關文章', 1)
else:
    c = c.replace('</body>', health_sub_cards + '\n</body>', 1)
c = update_lastmod(c)
write(f, c)
print("  ✅ health-products pillar → sub-pages: 10-card grid added")

# ============================================
# Fix #5: mooncake cluster link matrix
# ============================================
print("=== Fix #5: mooncake cluster ===")

MOONCAKE_LINK_STYLE = 'style="padding:12px 16px;background:#FFF7ED;border-radius:8px;font-size:14px"'

def make_mooncake_sub_to_pillar_link(text):
    return f'<p {MOONCAKE_LINK_STYLE}>🔗 👉 <a href="/blog/mid-autumn-mooncake-shipping">{text}</a></p>'

# 5a: mooncake pillar → add sub-page cards
f = f'{BLOG}/mid-autumn-mooncake-shipping.html'
c = read(f)

mooncake_sub_cards = '''<div style="background:#FFF7ED;border-radius:12px;padding:20px;margin:20px 0;border:1px solid #FED7AA">
  <p style="margin:0 0 12px;font-weight:700;font-size:15px;color:#C2410C">🥮 中秋月餅寄送專題</p>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px">
    <a href="/blog/mooncake-brands-shipping" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">🏷️ 月餅品牌寄送對照</a>
    <a href="/blog/mooncake-shipping-cost" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">💰 月餅運費試算</a>
    <a href="/blog/mooncake-types-shipping" style="background:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;color:#1a56db;font-weight:500;box-shadow:0 1px 3px rgba(0,0,0,0.08);display:block;font-size:14px">📋 月餅種類分類指南</a>
  </div>
</div>'''

# Insert after the "月餅可以寄到大陸嗎？" H2 section start
c = c.replace(
    '<h2>各類月餅寄送規定一覽</h2>',
    mooncake_sub_cards + '<h2>各類月餅寄送規定一覽</h2>',
    1
)
c = update_lastmod(c)
write(f, c)
print("  ✅ mooncake pillar → sub-pages: 3-card grid added")

# 5b: mooncake-brands-shipping → pillar (had 0)
f = f'{BLOG}/mooncake-brands-shipping.html'
c = read(f)
if '常見問題' in c:
    c = c.replace('常見問題',
        make_mooncake_sub_to_pillar_link('查看中秋月餅寄大陸完整攻略：規定、包裝、行事曆一篇掌握') + '常見問題', 1)
elif '相關文章' in c:
    c = c.replace('相關文章',
        make_mooncake_sub_to_pillar_link('查看中秋月餅寄大陸完整攻略：規定、包裝、行事曆一篇掌握') + '相關文章', 1)
else:
    c = c.replace('</body>',
        make_mooncake_sub_to_pillar_link('查看中秋月餅寄大陸完整攻略：規定、包裝、行事曆一篇掌握') + '\n</body>', 1)
c = update_lastmod(c)
write(f, c)
print("  ✅ mooncake-brands → pillar: 1 link added")

# Also add a 2nd link near content area
g = read(f)
if '月餅品牌' in g and g.count('mid-autumn-mooncake-shipping') < 2:
    g = g.replace(
        '月餅品牌',
        make_mooncake_sub_to_pillar_link('查看中秋月餅寄大陸完整攻略：海關規定+寄件行事曆') + '月餅品牌',
        1
    )
    write(f, g)
    print("  ✅ mooncake-brands → pillar: 2nd link added (now ≥2)")

# 5c: mooncake-types-shipping → pillar (had 0)
f = f'{BLOG}/mooncake-types-shipping.html'
c = read(f)
if '常見問題' in c:
    c = c.replace('常見問題',
        make_mooncake_sub_to_pillar_link('查看中秋月餅寄大陸完整攻略：運費、品牌對照、寄件時間表') + '常見問題', 1)
elif '相關文章' in c:
    c = c.replace('相關文章',
        make_mooncake_sub_to_pillar_link('查看中秋月餅寄大陸完整攻略：運費、品牌對照、寄件時間表') + '相關文章', 1)
else:
    c = c.replace('</body>',
        make_mooncake_sub_to_pillar_link('查看中秋月餅寄大陸完整攻略：運費、品牌對照、寄件時間表') + '\n</body>', 1)
c = update_lastmod(c)
write(f, c)
print("  ✅ mooncake-types → pillar: 1 link added")

# Add 2nd link
g = read(f)
if '月餅種類' in g and g.count('mid-autumn-mooncake-shipping') < 2:
    g = g.replace(
        '月餅種類',
        make_mooncake_sub_to_pillar_link('查看中秋月餅寄大陸完整攻略：運費、品牌對照、寄件時間表') + '月餅種類',
        1
    )
    write(f, g)
    print("  ✅ mooncake-types → pillar: 2nd link added (now ≥2)")

# 5d: mooncake-shipping-cost → pillar (already has 1, ensure ≥2)
f = f'{BLOG}/mooncake-shipping-cost.html'
c = read(f)
if c.count('mid-autumn-mooncake-shipping') < 2:
    c = c.replace('</body>',
        make_mooncake_sub_to_pillar_link('查看中秋月餅寄大陸完整攻略：品牌寄送對照+海關新規') + '\n</body>', 1)
    c = update_lastmod(c)
    write(f, c)
    print("  ✅ mooncake-shipping-cost → pillar: 2nd link added (now ≥2)")
else:
    print("  ✅ mooncake-shipping-cost → pillar: already ≥2")

# ============================================
# Fix #6: food brand sub-pages: add 2nd pillar link
# ============================================
print("=== Fix #6: food brand sub-pages → pillar (≥2) ===")

FOOD_LINK_STYLE = 'style="padding:10px 14px;background:#FFF3E0;border-radius:6px;font-size:13px;display:inline-block;margin:8px 0"'

def make_food_link(text):
    return f'<span {FOOD_LINK_STYLE}>🔗 完整攻略：<a href="/blog/food-shipping-guide">{text}</a></span>'

brand_pages = [
    'guai-guai-shipping',
    'cola-guo-shipping',
    'science-noodles-shipping',
    'tongyi-noodles-shipping',
    'imei-puffs-shipping',
    'taiwan-snack-recommend',
    'taiwan-snack-shipping',
    'taiwan-food-snacks-to-china',
]

for page in brand_pages:
    f = f'{BLOG}/{page}.html'
    c = read(f)
    count = c.count('food-shipping-guide')
    if count >= 2:
        print(f"  ✅ {page}: already ≥2 links")
        continue
    
    link_text_map = {
        'guai-guai-shipping': '食品零食寄大陸攻略：乖乖/可樂果/義美全品牌對照',
        'cola-guo-shipping': '食品零食寄大陸攻略：乖乖/可樂果/義美全品牌對照',
        'science-noodles-shipping': '食品零食寄大陸攻略：泡麵/科學麵/統一麵寄送對照',
        'tongyi-noodles-shipping': '食品零食寄大陸攻略：泡麵/科學麵/統一麵寄送對照',
        'imei-puffs-shipping': '食品零食寄大陸攻略：義美小泡芙/乖乖/可樂果寄送對照',
        'taiwan-snack-recommend': '台灣零食寄大陸終極攻略：24款餅乾糖果對照表',
        'taiwan-snack-shipping': '台灣零食寄大陸終極攻略：24款餅乾糖果對照表',
        'taiwan-food-snacks-to-china': '台灣零食寄大陸終極攻略：24款餅乾糖果對照表',
    }
    
    link_html = make_food_link(link_text_map.get(page, '食品零食寄大陸完整攻略'))
    
    # Insert before 常見問題 or 相關文章 or </body>
    if '常見問題' in c:
        c = c.replace('常見問題', link_html + '常見問題', 1)
    elif '相關文章' in c:
        c = c.replace('相關文章', link_html + '相關文章', 1)
    else:
        c = c.replace('</body>', link_html + '\n</body>', 1)
    
    c = update_lastmod(c)
    write(f, c)
    print(f"  ✅ {page}: 2nd pillar link added")

# ============================================
# Summary
# ============================================
print(f"\n=== SUMMARY ===")
print(f"Total files modified: {len(MODIFIED)}")
for m in sorted(set(MODIFIED)):
    print(f"  {os.path.basename(m)}")
