#!/usr/bin/env python3
"""Deploy dropdown nav to all subao.tw pages."""
import re, os

SITE_DIR = "/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn"

# New CSS to inject
DROPDOWN_CSS = '''
    /* Dropdown nav */
    .dropdown{position:relative}
    .dropdown>a::after{content:"▾";font-size:10px;margin-left:5px}
    .dropdown-menu{display:none;position:absolute;top:100%;left:0;min-width:180px;background:#fff;border-radius:8px;box-shadow:0 8px 30px rgba(0,0,0,0.12);padding:8px 0;z-index:100;margin-top:4px;border:1px solid #e8ecf0}
    .dropdown:hover .dropdown-menu,.dropdown:focus-within .dropdown-menu{display:block}
    .dropdown-menu a{display:block;padding:10px 16px;font-size:14px;color:var(--text-dark);text-decoration:none;transition:var(--transition)}
    .dropdown-menu a:hover{background:var(--primary-light);color:var(--primary)}
    .dropdown-menu a.active{background:var(--primary-light);color:var(--primary);font-weight:600}
    .header .container{gap:0}'''

# Desktop nav builder
def desktop_nav(active):
    items = [
        ("/tw-to-cn", "台灣發大陸"),
        ("/customs-guide", "關稅速查"),
        ("/article-list", "文章攻略"),
        ("/faq", "常見問題"),
        ("/partners", "合作夥伴"),
        ("/about", "關於我們"),
    ]
    lines = []
    for href, label in items:
        cls = ' class="active"' if href == active else ""
        lines.append(f'<a href="{href}"{cls}>{label}</a>')

    # Check if pricing or pricing-calculator is active for dropdown
    dropdown_active = ' class="active"' if active in ('/pricing','/pricing-calculator') else ''
    pa_cls = ' class="active"' if active == '/pricing' else ''
    pc_cls = ' class="active"' if active == '/pricing-calculator' else ''

    dropdown_html = f'''<div class="dropdown"><a href="/pricing"{dropdown_active}>運費</a>
      <div class="dropdown-menu"><a href="/pricing"{pa_cls}>💰 運費報價</a><a href="/pricing-calculator"{pc_cls}>🧮 運費試算</a></div></div>'''

    # Insert dropdown after 台灣發大陸
    lines.insert(1, dropdown_html)
    return '\n        '.join(lines)

# Mobile menu builder
def mobile_menu(active):
    items_main = [
        ("/tw-to-cn", "台灣發大陸"),
        ("/customs-guide", "關稅速查"),
        ("/article-list", "文章攻略"),
        ("/faq", "常見問題"),
        ("/partners", "合作夥伴"),
        ("/about", "關於我們"),
    ]
    lines = ['  <div class="mobile-menu" id="mobileMenu">']
    for href, label in items_main:
        cls = ' class="mobile-nav-link active"' if href == active else ' class="mobile-nav-link"'
        lines.append(f'    <a href="{href}"{cls}>{label}</a>')
    
    # Pricing dropdown in mobile
    pa_cls = ' class="active"' if active == '/pricing' else ''
    pc_cls = ' class="active"' if active == '/pricing-calculator' else ''
    dd_active = ' active' if active in ('/pricing','/pricing-calculator') else ''
    
    lines.append(f'    <div class="m-dropdown{dd_active}">')
    lines.append(f'      <span>運費</span>')
    lines.append(f'      <div class="m-dropdown-links">')
    lines.append(f'        <a href="/pricing"{pa_cls}>運費報價</a>')
    lines.append(f'        <a href="/pricing-calculator"{pc_cls}>運費試算</a>')
    lines.append(f'      </div>')
    lines.append(f'    </div>')

    lines.append('    <a href="https://line.me/ti/p/~subaotw5988" class="mobile-nav-link cta" target="_blank" onclick="gtag(\'event\',\'line_click\',{event_category:\'conversion\',event_label:\'line_consult\',value:1})">')
    lines.append('      <i class="fab fa-line"></i> 加入LINE')
    lines.append('    </a>')
    lines.append('  </div>')
    return '\n'.join(lines)

# Header CTA button
HEADER_CTA = '''      <div class="header-cta">
        <a href="https://line.me/ti/p/~subaotw5988" class="btn-line" target="_blank" onclick="gtag('event','line_click',{event_category:'conversion',event_label:'line_consult',value:1})">
          <i class="fab fa-line"></i> LINE 咨詢
        </a>
      </div>'''

