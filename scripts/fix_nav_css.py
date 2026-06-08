#!/usr/bin/env python3
"""彻底修复所有页面的导航CSS问题"""
import os, re

BASE = '/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn'

# 规范CSS块（从index.html提取）
CANONICAL_HEADER = """    .header{position:fixed;top:0;left:0;right:0;height:70px;background:var(--bg-white);z-index:1000;transition:box-shadow .3s}
    .header.scrolled{box-shadow:var(--shadow)}
    .header .container{display:flex;align-items:center;justify-content:space-between;height:100%}
    .logo{font-size:24px;font-weight:700;color:var(--primary);flex-shrink:0}
    .logo img{background:#fff;max-height:50px;max-width:200px;width:auto;display:block}
    .nav{display:flex;align-items:center;gap:32px}
    .nav a,.nav-dropdown>a{font-weight:500;color:var(--text-dark);transition:var(--transition);position:relative;font-size:16px;white-space:nowrap}
    .nav a:hover,.nav a.active{color:var(--primary)}
    .nav a::after{content:'';position:absolute;bottom:-4px;left:0;width:0;height:2px;background:var(--primary);transition:var(--transition)}
    .nav a:hover::after,.nav a.active::after{width:100%}
    .nav-dropdown{position:relative;display:flex;align-items:center}
    .dd-arrow{font-size:9px;margin-left:4px;display:inline-block}
    .dd-menu{display:none;position:absolute;top:100%;left:0;min-width:170px;background:#fff;border-radius:8px;box-shadow:0 8px 30px rgba(0,0,0,.12);padding:8px 0;z-index:100;margin-top:8px;border:1px solid #e8ecf0}
    .nav-dropdown:hover .dd-menu,.nav-dropdown:focus-within .dd-menu{display:block}
    .dd-menu a{display:block;padding:10px 16px;font-size:13px;color:var(--text-dark);transition:var(--transition)}
    .dd-menu a:hover{background:var(--primary-light);color:var(--primary)}
    .header-cta{display:flex;align-items:center;gap:12px;flex-shrink:0}
    .btn-line{display:inline-flex;padding:10px 20px;background:var(--line-green);color:#fff;border-radius:8px;font-size:14px;font-weight:600;text-decoration:none;align-items:center;gap:6px;transition:var(--transition);white-space:nowrap}
    .btn-line:hover{background:#009900;transform:translateY(-1px);box-shadow:0 4px 12px rgba(0,185,0,.25)}
    .menu-toggle{display:none;background:none;border:none;font-size:22px;cursor:pointer;color:var(--text-dark);padding:4px}
    @media(max-width:992px){.nav,.header-cta{display:none}.menu-toggle{display:block}}"""

CANONICAL_MOBILE = """    .mobile-menu{display:none;position:fixed;top:70px;left:0;right:0;bottom:0;background:#fff;padding:24px;overflow-y:auto;z-index:999;box-shadow:0 4px 12px rgba(0,0,0,.1)}
    .mobile-menu.active{display:block}
    .mobile-nav-link{display:block;padding:16px 0;font-size:16px;font-weight:500;color:var(--text-dark);border-bottom:1px solid var(--border)}
    .mobile-nav-link.active{color:var(--primary);font-weight:700}
    .mobile-nav-link.cta{margin-top:24px;padding:16px 24px;background:var(--primary);color:#fff;border-radius:8px;text-align:center;border:none}
    .m-dropdown>span{display:flex;justify-content:space-between;align-items:center;padding:16px 0;font-size:16px;font-weight:500;color:var(--text-dark);border-bottom:1px solid var(--border);cursor:pointer}
    .m-dropdown>span::after{content:"▾";font-size:12px;transition:transform .2s}
    .m-dropdown.open>span::after{transform:rotate(180deg)}
    .m-dropdown-links{display:none;padding-left:16px}
    .m-dropdown.open .m-dropdown-links{display:block}
    .m-dropdown-links a{display:block;padding:12px 8px;font-size:14px;color:var(--text-dark);border-bottom:1px solid #f0f0f0}"""


