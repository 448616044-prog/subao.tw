#!/usr/bin/env python3
"""批量优化：中词title + 内链矩阵 + lastmod更新"""
import os, re

BASE = '/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn'
TODAY = '2026-07-31'
COUNT = 0

def update_dates(html):
    html = re.sub(r'<meta name="lastmod" content="[^"]*"', f'<meta name="lastmod" content="{TODAY}"', html)
    html = re.sub(r'"datePublished":\s*"[^"]*"', f'"datePublished": "{TODAY}"', html)
    html = re.sub(r'"dateModified":\s*"[^"]*"', f'"dateModified": "{TODAY}"', html)
    return html

def replace_title(html, old, new):
    if old in html:
        return html.replace(f'<title>{old}</title>', f'<title>{new}</title>')
    return html

# ── 1. index.html: 强化品牌+中词 ──
path = os.path.join(BASE, 'index.html')
with open(path) as f:
    html = f.read()

html = replace_title(html,
    '台灣寄大陸快遞首選｜NT$290起包稅最快5-7天 - 速豹集運',
    '台灣寄大陸快遞推薦2026｜NT$290/kg起敏感貨專線包稅雙清 | 速豹集運')

html = update_dates(html)

# Add internal link hub to pillar pages in the hero area
link_hub = '<p style="font-size:13px;margin-top:8px;color:#64748b">🔥 熱門：<a href="/tw-to-cn" style="color:#1a56db">台灣寄大陸專線</a> · <a href="/pricing" style="color:#1a56db">運費試算</a> · <a href="/express-comparison" style="color:#1a56db">���遞對比</a> · <a href="/sensitive-goods-shipping" style="color:#1a56db">敏感貨攻略</a></p>'
if '熱門：' not in html:
    html = html.replace('</h1>', f'</h1>\n{link_hub}', 1)

with open(path, 'w') as f:
    f.write(html)
COUNT += 1
print(f'✅ index.html')

# ── 2. express-comparison.html: 中词优化 ──
path = os.path.join(BASE, 'express-comparison.html')
with open(path) as f:
    html = f.read()

html = replace_title(html,
    '台灣寄大陸快遞推薦2026｜郵局vs順豐vs專線費用時效實測',
    '台灣寄大陸快遞怎麼選2026｜郵局vs順豐vs專線費用時效完整對比 | 速豹集運')

html = update_dates(html)
with open(path, 'w') as f:
    f.write(html)
COUNT += 1
print(f'✅ express-comparison.html')

# ── 3. sensitive-goods-shipping.html ──
path = os.path.join(BASE, 'sensitive-goods-shipping.html')
with open(path) as f:
    html = f.read()

html = replace_title(html,
    '台灣寄大陸敏感貨怎麼寄？食品/保��品/化妝品攻略',
    '台灣寄大陸敏感貨專線2026｜食品/保健品/化妝品/茶葉寄送攻略 | 速豹集運')

html = update_dates(html)
with open(path, 'w') as f:
    f.write(html)
COUNT += 1
print(f'✅ sensitive-goods-shipping.html')

# ── 4. faq.html ──
path = os.path.join(BASE, 'faq.html')
if os.path.exists(path):
    with open(path) as f:
        html = f.read()
    html = update_dates(html)
    with open(path, 'w') as f:
        f.write(html)
    COUNT += 1
    print(f'✅ faq.html')

# ── 5. 内链矩阵：top 10 blog pages 加回链到 pillar页 ──
pillar_links = '''
<div style="background:#f0f7ff;border-radius:8px;padding:12px 16px;margin:20px 0;font-size:14px">
  <strong>📦 台灣寄大陸快速入口：</strong>
  <a href="/tw-to-cn" style="color:#1a56db">專線首頁</a> ·
  <a href="/pricing" style="color:#1a56db">運費試算</a> ·
  <a href="/express-comparison" style="color:#1a56db">快遞對比</a> ·
  <a href="/faq" style="color:#1a56db">常見問題</a>
</div>
'''

# Pick 10 high-value blog pages
top_blogs = [
    'food-shipping-guide.html',
    'cosmetics-shipping.html',
    'health-products-shipping.html',
    'tea-shipping-guide.html',
    'noodles-ramen-shipping.html',
    'taiwan-souvenir-shipping.html',
    'tw-to-cn-shipping-guide.html',
    'clothing-shoes-shipping.html',
    '3c-electronics-shipping.html',
    'daigou-shipping.html',
]

blog_dir = os.path.join(BASE, 'blog')
linked = 0
for blog in top_blogs:
    path = os.path.join(blog_dir, blog)
    if not os.path.exists(path):
        continue
    with open(path) as f:
        html = f.read()
    if '快速入口' in html:
        continue
    # Insert before </article> or before first CTA
    if '</article>' in html:
        html = html.replace('</article>', f'{pillar_links}\n</article>', 1)
    elif '<footer' in html:
        html = html.replace('<footer', f'{pillar_links}\n<footer', 1)
    html = update_dates(html)
    with open(path, 'w') as f:
        f.write(html)
    linked += 1

print(f'✅ 内链矩阵: {linked}/10 blog pages 已加pillar回链')

# ── 6. bulk-shipping.html / economy-shipping.html / fast-shipping.html ──
for fname in ['bulk-shipping.html', 'economy-shipping.html', 'fast-shipping.html', 'shipping-checklist.html']:
    path = os.path.join(BASE, fname)
    if os.path.exists(path):
        with open(path) as f:
            html = f.read()
        html = update_dates(html)
        with open(path, 'w') as f:
            f.write(html)
        COUNT += 1  # already counted in title optimization

print(f'\n📊 总计优化: {COUNT}个页面 + {linked}个blog内链')
