#!/usr/bin/env python3
"""统一全站导航：精简为5项核心+dropdown，CSS统一"""
import os, re, shutil

BASE = '/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn'

# ===== 新的导航 HTML（精简版） =====
NEW_NAV = '''      <nav class="nav" id="desktopNav">
        <a href="/tw-to-cn" data-nav="tw-to-cn">台灣發大陸</a>
        <div class="nav-dropdown"><a href="/pricing" data-nav="pricing">運費<span class="dd-arrow">▾</span></a>
        <div class="dd-menu"><a href="/pricing">運費報價</a><a href="/pricing-calculator">運費試算</a></div></div>
        <a href="/can-i-ship" data-nav="can-i-ship">可以寄嗎</a>
        <a href="/article-list" data-nav="article-list">文章攻略</a>
        <div class="nav-dropdown"><a href="#more">更多<span class="dd-arrow">▾</span></a>
        <div class="dd-menu">
          <a href="/customs-guide">關稅速查</a>
          <a href="/volume-calculator">材積計算</a>
          <a href="/faq">常見問題</a>
          <a href="/partners">合作夥伴</a>
          <a href="/about">關於我們</a>
        </div></div>
      </nav>'''

NEW_MOBILE = '''  <div class="mobile-menu" id="mobileMenu">
    <a href="/tw-to-cn" class="mobile-nav-link" data-nav="tw-to-cn">台灣發大陸</a>
    <div class="m-dropdown">
      <span>運費</span>
      <div class="m-dropdown-links">
        <a href="/pricing">運費報價</a>
        <a href="/pricing-calculator">運費試算</a>
      </div>
    </div>
    <a href="/can-i-ship" class="mobile-nav-link" data-nav="can-i-ship">可以寄嗎</a>
    <a href="/article-list" class="mobile-nav-link" data-nav="article-list">文章攻略</a>
    <div class="m-dropdown">
      <span>更多</span>
      <div class="m-dropdown-links">
        <a href="/customs-guide">關稅速查</a>
        <a href="/volume-calculator">材積計算</a>
        <a href="/faq">常見問題</a>
        <a href="/partners">合作夥伴</a>
        <a href="/about">關於我們</a>
      </div>
    </div>
    <a href="https://line.me/ti/p/~subaotw5988" class="mobile-nav-link cta" target="_blank" onclick="gtag('event','line_click',{event_category:'conversion',event_label:'line_consult',value:1})">
      <i class="fab fa-line"></i> 加入LINE
    </a>
  </div>'''

# ===== 新的 header CSS =====
NEW_HEADER_CSS = '.header{position:fixed;top:0;left:0;right:0;height:70px;background:var(--bg-white);z-index:1000;transition:box-shadow .3s}.header.scrolled{box-shadow:var(--shadow)}.header .container{display:flex;align-items:center;justify-content:space-between;height:100%}.logo{font-size:24px;font-weight:700;color:var(--primary);flex-shrink:0}.logo img{background:#fff;max-height:50px;max-width:200px;width:auto;display:block}'

NEW_NAV_CSS = '.nav{display:flex;align-items:center;gap:24px}.nav a,.nav-dropdown>a{font-weight:500;color:var(--text-dark);transition:var(--transition);position:relative;font-size:14px;white-space:nowrap}.nav a::after{content:"";position:absolute;bottom:-4px;left:0;width:0;height:2px;background:var(--primary);transition:var(--transition)}.nav a:hover,.nav a.active{color:var(--primary)}.nav a:hover::after,.nav a.active::after{width:100%}'

NEW_DD_CSS = '.nav-dropdown{position:relative;display:flex;align-items:center}.dd-arrow{font-size:9px;margin-left:4px;display:inline-block}.dd-menu{display:none;position:absolute;top:100%;left:0;min-width:170px;background:#fff;border-radius:8px;box-shadow:0 8px 30px rgba(0,0,0,.12);padding:8px 0;z-index:100;margin-top:8px;border:1px solid #e8ecf0}.nav-dropdown:hover .dd-menu,.nav-dropdown:focus-within .dd-menu{display:block}.dd-menu a{display:block;padding:10px 16px;font-size:13px;color:var(--text-dark);transition:var(--transition)}.dd-menu a:hover{background:var(--primary-light);color:var(--primary)}'

NEW_CTA_CSS = '.header-cta{display:flex;align-items:center;gap:12px;flex-shrink:0}.btn-line{display:inline-flex;padding:10px 20px;background:var(--line-green);color:#fff;border-radius:8px;font-size:14px;font-weight:600;text-decoration:none;align-items:center;gap:6px;transition:var(--transition);white-space:nowrap}.btn-line:hover{background:#009900;transform:translateY(-1px);box-shadow:0 4px 12px rgba(0,185,0,.25)}.menu-toggle{display:none;background:none;border:none;font-size:22px;cursor:pointer;color:var(--text-dark);padding:4px}@media(max-width:992px){.nav,.header-cta{display:none}.menu-toggle{display:block}}'

