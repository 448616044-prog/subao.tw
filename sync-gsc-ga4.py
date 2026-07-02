#!/usr/bin/env python3
"""
subao.tw GSC + GA4 自动同步脚本
每天拉取 Google Search Console 和 GA4 数据，写入子部数据面板

用法:
  python sync-gsc-ga4.py

前置条件:
  1. pip install google-api-python-client google-analytics-data
  2. 服务账号 JSON 密钥在 相关材料截图/ 目录
  3. 服务账号已授权 GSC + GA4
"""

import os
import sys
import json
import re
from datetime import datetime, timedelta
from pathlib import Path

# ============================================================
# 配置区 — 你的服务账号JSON文件名
# ============================================================
SERVICE_ACCOUNT_DIR = os.path.expanduser("~/Desktop/相关材料截图")
SERVICE_ACCOUNT_GLOB = "subao-seo-*.json"  # 匹配文件名模式

SITE_URL = "https://subao.tw"
GSC_SITE = "sc-domain:subao.tw"  # 带斜杠
GA4_PROPERTY_ID = "properties/536944301"  # GA4 subao.tw 属性ID

PANEL_FILE = os.path.join(os.path.dirname(__file__), "subao-数据面板.md")
DATA_DUMP = os.path.join(os.path.dirname(__file__), "gsc-ga4-raw.json")

# ============================================================
# 1. 找到服务账号 JSON
# ============================================================
def find_service_account_json():
    import glob
    pattern = os.path.join(SERVICE_ACCOUNT_DIR, SERVICE_ACCOUNT_GLOB)
    files = glob.glob(pattern)
    if not files:
        # Also try without subao- prefix
        files = glob.glob(os.path.join(SERVICE_ACCOUNT_DIR, "*.json"))
        if files:
            for f in files:
                with open(f) as fh:
                    data = json.load(fh)
                    if "client_email" in data and "iam.gserviceaccount.com" in data["client_email"]:
                        return f
    if files:
        return files[0]
    return None

# ============================================================
# 2. GSC 数据抓取 (Search Console API)
# ============================================================
def fetch_gsc_data(credentials_file):
    from google.oauth2 import service_account
    from google.auth.transport.requests import AuthorizedSession

    creds = service_account.Credentials.from_service_account_file(
        credentials_file,
        scopes=["https://www.googleapis.com/auth/webmasters.readonly"]
    )
    authed = AuthorizedSession(creds)
    base = f"https://www.googleapis.com/webmasters/v3/sites/{GSC_SITE.replace(':', '%3A').replace('/', '%2F')}/searchAnalytics/query"

    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=28)).strftime("%Y-%m-%d")

    results = {"gsc": {"period": f"{start_date} to {end_date}", "data": {}}}

    def gsc_query(body):
        try:
            r = authed.post(base, json=body, timeout=30)
            if r.status_code == 200:
                return r.json().get("rows", [])
            print(f"  GSC API {body.get('dimensions')}: status={r.status_code}, body={r.text[:200]}", flush=True)
            return []
        except Exception as e:
            print(f"  GSC query error: {e}", flush=True)
            return []

    # 2a. 查询词
    rows = gsc_query({"startDate": start_date, "endDate": end_date, "dimensions": ["query"], "rowLimit": 30})
    results["gsc"]["data"]["queries"] = [{
        "query": r["keys"][0], "clicks": r.get("clicks", 0),
        "impressions": r.get("impressions", 0), "ctr": round(r.get("ctr", 0) * 100, 1),
        "position": round(r.get("position", 0), 1)
    } for r in rows]

    # 2b. 页面
    rows = gsc_query({"startDate": start_date, "endDate": end_date, "dimensions": ["page"], "rowLimit": 30})
    results["gsc"]["data"]["pages"] = [{
        "page": r["keys"][0].replace(SITE_URL, ""), "clicks": r.get("clicks", 0),
        "impressions": r.get("impressions", 0), "ctr": round(r.get("ctr", 0) * 100, 1),
        "position": round(r.get("position", 0), 1)
    } for r in rows]

    # 2c. 国家
    rows = gsc_query({"startDate": start_date, "endDate": end_date, "dimensions": ["country"], "rowLimit": 20})
    results["gsc"]["data"]["countries"] = [{
        "country": r["keys"][0], "clicks": r.get("clicks", 0), "impressions": r.get("impressions", 0)
    } for r in rows]

    # 2d. 设备
    rows = gsc_query({"startDate": start_date, "endDate": end_date, "dimensions": ["device"], "rowLimit": 10})
    results["gsc"]["data"]["devices"] = [{
        "device": r["keys"][0], "clicks": r.get("clicks", 0), "impressions": r.get("impressions", 0)
    } for r in rows]

    # 2e. 每日概览
    rows = gsc_query({"startDate": start_date, "endDate": end_date, "dimensions": ["date"], "rowLimit": 28})
    total_clicks = sum(r.get("clicks", 0) for r in rows)
    total_impressions = sum(r.get("impressions", 0) for r in rows)
    avg_ctr = round((total_clicks / total_impressions * 100), 1) if total_impressions > 0 else 0
    avg_position = round(sum(r.get("position", 0) for r in rows) / len(rows), 1) if rows else 0
    results["gsc"]["data"]["summary"] = {
        "total_clicks": total_clicks, "total_impressions": total_impressions,
        "avg_ctr": avg_ctr, "avg_position": avg_position
    }
    # 保存 daily 趋势
    results["gsc"]["data"]["daily_trend"] = [{
        "date": r["keys"][0], "clicks": r.get("clicks", 0), "impressions": r.get("impressions", 0),
        "ctr": round(r.get("ctr", 0) * 100, 1), "position": round(r.get("position", 0), 1)
    } for r in rows]

    print(f"  GSC ✅: {len(results['gsc']['data']['queries'])} queries, {len(results['gsc']['data']['pages'])} pages, {len(results['gsc']['data']['countries'])} countries", flush=True)
    return results



