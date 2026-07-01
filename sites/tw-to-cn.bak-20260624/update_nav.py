#!/usr/bin/env python3
"""统一全站导航样式 + 精简导航项"""
import re, os

BASE = '/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn'

# ===== 新的桌面导航 HTML =====
NEW_NAV = '''      <nav class="nav" id="desktopNav">
        <a href="/tw-to-cn">台灣發大陸</a>
        <div class="nav-dropdown"><a href="/pricing">運費<span class="dd-arrow">▾</span></a>
        <div class="dd-menu"><a href="/pricing">運費報價</a><a href="/pricing-calculator">運費試算</a></div></div>
        <a href="/can-i-ship">可以寄嗎</a>
        <a href="/article-list">文章攻略</a>
        <div class="nav-dropdown"><a href="#more">更多<span class="dd-arrow">▾</span></a>
        <div class="dd-menu">
          <a href="/customs-guide">關稅速查</a>
          <a href="/volume-calculator">材積計算</a>
          <a href="/faq">常見問題</a>
          <a href="/partners">合作夥伴</a>
          <a href="/about">關於我們</a>
        </div></div>
      </nav>'''

# ===== 新的手机菜单 HTML（blog 页面）=====
NEW_MOBILE_MENU_BLOG = '''  <div class="mobile-menu" id="mobileMenu">
    <a href="/tw-to-cn" class="mobile-nav-link">台灣發大陸</a>
    <div class="m-dropdown">
      <span>運費</span>
      <div class="m-dropdown-links">
        <a href="/pricing">運費報價</a>
        <a href="/pricing-calculator">運費試算</a>
      </div>
    </div>
    <a href="/can-i-ship" class="mobile-nav-link">可以寄嗎</a>
    <a href="/article-list" class="mobile-nav-link">文章攻略</a>
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

# ===== 新的手机菜单 HTML（root 页面）=====
NEW_MOBILE_MENU_ROOT = '''  <div class="mobile-menu" id="mobileMenu">
    <a href="/tw-to-cn" class="mobile-nav-link">台灣發大陸</a>
    <div class="m-dropdown">
      <span>運費</span>
      <div class="m-dropdown-links">
        <a href="/pricing">運費報價</a>
        <a href="/pricing-calculator">運費試算</a>
      </div>
    </div>
    <a href="/can-i-ship" class="mobile-nav-link">可以寄嗎</a>
    <a href="/article-list" class="mobile-nav-link">文章攻略</a>
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

# ===== 新的 header CSS（统一所有页面） =====
NEW_HEADER_CSS = '''    .header{position:fixed;top:0;left:0;right:0;height:70px;background:var(--bg-white);z-index:1000;transition:box-shadow 0.3s}
    .header.scrolled{box-shadow:var(--shadow)}
    .header .container{display:flex;align-items:center;justify-content:space-between;height:100%}
    .logo{font-size:24px;font-weight:700;color:var(--primary);flex-shrink:0}
    .logo img{background:#fff;max-height:50px;max-width:200px;width:auto;display:block}
    .nav{display:flex;align-items:center;gap:24px}
    .nav a,.nav-dropdown>a{font-weight:500;color:var(--text-dark);transition:var(--transition);position:relative;font-size:14px;white-space:nowrap}
    .nav a::after{content:'';position:absolute;bottom:-4px;left:0;width:0;height:2px;background:var(--primary);transition:var(--transition)}
    .nav a:hover,.nav a.active{color:var(--primary)}
    .nav a:hover::after,.nav a.active::after{width:100%}
    .nav-dropdown{position:relative;display:flex;align-items:center}
    .dd-arrow{font-size:9px;margin-left:4px;display:inline-block}
    .dd-menu{display:none;position:absolute;top:100%;left:0;min-width:170px;background:#fff;border-radius:8px;box-shadow:0 8px 30px rgba(0,0,0,0.12);padding:8px 0;z-index:100;margin-top:8px;border:1px solid #e8ecf0}
    .nav-dropdown:hover .dd-menu,.nav-dropdown:focus-within .dd-menu{display:block}
    .dd-menu a{display:block;padding:10px 16px;font-size:13px;color:var(--text-dark);text-decoration:none;transition:var(--transition)}
    .dd-menu a:hover{background:var(--primary-light);color:var(--primary)}
    .header-cta{display:flex;align-items:center;gap:12px;flex-shrink:0}
    .btn-line{display:inline-flex;padding:10px 18px;background:var(--line-green);color:#fff;border-radius:8px;font-size:13px;font-weight:600;text-decoration:none;align-items:center;gap:6px;transition:var(--transition);white-space:nowrap}
    .btn-line:hover{background:#009900;transform:translateY(-1px);box-shadow:0 4px 12px rgba(0,185,0,0.25)}
    .menu-toggle{display:none;background:none;border:none;font-size:22px;cursor:pointer;color:var(--text-dark);padding:4px}
    @media(max-width:992px){.nav,.header-cta{display:none}.menu-toggle{display:block}}'''

