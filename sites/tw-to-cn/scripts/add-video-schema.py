#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为嵌入 YouTube 视频的页面自动生成 VideoObject 结构化数据。
从 iframe 的 title 属性提取视频标题，拼出合法的 VideoObject JSON-LD。
"""
import re
import sys
import pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent

# 需要处理的目标页面（相对 BASE）
TARGETS = [
    "tw-to-cn.html",
    "about.html",
    "warehouse.html",
    "bulk-shipping.html",
    "daigou-service.html",
    "pickup-service.html",
]

IFRAME_RE = re.compile(
    r'<iframe[^>]*src="https://www\.youtube(?:-nocookie)?\.com/embed/([A-Za-z0-9_-]+)"[^>]*title="([^"]*)"[^>]*>'
)

def build_videoobject(vid, title, page_title):
    return {
        "@context": "https://schema.org",
        "@type": "VideoObject",
        "name": title,
        "description": f"{page_title}｜{title}｜速豹集運倉庫實拍",
        "thumbnailUrl": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",
        "contentUrl": f"https://www.youtube.com/watch?v={vid}",
        "embedUrl": f"https://www.youtube.com/embed/{vid}",
        "uploadDate": "2026-05-01",
    }

def main():
    import json
    total = 0
    for rel in TARGETS:
        p = BASE / rel
        if not p.exists():
            print(f"[跳过] {rel} 不存在")
            continue
        html = p.read_text(encoding="utf-8")
        # 已有 VideoObject 则跳过
        if '"@type":"VideoObject"' in html or '"@type": "VideoObject"' in html:
            print(f"[跳过] {rel} 已含 VideoObject")
            continue
        m_title = re.search(r'<title>([^<]*)</title>', html)
        page_title = m_title.group(1).split('|')[0].strip() if m_title else rel
        seen = set()
        blocks = []
        for m in IFRAME_RE.finditer(html):
            vid, title = m.group(1), m.group(2)
            if vid in seen:
                continue
            seen.add(vid)
            blocks.append(build_videoobject(vid, title, page_title))
        if not blocks:
            print(f"[跳过] {rel} 无带 title 的 YouTube iframe")
            continue
        # 生成 JSON-LD 脚本
        scripts = ""
        for b in blocks:
            scripts += '<script type="application/ld+json">' + json.dumps(b, ensure_ascii=False) + '</script>\n'
        # 插入到 </head> 前
        if '</head>' in html:
            html = html.replace('</head>', scripts + '</head>', 1)
        else:
            html = scripts + html
        p.write_text(html, encoding="utf-8")
        total += len(blocks)
        print(f"✅ {rel}: 插入 {len(blocks)} 个 VideoObject")
    print(f"\n共插入 {total} 个 VideoObject")

if __name__ == "__main__":
    main()
