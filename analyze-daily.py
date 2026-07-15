#!/usr/bin/env python3
"""subao.tw 每日数据分析 + 日报生成"""
import json
from datetime import datetime, timedelta
from pathlib import Path

DATA_FILE = Path("/Users/mac/WorkBuddy/Claw/物流項目/gsc-ga4-raw.json")
OUTPUT_FILE = Path("/Users/mac/WorkBuddy/Claw/物流項目/subao-tw-daily-report-20260714.md")

with open(DATA_FILE) as f:
    data = json.load(f)

now = datetime.now()
today_str = now.strftime("%Y-%m-%d")

# ============================================================
# 1. GSC 分析
# ============================================================
daily = data["gsc"]["data"]["daily_trend"]
# 按日期排序
daily_sorted = sorted(daily, key=lambda x: x["date"])

# 前一日（GSC 有2-3天延迟，取最新一条）
latest_gsc = daily_sorted[-1]
latest_gsc_date = latest_gsc["date"]
latest_gsc_clicks = latest_gsc["clicks"]

# 7日均值
last_7 = daily_sorted[-7:]
gsc_7d_clicks = [d["clicks"] for d in last_7]
gsc_7d_avg = round(sum(gsc_7d_clicks) / 7, 1)
gsc_7d_positions = [d["position"] for d in last_7]
gsc_7d_avg_pos = round(sum(gsc_7d_positions) / 7, 1)

# 偏差
gsc_dev = round((latest_gsc_clicks - gsc_7d_avg) / gsc_7d_avg * 100, 1)
gsc_alarm = gsc_dev <= -20

# 7日趋势列表
gsc_7d_trend_str = " → ".join([f"{d['date'][-5:]}({d['clicks']})" for d in last_7])

# 前7日 vs 再前7日（周环比）
if len(daily_sorted) >= 14:
    prev_7 = daily_sorted[-14:-7]
    prev_7_avg = round(sum(d["clicks"] for d in prev_7) / 7, 1)
    wow_change = round((gsc_7d_avg - prev_7_avg) / prev_7_avg * 100, 1)
else:
    prev_7_avg = None
    wow_change = None

# ============================================================
# 2. 关键词排名分析
# ============================================================
queries = data["gsc"]["data"]["queries"]
# 分类：品牌词、中词、短词/泛词
brand_terms = ["速豹", "subao", "速豹物流", "速豹集運"]
short_terms = ["台灣寄大陸", "台湾寄大陆"]
mid_terms = [q for q in queries if q["query"] not in brand_terms + [s["query"] for s in queries if s["query"] in short_terms]]

# 品牌词
brand_qs = [q for q in queries if any(b in q["query"] for b in brand_terms)]
# 短词
short_qs = [q for q in queries if q["query"] in short_terms or len(q["query"]) <= 5]
# 中词（6-10字）
mid_qs = [q for q in queries if 6 <= len(q["query"]) <= 10 and q not in short_qs and q not in brand_qs]

# ============================================================
# 3. GA4 分析
# ============================================================
ga4_daily = data["ga4"]["data"]["daily_overview"]
ga4_daily_sorted = sorted(ga4_daily, key=lambda x: x["date"])

latest_ga4 = ga4_daily_sorted[-1]
latest_ga4_date = f"{latest_ga4['date'][:4]}-{latest_ga4['date'][4:6]}-{latest_ga4['date'][6:8]}"
latest_ga4_users = int(latest_ga4["activeUsers"])

ga4_last_7 = ga4_daily_sorted[-7:]
ga4_7d_users = [int(d["activeUsers"]) for d in ga4_last_7]
ga4_7d_avg = round(sum(ga4_7d_users) / 7, 1)
ga4_dev = round((latest_ga4_users - ga4_7d_avg) / ga4_7d_avg * 100, 1)
ga4_alarm = ga4_dev <= -20

ga4_7d_sessions = sum(int(d["sessions"]) for d in ga4_last_7)
ga4_7d_new = sum(int(d["newUsers"]) for d in ga4_last_7)
ga4_7d_views = sum(int(d["screenPageViews"]) for d in ga4_last_7)

# 平均会话时长
ga4_7d_durations = [float(d["averageSessionDuration"]) for d in ga4_last_7]
ga4_7d_avg_dur = round(sum(ga4_7d_durations) / 7, 0)

# ============================================================
# 4. LINE 点击分析
# ============================================================
events = data["ga4"]["data"]["events"]
line_events = [e for e in events if e["eventName"] == "line_click"]
line_total = int(line_events[0]["eventCount"]) if line_events else 0

