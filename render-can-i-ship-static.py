#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把 can-i-ship.html 的 JS 数据 DB（212 商品）静态渲染成 HTML 清单，
插入 cta-section 之前，供搜索引擎抓取「XX可以寄大陸嗎」的答案。
"""
import re

PATH = "sites/tw-to-cn/can-i-ship.html"
html = open(PATH, encoding="utf-8").read()

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

def render_group(title, group, color):
    lis = []
    for it in group:
        icon = STATUS_ICON[it["status"]]
        note = it["note"] if it["note"] else ""
        lis.append(f'<li><strong>{it["id"]}</strong> {icon}{STATUS_LABEL[it["status"]]} — {note}</li>')
    body = "\n".join(lis)
    return (
        f'<h3 style="margin:20px 0 8px;color:{color};font-size:18px">{title}（{len(group)} 項）</h3>\n'
        f'<ul style="margin:0;padding-left:20px;color:#555;line-height:1.7;font-size:14px">\n{body}\n</ul>'
    )

block = (
    '<section class="container" style="padding:32px 20px;max-width:900px;margin:0 auto">\n'
    '<h2 class="section-title">📦 212 項商品寄大陸完整清單（靜態版，供查詢與搜尋）</h2>\n'
    '<p style="color:#666;margin:8px 0 20px">以下為速豹集運整理的完整商品清單，依「可寄 / 需確認 / 禁運」三類呈現。'
    '每一項都附上寄送判定與注意事項，可直接搜尋或對照上方查詢工具使用。</p>\n'
    + render_group("✅ 可寄商品", can, "#16A34A")
    + "\n"
    + render_group("⚠️ 需單獨確認商品", maybe, "#D97706")
    + "\n"
    + render_group("❌ 禁運商品", cannot, "#DC2626")
    + "\n</section>\n"
)

# 4. 插入到 cta-section 之前
anchor = '<div class="cta-section">'
if anchor not in html:
    raise SystemExit("cta-section anchor not found")
html = html.replace(anchor, block + anchor, 1)

open(PATH, "w", encoding="utf-8").write(html)
print(f"解析商品: {len(items)} (can={len(can)}, maybe={len(maybe)}, cannot={len(cannot)})")
print("静态清单已插入 can-i-ship.html")
