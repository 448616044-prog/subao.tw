#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
subao.tw 价格文案口径对齐（第一轮）
方向 C：保留「普貨/最低 290」钩子，把「敏感貨/特貨」品类单价改准

规则（严格锚定品类词，句边界+排除"普"字防误伤）：
  R1 : 特貨/特货 ... 350  -> 500   （经济 C 类 华南最低 500）
  R1b: NT$290/350          -> NT$290/500 （最低收费 普货290/特货500）
  R2 : 敏感貨/敏感货 ... 290 -> 360  （经济 B 类 华南最低 360）

幂等：规则替换后不会再次匹配自身（350已变500，290已变360，不会重复命中）。
"""
import re, glob, os, sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sites', 'tw-to-cn')

RULES = [
    ('R1_tehuo_350_500', re.compile(r'(特貨|特货)([^。；;0-9]{0,30}?)NT\$\s?350'), r'\1\2NT$500'),
    ('R1b_min_290_350', re.compile(r'NT\$\s?290\s*/\s*350'), r'NT$290/500'),
    ('R2_mingan_290_360', re.compile(r'(敏感貨|敏感货)([^。；;普0-9]{0,30}?)NT\$\s?290'), r'\1\2NT$360'),
    ('R2b_mingan_350_360', re.compile(r'(敏感貨|敏感货)([^。；;普特0-9]{0,30}?)NT\$\s?350'), r'\1\2NT$360'),
]

def main():
    if not os.path.isdir(BASE):
        print(f"BASE not found: {BASE}", file=sys.stderr)
        sys.exit(1)
    total_files = 0
    total_changes = 0
    per_rule = {name: 0 for name, _, _ in RULES}
    changed_files = []
    for p in glob.glob(os.path.join(BASE, '**/*.html'), recursive=True):
        h = open(p, encoding='utf-8').read()
        orig = h
        for name, rx, rep in RULES:
            h, n = rx.subn(rep, h)
            per_rule[name] += n
            total_changes += n
        if h != orig:
            open(p, 'w', encoding='utf-8').write(h)
            total_files += 1
            changed_files.append(os.path.relpath(p, BASE))
    print(f"改动文件: {total_files}")
    print(f"改动总处数: {total_changes}")
    for name, n in per_rule.items():
        print(f"  {name}: {n}")
    return changed_files

if __name__ == '__main__':
    changed = main()
