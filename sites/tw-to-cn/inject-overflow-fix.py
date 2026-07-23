#!/usr/bin/env python3
"""Inject html, body { overflow-x: hidden } into all blog pages and inner pages that don't have it"""
import re, glob, os

BASE = os.path.dirname(os.path.abspath(__file__))
INJECT_RULE = "html,body{overflow-x:hidden}"

files = glob.glob(f'{BASE}/blog/*.html') + glob.glob(f'{BASE}/*.html')
fixed = 0
for fp in files:
    if 'index.html' == fp: continue
    with open(fp, encoding='utf-8') as f:
        content = f.read()

    # Check if already has the rule
    if 'html,body{overflow-x:hidden}' in content or 'html, body{overflow-x:hidden}' in content:
        continue

    # Inject the rule right after </title> in the <head>
    # This places it at the top of the document so it takes precedence
    if '</head>' in content:
        new_content = content.replace(
            '</head>',
            f'<style>{INJECT_RULE}</style></head>',
            1
        )
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        fixed += 1

print(f'Injected html,body{{overflow-x:hidden}} into {fixed} files')
