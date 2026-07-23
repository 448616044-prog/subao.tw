#!/usr/bin/env python3
"""Remove duplicate menuToggle click handlers from all inner pages"""
import re, glob, os

BASE = os.path.dirname(os.path.abspath(__file__))
PATTERN = re.compile(
    r'\.addEventListener\(\"click\",\s*function\s*\(\s*\)\s*\{'
    r'\s*m\.classList\.toggle\(\"active\"\);\s*'
    r'document\.body\.classList\.toggle\(\"menu-open\"\)\s*\}\)'
)

files = glob.glob(f'{BASE}/*.html') + glob.glob(f'{BASE}/blog/*.html')
total_removed = 0
fixed_files = 0

for fp in files:
    if 'index.html' in fp: continue
    with open(fp, encoding='utf-8') as f:
        content = f.read()
    
    matches = list(PATTERN.finditer(content))
    if len(matches) <= 1:
        continue
    
    # Keep first, remove rest (process in reverse to preserve positions)
    for m in reversed(matches[1:]):
        content = content[:m.start()] + content[m.end():]
        total_removed += 1
    
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    fixed_files += 1

print(f'Fixed {fixed_files} files, removed {total_removed} duplicate handlers')
