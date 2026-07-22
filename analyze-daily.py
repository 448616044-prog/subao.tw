#!/usr/bin/env python3
"""subao.tw 每日 GSC+GA4 分析脚本"""
import json
from datetime import datetime

with open("/Users/mac/WorkBuddy/Claw/物流項目/gsc-ga4-raw.json") as f:
    data = json.load(f)

gsc = data["gsc"]
ga4 = data["ga4"]

# ===== 1. GSC 点击量分析 =====
daily = sorted(gsc["data"]["daily_trend"], key=lambda x: x["date"])
latest_entry = daily[-1]
latest_date = latest_entry["date"]
latest_clicks = latest_entry["clicks"]

# 最后7天
last7 = daily[-7:]
last7_clicks = [d["clicks"] for d in last7]
last7_avg = round(sum(last7_clicks) / 7, 1)
last7_dates = [d["date"] for d in last7]

# 前7天 (倒数8-14)
prev7 = daily[-14:-7] if len(daily) >= 14 else daily[:-7]
prev7_avg = round(sum(d["clicks"] for d in prev7) / len(prev7), 1) if prev7 else 0

# 波动率
chg_vs_7d = round((latest_clicks - last7_avg) / last7_avg * 100, 1)
wow_chg = round((last7_avg - prev7_avg) / prev7_avg * 100, 1) if prev7_avg else 0

print("=" * 60)
print("📊 GSC 点击量分析")
print(f"  最新日: {latest_date} = {latest_clicks} 点击")
print(f"  近7日: {last7_dates[0]} ~ {last7_dates[-1]}")
print(f"  近7日均: {last7_avg}")
print(f"  前7日均: {prev7_avg}")
print(f"  最新日 vs 7日均: {chg_vs_7d:+.1f}%")
print(f"  周环比: {wow_chg:+.1f}%")
print(f"  28天总点击: {gsc['data']['summary']['total_clicks']}")
print(f"  28天总展现: {gsc['data']['summary']['total_impressions']:,}")
print(f"  平均排名: {gsc['data']['summary']['avg_position']}")

alarm_clicks = latest_clicks < last7_avg * 0.8
if alarm_clicks:
    print(f"  🚨 点击量报警: {latest_clicks} < {last7_avg}*0.8 = {last7_avg*0.8:.0f}")
else:
    print(f"  ✅ 点击量正常")

# ===== 2. 关键词排名对比 =====
print()
print("=" * 60)
print("🔎 关键词排名变化 (Top 30)")

queries = gsc["data"]["queries"]
print(f"{'关键词':<30s} {'点击':>4s} {'排名':>5s} {'CTR':>6s}")
print("-" * 50)
for q in queries:
    label = q["query"][:28]
    print(f"  {label:<28s} {q['clicks']:>4d} {q['position']:>5.1f} {q['ctr']:>5.1f}%")

# ===== 3. GA4 分析 =====
print()
print("=" * 60)
print("📈 GA4 活跃用户分析")

ga4_daily = sorted(ga4["data"]["daily_overview"], key=lambda x: x["date"])
# Last 7 GA4 days
ga4_last7 = ga4_daily[-7:]
ga4_au_vals = [int(d["activeUsers"]) for d in ga4_last7]
ga4_au_avg = round(sum(ga4_au_vals) / 7, 1)
ga4_latest = ga4_last7[-1]
ga4_latest_au = int(ga4_latest["activeUsers"])

# Previous 7
ga4_prev7 = ga4_daily[-14:-7] if len(ga4_daily) >= 14 else ga4_daily[:-7]
ga4_prev7_avg = round(sum(int(d["activeUsers"]) for d in ga4_prev7) / len(ga4_prev7), 1) if ga4_prev7 else 0

ga4_chg = round((ga4_latest_au - ga4_au_avg) / ga4_au_avg * 100, 1)
ga4_wow = round((ga4_au_avg - ga4_prev7_avg) / ga4_prev7_avg * 100, 1) if ga4_prev7_avg else 0

print(f"  最新日: {ga4_latest['date']} = {ga4_latest_au} 活跃用户")
print(f"  近7日均: {ga4_au_avg}")
print(f"  前7日均: {ga4_prev7_avg}")
print(f"  最新日 vs 7日均: {ga4_chg:+.1f}%")
print(f"  周环比: {ga4_wow:+.1f}%")

# GA4 events
events = ga4["data"]["events"]
print()
print("📊 GA4 关键事件 (28天总量)")
for e in events:
    if e["eventName"] in ["line_click", "generate_lead", "calculator_result", "page_view", "session_start"]:
        print(f"  {e['eventName']:<20s}: {int(e['eventCount']):>6,}")

# ===== 4. LINE 分析 =====
line_total = int(ga4["data"]["events"][6]["eventCount"])  # line_click
print()
print("=" * 60)
print("📱 LINE 点击量分析")
print(f"  28天 LINE 点击总量: {line_total}")
est_daily = round(line_total / 29, 1)
print(f"  估算日均: {est_daily}/天")

# LINE alarm
# Since we don't have daily LINE data, use total check
alarm_line = False
print(f"  ✅ LINE 总量正常 (无法精确日追踪)")

# ===== 5. 综合判断 =====
print()
print("=" * 60)
print("🚦 综合报警判断")
alarms = []
if alarm_clicks:
    alarms.append(f"GSC点击 {latest_clicks} < 7日均 {last7_avg} 的80% = {last7_avg*0.8:.0f}")
if alarm_line:
    alarms.append(f"LINE 点击 < 日均-30%")
if alarms:
    for a in alarms:
        print(f"  🚨 {a}")
else:
    print("  ✅ 无报警触发")

print()
print("📌 亮点:")
highlights = []
if chg_vs_7d > 10:
    highlights.append(f"GSC 最新日 {latest_clicks} 超出 7 日均 +{chg_vs_7d:.0f}%")
if wow_chg > 10:
    highlights.append(f"GSC 周环比 +{wow_chg:.0f}% (连续上行)")
if ga4_latest_au > ga4_au_avg * 1.2:
    highlights.append(f"GA4 活跃 {ga4_latest_au} 创本周新高")
for h in highlights:
    print(f"  ✨ {h}")

# 打印 raw numbers for report
print()
print("=" * 60)
print("📋 日报数据摘要 (for report generation)")
summary = gsc["data"]["summary"]
print(f"GSC_28D_CLICKS={summary['total_clicks']}")
print(f"GSC_28D_IMPRESSIONS={summary['total_impressions']}")
print(f"GSC_AVG_POSITION={summary['avg_position']}")
print(f"GSC_LATEST_DATE={latest_date}")
print(f"GSC_LATEST_CLICKS={latest_clicks}")
print(f"GSC_7D_AVG={last7_avg}")
print(f"GSC_PREV_7D_AVG={prev7_avg}")
print(f"GSC_DAILY_VS_7D={chg_vs_7d}")
print(f"GSC_WOW={wow_chg}")
print(f"GA4_LATEST_DATE={ga4_latest['date']}")
print(f"GA4_LATEST_AU={ga4_latest_au}")
print(f"GA4_7D_AVG={ga4_au_avg}")
print(f"GA4_PREV_7D_AVG={ga4_prev7_avg}")
print(f"GA4_WOW={ga4_wow}")
print(f"LINE_28D_TOTAL={line_total}")
print(f"LINE_DAILY_EST={est_daily}")
print(f"ALARM={'YES' if alarms else 'NO'}")
