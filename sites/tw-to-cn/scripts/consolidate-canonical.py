#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
subao.tw 关键词蚕食合并脚本
将重复意图的页面 canonical 收敛到各集群的「赢家页」，消除中短词自我竞争。
原则：赢家页 = 该集群当前 GSC 表现最好/内容最完整的页面。
"""
import re
import sys
import pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent  # sites/tw-to-cn/

# loser 文件（相对 BASE）-> 赢家 canonical URL
MAPPING = {
    # 「台灣寄大陸」指南/教學 cluster -> 赢家 tw-to-cn-shipping-guide（当前 6504 展现的工作马）
    "blog/tw-to-cn-ultimate-guide.html": "https://subao.tw/blog/tw-to-cn-shipping-guide",
    "blog/tw-to-cn-quick-start-guide.html": "https://subao.tw/blog/tw-to-cn-shipping-guide",

    # 「快遞比較/推薦」cluster -> 赢家 express-ultimate-comparison-2026
    "blog/tw-to-cn-express-comparison.html": "https://subao.tw/blog/tw-to-cn-express-ultimate-comparison-2026",
    "blog/tw-to-cn-logistics-comparison.html": "https://subao.tw/blog/tw-to-cn-express-ultimate-comparison-2026",
    "blog/tw-to-cn-logistics-recommend.html": "https://subao.tw/blog/tw-to-cn-express-ultimate-comparison-2026",
    "blog/tw-to-cn-shipping-recommend-2026.html": "https://subao.tw/blog/tw-to-cn-express-ultimate-comparison-2026",
    "blog/tw-to-cn-shipping-methods.html": "https://subao.tw/blog/tw-to-cn-express-ultimate-comparison-2026",

    # 「運費/價格」cluster -> 赢家 tw-to-cn-cost
    "blog/tw-to-cn-full-price-2026.html": "https://subao.tw/blog/tw-to-cn-cost",
    "blog/tw-to-cn-shipping-cost-comparison.html": "https://subao.tw/blog/tw-to-cn-cost",
    "blog/tw-to-cn-shipping-cost-ultimate-guide.html": "https://subao.tw/blog/tw-to-cn-cost",

    # 「時效」cluster -> 赢家 transit-time
    "blog/tw-to-cn-shipping-time-comparison.html": "https://subao.tw/blog/tw-to-cn-transit-time",

    # 「禁運」cluster -> 赢家 prohibited-items
    "blog/tw-to-cn-prohibited-items-list.html": "https://subao.tw/blog/tw-to-cn-prohibited-items",
    "blog/tw-to-cn-prohibited-items-complete-2026.html": "https://subao.tw/blog/tw-to-cn-prohibited-items",
}

CANONICAL_RE = re.compile(r'(<link\s+rel="canonical"\s+href=")[^"]*("\s*/?>)', re.IGNORECASE)

def main():
    changed = []
    for rel, target in MAPPING.items():
        p = BASE / rel
        if not p.exists():
            print(f"[跳过] 文件不存在: {rel}")
            continue
        html = p.read_text(encoding="utf-8")
        new_tag = f'<link rel="canonical" href="{target}">'
        if CANONICAL_RE.search(html):
            html2, n = CANONICAL_RE.subn(lambda m: m.group(1) + target + m.group(2), html, count=1)
        else:
            # 无 canonical：插入到 </head> 前
            html2 = html.replace("</head>", f'  {new_tag}\n</head>', 1)
            n = 1
        if n:
            p.write_text(html2, encoding="utf-8")
            changed.append((rel, target))
        else:
            print(f"[未变] {rel}")
    print(f"\n✅ 共 {len(changed)} 个页面 canonical 已收敛：")
    for rel, target in changed:
        print(f"  {rel}  ->  {target}")

if __name__ == "__main__":
    main()
