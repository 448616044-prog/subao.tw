#!/usr/bin/env python3
"""Inject missing mobile menu CSS into all pages that have mobile-nav-link but no CSS for it"""
import re, glob, os

BASE = os.path.dirname(os.path.abspath(__file__))

# Required mobile menu CSS rules
REQUIRED_CSS = """
.mobile-nav-link{display:block;padding:14px 0;font-size:16px;font-weight:500;color:var(--text-dark);border-bottom:1px solid var(--border);text-decoration:none}
.mobile-nav-link.cta{margin-top:16px;padding:14px 20px;background:var(--primary);color:#fff;border-radius:8px;text-align:center;border:none;display:flex;align-items:center;justify-content:center;gap:6px}
.mobile-nav-link.active{color:var(--primary);font-weight:700}
.m-dropdown>span{display:block;padding:14px 0;font-size:16px;font-weight:500;color:var(--text-dark);border-bottom:1px solid var(--border);cursor:pointer;position:relative}
.m-dropdown>span::after{content:"+";position:absolute;right:0;top:50%;transform:translateY(-50%);font-size:20px;color:var(--text-light);transition:transform .2s}
.m-dropdown.open>span::after{content:"−"}
.m-dropdown-links{display:none;padding:8px 0 8px 16px;background:#f9f9f9}
.m-dropdown.open .m-dropdown-links{display:block}
.m-dropdown-links a{display:block;padding:10px 0;font-size:15px;color:var(--text-light);text-decoration:none;border-bottom:1px solid #eee}
.m-dropdown-links a:last-child{border-bottom:none}
#mobileClose{background:none;border:none;font-size:28px;cursor:pointer;color:#999;line-height:1}
"""

# Check if file already has these rules
CHECK_RULES = ['.mobile-nav-link{', '.m-dropdown>span{', '.m-dropdown-links{']

files = glob.glob(f'{BASE}/*.html') + glob.glob(f'{BASE}/blog/*.html')
fixed = 0
skipped = 0

for fp in files:
    if 'index.html' == fp: continue
    with open(fp, encoding='utf-8') as f:
        content = f.read()

    # Check if file uses mobile-nav-link class
    if 'class="mobile-nav-link"' not in content and 'mobile-nav-link"' not in content:
        skipped += 1
        continue

    # Check if all required rules are present
    all_present = all(rule in content for rule in CHECK_RULES)
    if all_present:
        skipped += 1
        continue

    # Find the <head> closing or </style> tag to inject after
    # Inject before </head>
    if '</head>' in content:
        # Build injection
        inject = f'<style>{REQUIRED_CSS}</style>'
        new_content = content.replace('</head>', f'{inject}</head>', 1)
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        fixed += 1

print(f'Fixed: {fixed}, Skipped: {skipped}')
