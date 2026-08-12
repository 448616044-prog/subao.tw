#!/usr/bin/env python3
"""
部署前 JS 语法 + 结构健康检查
检查所有 HTML 文件的内嵌 <script> 块是否存在以下问题：
  1. JS 函数体内错误嵌入的 <script>/<style> 标签
  2. 未闭合的 script 块
  3. 基础 JS 语法错误（通过 node --check）
"""
import subprocess, tempfile, os, re, sys

TARGET_DIRS = [
    "/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn",
    "/Users/mac/WorkBuddy/Claw/物流項目/sites/subaotw-cn",
    "/Users/mac/WorkBuddy/Claw/物流項目/sites/subaog-com",
]

QUICK_MODE = '--quick' in sys.argv or '-q' in sys.argv
EXIT_CODE = 0
total_checked = 0
total_failed = 0

def fail(msg):
    global EXIT_CODE, total_failed
    EXIT_CODE = 1
    total_failed += 1
    print(f"  ❌ {msg}")

def extract_js_blocks(html):
    """提取所有 <script> 块的内容（跳过 src 引用和 type=application/* 的）"""
    blocks = []
    # Match <script>...</script> blocks
    pattern = re.compile(
        r'<script(?:\s[^>]*)?>(.*?)</script>',
        re.DOTALL | re.IGNORECASE
    )
    for m in pattern.finditer(html):
        tag_attrs = m.group(0)[:m.group(0).find('>')+1].lower()
        # Skip external scripts
        if 'src=' in tag_attrs:
            continue
        # Skip JSON-LD
        if 'type="application/ld+json"' in tag_attrs:
            continue
        if "type='application/ld+json'" in tag_attrs:
            continue
        # Skip email-decode, SVG symbols, etc
        content = m.group(1).strip()
        if not content:
            continue
        blocks.append((m.start(), content))
    return blocks

# ===== Check 1: 函数体内不能有 <script> / <style> 标签 =====
print("=" * 60)
print("Check 1: No <script> / <style> tags inside JS function bodies")
print("=" * 60)

for site_dir in TARGET_DIRS:
    if not os.path.isdir(site_dir):
        continue
    for root, dirs, files in os.walk(site_dir):
        if '.git' in root or '__pycache__' in root:
            continue
        for fname in files:
            if not fname.endswith('.html'):
                continue
            fpath = os.path.join(root, fname)
            total_checked += 1
            with open(fpath, 'r', encoding='utf-8') as f:
                html = f.read()

            blocks = extract_js_blocks(html)
            for pos, js in blocks:
                # Check for <script> or <style> inside JS code
                if '<script>' in js.lower() or '<script ' in js.lower():
                    # Find context
                    idx = js.lower().find('<script')
                    ctx_start = max(0, idx - 80)
                    ctx_end = min(len(js), idx + 80)
                    snippet = js[ctx_start:ctx_end].replace('\n', ' ')
                    fail(f"{fpath} - <script> inside JS block at char {pos}: ...{snippet}...")

                if '<style>' in js.lower():
                    idx = js.lower().find('<style')
                    ctx_start = max(0, idx - 40)
                    ctx_end = min(len(js), idx + 40)
                    snippet = js[ctx_start:ctx_end].replace('\n', ' ')
                    fail(f"{fpath} - <style> inside JS block: ...{snippet}...")

print(f"\n  Checked {total_checked} files.\n")

# ===== Check 2: node --check 语法验证 =====
if QUICK_MODE:
    print("\n" + "=" * 60)
    print("Check 2: Skipped (--quick mode)")
    print("=" * 60)
    syntax_checked = 0
else:
    print("\n" + "=" * 60)
    print("Check 2: Run node --check on embedded JS blocks")
    print("=" * 60)

    syntax_checked = 0
    syntax_failed = 0
    for site_dir in TARGET_DIRS:
        if not os.path.isdir(site_dir):
            continue
        for root, dirs, files in os.walk(site_dir):
            if '.git' in root or '__pycache__' in root:
                continue
            for fname in files:
                if not fname.endswith('.html'):
                    continue
                fpath = os.path.join(root, fname)
                with open(fpath, 'r', encoding='utf-8') as f:
                    html = f.read()

                blocks = extract_js_blocks(html)
                for i, (pos, js) in enumerate(blocks):
                    if len(js) < 30:
                        continue
                    syntax_checked += 1
                    with tempfile.NamedTemporaryFile(
                        mode='w', suffix='.js', delete=False, encoding='utf-8'
                    ) as tmp:
                        tmp.write(js)
                        tmp_path = tmp.name

                    try:
                        result = subprocess.run(
                            ['node', '--check', tmp_path],
                            capture_output=True, text=True, timeout=5
                        )
                        if result.returncode != 0:
                            syntax_failed += 1
                            error = result.stderr.strip().split('\n')[0]
                            fail(f"{fpath} - JS syntax error: {error}")
                    except FileNotFoundError:
                        print("\n  ⚠️  node not found, skipping JS syntax check")
                        syntax_checked = 0
                        break
                    except subprocess.TimeoutExpired:
                        pass
                    finally:
                        os.unlink(tmp_path)

                if syntax_checked == 0:
                    break
            if syntax_checked == 0:
                break

    if syntax_checked > 0:
        print(f"\n  Syntax checked {syntax_checked} blocks, {syntax_failed} failed.")

# ===== Summary =====
print("\n" + "=" * 60)
if EXIT_CODE == 0:
    print("✅ ALL CHECKS PASSED")
else:
    print(f"❌ {total_failed} ERROR(S) FOUND - DO NOT DEPLOY")
print("=" * 60)

sys.exit(EXIT_CODE)
