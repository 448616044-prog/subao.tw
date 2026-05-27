#!/usr/bin/env python3
"""批量注入 GA4 追踪代码到所有缺失的 HTML 页面"""

import os
import re

GA4_SNIPPET = '''  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-X2T4LGTKJ1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-X2T4LGTKJ1');
  </script>
'''

SITE_ROOT = "/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn"

# 已有的 GA4 页面（保持不变）
pages_with_ga4 = {"pricing.html", "about.html", "tw-to-cn.html"}

html_files = []
for root, dirs, files in os.walk(SITE_ROOT):
    if ".git" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

html_files.sort()

modified = []
skipped = []

for fpath in html_files:
    fname = os.path.basename(fpath)
    relpath = os.path.relpath(fpath, SITE_ROOT)

    # 已有 GA4 的跳过
    if fname in pages_with_ga4:
        skipped.append(relpath)
        continue

    with open(fpath, "r", encoding="utf-8") as fh:
        content = fh.read()

    # 已有的跳过
    if "G-X2T4LGTKJ1" in content:
        skipped.append(relpath)
        continue

    # 找 </head> 标签（可能有空格变体）
    head_match = re.search(r'</head>', content, re.IGNORECASE)
    if not head_match:
        print(f"⚠️  无 </head>：{relpath}")
        continue

    insert_pos = head_match.start()
    new_content = content[:insert_pos] + GA4_SNIPPET + content[insert_pos:]

    with open(fpath, "w", encoding="utf-8") as fh:
        fh.write(new_content)

    modified.append(relpath)

print(f"\n✅ GA4 已注入：{len(modified)} 个页面")
for p in modified:
    print(f"   + {p}")

print(f"\n⏭️  跳过（已有或无 </head>）：{len(skipped)} 个页面")
for p in skipped:
    print(f"   · {p}")
