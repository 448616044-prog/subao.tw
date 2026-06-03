#!/usr/bin/env python3
"""为 subao.tw 全站 LINE 链接注入 GA4 转化事件追踪"""

import os
import re

BASE = "/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn"

GTAG_EVENT = "gtag('event','line_click',{event_category:'conversion',event_label:'line_consult',value:1})"

# 匹配 LINE 链接的 <a> 标签
LINE_RE = re.compile(
    r'(<a[^>]*href=["\']https://line\.me/ti/p/~mmmppp004["\'][^>]*)(>)',
    re.IGNORECASE
)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    def add_onclick(match):
        a_open = match.group(1)
        # 检查是否已有 onclick
        if 'onclick=' in a_open or "onclick='" in a_open:
            return match.group(0)
        # 在 > 前插入 onclick
        return f'{a_open} onclick="{GTAG_EVENT}"{match.group(2)}'

    content = LINE_RE.sub(add_onclick, content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

count = 0
for root, dirs, files in os.walk(BASE):
    for f in files:
        if f.endswith('.html'):
            fp = os.path.join(root, f)
            if process_file(fp):
                count += 1
                print(f"✅ {os.path.relpath(fp, BASE)}")

print(f"\n🎉 共处理 {count} 个文件")
