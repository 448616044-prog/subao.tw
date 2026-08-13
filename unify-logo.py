#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一 header logo：把纯文字 logo 替换为图片 logo（picture + webp + png）
- 文字 logo: <a href="/" class="logo">速豹<span>集運</span></a>  (59页)
- 图片 logo: <picture><source webp><img png></picture>          (31页)
统一为图片 logo，用绝对路径 /images/，带 fetchpriority="high" 优化 LCP
"""
import re
import glob

BASE = "sites/tw-to-cn"
OLD = '<a href="/" class="logo">速豹<span>集運</span></a>'
NEW = (
    '<a href="/" class="logo"><picture>'
    '<source srcset="/images/subao-logo-new.webp" type="image/webp">'
    '<img src="/images/subao-logo-new.png" alt="速豹集運" width="200" height="50" fetchpriority="high" decoding="async">'
    '</picture></a>'
)

files = glob.glob(f"{BASE}/*.html") + glob.glob(f"{BASE}/blog/*.html")
changed = 0
for f in files:
    with open(f, encoding="utf-8") as fh:
        html = fh.read()
    if OLD in html:
        html = html.replace(OLD, NEW)
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(html)
        changed += 1
        print(f"[OK] {f.replace(BASE + '/', '')}")

print(f"\n共替换 {changed} 个文字 logo 页面")
