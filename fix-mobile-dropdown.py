#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
subao.tw 移动菜单「運費」下拉失效修复（2026-08-14）：

根因：inline script 里 `window.addEventListener('scroll',...)})` 后缺分号直接跟 `var mc=...`，
导致 "Unexpected token 'var'" 语法错误，整个 script 块（含 .m-dropdown>span 下拉 handler）解析失败。
叠加重复 handler 偶数个 toggle 抵消 → 「運費」点了没反应。

修复：
1. 补上缺失分号：`}})  var mc=` → `}});  var mc=`
2. 去重 .m-dropdown>span 的 click handler（多份重复导致 toggle 偶数抵消），只保留 1 份

幂等可重跑。
"""
import re, os, glob

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sites", "tw-to-cn")

# 缺失分号：`}})` + 空白 + `var mc=document`
RE_MISSING_SEMI = re.compile(r'\}\)\)\)(\s{1,3})(var mc=document)')

# .m-dropdown>span 的 click handler（两种引号/两种 parentElement 引用）
RE_DROPDOWN = re.compile(
    r"document\.querySelectorAll\(['\"]\.m-dropdown>span['\"]\)\.forEach\(function\(s\)\{"
    r"s\.addEventListener\(['\"]click['\"],\s*function\(e\)\{e\.stopPropagation\(\);"
    r"(?:this|s)\.parentElement\.classList\.toggle\(['\"]open['\"]\)\s*\}\)\}\);?"
)

def fix(path):
    with open(path, encoding="utf-8") as f:
        html = f.read()
    orig = html

    # 1) 补分号
    html = RE_MISSING_SEMI.sub(lambda m: "}}});" + m.group(1) + m.group(2), html)

    # 2) 去重：保留第 1 份，删除其余
    matches = list(RE_DROPDOWN.finditer(html))
    if len(matches) > 1:
        # 从后往前删，避免索引偏移
        for m in reversed(matches[1:]):
            html = html[:m.start()] + html[m.end():]

    if html != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        return True
    return False

def main():
    fixed = 0
    total = 0
    for path in glob.glob(os.path.join(BASE, "**", "*.html"), recursive=True):
        total += 1
        if fix(path):
            fixed += 1
    print(f"修复页数: {fixed}/{total}")

if __name__ == "__main__":
    main()
