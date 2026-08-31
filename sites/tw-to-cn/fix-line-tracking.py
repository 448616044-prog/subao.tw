#!/usr/bin/env python3
"""
修复 subao.tw 全站 LINE 链接的 GA4 事件埋点漏报问题

根因：所有 LINE <a> 都用 target="_blank" + 同步 onclick="gtag(...)"，
      浏览器立即开新 tab 跳 line.me，原页面 sendBeacon 被中断 → 漏报 60%+
      （真实添加 45 vs GA4 line_click 17，捕获率仅 38%）

修复方案（C）：
  1. 去掉 target="_blank"（由 onclick 接管跳转）
  2. onclick 统一改造为：try{gtag(beacon)}catch + setTimeout 180ms 延迟跳转 + return false
  3. 统一补 generate_lead 事件 + transport_type:'beacon' + value:1
  4. 保留原 event_label（位置语义：hero_cta/float_bar/top_promo 等）

用法：
  python3 fix-line-tracking.py --dry-run   # 只统计不写
  python3 fix-line-tracking.py             # 实际写入
"""
import re
import sys
import glob

DRY = '--dry-run' in sys.argv

# 统一的新 onclick 模板（LABEL 占位）
TEMPLATE = (
    "var _h=this.href;"
    "try{if(typeof gtag==='function'){"
    "gtag('event','line_click',{event_category:'conversion',event_label:'{label}',value:1,transport_type:'beacon'});"
    "gtag('event','generate_lead',{event_category:'lead',event_label:'line',transport_type:'beacon'});"
    "}}catch(e){}"
    "setTimeout(function(){window.location.href=_h;},180);"
    "return false;"
)

# 匹配 <a ... line.me ...> 标签（属性内不含 > ，line.me 链接安全）
LINK_RE = re.compile(r'<a\b[^>]*line\.me[^>]*>')

def extract_label(onclick):
    """从 onclick 里提取 event_label，兼容 ' 和 \\' 两种写法"""
    # event_label:'xxx' 或 event_label:'xxx' 或 event_label:"xxx"
    m = re.search(r"event_label\s*:\s*\\*['\"]([^'\"\\]+)", onclick)
    if m:
        return m.group(1)
    return 'line_consult'

def transform_tag(m):
    tag = m.group(0)
    # 1. 去掉 target="_blank" / target='_blank'
    new_tag = re.sub(r'\s+target=(["\'])_blank\1', '', tag)
    # 2. 提取原 onclick（如果有）
    om = re.search(r'\sonclick=(["\'])(.*?)\1', new_tag, flags=re.S)
    if om:
        label = extract_label(om.group(2))
        # 移除原 onclick（连同属性）
        new_tag = re.sub(r'\sonclick=(["\']).*?\1', '', new_tag, flags=re.S)
    else:
        label = 'line_consult'
    # 3. 追加新的 onclick（在 > 之前）
    onclick_attr = ' onclick="' + TEMPLATE.replace('{label}', label) + '"'
    new_tag = new_tag[:-1] + onclick_attr + '>'
    return new_tag

def process_file(path):
    with open(path, encoding='utf-8') as f:
        html = f.read()
    tags = LINK_RE.findall(html)
    if not tags:
        return 0, 0
    new_html = LINK_RE.sub(transform_tag, html)
    changed = 0
    for old, new in zip(tags, LINK_RE.findall(new_html)):
        if old != new:
            changed += 1
    if not DRY:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_html)
    return len(tags), changed

def main():
    files = [f for f in glob.glob('**/*.html', recursive=True) if 'node_modules' not in f]
    total_tags = 0
    total_changed = 0
    changed_files = []
    for f in sorted(files):
        n, c = process_file(f)
        if n:
            total_tags += n
            total_changed += c
            if c:
                changed_files.append((f, n, c))
    print(f'模式: {"DRY-RUN（不写入）" if DRY else "实际写入"}')
    print(f'扫描文件: {len(files)} 个 HTML')
    print(f'LINE 链接总数: {total_tags}')
    print(f'被改造标签: {total_changed}')
    print(f'改动文件数: {len(changed_files)}')
    if DRY:
        print()
        print('=== 改动明细（前20个文件）===')
        for f, n, c in changed_files[:20]:
            print(f'  {f}: {c}/{n} 标签')
    else:
        print()
        print('=== 已写入文件数 ===')
        print(f'  {len(changed_files)} 个文件')

if __name__ == '__main__':
    main()
