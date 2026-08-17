#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
重新生成 sitemap.xml：
1. 枚举所有真实 .html 页面（排除 404/验证/.bak/工具目录索引）
2. 以各页面 canonical URL 为唯一来源（保证 sitemap 与 canonical 一致）
3. 按层级分配 priority，lastmod 取文件 mtime
"""
import re
import pathlib
import datetime

BASE = pathlib.Path(__file__).resolve().parent.parent
SITEMAP = BASE / 'sitemap.xml'

EXCLUDE_SUBSTR = ('404.html', '.bak', 'google', 'apple-touch-icon', 'baidu')

def main():
    entries = []  # (url, lastmod, priority, changefreq)
    seen = set()

    for p in sorted(BASE.rglob('*.html')):
        rel = str(p.relative_to(BASE))
        if any(s in rel for s in EXCLUDE_SUBSTR):
            continue
        # 跳过目录索引页（tools/widget 的 index.html 不作为独立收录）
        if rel.endswith('tools/index.html') or rel.endswith('widget/index.html'):
            continue

        html = p.read_text(encoding='utf-8', errors='ignore')

        # 1) canonical 优先
        m = re.search(r'rel="canonical"\s+href="([^"]+)"', html)
        if m:
            url = m.group(1)
        else:
            # 2) 回退：从路径推导（去 .html，index 特殊）
            stem = rel[:-5] if rel.endswith('.html') else rel
            url = 'https://subao.tw/' + ('' if stem == 'index' else stem)

        if url in seen:
            continue
        seen.add(url)

        # 路径层级决定 priority
        depth = url.count('/') - 2  # 去掉 https:// 的 2 个斜杠
        if url == 'https://subao.tw/':
            priority = '1.0'
            changefreq = 'daily'
        elif url.startswith('https://subao.tw/blog/'):
            priority = '0.7'
            changefreq = 'weekly'
        else:
            priority = '0.8'
            changefreq = 'weekly'

        # lastmod 取文件 mtime
        mtime = datetime.datetime.fromtimestamp(p.stat().st_mtime)
        lastmod = mtime.strftime('%Y-%m-%d')

        entries.append((url, lastmod, changefreq, priority))

    # 生成 XML
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url, lastmod, changefreq, priority in entries:
        lines.append(f'  <url><loc>{url}</loc><lastmod>{lastmod}</lastmod>'
                     f'<changefreq>{changefreq}</changefreq><priority>{priority}</priority></url>')
    lines.append('</urlset>')
    SITEMAP.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'✅ sitemap.xml 已重新生成：{len(entries)} 个 URL')

if __name__ == '__main__':
    main()