def clean_duplicates(text):
    """Remove duplicate CSS rules that may conflict"""
    # Remove duplicate .header-cta rules (keep first one only)
    text = re.sub(
        r'\n\s*\.header-cta\{display:flex;align-items:center;gap:12px\}\s*\n',
        '\n',
        text
    )
    # Remove duplicate .btn-line rules
    text = re.sub(
        r'\n\s*\.btn-line\{display:inline-flex;padding:10px 20px;background:var\(--line-green\);color:#fff;border-radius:8px;font-size:14px;font-weight:600;text-decoration:none;align-items:center;gap:6px;transition:var\(--transition\);white-space:nowrap\}',
        '',
        text
    )
    text = re.sub(
        r'\n\s*\.btn-line:hover\{background:#009900;transform:translateY\(-1px\);box-shadow:0 4px 12px rgba\(0,185,0,0\.25\)\}',
        '',
        text
    )
    # Remove duplicate .menu-toggle rules
    text = re.sub(
        r'\n\s*\.menu-toggle\{display:none;background:none;border:none;font-size:22px;cursor:pointer;color:var\(--text-dark\);padding:4px\}\s*\n',
        '\n',
        text
    )
    # Remove duplicate .logo rules
    text = re.sub(
        r'\n\s*\.logo\{font-size:24px;font-weight:700;color:var\(--primary\)\}\s*\n',
        '\n',
        text
    )
    # Remove duplicate .logo img rules (old format with height:40px)
    text = re.sub(
        r'\n\s*\.logo img\{height:40px;background:#fff\}\s*\n',
        '\n',
        text
    )
    # Remove orphaned .dd-menu{display:block} without context
    text = re.sub(
        r'\n\s*\.dd-menu\{display:block\}\s*\n',
        '\n',
        text
    )
    return text


