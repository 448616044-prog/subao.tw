#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
subao.tw 移动端适配修复（2026-08-14）：

1. 移除每页 inline script 中残缺/冲突的 menuToggle 绑定（保留其它功能）
   - 删 `if(t&&m)t.addEventListener("click",function(){m.classList.toggle("active");...});`
   - 删 `if(t&&m)t;` 残骸
2. 在 </body> 前注入一套干净的菜单 handler（开/关/点链接自动关）
3. 对 index.html（首页）额外注入 mobile-menu 兜底隐藏 CSS（解决 LINE logo 漏出问题）

- 幂等（重跑安全）
- 跳过无 menuToggle 的页面
"""
import re, os, sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sites", "tw-to-cn")

CLEAN_MENU_SCRIPT = (
    "<script>\n"
    "document.addEventListener('DOMContentLoaded',function(){\n"
    "  var mt=document.getElementById('menuToggle'),mm=document.getElementById('mobileMenu'),mc=document.getElementById('mobileClose');\n"
    "  if(mt&&mm){mt.addEventListener('click',function(e){e.preventDefault();e.stopPropagation();mm.classList.toggle('active');document.body.classList.toggle('menu-open')})}\n"
    "  if(mc&&mm){mc.addEventListener('click',function(){mm.classList.remove('active');document.body.classList.remove('menu-open')})}\n"
    "  if(mm){mm.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){mm.classList.remove('active');document.body.classList.remove('menu-open')})})}\n"
    "});\n"
    "</script>\n"
)

# 兜底 CSS：mobile-menu 非 active 状态双重隐藏
SAFETY_CSS_INDEX = (
    "<style>\n"
    ".mobile-menu:not(.active){display:none!important;visibility:hidden!important;pointer-events:none!important}\n"
    "</style>\n"
)

# 待移除的菜单绑定片段
RE_BROKEN_IF = re.compile(
    r'if\s*\(\s*t\s*&&\s*m\s*\)\s*t\s*;',
    re.DOTALL,
)
RE_OPEN_TOGGLE = re.compile(
    r'if\s*\(\s*t\s*&&\s*m\s*\)\s*t\.addEventListener\s*\(\s*["\']click["\']\s*,\s*function\s*\(\s*\)\s*\{\s*m\.classList\.toggle\s*\(\s*["\']active["\']\s*\)\s*;[^}]*\}\s*\)',
    re.DOTALL,
)

def fix_html(path):
    with open(path, encoding="utf-8") as f:
        html = f.read()

    if 'id="menuToggle"' not in html:
        return False  # 无菜单元素，跳过

    original = html
    # 1) 移除残骸/冲突绑定
    html = RE_BROKEN_IF.sub("", html)
    html = RE_OPEN_TOGGLE.sub("", html)

    changed = (html != original)

    # 2) 注入干净 handler（幂等：先移除已注入的）
    html = re.sub(
        r"<script>\s*document\.addEventListener\('DOMContentLoaded',function\(\)\{\s*var mt=document\.getElementById\('menuToggle'\)[\s\S]*?\}\)\s*</script>\n?",
        "", html,
    )
    if "</body>" in html:
        html = html.replace("</body>", CLEAN_MENU_SCRIPT + "</body>", 1)
    elif "</html>" in html:
        html = html.replace("</html>", CLEAN_MENU_SCRIPT + "</html>", 1)
    else:
        html += CLEAN_MENU_SCRIPT

    # 3) index.html 加 mobile-menu 兜底 CSS（幂等）
    fname = os.path.basename(path)
    if fname == "index.html":
        html = re.sub(
            r"<style>\s*\.mobile-menu:not\(\.active\)\{display:none!important;visibility:hidden!important;pointer-events:none!important\}\s*</style>\n?",
            "", html,
        )
        if "</head>" in html:
            html = html.replace("</head>", SAFETY_CSS_INDEX + "</head>", 1)

    if html != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        return True
    return False

def main():
    if not os.path.isdir(BASE):
        print(f"BASE not found: {BASE}", file=sys.stderr)
        sys.exit(1)
    fixed = []
    for root, _, files in os.walk(BASE):
        for fn in files:
            if not fn.endswith(".html"):
                continue
            p = os.path.join(root, fn)
            if fix_html(p):
                fixed.append(os.path.relpath(p, BASE))
    print(f"修复页数: {len(fixed)}")
    for f in fixed[:20]:
        print(f"  - {f}")
    if len(fixed) > 20:
        print(f"  ... 还有 {len(fixed)-20} 个")

if __name__ == "__main__":
    main()