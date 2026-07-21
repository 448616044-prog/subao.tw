#!/usr/bin/env python3
"""Fix pricing compliance:
- Task #868: 7 city pages - unify 敏感貨 pricing to NT$290 (普貨铁律)
- Task #869: used-phone-tablet - NT$380 → NT$350 (特貨铁律)
"""

import os

BASE = "/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn/blog"

# ===== Task #868: City Pages =====

# For 5 standard cities: change 敏感貨 in 經濟專線 from NT$360 to NT$290
# Also fix meta description: 快件線NT$450/kg起 → NT$380/kg起

standard_city_replacements = [
    # Schema FAQ text + Tip-box (both contain this substring)
    ("敏感貨（食品/化妝品/含電池）NT$360/kg", "敏感貨（食品/化妝品/含電池）NT$290/kg"),
    # Subtitle
    ("敏感貨NT$360/kg起", "敏感貨NT$290/kg起"),
    # Table: 經濟專線 敏感貨 cell (unique context with 7-12天)
    ("<td>NT$360/kg</td><td>7-12天</td>", "<td>NT$290/kg</td><td>7-12天</td>"),
]

# Cities that need meta description fix (快件線NT$450 → NT$380)
# hangzhou already has NT$380 in description
desc_fix_cities = ["shenzhen", "guangzhou", "xiamen", "nanjing"]

# Beijing: all 4 prices change
beijing_replacements = [
    # Schema FAQ text - replace entire pricing section
    (
        "經濟線一般貨（衣服/書籍/日用品）NT$320/kg，敏感貨（食品/化妝品/含電池）NT$390/kg（7-12天）。快件線更快：一般貨NT$410/kg，敏感貨NT$480/kg（5-7天）",
        "經濟線一般貨（衣服/書籍/日用品）NT$290/kg，敏感貨（食品/化妝品/含電池）NT$290/kg（7-12天）。快件線更快：一般貨NT$380/kg，敏感貨NT$450/kg（5-7天）"
    ),
    # Meta description
    ("經濟線NT$320/kg起、快件線NT$480/kg起", "經濟線NT$290/kg起、快件線NT$380/kg起"),
    # Subtitle
    ("一般貨NT$320/kg起 · 敏感貨NT$390/kg起", "一般貨NT$290/kg起 · 敏感貨NT$290/kg起"),
    # Tip-box
    (
        "經濟線一般貨（衣服/書籍/日用品）NT$320/kg，敏感貨（食品/化妝品/含電池）NT$390/kg。快件線更快：一般貨NT$410/kg，敏感貨NT$480/kg",
        "經濟線一般貨（衣服/書籍/日用品）NT$290/kg，敏感貨（食品/化妝品/含電池）NT$290/kg。快件線更快：一般貨NT$380/kg，敏感貨NT$450/kg"
    ),
    # Table rows (經濟 + 快件)
    ("<td>NT$320/kg</td><td>NT$390/kg</td>", "<td>NT$290/kg</td><td>NT$290/kg</td>"),
    ("<td>NT$410/kg</td><td>NT$480/kg</td>", "<td>NT$380/kg</td><td>NT$450/kg</td>"),
]

# Wuhan: all 4 prices change
wuhan_replacements = [
    # Schema FAQ text - replace entire pricing section
    (
        "經濟線一般貨（衣服/書籍/日用品）NT$300/kg，敏感貨（食品/化妝品/含電池）NT$380/kg（7-12天）。快件線更快：一般貨NT$390/kg，敏感貨NT$470/kg（5-7天）",
        "經濟線一般貨（衣服/書籍/日用品）NT$290/kg，敏感貨（食品/化妝品/含電池）NT$290/kg（7-12天）。快件線更快：一般貨NT$380/kg，敏感貨NT$450/kg（5-7天）"
    ),
    # Meta description
    ("經濟線NT$300/kg起、快件線NT$470/kg起", "經濟線NT$290/kg起、快件線NT$380/kg起"),
    # Subtitle
    ("一般貨NT$300/kg起 · 敏感貨NT$380/kg起", "一般貨NT$290/kg起 · 敏感貨NT$290/kg起"),
    # Tip-box
    (
        "經濟線一般貨（衣服/書籍/日用品）NT$300/kg，敏感貨（食品/化妝品/含電池）NT$380/kg。快件線更快：一般貨NT$390/kg，敏感貨NT$470/kg",
        "經濟線一般貨（衣服/書籍/日用品）NT$290/kg，敏感貨（食品/化妝品/含電池）NT$290/kg。快件線更快：一般貨NT$380/kg，敏感貨NT$450/kg"
    ),
    # Table rows (經濟 + 快件)
    ("<td>NT$300/kg</td><td>NT$380/kg</td>", "<td>NT$290/kg</td><td>NT$290/kg</td>"),
    ("<td>NT$390/kg</td><td>NT$470/kg</td>", "<td>NT$380/kg</td><td>NT$450/kg</td>"),
]

# ===== Task #869: used-phone-tablet-shipping.html =====

used_phone_replacements = [
    # All NT$380 → NT$350 (this page is about 含電池 3C = 特货 at NT$350)
    ("NT$380", "NT$350"),
    # Derived calculations in Schema (L41) and visible FAQ (L174)
    # iPad 0.5-0.7kg at NT$350: both below 1kg, minimum charge NT$350 applies
    ("運費約NT$190-270", "運費約NT$350"),
    ("運費約 NT$190-270", "運費約 NT$350"),
    # MacBook Air 1.3kg at NT$350: 1.3 × 350 = 455
    ("運費約NT$495", "運費約NT$455"),
    ("運費約 NT$495", "運費約 NT$455"),
]

# ===== Execute replacements =====

def apply_replacements(filepath, replacements, label):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    total_changes = 0
    for old, new in replacements:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            total_changes += count
            print(f"  [{label}] Replaced {count}x: {old[:60]}...")
        else:
            print(f"  [{label}] WARNING NOT FOUND: {old[:60]}...")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return total_changes

total = 0

# Task #868: 5 standard cities
for city in ["shenzhen", "guangzhou", "xiamen", "nanjing", "hangzhou"]:
    filepath = os.path.join(BASE, f"{city}-shipping-guide.html")
    reps = list(standard_city_replacements)
    if city in desc_fix_cities:
        reps.append(("快件線NT$450/kg起", "快件線NT$380/kg起"))
    print(f"\n=== {city}-shipping-guide.html ===")
    total += apply_replacements(filepath, reps, city)

# Task #868: Beijing
filepath = os.path.join(BASE, "beijing-shipping-guide.html")
print(f"\n=== beijing-shipping-guide.html ===")
total += apply_replacements(filepath, beijing_replacements, "beijing")

# Task #868: Wuhan
filepath = os.path.join(BASE, "wuhan-shipping-guide.html")
print(f"\n=== wuhan-shipping-guide.html ===")
total += apply_replacements(filepath, wuhan_replacements, "wuhan")

# Task #869: used-phone-tablet
filepath = os.path.join(BASE, "used-phone-tablet-shipping.html")
print(f"\n=== used-phone-tablet-shipping.html ===")
total += apply_replacements(filepath, used_phone_replacements, "used-phone")

print(f"\n{'='*60}")
print(f"Total replacements: {total}")