def fix_root_page(filepath):
    """修复root类型页面（can-i-ship, pricing等）"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # Step 1: 删除所有旧的 header/nav/dropdown/mobile 相关CSS
    # 针对 can-i-ship 的独特模式
    # 先从 .header 开始到 mobile 相关的所有规则全部删除
    
    # 删除 .header 行（含各种变体）
    content = re.sub(r'\n\s*\.header\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.header\.scrolled\{[^}]+\}\s*\n', '\n', content)
    
    # 删除 .header .container
    content = re.sub(r'\n\s*\.header\s+\.container\{[^}]+\}\s*\n', '\n', content)
    
    # 删除旧 .logo 规则（保留非header相关的）
    content = re.sub(r'\n\s*\.logo\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.logo\s+img\{[^}]+\}\s*\n', '\n', content)
    
    # 删除旧 .nav 规则
    content = re.sub(r'\n\s*\.nav\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.nav>a\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.nav a\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.nav a,[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.nav-dropdown>a\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.nav a::after\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.nav a:hover[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.nav>a:hover[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.nav>a\.active\{[^}]+\}\s*\n', '\n', content)
    
    # 删除旧 .dropdown 规则
    content = re.sub(r'\n\s*\.dropdown\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.dropdown>a::after\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.dropdown-menu\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.dropdown:hover[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.dropdown-menu a\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.dropdown-menu a:hover\{[^}]+\}\s*\n', '\n', content)
    
    # 删除旧的 .nav-dropdown / .dd-menu / .dd-arrow 规则
    content = re.sub(r'\n\s*\.nav-dropdown\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.dd-arrow\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.dd-menu\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.nav-dropdown:hover[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.dd-menu a\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.dd-menu a:hover\{[^}]+\}\s*\n', '\n', content)
    
    # 删除旧的 .nav a, .nav-dropdown>a 规则
    content = re.sub(r'\n\s*\.nav a,\.nav-dropdown[^}]+\}\s*\n', '\n', content)
    
    # 删除 .header-cta
    content = re.sub(r'\n\s*\.header-cta\{[^}]+\}\s*\n', '\n', content)
    
    # 删除旧的 .btn-line (不在CANONICAL里的那些)
    content = re.sub(r'\n\s*\.btn-line\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.btn-line:hover[^}]+\}\s*\n', '\n', content)
    
    # 删除 .menu-toggle
    content = re.sub(r'\n\s*\.menu-toggle\{[^}]+\}\s*\n', '\n', content)
    
    # 删除旧的 mobile-menu 规则
    content = re.sub(r'\n\s*\.mobile-menu\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.mobile-menu\.active\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.mobile-nav-link\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.mobile-nav-link\.active\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.mobile-nav-link\.cta\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.m-dropdown>span\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.m-dropdown>span::after\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.m-dropdown\.open>span::after\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.m-dropdown-links\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.m-dropdown\.open\s+\.m-dropdown-links\{[^}]+\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.m-dropdown-links a\{[^}]+\}\s*\n', '\n', content)
    
    # 删除 @media 中涉及 nav/header-cta/menu-toggle 的规则
    content = re.sub(r'\n\s*@media\(max-width:992px\)\{[^}]*\.nav[^}]*display:none[^}]*\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*@media\s*\(\s*max-width:\s*992px\s*\)\s*\{[^}]*\}\s*\n', '\n', content)
    
    # Step 2: 在 .section 或第一个内容CSS之前插入规范CSS
    # 找到合适位置插入：在 .page-hero 或其他第一个页面特定样式之前
    insert_point = content.find('.page-hero')
    if insert_point == -1:
        insert_point = content.find('.section')
    if insert_point == -1:
        insert_point = content.find('/* Search')
    if insert_point == -1:
        # 找一个锚点：在 :root 定义后面
        insert_point = content.find('    }') + 6
    
    if insert_point > 0:
        content = content[:insert_point] + '\n' + CANONICAL_HEADER + '\n' + content[insert_point:]
    
    # Step 3: 找到旧的 mobile menu CSS 区域，替换
    # 找到 .mobile-menu 开始到下一个非mobile section 的内容
    # 删除所有旧的mobile规则后，在 </style> 前插入规范的mobile CSS
    
    # 删除旧的 mobile CSS（第二轮清理）
    try:
        start = content.index('.mobile-menu{')
        # 向前找到换行
        nl = content.rfind('\n', 0, start)
        # 找到mobile块结束（下一个独立section的CSS）
        end_marker = content.find('\n\n    ', start + 50)
        if end_marker == -1:
            end_marker = content.find('\n  </style>', start)
        if end_marker > start:
            content = content[:nl] + content[end_marker:]
    except ValueError:
        pass
    
    # 在 </style> 之前插入 mobile CSS
    style_end = content.rfind('</style>')
    if style_end > 0:
        content = content[:style_end] + '\n' + CANONICAL_MOBILE + '\n' + content[style_end:]
    
    # Step 4: 清理重复规则
    content = clean_duplicates(content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def fix_blog_page(filepath):
    """修复blog类型页面"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    
    # Blog页面的CSS结构：:root ... { ... } *{...} body{...} a{...} .header{...} ...
    # 找到 .header 开头到 .floating-cta CSS之前的内容，全部替换
    
    # 删除 .header 到第一个无关CSS之间的所有导航相关CSS
    hdr_start = content.find('.header{')
    if hdr_start == -1:
        return False
    
    # 找到下一个不是导航/mobile相关的CSS块的开始
    # 导航CSS结束后是 .btn (line 135), .article-hero (line 137) 等
    after_nav = content.find('.btn{display:inline-block;padding:10px 20px;border-radius', hdr_start)
    if after_nav == -1:
        after_nav = content.find('.article-hero{', hdr_start)
    if after_nav == -1:
        return False
    
    # 替换从 .header{ 到 after_nav 之间的内容
    content = content[:hdr_start] + CANONICAL_HEADER + '\n    ' + content[after_nav:]
    
    # 删除 blog 中重复的 mobile CSS 块，插入规范的
    mob_start = content.find('.mobile-menu{display:none;position:fixed;top:')
    if mob_start == -1:
        # 旧的变体
        mob_start = content.find('.mobile-menu{display:none;position:fixed;top:68px')
    
    if mob_start > 0:
        # 找到前面最近的换行
        nl = content.rfind('\n', 0, mob_start)
        # 找到mobile CSS块结束
        end_mob = content.find('\n    .floating-cta{', mob_start)
        if end_mob == -1:
            end_mob = content.find('\n    @media', mob_start)
        if end_mob == -1:
            end_mob = content.find('\n  </style>', mob_start)
        if end_mob > mob_start:
            content = content[:nl+1] + CANONICAL_MOBILE + content[end_mob:]
    
    # 清理旧的mobile规则残留
    content = re.sub(r'\n\s*\.mobile-menu\{display:none[^}]*position:fixed[^}]*\}\s*\n', '\n', content)
    content = re.sub(r'\n\s*\.mobile-menu\.active\{[^}]+\}\s*\n', '\n', content)
    
    # 确保有 scroll JS
    if 'window.addEventListener("scroll"' not in content:
        content = content.replace('</body>', '<script>window.addEventListener("scroll",function(){var h=document.getElementById("header");if(h)h.classList.toggle("scrolled",window.scrollY>10)})</script>\n</body>')
    
    # 清理重复
    content = clean_duplicates(content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    import sys
    
    blog_dir = os.path.join(BASE, 'blog')
    blog_files = sorted([os.path.join(blog_dir, f) for f in os.listdir(blog_dir) if f.endswith('.html')])
    
    root_dir = BASE
    skip = {'404.html', 'google3f7a9c2e4de8c3b1.html', 'index.html'}
    root_files = sorted([os.path.join(root_dir, f) for f in os.listdir(root_dir) if f.endswith('.html') and f not in skip])
    
    fixed_blog = 0
    fixed_root = 0
    
    print("=== Fixing ROOT pages ===")
    for f in root_files:
        try:
            if fix_root_page(f):
                fixed_root += 1
                print(f'  ✅ {os.path.basename(f)}')
        except Exception as e:
            print(f'  ❌ {os.path.basename(f)}: {e}')
    
    print(f'\n=== Fixing BLOG pages ({len(blog_files)}) ===')
    for f in blog_files:
        try:
            if fix_blog_page(f):
                fixed_blog += 1
                print(f'  ✅ blog/{os.path.basename(f)}')
            else:
                print(f'  ⏭️ blog/{os.path.basename(f)} (no change needed)')
        except Exception as e:
            print(f'  ❌ blog/{os.path.basename(f)}: {e}')
    
    print(f'\n📊 Root: {fixed_root}/{len(root_files)} fixed, Blog: {fixed_blog}/{len(blog_files)} fixed')


if __name__ == '__main__':
    main()
