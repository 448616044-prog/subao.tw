#!/usr/bin/env python3
"""
全站时效文案统一改写 v2 — 精准匹配版
改写规则（用户确认）：
  硬承诺: "X-X天送达/到" + "最快"前缀 → "最快5-7天（具體貨品時效請添加LINE與客服確認）"
  首页H1: "5-7天包稅到府" → "最快5-7天到（空運）包稅到府"
  Title/Meta: 短版 "最快5-7天（空運）"
  Schema FAQ: 短版 "最快5-7天（具體時效請加LINE確認）"
  对比表格: 保留不同数字 + "（一般參考）"
  排除: 客户证言、kg/公斤/元/歲 单位数字
"""

import re
import os
import sys

BASE_DIR = "/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn"

FALLBACK = "（具體貨品時效請添加LINE與客服確認）"
FALLBACK_SHORT = "（具體時效請加LINE確認）"
TITLE_SUFFIX = "（空運）"

changes = {}
stats = {"total": 0, "title": 0, "body": 0, "schema": 0, "table": 0}

def log(filepath, line_num, tag, old, new):
    if filepath not in changes:
        changes[filepath] = []
    old_s = old.strip()[:80]
    new_s = new.strip()[:80]
    changes[filepath].append(f"  [{tag}] L{line_num}: {old_s} → {new_s}")
    stats["total"] += 1
    stats[tag] = stats.get(tag, 0) + 1

def replace_in_line(line, old_str, new_str, tag, filepath, line_num):
    """在单行内替换，仅在未被替换过时执行"""
    if old_str in line:
        result = line.replace(old_str, new_str)
        if result != line:
            log(filepath, line_num, tag, old_str, new_str)
            return result
    return line