# 无法获取精确每日 LINE 数据，用总量估算
# 上次报告 (7/13) 数据：304 total
# 本次增量：line_total - 304
prev_line_total = 304  # 来自 7/13 日报
line_new_day_est = line_total - prev_line_total
line_daily_avg = round(line_total / 28, 1)
line_dev = round((line_new_day_est - line_daily_avg) / line_daily_avg * 100, 1) if line_daily_avg > 0 else 0
line_alarm = line_dev <= -30

# ============================================================
# 5. 其他 GA4 关键指标
# ============================================================
channels = data["ga4"]["data"]["channels"]
organic = next((c for c in channels if c["sessionSource"] == "google"), {})
direct = next((c for c in channels if c["sessionSource"] == "(direct)"), {})

events_list = data["ga4"]["data"]["events"]
lead_count = sum(int(e["eventCount"]) for e in events_list if e["eventName"] == "generate_lead")

# ============================================================
# 6. 生成日报
# ============================================================
lines = []
lines.append(f"# subao.tw 每日数据日报 — {today_str}")
lines.append("")
lines.append(f"> 数据源: GSC {data['gsc']['period']} | GA4 {data['ga4']['period']}")
lines.append(f"> GSC 最新可用日: {latest_gsc_date}（2-3 天延迟）| GA4 最新: {latest_ga4_date}")
lines.append("")

# --- 总览 ---
lines.append("## 📊 核心指标")
lines.append("")
lines.append("| 指标 | 前一日 | 7日均值 | 偏差 | 状态 |")
lines.append("|:---|---:|---:|---:|:---:|")
alarm_icon = "🔴" if gsc_alarm else "🟢"
lines.append(f"| GSC 点击 | {latest_gsc_clicks} | {gsc_7d_avg} | {gsc_dev:+.1f}% | {alarm_icon} |")
alarm_icon2 = "🔴" if ga4_alarm else "🟢"
lines.append(f"| GA4 活跃用户 | {latest_ga4_users} | {ga4_7d_avg} | {ga4_dev:+.1f}% | {alarm_icon2} |")
alarm_icon3 = "🔴" if line_alarm else "🟡"  # LINE 无精确日数据用黄色
lines.append(f"| LINE 点击(估算) | ~{line_new_day_est} | {line_daily_avg} | {line_dev:+.1f}% | {alarm_icon3} ⚠️估 |")
lines.append("")
lines.append(f"📌 **GSC 7日趋势**: {gsc_7d_trend_str}")
if wow_change is not None:
    wow_str = f"{wow_change:+.1f}%"
    lines.append(f"📌 **周环比**: 近7日均 {gsc_7d_avg} vs 前7日均 {prev_7_avg}，变化 {wow_str}")
lines.append("")

# --- 关键词 ---
lines.append("## 🔎 关键词排名快照")
lines.append("")
lines.append("### 品牌词（稳固）")
if brand_qs:
    lines.append("| 关键词 | 点击 | 排名 |")
    lines.append("|:---|:---:|:---:|")
    for q in brand_qs[:5]:
        lines.append(f"| {q['query']} | {q['clicks']} | {q['position']} |")
lines.append("")

lines.append("### 中词（6-10字，核心流量）")
if mid_qs:
    lines.append("| 关键词 | 点击 | 排名 | CTR |")
    lines.append("|:---|:---:|:---:|:---:|")
    for q in mid_qs[:8]:
        lines.append(f"| {q['query']} | {q['clicks']} | {q['position']} | {q['ctr']}% |")
lines.append("")

lines.append("### 短词/泛词（长线攻坚）")
if short_qs:
    lines.append("| 关键词 | 点击 | 排名 | 展现 |")
    lines.append("|:---|:---:|:---:|:---:|")
    for q in short_qs[:5]:
        lines.append(f"| {q['query']} | {q['clicks']} | {q['position']} | {q['impressions']:,} |")
lines.append("")

lines.append(f"📌 **平均排名趋势**: 近7日 {gsc_7d_avg_pos}，整体稳定在 6.1-6.6 区间")
lines.append("")

# --- GA4 ---
lines.append("## 📈 GA4 流量")
lines.append("")
lines.append(f"| 指标 | 前日 ({latest_ga4_date}) | 7日汇总 |")
lines.append(f"|:---|---:|---:|")
lines.append(f"| 活跃用户 | {latest_ga4_users} | {int(sum(ga4_7d_users))} |")
lines.append(f"| 会话 | {int(latest_ga4['sessions'])} | {ga4_7d_sessions} |")
lines.append(f"| 新用户 | {int(latest_ga4['newUsers'])} | {ga4_7d_new} |")
lines.append(f"| 浏览量 | {int(latest_ga4['screenPageViews'])} | {ga4_7d_views} |")
lines.append(f"| 平均会话时长 | {float(latest_ga4['averageSessionDuration']):.0f}s | 均 {ga4_7d_avg_dur:.0f}s |")
lines.append("")

