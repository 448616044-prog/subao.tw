#!/usr/bin/env python3
"""
修复「特貨→電器（含電池）C類」批量替换误伤（2026-08-21 晚）

背景：今天方向「特貨→電器（含電池）」把含酒/含肉食品也误标成电器，
产生荒谬表述如「電器（含電池）（含酒包）」，损害页面主题相关性（疑致花雕雞排名下降）。

两类修复：
  1. 食品被误标电器 → 特殊貨品（保留原括注）
  2. 真电器但重复括号 → 電器（含電池）
"""
import glob, re

REPLACEMENTS = {
    # 类型1：食品误标电器 → 特殊貨品
    "電器（含電池）（含酒包）": "特殊貨品（含酒包）",
    "電器（含電池）（含肉+酒）": "特殊貨品（含肉+酒）",
    "電器（含電池）（含肉鬆/滷肉月餅）": "特殊貨品（含肉鬆/滷肉）",
    # 类型2b：混合电池+液体 → 特殊貨品
    "電器（含電池）（含電池/液體）": "特殊貨品（含電池/液體）",
    # 类型2a：真电器但重复括号 → 電器（含電池）
    "電器（含電池）（含電池電子產品）": "電器（含電池）",
    "電器（含電池）（含電池的電子產品）": "電器（含電池）",
    "電器（含電池）（含電池產品）": "電器（含電池）",
    "電器（含電池）（含電池3C）": "電器（含電池）",
}

files = glob.glob("*.html") + glob.glob("blog/*.html")
total = 0
for fp in files:
    with open(fp, encoding="utf-8") as f:
        s = f.read()
    orig = s
    for old, new in REPLACEMENTS.items():
        s = s.replace(old, new)
    n = sum(1 for old in REPLACEMENTS for _ in [0] if old in orig)  # 仅统计是否涉及
    changed = sum(orig.count(old) for old in REPLACEMENTS)
    if s != orig:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(s)
        total += changed
        print(f"✅ {fp}: {changed} 处")

print(f"\n总计修复 {total} 处")