NEW_MOBILE_CSS = '.mobile-menu{display:none;position:fixed;top:70px;left:0;right:0;bottom:0;background:#fff;padding:24px;overflow-y:auto;z-index:999;box-shadow:0 4px 12px rgba(0,0,0,.1)}.mobile-menu.active{display:block}.mobile-nav-link{display:block;padding:16px 0;font-size:16px;font-weight:500;color:var(--text-dark);border-bottom:1px solid #e0e0e0}.mobile-nav-link.active{color:var(--primary);font-weight:700}.mobile-nav-link.cta{margin-top:24px;padding:16px 24px;background:var(--primary);color:#fff;border-radius:8px;text-align:center;border:none}.m-dropdown>span{display:flex;justify-content:space-between;align-items:center;padding:16px 0;font-size:16px;font-weight:500;color:var(--text-dark);border-bottom:1px solid #e0e0e0;cursor:pointer}.m-dropdown>span::after{content:"▾";font-size:12px;transition:transform .2s}.m-dropdown.open>span::after{transform:rotate(180deg)}.m-dropdown-links{display:none;padding-left:16px}.m-dropdown.open .m-dropdown-links{display:block}.m-dropdown-links a{display:block;padding:12px 8px;font-size:14px;color:var(--text-dark);border-bottom:1px solid #f0f0f0}'

SCROLL_JS = '<script>window.addEventListener("scroll",function(){var h=document.getElementById("header");if(h)h.classList.toggle("scrolled",window.scrollY>10)})</script>'


def replace_block(text, start_pat, end_pat, replacement):
    """Replace content between start_pat and end_pat (inclusive)"""
    import re
    pattern = re.escape(start_pat) + r'.*?' + re.escape(end_pat)
    text, n = re.subn(pattern, replacement, text, flags=re.DOTALL)
    return text, n > 0


def fix_active_nav_class(html, page_path):
    """根据页面路径设置 active 导航标记"""
    # 识别当前页面对应的 nav key
    page_map = {
        '/tw-to-cn': 'tw-to-cn',
        '/pricing': 'pricing',
        '/pricing-calculator': 'pricing',  # 也标记 pricing
        '/can-i-ship': 'can-i-ship',
        '/article-list': 'article-list',
        '/customs-guide': 'customs-guide',
        '/volume-calculator': 'volume-calculator',
        '/faq': 'faq',
        '/partners': 'partners',
        '/about': 'about',
    }
    
    # Determine what page this is
    page_name = os.path.basename(page_path).replace('.html', '')
    if page_name == 'index':
        return html  # 首页没有 active
    
    # 查找匹配的 nav key
    nav_key = page_name
    if nav_key == 'pricing-calculator':
        nav_key = 'pricing'
    
    # 在桌面导航中标记 active
    html = html.replace(
        f'data-nav="{nav_key}"',
        f'data-nav="{nav_key}" class="active"'
    )
    
    # 在手机菜单中标记 active
    html = html.replace(
        f'class="mobile-nav-link" data-nav="{nav_key}"',
        f'class="mobile-nav-link active" data-nav="{nav_key}"'
    )
    
    return html


