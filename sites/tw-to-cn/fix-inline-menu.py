#!/usr/bin/env python3
"""Remove inline menuToggle handler from can-i-ship and express-comparison"""
import re

# The inline handler to remove - matches the minified block
PATTERN = re.compile(
    r'\n\s*//\s*Mobile menu\n\s*var\s+menuToggle\s*=\s*document\.getElementById\(\'menuToggle\'\)\s*,\s*mobileMenu\s*=\s*document\.getElementById\(\'mobileMenu\'\)\s*;'
    r'\s*menuToggle\.addEventListener\(\'click\'\s*,\s*function\(\)\{[^}]+\}\)\s*;'
    r'\s*mobileMenu\.querySelectorAll\(\'a\'\)\.forEach\([^;]+\);'
)

files = ['can-i-ship.html', 'express-comparison.html']
for fp in files:
    with open(fp, encoding='utf-8') as f:
        content = f.read()
    
    new_content = PATTERN.sub('', content)
    
    if new_content != content:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Fixed: {fp}')
    else:
        print(f'No match: {fp}')
