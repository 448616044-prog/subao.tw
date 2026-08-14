#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
subao.tw 修复「// 注释吞掉同行代码」历史 bug（简单文件，14个）
方法：把「// 注释文字」与其后紧跟的代码之间加换行，让代码脱离注释。
幂等：替换后「// 注释文字\\n代码」中的 \\n 会被 \\s* 再次匹配但替换结果不变。

注意：can-i-ship.html 的 26019 字符单行搜索脚本是复杂案例，单独处理（不在本脚本）。
"""
import re, glob, os, sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sites', 'tw-to-cn')

# (注释文字, 注释后缩进)
RULES = [
    ('滚动超过400px显示浮动栏', '    '),
    ('滚动浮动底栏', '    '),
    ('行動端漢堡選單', '    '),
    ('移动端菜单切换', '    '),
    ('Calculator logic', '    '),
    ('header 阴影', '    '),
    ('mobile menu toggle', '    '),
]

def fix_file(p):
    h = open(p, encoding='utf-8').read()
    orig = h
    n = 0
    for txt, indent in RULES:
        rx = re.compile(r'//\s*' + re.escape(txt) + r'\s*')
        n += len(rx.findall(h))
        h = rx.sub(lambda m: '// ' + txt + '\n' + indent, h)
    if h != orig:
        open(p, 'w', encoding='utf-8').write(h)
        return n
    return 0

def main():
    if not os.path.isdir(BASE):
        print(f"BASE not found: {BASE}", file=sys.stderr)
        sys.exit(1)
    files_changed = 0
    total = 0
    for p in glob.glob(os.path.join(BASE, '**/*.html'), recursive=True):
        n = fix_file(p)
        if n:
            files_changed += 1
            total += n
    print(f"改动文件: {files_changed} / 改动处数: {total}")
    return total

if __name__ == '__main__':
    total = main()