def process_file(filepath, is_blog):
    """处理单个文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    original = html
    
    # ===== 1. 替换导航 HTML =====
    html = re.sub(
        r'<nav class="nav" id="desktopNav">.*?</nav>',
        NEW_NAV,
        html,
        flags=re.DOTALL
    )
    
    # ===== 2. 替换手机菜单 =====
    html = re.sub(
        r'<div class="mobile-menu" id="mobileMenu">.*?</div>',
        NEW_MOBILE,
        html,
        flags=re.DOTALL
    )
    
    # ===== 3. 设置当前页面的 active 状态 =====
    html = fix_active_nav_class(html, filepath)
    
    # ===== 4. 替换 header CSS =====
    # Blog 模板：.header{position:fixed;top:0;left:0;right:0;height:70px;background:var(--bg-white);z-index:1000;box-shadow:var(--shadow)}
    old_header = r'\.header\{position:fixed;top:0;left:0;right:0;height:70px;background:var\(--bg-white\);z-index:1000;box-shadow:var\(--shadow\)\}'
    html = re.sub(old_header, NEW_HEADER_CSS, html)
    
    # Root 模板变体
    old_header2 = r'\.header\{position:fixed;top:0;left:0;right:0;height:var\(--header-height\);background:var\(--bg-white\);z-index:1000;transition:var\(--transition\);\}\.header\.scrolled\{box-shadow:var\(--shadow\);\}'
    new_header2 = '.header{position:fixed;top:0;left:0;right:0;height:70px;background:var(--bg-white);z-index:1000;transition:box-shadow .3s}.header.scrolled{box-shadow:var(--shadow)}'
    html = re.sub(old_header2, new_header2, html)
    
    # Root template: .header{position:fixed;top:0;left:0;right:0;height:var(--header-height);background:var(--bg-white);z-index:1000;transition:var(--transition);}
    old_header3 = r'\.header\{position:fixed;top:0;left:0;right:0;height:var\(--header-height\);background:var\(--bg-white\);z-index:1000;transition:var\(--transition\);\}'
    html = re.sub(old_header3, new_header2, html)
    
    # ===== 5. 替换 nav CSS =====
    # Blog: .nav{display:flex;gap:32px}
    html = re.sub(r'\.nav\{display:flex;gap:32px\}', '.nav{display:flex;align-items:center;gap:24px}', html)
    # Root: .nav{display:flex;align-items:center;gap:28px;}
    html = re.sub(r'\.nav\{display:flex;align-items:center;gap:28px;\}', '.nav{display:flex;align-items:center;gap:24px}', html)
    # Root minified
    html = re.sub(r'\.nav\{display:flex;align-items:center;gap:28px\}', '.nav{display:flex;align-items:center;gap:24px}', html)
    
    # ===== 6. 替换 nav a CSS（只对 blog 页面）=====
    if is_blog:
        html = re.sub(
            r'\.nav>a\{font-weight:500;color:var\(--text-dark\);font-size:15px;white-space:nowrap;position:relative\}',
            '.nav a,.nav-dropdown>a{font-weight:500;color:var(--text-dark);transition:var(--transition);position:relative;font-size:14px;white-space:nowrap}',
            html
        )
        # Also the ::after pseudo
        html = re.sub(
            r'\.nav>a::after\{content:"";position:absolute;bottom:-4px;left:0;width:0;height:2px;background:var\(--primary\);transition:var\(--transition\)\}',
            '',
            html
        )
        html = re.sub(
            r'\.nav>a:hover::after,\.nav>a\.active::after\{width:100%\}',
            '',
            html
        )
    
    # ===== 7. 替换 dropdown CSS 为 nav-dropdown CSS =====
    # Old dropdown CSS (blog template)
    html = re.sub(
        r'\.dropdown\{position:relative;display:flex;align-items:center\}',
        '.nav-dropdown{position:relative;display:flex;align-items:center}',
        html
    )
    html = re.sub(
        r'\.dropdown-menu\{display:none;position:absolute;top:100%;left:0;background:var\(--bg-white\);border-radius:var\(--radius\);box-shadow:var\(--shadow-lg\);min-width:160px;padding:8px 0;z-index:1001\}',
        '.dd-menu{display:none;position:absolute;top:100%;left:0;min-width:170px;background:#fff;border-radius:8px;box-shadow:0 8px 30px rgba(0,0,0,.12);padding:8px 0;z-index:100;margin-top:8px;border:1px solid #e8ecf0}',
        html
    )
    html = re.sub(
        r'\.dropdown:hover \.dropdown-menu\{display:block\}',
        '.nav-dropdown:hover .dd-menu,.nav-dropdown:focus-within .dd-menu{display:block}',
        html
    )
    html = re.sub(
        r'\.dropdown-menu a\{display:block;padding:10px 20px;font-size:14px;white-space:nowrap;transition:var\(--transition\)\}',
        '.dd-menu a{display:block;padding:10px 16px;font-size:13px;color:var(--text-dark);transition:var(--transition)}',
        html
    )
    html = re.sub(
        r'\.dropdown-menu a:hover\{background:var\(--primary-light\);color:var\(--primary\)\}',
        '.dd-menu a:hover{background:var(--primary-light);color:var(--primary)}',
        html
    )
    
    # Handle old HTML class names: <div class="dropdown"> -> <div class="nav-dropdown">
    # and <div class="dropdown-menu"> -> <div class="dd-menu">
    html = html.replace('class="dropdown"', 'class="nav-dropdown"')
    html = html.replace('class="dropdown-menu"', 'class="dd-menu"')
    
    # ===== 8. 替换 mobile CSS =====
    # Old mobile CSS (blog)
    html = re.sub(
        r'\.mobile-menu\{display:none;position:fixed;top:68px;left:0;right:0;bottom:0;background:#fff;padding:16px 24px;overflow-y:auto;z-index:999\}',
        '.mobile-menu{display:none;position:fixed;top:70px;left:0;right:0;bottom:0;background:#fff;padding:24px;overflow-y:auto;z-index:999;box-shadow:0 4px 12px rgba(0,0,0,.1)}',
        html
    )
    html = re.sub(
        r'\.mobile-menu\.active\{display:block\}',
        '.mobile-menu.active{display:block}',
        html
    )
    # Blog mobile nav link
    html = re.sub(
        r'\.mobile-nav-link\{display:block;padding:14px 8px;font-size:15px;font-weight:500;color:var\(--text-dark\);text-decoration:none;border-bottom:1px solid #f0f0f0\}',
        '.mobile-nav-link{display:block;padding:16px 0;font-size:16px;font-weight:500;color:var(--text-dark);border-bottom:1px solid #e0e0e0}',
        html
    )
    html = re.sub(
        r'\.mobile-nav-link\.active\{color:var\(--primary\);font-weight:700\}',
        '.mobile-nav-link.active{color:var(--primary);font-weight:700}',
        html
    )
    html = re.sub(
        r'\.mobile-nav-link\.cta\{margin-top:16px;padding:14px;background:var\(--primary\);color:#fff;border-radius:8px;text-align:center;border:none;display:block\}',
        '.mobile-nav-link.cta{margin-top:24px;padding:16px 24px;background:var(--primary);color:#fff;border-radius:8px;text-align:center;border:none}',
        html
    )
    # Blog m-dropdown
    html = re.sub(
        r'\.m-dropdown>span\{display:flex;justify-content:space-between;align-items:center;padding:14px 8px;font-size:15px;font-weight:500;color:var\(--text-dark\);border-bottom:1px solid #f0f0f0;cursor:pointer\}',
        '.m-dropdown>span{display:flex;justify-content:space-between;align-items:center;padding:16px 0;font-size:16px;font-weight:500;color:var(--text-dark);border-bottom:1px solid #e0e0e0;cursor:pointer}',
        html
    )
    html = re.sub(
        r'\.m-dropdown-links\{display:none;padding-left:16px\}',
        '.m-dropdown-links{display:none;padding-left:16px}',
        html
    )
    html = re.sub(
        r'\.m-dropdown\.open \.m-dropdown-links\{display:block\}',
        '.m-dropdown.open .m-dropdown-links{display:block}',
        html
    )
    html = re.sub(
        r'\.m-dropdown-links a\{display:block;padding:10px 8px;font-size:14px;color:var\(--text-dark\);text-decoration:none;border-bottom:1px solid #f0f0f0\}',
        '.m-dropdown-links a{display:block;padding:12px 8px;font-size:14px;color:var(--text-dark);border-bottom:1px solid #f0f0f0}',
        html
    )
    
    # Root m-dropdown variants
    html = re.sub(
        r'\.m-dropdown>span\{display:flex;justify-content:space-between;align-items:center;padding:16px 0;font-size:16px;font-weight:500;color:var\(--text-dark\);border-bottom:1px solid var\(--border\);cursor:pointer\}',
        '.m-dropdown>span{display:flex;justify-content:space-between;align-items:center;padding:16px 0;font-size:16px;font-weight:500;color:var(--text-dark);border-bottom:1px solid #e0e0e0;cursor:pointer}',
        html
    )
    
    # ===== 9. 确保有 scroll JS（处理 blog 页面） =====
    if is_blog and 'window.addEventListener("scroll"' not in html:
        # 在 </body> 之前插入
        html = html.replace('</body>', '<script>window.addEventListener("scroll",function(){var h=document.getElementById("header");if(h)h.classList.toggle("scrolled",window.scrollY>10)})</script>\n</body>')
    
    # ===== 10. Clean up: 移除重复或孤立的 CSS 规则 =====
    # 移除孤立的 .nav>a:hover::after 规则
    html = re.sub(r'\n\s*\.nav>a:hover::after,\.nav>a\.active::after\{width:100%\}', '', html)
    
    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return True
    return False


def main():
    pages = []
    # Blog pages
    blog_dir = os.path.join(BASE, 'blog')
    for f in os.listdir(blog_dir):
        if f.endswith('.html'):
            pages.append((os.path.join(blog_dir, f), True))
    
    # Root pages (skip 404, google verification)
    skip = {'404.html', 'google3f7a9c2e4de8c3b1.html', 'index.html'}
    for f in os.listdir(BASE):
        if f.endswith('.html') and f not in skip:
            pages.append((os.path.join(BASE, f), False))
    
    updated = 0
    for path, is_blog in pages:
        try:
            if process_file(path, is_blog):
                label = 'blog/' if is_blog else ''
                print(f'  ✅ {label}{os.path.basename(path)}')
                updated += 1
        except Exception as e:
            label = 'blog/' if is_blog else ''
            print(f'  ❌ {label}{os.path.basename(path)}: {e}')
    
    print(f'\n📊 {updated}/{len(pages)} 页面已更新（不含 index.html）')
    print('⚠️  index.html 需手动处理')


if __name__ == '__main__':
    main()