def fetch_ga4_data(credentials_file):
    from google.oauth2 import service_account
    from google.auth.transport.requests import AuthorizedSession

    creds = service_account.Credentials.from_service_account_file(
        credentials_file,
        scopes=["https://www.googleapis.com/auth/analytics.readonly"]
    )
    authed = AuthorizedSession(creds)
    prop_id = GA4_PROPERTY_ID.replace("properties/", "")
    base = f"https://analyticsdata.googleapis.com/v1beta/properties/{prop_id}:runReport"

    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=28)).strftime("%Y-%m-%d")

    results = {"ga4": {"period": f"{start_date} to {end_date}", "data": {}}}

    def ga4_query(dimensions, metrics, name, limit=30, order_by=None):
        body = {
            "dateRanges": [{"startDate": start_date, "endDate": end_date}],
            "dimensions": [{"name": d} for d in dimensions],
            "metrics": [{"name": m} for m in metrics],
            "limit": limit
        }
        if order_by:
            body["orderBys"] = order_by
        try:
            r = authed.post(base, json=body, timeout=30)
            if r.status_code == 200:
                data = []
                for row in r.json().get("rows", []):
                    entry = {}
                    for i, d in enumerate(dimensions):
                        entry[d] = row["dimensionValues"][i]["value"]
                    for i, m in enumerate(metrics):
                        entry[m] = row["metricValues"][i]["value"]
                    data.append(entry)
                results["ga4"]["data"][name] = data
                return data
            print(f"  GA4 {name}: status={r.status_code}, body={r.text[:150]}", flush=True)
        except Exception as e:
            print(f"  GA4 {name} error: {e}", flush=True)
        return []

    # 3a. 每日概览
    ga4_query(["date"], ["activeUsers", "sessions", "screenPageViews", "newUsers", "averageSessionDuration", "eventCount"], "daily_overview", 28)

    # 3b. 渠道来源
    ga4_query(["sessionSource"], ["sessions", "activeUsers", "newUsers", "averageSessionDuration", "eventCount"], "channels", 10, order_by=[{"metric": {"metricName": "sessions"}, "desc": True}])

    # 3c. 页面浏览 Top 20
    ga4_query(["pagePath"], ["screenPageViews", "activeUsers", "averageSessionDuration", "bounceRate"], "top_pages", 20, order_by=[{"metric": {"metricName": "screenPageViews"}, "desc": True}])

    # 3d. 着陆页 Top 15
    ga4_query(["landingPage"], ["sessions", "activeUsers", "bounceRate"], "landing_pages", 15, order_by=[{"metric": {"metricName": "sessions"}, "desc": True}])

    # 3e. 地理分布
    ga4_query(["country"], ["activeUsers", "sessions"], "geo", 20, order_by=[{"metric": {"metricName": "activeUsers"}, "desc": True}])

    # 3f. 转化事件
    ga4_query(["eventName"], ["eventCount"], "events", 10, order_by=[{"metric": {"metricName": "eventCount"}, "desc": True}])

    # 3g. 设备分布
    ga4_query(["deviceCategory"], ["activeUsers", "sessions"], "devices", 5, order_by=[{"metric": {"metricName": "activeUsers"}, "desc": True}])

    # 3h. 新老用户
    ga4_query(["newVsReturning"], ["activeUsers", "sessions"], "new_vs_returning", 5)

    print(f"  GA4 ✅: {sum(len(v) for k,v in results['ga4']['data'].items() if isinstance(v, list))} rows total", flush=True)
    return results



