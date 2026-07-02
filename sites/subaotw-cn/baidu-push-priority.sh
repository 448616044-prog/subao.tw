#!/bin/bash
# 高优先级百度推送 — 凌晨00:01执行，抢每日配额
# 推送顺序：首页 → 新内容页 → 孤页

API="http://data.zz.baidu.com/urls?site=https://www.subaotw.cn&token=K4kVPs6NwjtWr4ij"
LOG="/tmp/baidu-push-priority.log"

# 优先URL列表（前10个最重要）
URLS=(
  "https://www.subaotw.cn/"
  "https://www.subaotw.cn/article-list"
  "https://www.subaotw.cn/sitemap.xml"
  "https://www.subaotw.cn/tw-to-cn/"
  "https://www.subaotw.cn/blog/food-shipping-guide"
  "https://www.subaotw.cn/blog/tea-shipping-guide"
  "https://www.subaotw.cn/blog/noodles-ramen-shipping"
  "https://www.subaotw.cn/tw-to-cn/noodles-to-cn"
  "https://www.subaotw.cn/tw-to-cn/taiwan-snacks-to-cn"
  "https://www.subaotw.cn/tw-to-cn/birds-nest-to-cn"
  "https://www.subaotw.cn/tw-to-cn/perfume-to-cn"
  "https://www.subaotw.cn/tw-to-cn/chinese-medicine-to-cn"
  "https://www.subaotw.cn/tw-to-cn/glucose-meter-to-cn"
  "https://www.subaotw.cn/blog/clothes-to-taiwan"
  "https://www.subaotw.cn/blog/food-to-taiwan"
  "https://www.subaotw.cn/blog/furniture-to-taiwan"
  "https://www.subaotw.cn/blog/home-appliances-to-taiwan"
  "https://www.subaotw.cn/blog/daily-items-to-taiwan"
  "https://www.subaotw.cn/tw-to-cn/homemade-food-to-cn"
  "https://www.subaotw.cn/tw-to-cn/commercial-goods-to-cn"
  "https://www.subaotw.cn/tw-to-cn/computer-parts-to-cn"
  "https://www.subaotw.cn/tw-to-cn/customs-tax-guide"
  "https://www.subaotw.cn/tw-to-cn/personal-items-to-cn"
  "https://www.subaotw.cn/tw-to-cn/shipping-channel-compare"
  "https://www.subaotw.cn/tw-to-cn/taiwanese-in-china-guide"
)

# 取前10个
BATCH=$(printf '%s\n' "${URLS[@]}" | head -10)
DATA=$(echo "$BATCH" | tr '\n' '\n')

RESP=$(curl -s -w "\n%{http_code}" -H "Content-Type: text/plain" --data "$DATA" "$API" 2>&1)
CODE=$(echo "$RESP" | tail -1)
BODY=$(echo "$RESP" | head -1)

echo "[$(date '+%Y-%m-%d %H:%M:%S')] HTTP $CODE: $BODY" >> "$LOG"

if echo "$BODY" | grep -q '"success"'; then
    echo "✅ 推送成功" >> "$LOG"
else
    echo "❌ $BODY" >> "$LOG"
fi
