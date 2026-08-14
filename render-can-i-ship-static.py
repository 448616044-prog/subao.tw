#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把 can-i-ship.html 的 JS 数据 DB（212 商品）静态渲染成可折叠 HTML 清单（<details>），
插入 cta-section 之前，供搜索引擎抓取「XX可以寄大陸嗎」的答案。

- 默认收起（不设 open），视觉干净；Google/Baidu 均索引 <details> 内闭合内容。
- 带 <!-- ship-list-static:start/end --> 标记，可幂等重跑（先删旧块再注入）。
"""
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "sites/tw-to-cn/can-i-ship.html")

html = open(PATH, encoding="utf-8").read()

# 0. 幂等：先删除旧注入块（含带标记的新版 + 无标记的旧版）
html = re.sub(
    r'<!-- ship-list-static:start -->.*?<!-- ship-list-static:end -->\s*',
    "", html, count=1, flags=re.DOTALL,
)
html = re.sub(
    r'<section class="container" style="padding:32px 20px;max-width:900px;margin:0 auto">.*?</section>\s*(?=<div class="cta-section">)',
    "", html, count=1, flags=re.DOTALL,
)

# 1. 提取 DB 数组
start = html.find("const DB = [")
end = html.find("];", start)
if start == -1 or end == -1:
    raise SystemExit("DB not found")
db_raw = html[start + len("const DB = ["):end]

# 2. 解析每个商品
pattern = re.compile(
    r'\{id:"(?P<id>[^"]+)",cat:"(?P<cat>[^"]+)",status:"(?P<status>[^"]+)",'
    r'note:"(?P<note>[^"]*)",channel:"(?P<channel>[^"]*)",tax:"(?P<tax>[^"]*)"\}'
)
items = [m.groupdict() for m in pattern.finditer(db_raw)]

# 3. 分组
can = [it for it in items if it["status"] == "can"]
maybe = [it for it in items if it["status"] == "maybe"]
cannot = [it for it in items if it["status"] == "cannot"]

STATUS_ICON = {"can": "✅", "maybe": "⚠️", "cannot": "❌"}
STATUS_LABEL = {"can": "可寄", "maybe": "需確認", "cannot": "禁運"}
HEADER_COLOR = {"can": "#16A34A", "maybe": "#D97706", "cannot": "#DC2626"}
HEADER_BG = {"can": "#F0FDF4", "maybe": "#FFFBEB", "cannot": "#FEF2F2"}

def render_group(title, group, status):
    lis = []
    for it in group:
        icon = STATUS_ICON[it["status"]]
        note = it["note"] if it["note"] else ""
        lis.append(f'<li><strong>{it["id"]}</strong> {icon}{STATUS_LABEL[it["status"]]} — {note}</li>')
    body = "\n".join(lis)
    color = HEADER_COLOR[status]
    bg = HEADER_BG[status]
    return (
        f'<details>\n'
        f'  <summary style="background:{bg};color:{color}">{title}（{len(group)} 項）</summary>\n'
        f'  <ul>\n{body}\n  </ul>\n'
        f'</details>'
    )

block = (
    '<!-- ship-list-static:start -->\n'
    '<section class="container" style="padding:32px 20px;max-width:960px;margin:0 auto">\n'
    '<style>\n'
    '.ship-list details{background:#fff;border:1px solid #eee;border-radius:12px;'
    'box-shadow:0 2px 10px rgba(0,0,0,.06);margin-bottom:12px;overflow:hidden}\n'
    '.ship-list summary{cursor:pointer;padding:16px 20px;font-size:17px;font-weight:700;'
    'list-style:none;display:flex;align-items:center;justify-content:space-between;user-select:none}\n'
    '.ship-list summary::-webkit-details-marker{display:none}\n'
    '.ship-list summary::after{content:"▾";font-size:14px;opacity:.7;transition:transform .2s}\n'
    '.ship-list details[open] summary::after{transform:rotate(180deg)}\n'
    '.ship-list ul{margin:0;padding:16px 24px;color:#555;line-height:1.8;font-size:14px;'
    'columns:2;column-gap:32px;list-style:none}\n'
    '.ship-list li{padding:5px 0;break-inside:avoid}\n'
    '.ship-list li+li{border-top:1px dashed #eee}\n'
    '@media(max-width:640px){.ship-list ul{columns:1}}\n'
    '</style>\n'
    '<h2 class="section-title">📦 212 項商品寄大陸完整清單</h2>\n'
    '<p style="color:#666;margin:8px 0 20px;text-align:center">點擊下方區塊展開查看「可寄 / 需確認 / 禁運」完整清單，每一項附寄送判定與注意事項。</p>\n'
    '<div class="ship-list">\n'
    + render_group("✅ 可寄商品", can, "can")
    + "\n"
    + render_group("⚠️ 需單獨確認商品", maybe, "maybe")
    + "\n"
    + render_group("❌ 禁運商品", cannot, "cannot")
    + "\n</div>\n</section>\n"
    '<!-- ship-list-static:end -->\n'
)

# 4. 插入到 cta-section 之前
anchor = '<div class="cta-section">'
if anchor not in html:
    raise SystemExit("cta-section anchor not found")
html = html.replace(anchor, block + anchor, 1)

open(PATH, "w", encoding="utf-8").write(html)
print(f"解析商品: {len(items)} (can={len(can)}, maybe={len(maybe)}, cannot={len(cannot)})")
print("可折叠清单已写入 can-i-ship.html")