# ===== 新的 mobile CSS =====
NEW_MOBILE_CSS = '''    .mobile-menu{display:none;position:fixed;top:70px;left:0;right:0;bottom:0;background:#fff;padding:24px;overflow-y:auto;z-index:999;box-shadow:0 4px 12px rgba(0,0,0,0.1)}
    .mobile-menu.active{display:block}
    .mobile-nav-link{display:block;padding:16px 0;font-size:16px;font-weight:500;color:var(--text-dark);border-bottom:1px solid var(--border)}
    .mobile-nav-link.active{color:var(--primary);font-weight:700}
    .mobile-nav-link.cta{margin-top:24px;padding:16px 24px;background:var(--primary);color:#fff;border-radius:var(--radius);text-align:center;border:none}
    .m-dropdown>span{display:flex;justify-content:space-between;align-items:center;padding:16px 0;font-size:16px;font-weight:500;color:var(--text-dark);border-bottom:1px solid var(--border);cursor:pointer}
    .m-dropdown>span::after{content:"▾";font-size:12px;transition:transform .2s}
    .m-dropdown.open>span::after{transform:rotate(180deg)}
    .m-dropdown-links{display:none;padding-left:16px}
    .m-dropdown.open .m-dropdown-links{display:block}
    .m-dropdown-links a{display:block;padding:12px 8px;font-size:14px;color:var(--text-dark);border-bottom:1px solid #f0f0f0}'''

# ===== 滚动 JS（仅 blog 页面需要，root 已有）=====
SCROLL_JS = '\n    // header scroll shadow\n    window.addEventListener(\'scroll\',function(){var h=document.getElementById(\'header\');if(h)h.classList.toggle(\'scrolled\',window.scrollY>10)});'

