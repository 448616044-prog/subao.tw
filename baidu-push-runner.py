#!/usr/bin/env python3
"""百度每日主动推送 — subaotw.cn 轮转式推送（每次5条）"""
import xml.etree.ElementTree as ET
import requests
import os
from datetime import datetime, timezone, timedelta

SITEMAP_PATH = "/Users/mac/WorkBuddy/Claw/物流項目/sites/subaotw-cn/sitemap.xml"
LOG_PATH = "/Users/mac/WorkBuddy/Claw/物流項目/baidu-push-log.md"
BAIDU_API = "http://data.zz.baidu.com/urls?site=www.subaotw.cn&token=K4kVPs6NwjtWr4ij"
PUSH_SIZE = 5

# ---- 1. Parse sitemap, get unique URLs in document order ----
ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
tree = ET.parse(SITEMAP_PATH)
root = tree.getroot()
all_urls = []
seen = set()
for url_el in root.findall("s:url", ns):
    loc_el = url_el.find("s:loc", ns)
    if loc_el is not None and loc_el.text:
        url = loc_el.text.strip()
        if url not in seen:
            seen.add(url)
            all_urls.append(url)

total = len(all_urls)
print(f"📡 Sitemap 共 {total} 个唯一URL")

# ---- 2. Determine rotation index from existing log ----
tz_8 = timezone(timedelta(hours=8))
now = datetime.now(tz_8)
last_index = -1
if os.path.exists(LOG_PATH):
    with open(LOG_PATH, "r") as f:
        lines = f.readlines()
    # Find the last "next_start" info
    for line in reversed(lines):
        if line.startswith("## next_start:"):
            try:
                last_index = int(line.split("next_start:")[1].strip())
            except ValueError:
                pass
            break

start_idx = last_index + 1 if last_index >= 0 else 0
# Wrap around if needed
start_idx = start_idx % total
end_idx = min(start_idx + PUSH_SIZE, total)
batch = all_urls[start_idx:end_idx]

# If we don't have enough at the end, wrap around
if len(batch) < PUSH_SIZE:
    batch += all_urls[: PUSH_SIZE - len(batch)]

print(f"📤 本次推送起点: {start_idx}, URL数: {len(batch)}")
for i, u in enumerate(batch):
    print(f"  {start_idx + i}. {u}")

# ---- 3. Push to Baidu ----
data = "\n".join(batch)
result = None
error = None
try:
    resp = requests.post(
        BAIDU_API,
        data=data.encode("utf-8"),
        headers={"Content-Type": "text/plain"},
        timeout=30,
    )
    result = resp.json()
    print(f"\n📨 百度API返回: {result}")
except Exception as e:
    error = str(e)
    print(f"\n❌ 推送失败: {e}")

# ---- 4. Calculate next start for next run ----
next_start = (start_idx + PUSH_SIZE) % total

# ---- 5. Append to log ----
date_str = now.strftime("%Y-%m-%d %H:%M")
entry_lines = [
    f"\n## {date_str}\n",
    f"- **推送URL数**: {len(batch)}\n",
    f"- **起点索引**: {start_idx}\n",
]
for i, u in enumerate(batch):
    entry_lines.append(f"- [{start_idx + i}] {u}\n")

if result:
    entry_lines.append(f"- **API返回**: `{result}`\n")
if error:
    entry_lines.append(f"- **错误**: {error}\n")
entry_lines.append(f"\n## next_start: {next_start}\n")

# Create or append
if not os.path.exists(LOG_PATH):
    header = "# subaotw.cn 百度主动推送日志\n\n> 每天5条URL，轮转式推送\n> \n> API: data.zz.baidu.com\n> Token: K4kVPs6NwjtWr4ij\n"
    with open(LOG_PATH, "w") as f:
        f.write(header)
        f.writelines(entry_lines)
else:
    with open(LOG_PATH, "r") as f:
        old = f.read()
    # Remove old next_start lines
    lines_out = []
    for line in old.split("\n"):
        if not line.startswith("## next_start:"):
            lines_out.append(line)
    new_content = "\n".join(lines_out) + "".join(entry_lines)
    with open(LOG_PATH, "w") as f:
        f.write(new_content)

print(f"\n✅ 日志已写入 {LOG_PATH}")
print(f"🔄 下次起点索引: {next_start}")