def process_text(text, filepath):
    """核心替换逻辑"""
    lines = text.split('\n')
    new_lines = []
    in_schema = False
    in_testimonial = False
    
    for i, line in enumerate(lines):
        modified = line.strip('\n')
        orig = modified
        ln = i + 1
        
        # 跟踪区块 & 单行 Schema 特殊处理
        is_single_line_schema = (
            ('<script type="application/ld+json"' in modified) and 
            ('</script>' in modified)
        )
        if not is_single_line_schema:
            if '<script type="application/ld+json">' in modified or '<script type="application/ld+json"' in modified:
                in_schema = True
            if '</script>' in modified and in_schema:
                in_schema = False
        
        # ============================================================
        # 单行 Schema: 处理完直接 continue
        # ============================================================
        if is_single_line_schema:
            for pat, repl in [
                ('5-7天送達', f'最快5-7天{FALLBACK_SHORT}'),
                ('5-7個工作天送達', f'最快5-7天{FALLBACK_SHORT}'),
                ('5-7個工作天', f'最快5-7天{FALLBACK_SHORT}'),
                ('7-14個工作天送達', f'最快5-7天{FALLBACK_SHORT}'),
                ('7-12天送達', f'最快5-7天{FALLBACK_SHORT}'),
                ('3-5個工作日送達', f'最快5-7天{FALLBACK_SHORT}'),
                ('一般7-12天', f'最快5-7天{FALLBACK_SHORT}'),
            ]:
                modified = modified.replace(pat, repl)
                if modified != orig:
                    log(filepath, ln, 'schema_single', pat, repl)
            
            # 清理重复兜底
            modified = modified.replace(f'{FALLBACK_SHORT}{FALLBACK_SHORT}', FALLBACK_SHORT)
            if modified != orig:
                new_lines.append(modified + ('\n' if i < len(lines)-1 else ''))
            else:
                new_lines.append(line)
            continue
        
        # ============================================================
        # TITLE / META: 短版
        # ============================================================
        if '<title>' in modified and '</title>' in modified:
            # 替换 Title 中的时效
            modified = replace_in_line(modified, '5-7天到', f'最快5-7天{TITLE_SUFFIX}', 'title', filepath, ln)
            modified = replace_in_line(modified, '5-7天包稅', f'最快5-7天{TITLE_SUFFIX}包稅', 'title', filepath, ln)
            modified = replace_in_line(modified, '5-7天送達', f'最快5-7天{TITLE_SUFFIX}', 'title', filepath, ln)
        
        if 'name="description"' in modified or 'property="og:description"' in modified:
            modified = replace_in_line(modified, '5-7天送達', f'最快5-7天{TITLE_SUFFIX}', 'meta', filepath, ln)
            modified = replace_in_line(modified, '5-7天到', f'最快5-7天{TITLE_SUFFIX}', 'meta', filepath, ln)
            # 只在未被前两条替换时处理裸"最快5-7天"（防止双"（空運）"）
            if f'最快5-7天{TITLE_SUFFIX}' not in modified:
                modified = replace_in_line(modified, '最快5-7天', f'最快5-7天{TITLE_SUFFIX}', 'meta', filepath, ln)
        
        if 'property="og:title"' in modified:
            modified = replace_in_line(modified, '5-7天到', f'最快5-7天{TITLE_SUFFIX}', 'og', filepath, ln)
            modified = replace_in_line(modified, '5-7天送達', f'最快5-7天{TITLE_SUFFIX}', 'og', filepath, ln)
        
        # ============================================================
        # SCHEMA: 短版
        # ============================================================
        if in_schema:
            modified = replace_in_line(modified, '5-7天送達', f'最快5-7天{FALLBACK_SHORT}', 'schema', filepath, ln)
            modified = replace_in_line(modified, '5-7個工作天送達', f'最快5-7天{FALLBACK_SHORT}', 'schema', filepath, ln)
            modified = replace_in_line(modified, '5-7個工作天', f'最快5-7天{FALLBACK_SHORT}', 'schema', filepath, ln)
            modified = replace_in_line(modified, '7-14個工作天送達', f'最快5-7天{FALLBACK_SHORT}', 'schema', filepath, ln)
            modified = replace_in_line(modified, '7-12天送達', f'最快5-7天{FALLBACK_SHORT}', 'schema', filepath, ln)
            modified = replace_in_line(modified, '3-5個工作日送達', f'最快5-7天{FALLBACK_SHORT}', 'schema', filepath, ln)
            modified = replace_in_line(modified, '一般7-12天', f'最快5-7天{FALLBACK_SHORT}', 'schema', filepath, ln)
            new_lines.append(modified + '\n' if i < len(lines)-1 else modified)
            continue
        
        # ============================================================
        # H1 特殊: 处理完直接 continue，避免被后续 body 规则再改
        # ============================================================
        if '<h1' in modified:
            modified = modified.replace('5-7天包稅到府', '最快5-7天到（空運）包稅到府')
            modified = modified.replace('5-7天到府', '最快5-7天（空運）到府')
            if modified != orig:
                log(filepath, ln, 'h1', orig, modified)
                new_lines.append(modified + ('\n' if i < len(lines)-1 else ''))
            else:
                new_lines.append(line)
            continue
        
        # ============================================================
        # 正文硬承诺: 精确模式
        # ============================================================
        # 核心: "5-7天送達" "5-7個工作天送達"
        modified = replace_in_line(modified, '5-7天送達', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '5-7個工作天送達', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '5-7個工作天', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '5-7天到', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '5-7天送', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        
        # "最快5-7天送達" → 加兜底（不重复"最快"）
        modified = replace_in_line(modified, '最快5-7天送達', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '最快5-7天到', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        
        # "空運5-7天" → "空運最快5-7天"
        modified = replace_in_line(modified, '空運5-7天送達', f'空運最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '空運5-7天，', f'空運最快5-7天{FALLBACK}，', 'body_hard', filepath, ln)
        
        # 其他时效数字硬承诺
        modified = replace_in_line(modified, '7-12天送達', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '7-14個工作天送達', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '7-14個工作天', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '3-5個工作日送達', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '3-5個工作日', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '最快2-3天', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '最快2-5天', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        # 补充：特殊时长数字
        modified = replace_in_line(modified, '10-15天送達', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '10-15天', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '12-18天送達', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '3-18天送達', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '5-12天送達', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '5-10 天送達', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '3-7 天送達', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        # 补充：带空格的格式
        modified = replace_in_line(modified, '5-7 天送達', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '10-15 天', f'最快5-7天{FALLBACK}', 'body_hard', filepath, ln)
        # 补充：孤立的天到/天到，/天到。 /天到空白
        modified = replace_in_line(modified, '3-5天到，', f'最快5-7天{FALLBACK}，', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '7-12天到。', f'最快5-7天{FALLBACK}。', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '5-7天到。', f'最快5-7天{FALLBACK}。', 'body_hard', filepath, ln)
        modified = replace_in_line(modified, '5-7天到，', f'最快5-7天{FALLBACK}，', 'body_hard', filepath, ln)
        
        # ============================================================
        # 对比表格 / FAQ 行: 保留不同数字 + "（一般參考）"
        # ============================================================
        # 只处理对比语境: "快速專線5-7天，標準專線5-7天，經濟專線7-12天"
        if re.search(r'[，,].*\d+-\d+\s*天.*[，,].*\d+-\d+\s*天', modified):
            modified = re.sub(r'(\d+-\d+\s*天)(?!.*（)','\\1（一般參考）', modified)
            if modified != orig:
                log(filepath, ln, 'table_ref', orig, modified)
        
        # ============================================================
        # 对比表格: 单独的数字天（如 period 类）
        # ============================================================
        if 'period' in modified or 'class="period"' in modified:
            modified = replace_in_line(modified, '5-7個工作天', f'5-7個工作天（一般參考）', 'table', filepath, ln)
            modified = replace_in_line(modified, '7-12個工作天', f'7-12個工作天（一般參考）', 'table', filepath, ln)
            modified = replace_in_line(modified, '7-14個工作天', f'7-14個工作天（一般參考）', 'table', filepath, ln)
        
        # ============================================================
        # 流程步骤中的时效
        # ============================================================
        modified = replace_in_line(modified, '5-7天送至', f'最快5-7天{FALLBACK}', 'body_step', filepath, ln)
        modified = replace_in_line(modified, '5-7天簽收', f'一般5-7天{FALLBACK}', 'body_step', filepath, ln)
        
        # ============================================================
        # 副标题/横幅
        # ============================================================
        modified = replace_in_line(modified, '5-7 個工作天送達', f'最快5-7天{FALLBACK}', 'body_subtitle', filepath, ln)
        modified = replace_in_line(modified, '7-12 個工作天', f'最快5-7天{FALLBACK}', 'body_subtitle', filepath, ln)
        
        # ============================================================
        # 清理: 重复"最快+最快"前缀
        # ============================================================
        modified = modified.replace(f'最快最快5-7天{FALLBACK}', f'最快5-7天{FALLBACK}')
        modified = modified.replace(f'最快最快5-7天{FALLBACK_SHORT}', f'最快5-7天{FALLBACK_SHORT}')
        modified = modified.replace(f'最快最快5-7天{TITLE_SUFFIX}', f'最快5-7天{TITLE_SUFFIX}')
        # Meta 中防止 "最快5-7天（空運）" 被再次匹配
        modified = modified.replace('最快5-7天（空運）5-7天', '最快5-7天（空運）')
        modified = modified.replace('（空運）（空運）', '（空運）')
        modified = modified.replace('（空運）最快5-7天', '最快5-7天（空運）')
        
        # ============================================================
        # 清理: 重复兜底句 (在正文替换后)
        # ============================================================
        modified = modified.replace(f'{FALLBACK}{FALLBACK}', FALLBACK)
        modified = modified.replace(f'{FALLBACK_SHORT}{FALLBACK_SHORT}', FALLBACK_SHORT)
        modified = modified.replace(f'{FALLBACK}{FALLBACK_SHORT}', FALLBACK)
        modified = modified.replace(f'{FALLBACK_SHORT}{FALLBACK}', FALLBACK)
        
        # 清理: 重复正文替换后的 "最快5-7天最快5-7天"
        modified = modified.replace(f'最快5-7天{FALLBACK}最快5-7天', f'最快5-7天{FALLBACK}')
        
        if modified != line.rstrip('\n'):
            new_lines.append(modified + ('\n' if i < len(lines)-1 else ''))
        else:
            new_lines.append(line)
    
    return ''.join(new_lines)


def process_file(filepath):
    if not filepath.endswith('.html'):
        return
    basename = os.path.basename(filepath)
    if basename in ['article-list.html']:
        return
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ⚠️ 读取失败 {filepath}: {e}")
        return False
    
    new_content = process_text(content, filepath)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--files', nargs='+', default=[])
    parser.add_argument('--dirs', nargs='+', default=['.', 'blog'])
    args = parser.parse_args()
    
    files_to_process = []
    if args.files:
        files_to_process = [os.path.join(BASE_DIR, f) for f in args.files]
    else:
        for d in args.dirs:
            target_dir = os.path.join(BASE_DIR, d)
            if not os.path.isdir(target_dir):
                continue
            for root, dirs, filenames in os.walk(target_dir):
                dirs[:] = [d for d in dirs if d not in
                    ['assets','images','js','tools','widget','.workbuddy','_qa-screenshots-2026-07-12']]
                for fname in filenames:
                    if fname.endswith('.html'):
                        files_to_process.append(os.path.join(root, fname))
    
    modified_count = 0
    for filepath in sorted(files_to_process):
        if args.dry_run:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                new_content = process_text(content, filepath)
                if new_content != content:
                    cnt = len(changes.get(filepath, []))
                    print(f"📝 {os.path.relpath(filepath, BASE_DIR)} ({cnt}处)")
                    for c in changes.get(filepath, []):
                        print(c)
                    print()
            except Exception as e:
                print(f"⚠️ {filepath}: {e}")
        else:
            if process_file(filepath):
                modified_count += 1
                cnt = len(changes.get(filepath, []))
                print(f"✅ {os.path.relpath(filepath, BASE_DIR)} ({cnt}处)")
    
    if not args.dry_run:
        print(f"\n✅ 修改 {modified_count}/{len(files_to_process)} 个文件")
    
    total = sum(len(v) for v in changes.values())
    print(f"📊 总计 {total} 处: title={stats.get('title',0)} meta={stats.get('meta',0)} schema={stats.get('schema',0)} h1={stats.get('h1',0)} body_hard={stats.get('body_hard',0)} table={stats.get('table',0)}")
    if not args.dry_run and modified_count == 0:
        print("⚠️ 无文件被修改，检查匹配模式")


if __name__ == '__main__':
    main()