def process_blog_page(path):
    """处理 blog 类型页面"""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    
    # 1. 替换桌面导航 HTML（<nav>...</nav> 块）
    content = re.sub(
        r'<nav class="nav" id="desktopNav">.*?</nav>',
        NEW_NAV.strip(),
        content,
        flags=re.DOTALL
    )
    
    # 2. 替换手机菜单
    content = re.sub(
        r'<div class="mobile-menu" id="mobileMenu">.*?</div>\s*</div>\s*(?=<a href="https://line\.me/ti/p/~subaotw5988" class="floating-cta")',
        NEW_MOBILE_MENU_BLOG.strip() + '\n\n  ',
        content,
        flags=re.DOTALL
    )
    # Alternative: before floating-cta or footer
    if '<div class="mobile-menu"' not in content:
        # Try simpler match
        content = re.sub(
            r'<div class="mobile-menu" id="mobileMenu">.*?</div>\s*\n\s*(?=</body>)',
            NEW_MOBILE_MENU_BLOG.strip() + '\n\n',
            content,
            flags=re.DOTALL
        )
    
    # 3. 替换 header CSS 块（从 .header{ 到 menu-toggle 结束）
    # Blog 模板中 header CSS 特征：.header{position:fixed;top:0... 开始
    content = re.sub(
        r'\.header\{position:fixed;top:0;left:0;right:0;height:70px;background:var\(--bg-white\);z-index:1000;box-shadow:var\(--shadow\)\}[^}]*\}.*?\.menu-toggle\{display:none;background:none;border:none;font-size:22px;cursor:pointer;color:var\(--text-dark\);padding:4px\}',
        NEW_HEADER_CSS,
        content,
        flags=re.DOTALL
    )
    
    # 4. 替换旧的 dropdown 类名为新的 nav-dropdown 类名
    # blog 中有 .dropdown{position:relative;...} 和 .dropdown-menu{...} 样式
    # 先删掉旧的 dropdown CSS
    # 旧的 dropdown CSS 通常在 .btn-line 之前
    content = re.sub(
        r'\s*\.dropdown\{position:relative;display:flex;align-items:center\}.*?\.dropdown-menu a:hover\{background:var\(--primary-light\);color:var\(--primary\)\}',
        '',
        content,
        flags=re.DOTALL
    )
    
    # 5. 替换 mobile menu CSS（旧样式）
    # Blog 中的 mobile menu 样式
    content = re.sub(
        r'\.mobile-menu\{display:none;position:fixed;top:68px;left:0;right:0;bottom:0;background:#fff;padding:16px 24px;overflow-y:auto;z-index:999\}.*?\.m-dropdown-links a\{display:block;padding:10px 8px;font-size:14px;color:var\(--text-dark\);text-decoration:none;border-bottom:1px solid #f0f0f0\}',
        NEW_MOBILE_CSS,
        content,
        flags=re.DOTALL
    )
    
    # 6. 确保有 header scroll JS
    if 'header.scrolled' not in content and 'scroll' not in content[-500:]:
        # 在 </script> 之前（最后的 script 标签）添加
        content = content.replace('</script>\n</body>', '</script>' + SCROLL_JS + '\n</body>')
    
    # 7. 修复 container max-width:1200px (blog header 需要)
    # Blog .header .container 有 max-width:1200px，保持不变
    
    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def process_root_page(path):
    """处理 root 类型页面"""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    
    # 1. 替换桌面导航
    content = re.sub(
        r'<nav class="nav"[^>]*>.*?</nav>',
        NEW_NAV.strip(),
        content,
        flags=re.DOTALL
    )
    
    # 2. 替换手机菜单
    content = re.sub(
        r'<div class="mobile-menu" id="mobileMenu">.*?</div>',
        NEW_MOBILE_MENU_ROOT.strip(),
        content,
        flags=re.DOTALL
    )
    
    # 3. 标准化 header CSS
    # 统一 .header 样式（去掉初始 box-shadow）
    content = re.sub(
        r'\.header\s*\{[^}]*position\s*:\s*fixed[^}]*\}',
        '.header{position:fixed;top:0;left:0;right:0;height:70px;background:var(--bg-white);z-index:1000;transition:box-shadow 0.3s}\n    .header.scrolled{box-shadow:var(--shadow)}',
        content
    )
    
    # 4. 标准化 nav CSS (.nav{...})
    content = re.sub(
        r'\.nav\s*\{[^}]*display\s*:\s*flex[^}]*\}',
        '.nav{display:flex;align-items:center;gap:24px}',
        content
    )
    
    # 5. 标准化 nav link
    content = re.sub(
        r'\.nav\s+a\s*\{[^}]*\}',
        '.nav a,.nav-dropdown>a{font-weight:500;color:var(--text-dark);transition:var(--transition);position:relative;font-size:14px;white-space:nowrap}',
        content
    )
    
    # 6. 替换旧 dropdown 为新 nav-dropdown
    content = re.sub(
        r'\.dropdown\s*\{position\s*:\s*relative[^}]*\}',
        '.nav-dropdown{position:relative;display:flex;align-items:center}',
        content
    )
    content = re.sub(
        r'\.dropdown\s*>\s*a\s*::after\s*\{[^}]*\}',
        '.dd-arrow{font-size:9px;margin-left:4px;display:inline-block}',
        content
    )
    content = re.sub(
        r'\.dropdown-menu\s*\{[^}]*\}',
        '.dd-menu{display:none;position:absolute;top:100%;left:0;min-width:170px;background:#fff;border-radius:8px;box-shadow:0 8px 30px rgba(0,0,0,0.12);padding:8px 0;z-index:100;margin-top:8px;border:1px solid #e8ecf0}',
        content
    )
    content = re.sub(
        r'\.dropdown\s*:hover\s+\.dropdown-menu\s*\{[^}]*\}',
        '.nav-dropdown:hover .dd-menu,.nav-dropdown:focus-within .dd-menu{display:block}',
        content
    )
    # Also handle .dropdown:hover .dropdown-menu,.dropdown:focus-within .dropdown-menu pattern
    content = re.sub(
        r'\.dropdown\s*:hover\s+\.dropdown-menu\s*,\s*\.dropdown\s*:focus-within\s+\.dropdown-menu\s*\{[^}]*\}',
        '.nav-dropdown:hover .dd-menu,.nav-dropdown:focus-within .dd-menu{display:block}',
        content
    )
    content = re.sub(
        r'\.dropdown-menu\s+a\s*\{[^}]*\}',
        '.dd-menu a{display:block;padding:10px 16px;font-size:13px;color:var(--text-dark);text-decoration:none;transition:var(--transition)}',
        content
    )
    content = re.sub(
        r'\.dropdown-menu\s+a\s*:hover\s*\{[^}]*\}',
        '.dd-menu a:hover{background:var(--primary-light);color:var(--primary)}',
        content
    )
    
    # 7. 标准化 btn-line
    content = re.sub(
        r'\.btn-line\s*\{[^}]*\}',
        '.btn-line{display:inline-flex;padding:10px 18px;background:var(--line-green);color:#fff;border-radius:8px;font-size:13px;font-weight:600;text-decoration:none;align-items:center;gap:6px;transition:var(--transition);white-space:nowrap}',
        content
    )
    
    # 8. 删除多余的 .header .btn-line 特定样式（如果存在）
    content = re.sub(
        r'\n\s*\.header\s+\.btn-line\s*\{[^}]*\}',
        '',
        content
    )
    
    # 9. 标准化 menu-toggle
    content = re.sub(
        r'\.menu-toggle\s*\{[^}]*\}',
        '.menu-toggle{display:none;background:none;border:none;font-size:22px;cursor:pointer;color:var(--text-dark);padding:4px}',
        content
    )
    
    # 10. 标准化 header-cta
    content = re.sub(
        r'\.header-cta\s*\{[^}]*\}',
        '.header-cta{display:flex;align-items:center;gap:12px;flex-shrink:0}',
        content
    )
    
    # 11. 标准化 mobile menu
    content = re.sub(
        r'\.mobile-menu\s*\{[^}]*display\s*:\s*none[^}]*\}',
        '.mobile-menu{display:none;position:fixed;top:70px;left:0;right:0;bottom:0;background:#fff;padding:24px;overflow-y:auto;z-index:999;box-shadow:0 4px 12px rgba(0,0,0,0.1)}',
        content
    )
    
    # 12. Handle @media 中的 nav/cta 隐藏
    content = re.sub(
        r'@media\s*\(\s*max-width\s*:\s*992px\s*\)\s*\{[^}]*\.nav[^}]*display\s*:\s*none[^}]*\}',
        '@media(max-width:992px){.nav,.header-cta{display:none}.menu-toggle{display:block}}',
        content
    )
    
    # 13. Fix scroll JS - ensure header gets .scrolled class
    if 'header.scrolled' not in content and '<header class="header"' in content:
        # Add scroll handler before </body>
        scroll_js = '\n<script>window.addEventListener(\"scroll\",function(){var h=document.getElementById(\"header\");if(h)h.classList.toggle(\"scrolled\",window.scrollY>10)})</script>\n</body>'
        content = content.replace('</body>', scroll_js)
    
    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    import sys
    
    # 查找所有 blog 页面
    blog_dir = os.path.join(BASE, 'blog')
    blog_pages = sorted([os.path.join(blog_dir, f) for f in os.listdir(blog_dir) if f.endswith('.html')])
    
    # 查找 root 页面
    root_pages = sorted([os.path.join(BASE, f) for f in os.listdir(BASE) if f.endswith('.html') and f != '404.html' and f != 'google3f7a9c2e4de8c3b1.html'])
    
    updated_blog = 0
    updated_root = 0
    
    # 先处理 blog 页面
    for p in blog_pages:
        try:
            if process_blog_page(p):
                updated_blog += 1
                print(f'  ✅ blog/{os.path.basename(p)}')
        except Exception as e:
            print(f'  ❌ blog/{os.path.basename(p)}: {e}')
    
    # 再处理 root 页面
    for p in root_pages:
        try:
            if process_root_page(p):
                updated_root += 1
                print(f'  ✅ {os.path.basename(p)}')
        except Exception as e:
            print(f'  ❌ {os.path.basename(p)}: {e}')
    
    print(f'\n📊 汇总: Blog {updated_blog}/{len(blog_pages)} 已更新, Root {updated_root}/{len(root_pages)} 已更新')


if __name__ == '__main__':
    main()