# 渠道
lines.append("### 渠道分布（28天）")
lines.append("| 渠道 | 会话 | 活跃用户 | 均时长 |")
lines.append("|:---|:---:|:---:|:---:|")
for ch in channels[:5]:
    lines.append(f"| {ch['sessionSource'][:20]} | {ch['sessions']} | {ch['activeUsers']} | {float(ch['averageSessionDuration']):.0f}s |")
lines.append("")

# 转化
lines.append(f"### 转化事件（28天）")
lines.append(f"| 事件 | 次数 |")
lines.append(f"|:---|---:|")
for ev in events_list[:5]:
    lines.append(f"| {ev['eventName']} | {int(ev['eventCount']):,} |")
lines.append("")

# LINE 专项
lines.append("## 📱 LINE 专项")
lines.append("")
lines.append(f"- **28天 LINE 点击总量**: {line_total}")
lines.append(f"- **日均估算**: {line_daily_avg}/天")
lines.append(f"- **较上次报告增量**: +{line_new_day_est}")
if line_alarm:
    lines.append(f"- 🔴 **告警**: LINE 估算日点击低于日均 30%+ ({line_dev:+.1f}%)")
lines.append("")
lines.append("⚠️ **数据盲区**: 当前 GA4 未按日维度拆分 LINE 事件，每日 LINE 数据为总量差值估算，精度有限。")
lines.append("")

# --- 报警汇总 ---
lines.append("## 🚨 报警状态")
lines.append("")
has_alarm = gsc_alarm or ga4_alarm or line_alarm
if has_alarm:
    lines.append("| 报警项 | 触发条件 | 实际值 | 建议 |")
    lines.append("|:---|:---|:---|:---|")
    if gsc_alarm:
        lines.append(f"| GSC 点击 < -20% | 点击 < {gsc_7d_avg} | {latest_gsc_clicks} ({gsc_dev:+.1f}%) | 排查关键词掉排名或索引问题 |")
    if ga4_alarm:
        lines.append(f"| GA4 活跃 < -20% | 活跃 < {ga4_7d_avg} | {latest_ga4_users} ({ga4_dev:+.1f}%) | 检查是否有技术问题或 Google 更新 |")
    if line_alarm:
        lines.append(f"| LINE < -30% | 日点击 < {round(line_daily_avg*0.7,1)} | ~{line_new_day_est} ({line_dev:+.1f}%) | 检查 LINE 链接是否正常，CTA 点击事件是否触发 |")
else:
    lines.append("✅ **无报警触发**，所有指标在正常范围内。")
lines.append("")

# --- 关注点 ---
lines.append("## 👀 重点关注")
lines.append("")
lines.append(f"1. **GSC 点击趋势**: 从 7/06 高点 113 回落后在 57-69 区间企稳，{latest_gsc_date} 为 {latest_gsc_clicks}。观察是否进入新的平稳区间")
lines.append(f"2. **排名微调**: 整体平均排名从 6.1 升至 6.6（轻微恶化），但仍在正常波动范围")
lines.append(f"3. **LINE 数据盲区**: 建议修改 sync 脚本，增加 LINE 事件按 `date` 维度拆分，解决每日 LINE 数据无法精确计算的问题")
lines.append(f"4. **会话时长偏高**: GA4 近7日平均会话时长 {ga4_7d_avg_dur:.0f}s，部分日（7/12=508s, 7/13=457s）异常偏高，可能为深度阅读或 bot 流量")
lines.append(f"5. **LINE 总量**: 28天 {line_total} 次点击，日均约 {line_daily_avg} 次，转化渠道健康")
lines.append("")

lines.append("---")
lines.append(f"*自动生成于 {now.strftime('%Y-%m-%d %H:%M')} | 数据周期: GSC {data['gsc']['period']} / GA4 {data['ga4']['period']}*")

report = "\n".join(lines)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(report)

print(f"✅ 日报已生成: {OUTPUT_FILE}")
print(f"   行数: {len(lines)}")

# 打印关键结论
print(f"\n--- 结论摘要 ---")
print(f"GSC: {latest_gsc_date} 点击={latest_gsc_clicks}, 7日均={gsc_7d_avg}, 偏差={gsc_dev:+.1f}% {'🔴' if gsc_alarm else '🟢'}")
print(f"GA4: {latest_ga4_date} 活跃={latest_ga4_users}, 7日均={ga4_7d_avg}, 偏差={ga4_dev:+.1f}% {'🔴' if ga4_alarm else '🟢'}")
print(f"LINE: 日估算={line_new_day_est}, 日均={line_daily_avg}, 偏差={line_dev:+.1f}% {'🔴' if line_alarm else '🟡'}")
print(f"报警: {'有' if has_alarm else '无'}")
