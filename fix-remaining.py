import re, os
from datetime import date

BASE = '/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn'
BLOG = f'{BASE}/blog'
TODAY = date.today().isoformat()
MODIFIED = []

def read(f):
    with open(f) as fh:
        return fh.read()

def write(f, c):
    with open(f, 'w') as fh:
        fh.write(c)
    MODIFIED.append(f)

def update_lastmod(c):
    return re.sub(r'"dateModified":\s*"[^"]*"', f'"dateModified": "{TODAY}"', c)

# ============================================
# Fix #1: tw-to-cn title 76→55 chars
# ============================================
print("Fix #1: tw-to-cn title trim")
f = f'{BASE}/tw-to-cn.html'
c = read(f)

c = c.replace(
    '<title>台灣寄大陸專線｜食品/保健品/化妝品/茶葉 敏感貨快遞 NT$290/kg起包稅雙清</title>',
    '<title>台灣寄大陸快遞推薦｜敏感貨專線NT$290/kg起包稅最快5-7天（空運） - 速豹集運</title>'
)
# Also fix H1 to match
c = c.replace(
    '<h1>台灣寄大陸專線｜食品/保健品/化妝品/茶葉 敏感貨快遞 NT$290/kg起包稅雙清</h1>',
    '<h1>台灣寄大陸快遞推薦｜敏感貨專線NT$290/kg起包稅最快5-7天（空運）</h1>'
)
c = update_lastmod(c)
write(f, c)
print(f"  ✅ tw-to-cn title: {len('台灣寄大陸快遞推薦｜敏感貨專線NT$290/kg起包稅最快5-7天（空運） - 速豹集運')} chars")

# ============================================
# Fix #2: taiwan-snack-shipping meta "最快5-7天送到"→标准
# ============================================
print("Fix #2: taiwan-snack-shipping meta")
f = f'{BLOG}/taiwan-snack-shipping.html'
c = read(f)
c = c.replace(
    '最快5-7天送到！',
    '最快5-7天（空運）包稅雙清！'
)
c = update_lastmod(c)
write(f, c)
print("  ✅ taiwan-snack-shipping meta fixed")

# ============================================
# Fix #3: real-customer-cases meta "鳳梨酥寄上海5天到"
# ============================================
print("Fix #3: real-customer-cases meta")
f = f'{BLOG}/real-customer-cases.html'
c = read(f)
# Meta description
c = c.replace(
    '鳳梨酥寄上海5天到、茶葉寄北京未課稅',
    '鳳梨酥寄上海成功送達、茶葉寄北京未課稅'
)
c = c.replace(
    '鳳梨酥寄上海5天到、茶葉寄北京未課稅',
    '鳳梨酥寄上海成功送達、茶葉寄北京未課稅'
)
# OG description
c = c.replace(
    '鳳梨酥寄上海5天到',
    '鳳梨酥寄上海成功送達'
)
c = update_lastmod(c)
write(f, c)
print("  ✅ real-customer-cases meta/OG fixed")

# ============================================
# Fix #4: case-milk-powder-herbs-jilin "5天送達"
# ============================================
print("Fix #4: case-milk-powder-herbs-jilin")
f = f'{BLOG}/case-milk-powder-herbs-jilin.html'
c = read(f)
# Title
c = c.replace(
    '<title>客戶案例｜奶粉+中藥粉寄吉林延邊，4.5kg敏感貨5天送達 | 速豹集運</title>',
    '<title>客戶案例｜奶粉+中藥粉寄吉林延邊，4.5kg敏感貨成功送達 | 速豹集運</title>'
)
# Meta description
c = c.replace(
    '4.5kg敏感貨5天成功送達',
    '4.5kg敏感貨成功送達'
)
# OG title
c = c.replace(
    'content="客戶案例｜奶粉+中藥粉寄吉林延邊，4.5kg敏感貨5天送達 | 速豹集運"',
    'content="客戶案例｜奶粉+中藥粉寄吉林延邊，4.5kg敏感貨成功送達 | 速豹集運"'
)
# OG description
c = c.replace(
    'content="客戶案例｜奶粉+中藥粉寄吉林延邊，4.5kg敏感貨5天送達。"',
    'content="客戶案例｜奶粉+中藥粉寄吉林延邊，4.5kg敏感貨成功送達。"'
)
c = update_lastmod(c)
write(f, c)
print("  ✅ case-milk-powder-herbs-jilin all fixed")

# ============================================
# Fix #5: food-shipping-guide meta add 鳳凰酥 for CTR boost
# ============================================
print("Fix #5: food-shipping-guide meta + keywords add 鳳凰酥")
f = f'{BLOG}/food-shipping-guide.html'
c = read(f)
# Add 鳳凰酥 into meta description (before "。含肉製品")
c = c.replace(
    '鳳梨酥✅泡麵⚠️肉乾❌，20+品類一表對照。含肉製品禁運紅線',
    '鳳梨酥✅鳳凰酥✅泡麵⚠️肉乾❌，20+品類一表對照。含肉製品禁運紅線'
)
# Add 鳳凰酥 into keywords
c = c.replace(
    'content="台灣零食寄大陸,台灣食品寄大陸,鳳梨酥寄大陸',
    'content="台灣零食寄大陸,台灣食品寄大陸,鳳凰酥寄大陸,鳳梨酥寄大陸'
)
# Also update OG description
c = c.replace(
    '鳳梨酥/泡麵/肉乾等22種熱門食品寄送規定 - 速豹集運',
    '鳳梨酥/鳳凰酥/泡麵/肉乾等22種熱門食品寄送規定 - 速豹集運'
)
c = update_lastmod(c)
write(f, c)
print("  ✅ food-shipping-guide meta+keywords+OG updated for 鳳凰酥")

# ============================================
# Summary
# ============================================
print(f"\n=== SUMMARY ===")
print(f"Files modified: {len(set(MODIFIED))}")
for m in sorted(set(MODIFIED)):
    print(f"  {os.path.basename(m)}")