def generate_panel(all_data, panel_file):
    now = datetime.now()
    period = all_data.get("gsc", {}).get("period", "unknown")
    
    lines = []
    lines.append(f"# subao.tw SEO 数据面板 - {now.strftime('%Y年%m月%d日')}（API自动同步 {period}）")
    lines.append("")
    lines.append("---")
    lines.append("")

    # --- GSC 总览 ---
    gsc_summary = all_data.get("gsc", {}).get("data", {}).get("summary", {})
    if gsc_summary:
        lines.append("## 📊 GSC 28天总览")
        lines.append(f"| 总点击 | 总展现 | 平均CTR | 平均排名 |")
        lines.append(f"|:---|:---|:---|:---|")
        lines.append(f"| {gsc_summary.get('total_clicks', 0):,} | {gsc_summary.get('total_impressions', 0):,} | {gsc_summary.get('avg_ctr', 0)}% | {gsc_summary.get('avg_position', 0)} |")
        lines.append("")

    # --- GSC 关键词 Top 20 ---
    queries = all_data.get("gsc", {}).get("data", {}).get("queries", [])
    if queries:
        lines.append("## 🔎 GSC 关键词 Top 20")
        lines.append(f"| 关键词 | 点击 | 展现 | CTR | 排名 |")
        lines.append(f"|:---|:---:|:---:|:---:|:---:|")
        for q in queries[:20]:
            lines.append(f"| {q['query'][:60]} | {q['clicks']} | {q['impressions']:,} | {q['ctr']}% | {q['position']} |")
        lines.append("")

    # --- GSC 页面 Top 15 ---
    pages = all_data.get("gsc", {}).get("data", {}).get("pages", [])
    if pages:
        lines.append("## 📄 GSC 页面 Top 15")
        lines.append(f"| 页面 | 点击 | 展现 | CTR | 排名 |")
        lines.append(f"|:---|:---:|:---:|:---:|:---:|")
        for p in pages[:15]:
            lines.append(f"| {p['page'][:50]} | {p['clicks']} | {p['impressions']:,} | {p['ctr']}% | {p['position']} |")
        lines.append("")

    # --- GA4 每日概览 ---
    daily = all_data.get("ga4", {}).get("data", {}).get("daily_overview", [])
    if daily:
        total_active = sum(int(d.get("activeUsers", 0)) for d in daily)
        total_sessions = sum(int(d.get("sessions", 0)) for d in daily)
        total_views = sum(int(d.get("screenPageViews", 0)) for d in daily)
        total_new = sum(int(d.get("newUsers", 0)) for d in daily)
        lines.append("## 📈 GA4 28天概览")
        lines.append(f"| 指标 | 数值 |")
        lines.append(f"|:---|:---:|")
        lines.append(f"| 活跃用户 | **{total_active:,}** |")
        lines.append(f"| 会议 | **{total_sessions:,}** |")
        lines.append(f"| 浏览量 | **{total_views:,}** |")
        lines.append(f"| 新用户 | **{total_new:,}** |")
        lines.append("")

    # --- GA4 渠道 ---
    channels = all_data.get("ga4", {}).get("data", {}).get("channels", [])
    if channels:
        lines.append("## 📣 GA4 流量渠道")
        lines.append(f"| 渠道 | 会话 | 活跃用户 | 新用户 | 参与时间 | 事件 |")
        lines.append(f"|:---|:---:|:---:|:---:|:---:|:---:|")
        for ch in channels[:8]:
            lines.append(f"| {ch.get('sessionSource', '')[:30]} | {ch.get('sessions', '')} | {ch.get('activeUsers', '')} | {ch.get('newUsers', '')} | {ch.get('averageSessionDuration', '')}s | {ch.get('eventCount', '')} |")
        lines.append("")

    # --- GA4 热门页面 ---
    top_pages = all_data.get("ga4", {}).get("data", {}).get("top_pages", [])
    if top_pages:
        lines.append("## 🏆 GA4 热门页面")
        lines.append(f"| 页面 | 浏览 | 用户 | 跳出率 |")
        lines.append(f"|:---|:---:|:---:|:---:|")
        for p in top_pages[:15]:
            lines.append(f"| {p.get('pagePath', '')[:50]} | {p.get('screenPageViews', '')} | {p.get('activeUsers', '')} | {p.get('bounceRate', '')}% |")
        lines.append("")

    # --- GA4 地理 ---
    geo = all_data.get("ga4", {}).get("data", {}).get("geo", [])
    if geo:
        lines.append("## 🌍 GA4 地理")
        lines.append(f"| 国家/地区 | 活跃用户 | 会话 |")
        lines.append(f"|:---|:---:|:---:|")
        for g in geo[:10]:
            lines.append(f"| {g.get('country', '')} | {g.get('activeUsers', '')} | {g.get('sessions', '')} |")
        lines.append("")

    # --- Footer ---
    lines.append(f"\n*自动更新于 {now.strftime('%Y-%m-%d %H:%M')} | 数据周期: {period}*")

    with open(panel_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"✅ 数据面板已更新: {panel_file}")
    print(f"   总行数: {len(lines)}")

