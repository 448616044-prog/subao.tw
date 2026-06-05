#!/usr/bin/env python3
"""Add mobile menu to main pages that don't have it."""
import re, os

SITE_DIR = "/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn"

MOBILE_CSS = '''
    .menu-toggle{display:none;background:none;border:none;font-size:24px;cursor:pointer;color:var(--text-dark)}
    .mobile-menu{display:none;position:fixed;top:70px;left:0;right:0;bottom:0;background:var(--bg-white);padding:24px;overflow-y:auto;z-index:999;box-shadow:0 4px 12px rgba(0,0,0,0.1)}
    .mobile-menu.active{display:block}
    .mobile-nav-link{display:block;padding:16px 0;font-size:16px;font-weight:500;color:var(--text-dark);border-bottom:1px solid var(--border)}
    .mobile-nav-link.active{color:var(--primary);font-weight:700}
    .mobile-nav-link.cta{margin-top:24px;padding:16px 24px;background:var(--primary);color:#fff;border-radius:var(--radius);text-align:center;border:none}'''

def mobile_menu_html(active_slug):
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

MENU_TOGGLE = '      <button class="menu-toggle" id="menuToggle"><i class="fas fa-bars"></i></button>'

MOBILE_JS = '''
    /* mobile menu */
    var menuToggle = document.getElementById('menuToggle');
    var mobileMenu = document.getElementById('mobileMenu');
    if(menuToggle && mobileMenu){
      menuToggle.addEventListener('click',function(){
        mobileMenu.classList.toggle('active');
        var icon = menuToggle.querySelector('i');
        icon.classList.toggle('fa-bars');
        icon.classList.toggle('fa-times');
      });
      mobileMenu.querySelectorAll('.mobile-nav-link').forEach(function(link){
        link.addEventListener('click',function(){mobileMenu.classList.remove('active');menuToggle.querySelector('i').classList.remove('fa-times');menuToggle.querySelector('i').classList.add('fa-bars')});
      });
    }'''

PAGES = {
    'pricing.html': '/pricing',
    'about.html': '/about',
    'faq.html': '/faq',
    'pricing-calculator.html': '/pricing-calculator',
    'article-list.html': '/article-list',
}

for filename, active in PAGES.items():
    filepath = os.path.join(SITE_DIR, filename)
    if not os.path.exists(filepath):
        print(f"  ⚠️  {filename}: not found")
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has mobile menu
    if 'mobile-menu' in content:
        print(f"  ⏭️  {filename}: already has mobile menu")
        continue

    # 1. Add .menu-toggle CSS class after existing CSS
    if '.menu-toggle' not in content:
        # Insert after the @media section or before </style>
        if '@media' in content:
            # Insert mobile CSS before @media
            content = content.replace('    @media', MOBILE_CSS + '\n    @media')
        else:
            content = content.replace('  </style>', MOBILE_CSS + '\n  </style>')

    # 2. Add menu-toggle button before </header> or </div> in header
    # Look for the line with the LINE button in header and add menu-toggle after it
    header_btn_match = re.search(r'(<a href="https://line\.me/ti/p/~subaotw5988"[^>]*>.*?</a>)\s*(</div>\s*</header>)', content)
    if not header_btn_match:
        # Try other patterns
        header_btn_match = re.search(r'(</div>)\s*(</header>)', content)
    
    if header_btn_match:
        insert_pos = header_btn_match.start(1) + len(header_btn_match.group(1))
        content = content[:insert_pos] + '\n' + MENU_TOGGLE + content[insert_pos:]

    # 3. Add mobile-menu div after </header>
    mm_html = mobile_menu_html(active)
    content = content.replace('</header>', '</header>\n\n' + mm_html)

    # 4. Add mobile JS before the existing scroll listener or before </body>
    if 'menuToggle' not in content:
        # Find the scroll listener and insert before it, or add before </body>
        scroll_match = re.search(r'window\.addEventListener\(\'scroll\'', content)
        if scroll_match:
            pos = scroll_match.start()
            # Find the line start
            line_start = content.rfind('\n', 0, pos) + 1
            content = content[:line_start] + MOBILE_JS + '\n' + content[line_start:]
        else:
            # Insert before </body>
            content = content.replace('</body>', MOBILE_JS + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✅ {filename}: mobile menu added")

print("\nDone!")
