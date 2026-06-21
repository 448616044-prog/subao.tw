#!/bin/bash
# Baidu daily URL push — cron: 0 8 * * * cd /var/www/subaotw-cn && bash baidu-daily-push.sh
# Quota: ~10-20 URLs/day for new sites (over quota = skip, try tomorrow)

cd "$(dirname "$0")"

API="http://data.zz.baidu.com/urls?site=https://www.subaotw.cn&token=K4kVPs6NwjtWr4ij"
TODAY=$(date +%Y-%m-%d)
LOG="/tmp/baidu-push-subaotw.log"

# Find recently changed files (last 24h)
CHANGED=$(find . -name "*.html" -mtime -1 ! -name "404.html" 2>/dev/null | head -20)

if [ -z "$CHANGED" ]; then
  # Fallback: push key index pages
  URLS=(
    "https://www.subaotw.cn/"
    "https://www.subaotw.cn/tw-to-cn/"
    "https://www.subaotw.cn/equipment/"
    "https://www.subaotw.cn/guide/"
    "https://www.subaotw.cn/article-list"
    "https://www.subaotw.cn/sitemap-page"
  )
else
  URLS=()
  for f in $CHANGED; do
    f="${f#./}"
    f="${f/.html/}"
    [[ "$f" == *"/index" ]] && f="${f%/index}"
    URLS+=("https://www.subaotw.cn/$f")
  done
fi

count=0
skipped=0
for url in "${URLS[@]}"; do
  result=$(curl -s -X POST "$API" -H "Content-Type: text/plain" -d "$url" 2>&1)
  echo "[$TODAY] $url → $result" >> "$LOG"
  if echo "$result" | grep -q '"success"'; then
    ((count++))
  elif echo "$result" | grep -q 'over quota'; then
    ((skipped++))
    echo "[$TODAY] Quota exceeded, stopping after $count successful" >> "$LOG"
    break
  fi
  sleep 1
done

echo "[$TODAY] Done: $count pushed, $skipped skipped (quota)" >> "$LOG"
