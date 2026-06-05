#!/usr/bin/env python3
"""Fix duplicate formsubmit + missing floating bars."""
import re, os

SITE_DIR = "/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn"

# Pages with duplicate formsubmit
DUP_FILES = [
    "contact-form.html",
    "blog/electronics-shipping.html",
    "blog/food-shipping-guide.html",
    "blog/health-products-shipping.html",
    "blog/personal-belongings-shipping.html",
    "blog/taiwan-medicine-to-china.html",
    "blog/tea-shipping-guide.html",
    "blog/tw-to-cn-prohibited-items.html",
]

# Page missing floating bar
NO_FLOAT = "blog/taiwan-souvenir-shipping.html"

for rel in DUP_FILES:
    fp = os.path.join(SITE_DIR, rel)
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # Count submitContactForm occurrences
    count = content.count('function submitContactForm')
    if count <= 1:
        print(f"  ✅ {rel}: no duplicate (count={count})")
        continue

    print(f"  🔧 {rel}: removing {count-1} duplicate(s)")

    # Strategy: remove the second occurrence.
    # Find first occurrence position, then find and remove the second one.
    first_pos = content.find('function submitContactForm')
    second_pos = content.find('function submitContactForm', first_pos + 1)

    if second_pos > -1:
        # The duplicate function is part of a repeated floating bar block.
        # Remove from the second function definition through to the closing of its script block.
        # The floating bar block starts with <style>, has contact form HTML, and <script>.
        # We need to remove the entire duplicate floating bar section.

        # Find the start of the duplicate section - look for the <!-- 悬浮按钮组 --> or <style> before the duplicate function
        # Search backwards from second_pos for the floating bar start
        search_start = max(0, second_pos - 5000)
        chunk = content[search_start:second_pos]

        # Find the last <!-- 悬浮按钮组 --> before the duplicate
        float_start_marker = chunk.rfind('<!-- 悬浮按钮组 -->')
        if float_start_marker == -1:
            float_start_marker = chunk.rfind('悬浮按钮组')
        if float_start_marker == -1:
            float_start_marker = chunk.rfind('.floating-bar{')
            if float_start_marker > -1:
                float_start_marker = chunk.rfind('<style>', 0, float_start_marker)

        if float_start_marker > -1:
            actual_start = search_start + float_start_marker

            # Find the end of this duplicate block - look for </script> after the duplicate function
            after_dup = content[second_pos:]
            # Find closing script tag after the duplicate function
            script_end = after_dup.find('</script>')
            if script_end > -1:
                # Also find the closing div for contact-modal if it exists
                modal_end = after_dup.find('</div>', script_end)
                # Find end of the section
                end_marker = max(script_end + 9, modal_end + 6 if modal_end > -1 else 0)
                # Also look for next <!-- comment --> or <footer or </body
                next_section = re.search(r'<!-- |<footer|<div class="mobile|</body', after_dup[end_marker:])
                if next_section:
                    actual_end = second_pos + end_marker + next_section.start()
                else:
                    actual_end = second_pos + end_marker + 100  # safe cutoff

                # Remove the duplicate section
                content = content[:actual_start] + content[actual_end:]
                print(f"     removed {actual_end - actual_start} chars of duplicate floating bar")
        else:
            # Fallback: just remove the duplicate function
            # Find the beginning of the script block for the duplicate
            before = content[:second_pos]
            script_start = before.rfind('<script>')
            if script_start == -1:
                script_start = before.rfind('<script')
            if script_start > -1:
                # Remove from script start to after function end
                func_end = content.find('</script>', second_pos)
                if func_end > -1:
                    content = content[:script_start] + content[func_end + 9:]
                    print(f"     fallback: removed duplicate script block")

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)

# Fix missing floating bar
fp = os.path.join(SITE_DIR, NO_FLOAT)
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

if 'floating-bar' in content:
    print(f"  ✅ {NO_FLOAT}: already has floating bar")
else:
    # Read a floating bar template from a working page
    ref_fp = os.path.join(SITE_DIR, 'blog/tea-shipping-guide.html')
    with open(ref_fp, 'r', encoding='utf-8') as f:
        ref = f.read()

    # Extract floating bar section
    float_start = ref.find('<!-- 悬浮按钮组 -->')
    if float_start == -1:
        # Search for the floating bar CSS
        float_start = ref.find('.floating-bar{')
        if float_start > -1:
            float_start = ref.rfind('<style>', 0, float_start)

    if float_start > -1:
        # Find end of the floating bar + contact modal + script
        contact_end = ref.find('</script>', float_start)
        # Find the closing of the actual script block
        script_close = ref.find('\n</script>', contact_end)
        # Go to the next section marker
        end_marker = ref.find('</body>', contact_end)
        if end_marker == -1:
            end_marker = ref.find('</html>', contact_end)

        float_block = ref[float_start:end_marker]

        # Insert before </body>
        body_end = content.rfind('</body>')
        if body_end > -1:
            content = content[:body_end] + '\n' + float_block + '\n' + content[body_end:]
            print(f"  ✅ {NO_FLOAT}: added floating bar ({len(float_block)} chars)")
        else:
            print(f"  ⚠️  {NO_FLOAT}: no </body> found")
    else:
        print(f"  ⚠️  {NO_FLOAT}: couldn't find floating bar template")

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)

print("\nDone!")
