#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
内链注入：给高流量页补正文锚文本内链
- /tw-to-cn（台灣寄大陸完整攻略）→ head term 助推
- /blog/daigou-shipping（代購代寄大陸）→ 代寄服务内链

防重复：块带 data-inject 标记
"""
import os

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sites", "tw-to-cn")

MARKER = '<footer class="footer">'

# 完整块：/tw-to-cn + daigou
BLOCK_FULL = (
    '<div data-inject="tw-cn-daigou" style="background:#f9f9f9;border-radius:8px;padding:16px 20px;margin:20px 0">\n'
    '<p style="font-weight:700;margin:0 0 8px">🔗 延伸閱讀</p>\n'
    '<ul style="margin:0;padding-left:20px">\n'
    '<li><a href="/tw-to-cn">📦 台灣寄大陸完整攻略</a> — 寄件流程、運費、禁運品一次看懂</li>\n'
    '<li><a href="/blog/daigou-shipping">🛍️ 台灣代購代寄大陸全攻略</a> — 化妝品/保健品/手機代購怎麼寄最省</li>\n'
    '</ul>\n'
    '</div>'
)

# 仅 daigou 块
BLOCK_DAIGOU = (
    '<div data-inject="tw-cn-daigou" style="background:#f9f9f9;border-radius:8px;padding:16px 20px;margin:20px 0">\n'
    '<p style="font-weight:700;margin:0 0 8px">🔗 延伸閱讀</p>\n'
    '<ul style="margin:0;padding-left:20px">\n'
    '<li><a href="/blog/daigou-shipping">🛍️ 台灣代購代寄大陸全攻略</a> — 化妝品/保健品/手機代購怎麼寄最省</li>\n'
    '</ul>\n'
    '</div>'
)

# 页面 -> 块类型
PAGES = {
    # #380 head term 助推（缺正文精准锚文本）
    "blog/food-shipping-guide.html": "full",
    "blog/tw-to-cn-shipping-guide.html": "full",
    "blog/tw-to-cn-cost.html": "full",
    # #384 代寄内链（daigou 正文入链仅1个）
    "blog/cosmetics-shipping.html": "daigou",
    "blog/health-products-shipping.html": "daigou",
    "blog/electronics-shipping.html": "daigou",
    "blog/taiwan-souvenir-shipping.html": "daigou",
}

def main():
    done = 0
    for rel, kind in PAGES.items():
        path = os.path.join(BASE, rel)
        if not os.path.exists(path):
            print(f"[MISS] {rel}")
            continue
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()
        if 'data-inject="tw-cn-daigou"' in html:
            print(f"[SKIP] {rel} (already injected)")
            continue
        if MARKER not in html:
            print(f"[NOFOOTER] {rel}")
            continue
        block = BLOCK_FULL if kind == "full" else BLOCK_DAIGOU
        html = html.replace(MARKER, block + "\n" + MARKER, 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        done += 1
        print(f"[OK] {rel} ({kind})")
    print(f"\nTotal injected: {done}")

if __name__ == "__main__":
    main()
