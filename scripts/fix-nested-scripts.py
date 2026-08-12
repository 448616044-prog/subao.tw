#!/usr/bin/env python3
"""批量修复 <script> 标签嵌套问题 — 把被错误合并的 script 块拆回两个独立块"""
import re, os, sys

SITE_DIR = "/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn"

# Pattern: find <script> that appears INSIDE another script block
# (not preceded by </script>)
# We detect this by finding <script> within a larger <script>...</script> block

def extract_script_ranges(html):
    """Return list of (start, end) positions of <script> tags that contain inline JS"""
    ranges = []
    pattern = re.compile(
        r'<script(?:\s[^>]*?)?>(.*?)</script>',
        re.DOTALL | re.IGNORECASE
    )
    for m in pattern.finditer(html):
        tag_open = html[m.start():m.start() + m.group(0).find('>') + 1]
        # Skip external scripts (src=) and JSON-LD
        if 'src=' in tag_open:
            continue
        if 'application/ld+json' in tag_open.lower():
            continue
        if 'type="application/ld+json"' in tag_open.lower():
            continue
        ranges.append((m.start(), m.end()))
    return ranges

def fix_nested_scripts(html):
    """Fix <script> that appears inside another script block"""
    ranges = extract_script_ranges(html)
    
    # Process from end to start to preserve positions
    fixes = 0
    for block_start, block_end in reversed(ranges):
        block_content = html[block_start:block_end]
        
        # Find <script> inside this block (not at position 0)
        inner_pattern = re.compile(r'<script(?:\s[^>]*?)?>', re.IGNORECASE)
        for m in reversed(list(inner_pattern.finditer(block_content))):
            inner_pos_in_block = m.start()
            if inner_pos_in_block == 0:
                continue  # This is the block's own opening tag
            
            absolute_pos = block_start + inner_pos_in_block
            
            # Check: is this preceded by </script>? If yes, it's already correct
            before = html[max(0, absolute_pos-50):absolute_pos]
            if '</script>' in before.lower():
                continue
            
            # Fix: insert </script> before this <script>
            html = html[:absolute_pos] + '</script>\n' + html[absolute_pos:]
            fixes += 1
    
    return html, fixes

def main():
    files = []
    for root, dirs, fs in os.walk(SITE_DIR):
        if '.git' in root or '__pycache__' in root:
            continue
        for f in fs:
            if f.endswith('.html'):
                files.append(os.path.join(root, f))
    
    total_fixed = 0
    total_files = 0
    
    for fpath in sorted(files):
        with open(fpath, 'r', encoding='utf-8') as f:
            original = f.read()
        
        fixed, count = fix_nested_scripts(original)
        
        if count > 0:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(fixed)
            rel = os.path.relpath(fpath, SITE_DIR)
            print(f'  ✅ {rel}: fixed {count} nested <script> tag(s)')
            total_fixed += count
            total_files += 1
    
    print(f'\n📊 Fixed {total_fixed} issues in {total_files} files.')
    
    if total_fixed == 0:
        print('✅ No issues found — all script blocks are clean.')
    else:
        print('⚠️  Run scripts/validate-js.py to verify.')

if __name__ == '__main__':
    main()
