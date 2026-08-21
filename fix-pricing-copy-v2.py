#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
subao.tw 价格文案口径纠正 v2（方案A：抬头统一 NT$290/kg 起 + 正文按品类×收货地点）
用户口径（2026-08-21 确认）：
  - 没有「普货/敏感货/特货」三分类，只分「品类(A/B/C/D) × 收货地点(7区)」
  - 敏感货也是 NT$290 起（食品属 A 类）
  - 价格表不动（A290/B360/C500/D780 × 7区）；快件线 NT$380 起保持

规则（幂等）：
  R1 三分类句 paren 变体 -> 品类句
  R2 三分类句 slash 变体 -> 品类句
  R3 敏感货/敏感货 ... NT$360 -> NT$290
  R4 title 内纯 NT$360/kg 起 -> NT$290/kg起（美妆类标题）
  R5 title 内含电池维修 NT$500/kg起 -> LINE 單獨報價
  R6 full-price 错乱标题 360-350 -> 290
  R7 about 食品NT$360 -> 食品NT$290
"""
import re, glob, os, sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sites', 'tw-to-cn')
DRY = '--dry' in sys.argv

RULES = [
    # R1 三分类句（括号变体，FAQ/正文）
    ('cat3_paren',
     '普貨（衣物/書籍）NT$290/kg起，敏感貨（食品/化妝品/保健品/茶葉）NT$360/kg起，特貨（含電池電子產品）NT$500/kg起',
     '食品/日用（A類）NT$290/kg起，美妝/保健品（B類）NT$360/kg起，電器含電池（C類）NT$500/kg起'),
    # R2 三分类句（斜杠变体，meta）
    ('cat3_slash',
     '普貨NT$290/kg起/敏感貨NT$360/kg起/特貨NT$500/kg起',
     '食品/日用NT$290/kg起，美妝/保健品NT$360/kg起，電器NT$500/kg起'),
    # R3 敏感货 360 -> 290（保留「敏感货」SEO 关键词，只改价）
    ('mingan360',
     r'(敏感貨|敏感货)([^。；;0-9]{0,30}?)NT\$\s?360',
     r'\1\2NT$290'),
    # R4 纯 NT$360/kg 起 -> NT$290/kg起（美妆类标题 dr-wu/neogence 等）
    ('title360', r'NT\$\s?360/kg\s?起', r'NT$290/kg起'),
    # R5 含电池维修标题 NT$500/kg起 -> LINE 單獨報價
    ('title500_repair', r'NT\$\s?500/kg起', r'LINE 單獨報價'),
    # R6 full-price 错乱标题
    ('fullprice', '普貨/敏感貨/特貨 NT$360-350/kg', 'NT$290/kg起'),
    # R7 about 食品 360 -> 290
    ('food360', '食品NT$360/kg起', '食品NT$290/kg起'),
]

def process_text(s):
    for name, pat, repl in RULES:
        s = re.sub(pat, repl, s)
    return s

def main():
    if not os.path.isdir(BASE):
        print(f"BASE not found: {BASE}", file=sys.stderr); sys.exit(1)
    files = [p for p in glob.glob(os.path.join(BASE, '**/*.html'), recursive=True)
             if '.bak' not in p]
    total_changes = 0
    changed_files = []
    per_rule = {}
    for p in files:
        s = open(p, encoding='utf-8').read()
        orig = s
        # R4/R5/R6 只在 title 标签内应用；其余全文档
        for name, pat, repl in RULES:
            if name in ('title360', 'title500_repair', 'fullprice'):
                # 仅 title 标签内
                def _sub_title(m):
                    inner = re.sub(pat, repl, m.group(1))
                    return '<title>' + inner + '</title>'
                s = re.sub(r'<title>(.*?)</title>', _sub_title, s, flags=re.S)
            else:
                s = re.sub(pat, repl, s)
        if s != orig:
            if not DRY:
                open(p, 'w', encoding='utf-8').write(s)
            changed_files.append(os.path.relpath(p, BASE))
            total_changes += 1
    # 统计命中次数
    for name, pat, repl in RULES:
        n = 0
        for p in files:
            s = open(p, encoding='utf-8').read()
            n += len(re.findall(pat, s))
        per_rule[name] = n
    print(f"模式: {'DRY-RUN' if DRY else 'EXECUTE'}")
    print(f"改动文件数: {len(changed_files)}")
    print("规则命中（改动后残留统计）:")
    for name in [r[0] for r in RULES]:
        print(f"  {name}: {per_rule[name]}")
    return changed_files

if __name__ == '__main__':
    main()