MENU_TOGGLE = '      <button class="menu-toggle" id="menuToggle"><i class="fas fa-bars"></i></button>'

# New header nav logic CSS
NAV_CSS_UPDATE = {
    '.nav a{font-weight:500;color:var(--text-dark);transition:var(--transition);position:relative}':
    '.nav>a{display:flex;align-items:center;padding:8px 14px;font-size:14.5px;font-weight:500;color:var(--text-dark);text-decoration:none;border-radius:6px;transition:var(--transition);white-space:nowrap}',
    '.nav a:hover,.nav a.active{color:var(--primary)}':
    '.nav>a:hover,.nav .dropdown:hover>a{background:var(--primary-light);color:var(--primary)}',
    '.nav a::after{content:\'\';position:absolute;bottom:-4px;left:0;width:0;height:2px;background:var(--primary);transition:var(--transition)}':
    '',
    '.nav a:hover::after,.nav a.active::after{width:100%}':
    '',
}

def fix_page(filepath, active_slug):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changes = []

    # 1. Replace the entire <header>...</header> section
    # Find the header block - from <header to the menu-toggle button line
    header_start = content.find('<header class="header"')
    if header_start == -1:
        header_start = content.find('<header class="site-header"')
    if header_start == -1:
        return ['no header found']

    # Find where header ends - look for </header>
    header_end = content.find('</header>', header_start)
    if header_end == -1:
        return ['no header end found']

    # Build new header
    dnav = desktop_nav(active_slug)
    new_header = f'''<header class="header" id="header">
    <div class="container">
      <a href="/" class="logo"><img src="images/subao-logo-new.png" alt="速豹集運" height="40"></a>
      <nav class="nav" id="desktopNav">
        {dnav}
      </nav>
{HEADER_CTA}
{MENU_TOGGLE}
    </div>
  </header>'''

    content = content[:header_start] + new_header + content[header_end + 9:]
    changes.append('header')

    # 2. Update nav link CSS styles
    for old, new in NAV_CSS_UPDATE.items():
        if old in content:
            if new:
                content = content.replace(old, new)
            else:
                # Remove the line
                content = content.replace(old + '\n', '')
            changes.append('nav-css')

    # 3. Add dropdown CSS before the @media section in the style block
    if '.dropdown' not in content:
        # Find the @media rule in style
        media_pos = content.find('    @media')
        if media_pos == -1:
            # Insert before </style>
            style_end = content.find('  </style>')
            if style_end > 0:
                content = content[:style_end] + DROPDOWN_CSS + '\n' + content[style_end:]
        else:
            content = content[:media_pos] + DROPDOWN_CSS + '\n' + content[media_pos:]
        changes.append('dropdown-css')

    # 4. Remove old header-btn CSS (we use header-cta now)
    if '.header-btn{' in content:
        # Replace .header-btn styles but keep them working
        content = content.replace('.header-btn{', '.header-cta{')

    # 5. Update mobile menu
    # Replace existing mobile-menu div
    mm_pattern = r'<div class="mobile-menu"[^>]*>.*?</div>\s*(?=<a href="https://line\.me)'
    mm_pattern2 = r'<div class="mobile-menu"[^>]*>.*?</div>'
    new_mm = mobile_menu(active_slug)

    # Add mobile menu CSS if not present
    if '.mobile-menu' not in content or 'mobile-menu{display:none' not in content:
        mobile_css = '''
    .mobile-menu{display:none;position:fixed;top:68px;left:0;right:0;bottom:0;background:#fff;padding:16px 24px;overflow-y:auto;z-index:999}
    .mobile-menu.active{display:block}
    .mobile-nav-link{display:block;padding:14px 8px;font-size:15px;font-weight:500;color:var(--text-dark);text-decoration:none;border-bottom:1px solid #f0f0f0}
    .mobile-nav-link.active{color:var(--primary);font-weight:700}
    .mobile-nav-link.cta{margin-top:16px;padding:14px;background:var(--primary);color:#fff;border-radius:8px;text-align:center;border:none;display:block}
    .m-dropdown>span{display:flex;justify-content:space-between;align-items:center;padding:14px 8px;font-size:15px;font-weight:500;color:var(--text-dark);border-bottom:1px solid #f0f0f0;cursor:pointer}
    .m-dropdown>span::after{content:"▾";font-size:12px;transition:transform .2s}
    .m-dropdown.open>span::after{transform:rotate(180deg)}
    .m-dropdown-links{display:none;padding-left:16px}
    .m-dropdown.open .m-dropdown-links{display:block}
    .m-dropdown-links a{display:block;padding:10px 8px;font-size:14px;color:var(--text-dark);text-decoration:none;border-bottom:1px solid #f0f0f0}
    .btn-line{display:inline-flex;padding:10px 20px;background:var(--line-green);color:#fff;border-radius:6px;font-size:14px;font-weight:600;text-decoration:none;align-items:center;gap:6px;transition:var(--transition);white-space:nowrap}
    .btn-line:hover{background:#009900;transform:translateY(-1px);box-shadow:0 4px 12px rgba(0,185,0,0.25)}
    .header-cta{display:flex;align-items:center;gap:12px}
    .menu-toggle{display:none;background:none;border:none;font-size:22px;cursor:pointer;color:var(--text-dark);padding:4px}'''
        
        # Insert before @media
        media_pos2 = content.find('    @media')
        if media_pos2 > 0:
            content = content[:media_pos2] + mobile_css + '\n' + content[media_pos2:]
            changes.append('mobile-css')

    # Replace mobile menu
    content, count = re.subn(mm_pattern, new_mm + '\n', content, count=1, flags=re.DOTALL)
    if count == 0:
        content, count = re.subn(mm_pattern2, new_mm, content, count=1, flags=re.DOTALL)
    if count > 0:
        changes.append('mobile-menu')

    # 6. Update JS - add mobile dropdown toggle
    if 'm-dropdown' in content and "querySelectorAll('.m-dropdown>span')" not in content:
        js_code = '''
    document.querySelectorAll('.m-dropdown>span').forEach(function(s){s.addEventListener('click',function(e){e.stopPropagation();this.parentElement.classList.toggle('open')})});'''
        
        # Insert before window.scroll or before </script> near </body>
        scroll_pos = content.rfind("window.addEventListener('scroll'")
        if scroll_pos > 0:
            line_start = content.rfind('\n', 0, scroll_pos) + 1
            content = content[:line_start] + js_code + '\n' + content[line_start:]
        else:
            content = content.replace('</body>', js_code + '\n</body>')
        changes.append('js-dropdown')

    # 7. Fix old header-btn class references in HTML/JS if any
    if '.header-btn' in content:
        content = content.replace('.header-btn', '.header-cta')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return changes