# ============================================================
# 5. Main
# ============================================================
def main():
    # 找服务账号 JSON
    json_file = find_service_account_json()
    if not json_file:
        print("❌ 找不到服务账号 JSON 文件！")
        print("   请把 JSON 放到: ~/Desktop/相关材料截图/")
        sys.exit(1)

    print(f"📄 使用服务账号: {json_file}")

    # 抓 GSC
    print("\n🔄 正在从 GSC 抓取数据...")
    gsc_data = fetch_gsc_data(json_file)
    print(f"   ✅ GSC: {len(gsc_data['gsc']['data'].get('queries', []))} 个关键词, "
          f"{len(gsc_data['gsc']['data'].get('pages', []))} 个页面")

    # 抓 GA4
    print("\n🔄 正在从 GA4 抓取数据...")
    ga4_data = fetch_ga4_data(json_file)
    print(f"   ✅ GA4: {len(ga4_data['ga4']['data'].get('daily_overview', []))} 天, "
          f"{len(ga4_data['ga4']['data'].get('channels', []))} 个渠道")

    # 合并 + 写入
    all_data = {**gsc_data, **ga4_data}

    # 保存原始 JSON
    with open(DATA_DUMP, "w") as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)
    print(f"\n💾 原始数据: {DATA_DUMP}")

    # 生成面板
    print("\n📝 生成数据面板...")
    generate_panel(all_data, PANEL_FILE)

    print("\n🎉 同步完成！")
    print(f"   面板: {PANEL_FILE}")
    print(f"   原始: {DATA_DUMP}")


if __name__ == "__main__":
    main()
