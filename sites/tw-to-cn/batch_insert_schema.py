#!/usr/bin/env python3
"""批量为 blog 页面注入 Schema.org JSON-LD（BreadcrumbList + Article + FAQPage）"""

import os
import re
import json
from datetime import datetime

SITE_ROOT = "/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn/blog"

def get_h1(content):
    m = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
    return m.group(1).strip() if m else "台灣寄大陸指南"

def get_description(content):
    m = re.search(r'<meta[^>]+name="description"[^>]+content="([^"]+)"', content, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    # Fallback: first paragraph
    m = re.search(r'<p[^>]*>([^<]{30,})</p>', content)
    return m.group(1).strip()[:160] if m else "速豹集運專業台灣到大陸物流服務"

def get_date_modified(content):
    m = re.search(r'(20\d{2})[-/年](0?[1-9]|1[0-2])[-/月](0?[1-9]|[12]\d|3[01])', content)
    if m:
        return f"{m.group(1)}-{m.group(2).zfill(2)}-{m.group(3).zfill(2)}"
    return "2026-05-27"

def get_faq_qa(content):
    """Extract FAQ Q&A pairs from page content"""
    qa_pairs = []
    # Match <div class="faq-q">Q：...question...</div> followed by <div class="faq-a">...answer...</div>
    pattern = r'<div class="faq-q">([^<]+)</div>\s*<div class="faq-a">([^<]+)</div>'
    for m in re.finditer(pattern, content):
        q = m.group(1).strip()
        a = m.group(2).strip()
        # Remove "Q：" prefix
        q = re.sub(r'^Q[：:]\s*', '', q)
        if q and a and len(q) > 3:
            qa_pairs.append((q, a))
    return qa_pairs

def get_page_url(filename):
    page = filename.replace('.html', '')
    return f"https://subao.tw/blog/{page}"

def get_breadcrumb_name(h1):
    """Truncate h1 for breadcrumb (max 40 chars)"""
    return h1[:40] + "..." if len(h1) > 40 else h1

def build_schema(h1, description, url, faq_qa, date_modified):
    """Build the @graph JSON-LD structure"""
    graph = []

    # 1. BreadcrumbList
    graph.append({
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "首頁", "item": "https://subao.tw/"},
            {"@type": "ListItem", "position": 2, "name": "文章攻略", "item": "https://subao.tw/article-list"},
            {"@type": "ListItem", "position": 3, "name": get_breadcrumb_name(h1), "item": url}
        ]
    })

    # 2. Article
    article = {
        "@type": "Article",
        "headline": h1,
        "description": description,
        "datePublished": "2026-03-01",
        "dateModified": date_modified,
        "author": {"@type": "Organization", "name": "速豹集運"},
        "publisher": {
            "@type": "Organization",
            "name": "速豹集運",
            "url": "https://subao.tw",
            "logo": {"@type": "ImageObject", "url": "https://subao.tw/images/subao-logo-new.png"}
        },
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "image": {"@type": "ImageObject", "url": "https://subao.tw/images/og-default.png"},
        "articleSection": "敏感貨寄送",
        "keywords": "台灣寄大陸,兩岸物流,速豹集運"
    }
    graph.append(article)

    # 3. FAQPage (only if Q&A found)
    if faq_qa:
        faq_main_entity = []
        for q, a in faq_qa:
            faq_main_entity.append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a}
            })
        graph.append({"@type": "FAQPage", "mainEntity": faq_main_entity})

    return {
        "@context": "https://schema.org",
        "@graph": graph
    }

def inject_schema(filepath, filename):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if already has JSON-LD
    if 'application/ld+json' in content:
        return False, "已有Schema"

    h1 = get_h1(content)
    description = get_description(content)
    url = get_page_url(filename)
    faq_qa = get_faq_qa(content)
    date_modified = get_date_modified(content)

    schema = build_schema(h1, description, url, faq_qa, date_modified)
    schema_json = json.dumps(schema, ensure_ascii=False, indent=2)

    # Build the full <script> tag
    script_tag = f'\n  <script type="application/ld+json">\n  {schema_json}\n  </script>\n'

    # Insert before </head>
    head_end = re.search(r'</head>', content, re.IGNORECASE)
    if not head_end:
        return False, "无</head>标签"

    pos = head_end.start()
    new_content = content[:pos] + script_tag + content[pos:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    faq_count = len(faq_qa)
    return True, f"✅ {h1[:30]}... | FAQ:{faq_count}条"

# Pages missing Schema
pages = [
    "shopee-shipping.html",
    "taiwan-medicine-to-china.html",
    "taiwan-to-china-guide.html",
    "taobao-consolidated-shipping.html",
    "tw-to-cn-cost.html",
    "tw-to-cn-customs.html",
    "tw-to-cn-logistics-comparison.html",
    "tw-to-cn-logistics-recommend.html",
    "tw-to-cn-shipping-guide.html",
]

print("=" * 60)
print("Schema.org 批量注入")
print("=" * 60)

results = []
for fname in pages:
    fpath = os.path.join(SITE_ROOT, fname)
    if not os.path.exists(fpath):
        print(f"❌ 文件不存在：{fname}")
        continue
    ok, msg = inject_schema(fpath, fname)
    results.append((ok, fname, msg))
    status = "✅" if ok else "⏭️ "
    print(f"{status} {fname}: {msg}")

success = sum(1 for r in results if r[0])
print(f"\n完成：{success}/{len(results)} 个页面已注入 Schema")