# Pages to fix
pages = {}
for root, dirs, files in os.walk(SITE_DIR):
    for f in files:
        if f.endswith('.html'):
            rel = os.path.relpath(os.path.join(root, f), SITE_DIR)
            slug = ''
            if rel == 'index.html': slug = ''
            elif rel == 'tw-to-cn.html': slug = '/tw-to-cn'
            elif rel == 'pricing.html': slug = '/pricing'
            elif rel == 'pricing-calculator.html': slug = '/pricing-calculator'
            elif rel == 'customs-guide.html': slug = '/customs-guide'
            elif rel == 'article-list.html': slug = '/article-list'
            elif rel == 'faq.html': slug = '/faq'
            elif rel == 'partners.html': slug = '/partners'
            elif rel == 'about.html': slug = '/about'
            elif rel == 'line.html': slug = '/line'
            elif rel == 'warehouse.html': slug = '/warehouse'
            elif rel == 'contact-form.html': slug = '/contact-form'
            pages[rel] = slug

print(f"Processing {len(pages)} pages...")
success = 0
errors = 0
for rel, slug in pages.items():
    fp = os.path.join(SITE_DIR, rel)
    try:
        changes = fix_page(fp, slug)
        if changes and 'no header' not in changes[0]:
            print(f"  ✅ {rel}: {' + '.join(changes)}")
            success += 1
        else:
            print(f"  ⚠️  {rel}: {changes[0]}")
            errors += 1
    except Exception as e:
        print(f"  ❌ {rel}: {e}")
        errors += 1

print(f"\nDone! {success} fixed, {errors} skipped.")
