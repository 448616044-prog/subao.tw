#!/usr/bin/env python3
"""Unify navigation bar across all subao.tw pages."""
import re, os, sys

SITE_DIR = "/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn"

# Standard desktop nav template
def desktop_nav(active_slug):
    items = [
        ("/tw-to-cn", "台灣發大陸"),
        ("/pricing", "運費報價"),
        ("/pricing-calculator", "運費試算"),
        ("/customs-guide", "關稅速查"),
        ("/article-list", "文章攻略"),
        ("/faq", "常見問題"),
        ("/line", "LINE 聯繫"),
        ("/partners", "合作夥伴"),
        ("/about", "關於我們"),
    ]
    lines = ['      <nav class="nav" id="desktopNav">']
    for href, label in items:
        cls = ' class="active"' if href == active_slug else ""
        lines.append(f'        <a href="{href}"{cls}>{label}</a>')
    lines.append('      </nav>')
    return '\n'.join(lines)

# Standard mobile menu template
def mobile_menu(active_slug):
    items = [
        ("/tw-to-cn", "台灣發大陸"),
        ("/pricing", "運費報價"),
        ("/pricing-calculator", "運費試算"),
        ("/customs-guide", "關稅速查"),
        ("/article-list", "文章攻略"),
        ("/faq", "常見問題"),
        ("/partners", "合作夥伴"),
        ("/about", "關於我們"),
    ]
    lines = ['  <div class="mobile-menu" id="mobileMenu">']
    for href, label in items:
        cls = ' class="mobile-nav-link active"' if href == active_slug else ' class="mobile-nav-link"'
        lines.append(f'    <a href="{href}"{cls}>{label}</a>')
    lines.append('    <a href="https://line.me/ti/p/~subaotw5988" class="mobile-nav-link cta" target="_blank" onclick="gtag(\'event\',\'line_click\',{event_category:\'conversion\',event_label:\'line_consult\',value:1})">')
    lines.append('      <i class="fab fa-line"></i> 加入LINE')
    lines.append('    </a>')
    lines.append('  </div>')
    return '\n'.join(lines)

# Standard footer "服務項目" section
def footer_section():
    return '''        <div class="footer-section">
          <h3>服務項目</h3>
          <a href="/tw-to-cn">台灣發大陸</a>
          <a href="/pricing">運費報價</a>
          <a href="/pricing-calculator">運費試算</a>
          <a href="/customs-guide">關稅速查</a>
          <a href="/article-list">寄件攻略</a>
          <a href="/faq">常見問題</a>
          <a href="/partners">合作夥伴</a>
        </div>'''

def fix_file(filepath, active_slug):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace desktop nav
    nav_pattern = r'<nav class="nav"[^>]*>.*?</nav>'
    new_nav = desktop_nav(active_slug)
    content, count1 = re.subn(nav_pattern, new_nav, content, count=1, flags=re.DOTALL)

    # Replace mobile menu if it exists  
    mobile_pattern = r'<div class="mobile-menu"[^>]*>.*?</div>\s*(?=<a href="https://line\.me/ti/p/)'
    mobile_pattern2 = r'<div class="mobile-menu"[^>]*>.*?</div>'
    new_mobile = mobile_menu(active_slug)
    
    # Try matching mobile menu followed by LINE link first
    content, count2 = re.subn(mobile_pattern, new_mobile + '\n', content, count=1, flags=re.DOTALL)
    if count2 == 0:
        # Try just replacing the mobile menu div
        content, count2 = re.subn(mobile_pattern2, new_mobile, content, count=1, flags=re.DOTALL)

    # Replace footer 服務項目 section (only if it exists and doesn't already have all items)
    footer_pattern = r'<div class="footer-section">\s*<h3>服務項目</h3>.*?</div>'
    if re.search(footer_pattern, content, re.DOTALL):
        existing_footer = re.search(footer_pattern, content, re.DOTALL).group()
        if 'customs-guide' not in existing_footer or 'partners' not in existing_footer:
            new_footer = footer_section()
            content = re.sub(footer_pattern, new_footer, content, count=1, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    changes = []
    if count1 > 0: changes.append('desktop nav')
    if count2 > 0: changes.append('mobile menu')
    return changes

# Pages to fix with their active slugs
PAGES = {
    'pricing.html': '/pricing',
    'about.html': '/about',
    'faq.html': '/faq',
    'pricing-calculator.html': '/pricing-calculator',
    'article-list.html': '/article-list',
    'line.html': '/line',
    'warehouse.html': '/warehouse',
    'contact-form.html': '/contact-form',
}

# Also fix blog pages (active = none of the above, no active class)
blog_dir = os.path.join(SITE_DIR, 'blog')
for f in os.listdir(blog_dir):
    if f.endswith('.html'):
        PAGES[f'blog/{f}'] = ''

print(f"Fixing {len(PAGES)} pages...")
for filename, active in PAGES.items():
    filepath = os.path.join(SITE_DIR, filename)
    if not os.path.exists(filepath):
        print(f"  ⚠️  {filename}: not found")
        continue
    try:
        changes = fix_file(filepath, active)
        status = ' + '.join(changes) if changes else 'no changes needed'
        print(f"  ✅ {filename}: {status}")
    except Exception as e:
        print(f"  ❌ {filename}: {e}")

print("\nDone!")
