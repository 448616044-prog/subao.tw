#!/usr/bin/env python3
"""Fix city page case studies:
- Recalculate prices based on new pricing (敏感貨 NT$290, 快件一般貨 NT$380, 快件敏感貨 NT$450)
- Fix all "2天從/3天從" → "5-7天從" (missed in previous round)
"""

import os

BASE = "/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn/blog"

# All case study fixes: (old_string, new_string)
# Each string is unique enough within its file

case_fixes = {
    # === chongqing L260: 商業件 6kg, NT$2,340 (old NT$390/kg) → NT$2,280 (NT$380/kg) ===
    "chongqing-shipping-guide.html": [
        ("運費NT$2,340，3天從桃園到重慶", "運費NT$2,280，5-7天從桃園到重慶"),
    ],

    # === nanjing L261: 商業件 4kg, NT$1,560 (old NT$390/kg) → NT$1,520 (NT$380/kg) ===
    "nanjing-shipping-guide.html": [
        ("運費NT$1,560，3天從台北內湖到南京", "運費NT$1,520，5-7天從台北內湖到南京"),
    ],

    # === wuhan L260: 商業件 5kg, NT$1,950 (old NT$390/kg) → NT$1,900 (NT$380/kg) ===
    "wuhan-shipping-guide.html": [
        ("運費NT$1,950，3天從新竹到武漢", "運費NT$1,900，5-7天從新竹到武漢"),
    ],

    # === shanghai L261: 快件 3-5kg, NT$1,170-1,950 (old NT$390/kg) → NT$1,140-1,900 (NT$380/kg) ===
    "shanghai-shipping-guide.html": [
        ("單箱運費NT$1,170-1,950，3天從桃園倉庫到上海", "單箱運費NT$1,140-1,900，5-7天從桃園倉庫到上海"),
    ],

    # === shenzhen L262: 敏感貨 含鋰電池, 單台 NT$580, 3天 → fix time only ===
    # Price ambiguous (includes unknown fees), only fix time
    "shenzhen-shipping-guide.html": [
        ("單台運費NT$580，3天從新北到深圳", "單台運費NT$490，5-7天從新北到深圳"),
    ],

    # === beijing L261: 快件敏感貨 8kg, NT$3,840 (old NT$480/kg) → NT$3,600 (NT$450/kg) ===
    "beijing-shipping-guide.html": [
        ("運費NT$3,840，3天從台北內湖到北京", "運費NT$3,600，5-7天從台北內湖到北京"),
    ],

    # === hangzhou L261: 快件 1-2kg, NT$410-820 (old NT$410/kg) → NT$380-760 (NT$380/kg) ===
    # === hangzhou L262: 敏感貨 5kg, NT$1,950 (old NT$390/kg) → NT$1,450 (NT$290/kg) ===
    "hangzhou-shipping-guide.html": [
        ("運費NT$410-820，2天從台北到杭州", "運費NT$380-760，5-7天從台北到杭州"),
        ("運費NT$1,950，3天從南投到杭州", "運費NT$1,450，5-7天從南投到杭州"),
    ],

    # === guangzhou L260: 敏感貨 3-4kg, NT$1,170-1,560 (old NT$390/kg) → NT$870-1,160 (NT$290/kg) ===
    # === guangzhou L261: 快件 2kg, NT$820 (old NT$410/kg) → NT$760 (NT$380/kg) ===
    "guangzhou-shipping-guide.html": [
        ("單箱運費NT$1,170-1,560，3天從台中到廣州", "單箱運費NT$870-1,160，5-7天從台中到廣州"),
        ("運費NT$820，2天從台北到番禺", "運費NT$760，5-7天從台北到番禺"),
    ],

    # === xiamen L259: 敏感貨 3-5kg, NT$1,170-1,950 (old NT$390/kg) → NT$870-1,450 (NT$290/kg) ===
    # === xiamen L260: 商業件 1.5kg, NT$585 (old NT$390/kg) → NT$570 (NT$380/kg) ===
    "xiamen-shipping-guide.html": [
        ("運費NT$1,170-1,950，3天從嘉義到廈門", "運費NT$870-1,450，5-7天從嘉義到廈門"),
        ("運費NT$585，5-7天送達", "運費NT$570，5-7天送達"),
    ],
}

def apply_replacements(filepath, replacements, label):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    total_changes = 0
    for old, new in replacements:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            total_changes += count
            print(f"  [{label}] Replaced {count}x: {old[:70]}...")
        else:
            print(f"  [{label}] WARNING NOT FOUND: {old[:70]}...")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return total_changes

total = 0
for filename, reps in case_fixes.items():
    filepath = os.path.join(BASE, filename)
    print(f"\n=== {filename} ===")
    total += apply_replacements(filepath, reps, filename.split('-')[0])

print(f"\n{'='*60}")
print(f"Total case study fixes: {total}")
