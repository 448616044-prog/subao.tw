#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补充：处理剩余文字 logo 变体（速豹集運 / 速豹集運<span>副标题</span>）"""
import re
import glob

BASE = "sites/tw-to-cn"
NEW = (
    '<a href="/" class="logo"><picture>'
    '<source srcset="/images/subao-logo-new.webp" type="image/webp">'
    '<img src="/images/subao-logo-new.png" alt="速豹集運" width="200" height="50" fetchpriority="high" decoding="async">'
    '</picture></a>'
)

# 匹配各种文字 logo 变体
PATTERNS = [
    r'<a href="/" class="logo">速豹集運</a>',
    r'<a href="/" class="logo">速豹集運<span[^>]*>[^<]*</span></a>',
]

files = glob.glob(f"{BASE}/*.html") + glob.glob(f"{BASE}/blog/*.html")
changed = 0
for f in files:
    with open(f, encoding="utf-8") as fh:
        html = fh.read()
    orig = html
    for pat in PATTERNS:
        html = re.sub(pat, NEW, html)
    if html != orig:
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(html)
        changed += 1

print(f"补充替换 {changed} 个页面")
