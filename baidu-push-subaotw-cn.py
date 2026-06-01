#!/usr/bin/env python3
"""subaotw.cn 百度主动推送脚本"""
import requests
import os

# 百度站长平台 — 主动推送 API（备案通过后在百度站长平台获取）
BAIDU_API_URL = "http://data.zz.baidu.com/urls?site=https://subaotw.cn&token=YOUR_BAIDU_TOKEN"

SITE_DIR = "/Users/mac/WorkBuddy/Claw/物流項目/sites/subaotw-cn"

def find_html_files():
    urls = []
    for root, dirs, files in os.walk(SITE_DIR):
        for f in files:
            if f.endswith('.html'):
                rel = os.path.relpath(os.path.join(root, f), SITE_DIR)
                if rel == 'index.html':
                    urls.append('https://subaotw.cn/')
                else:
                    url = 'https://subaotw.cn/' + rel.replace('.html', '').replace('/index', '')
                    urls.append(url)
    return sorted(urls)

def push_urls(urls):
    """推送URL到百度"""
    data = '\n'.join(urls)
    try:
        resp = requests.post(BAIDU_API_URL, data=data.encode('utf-8'),
                           headers={'Content-Type': 'text/plain'})
        print(f"推送结果: {resp.json()}")
        return resp.json()
    except Exception as e:
        print(f"推送失败: {e}")
        return None

if __name__ == '__main__':
    urls = find_html_files()
    print(f"\n共 {len(urls)} 个页面:\n")
    for u in urls:
        print(f"  {u}")
    
    if "YOUR_BAIDU_TOKEN" in BAIDU_API_URL:
        print("\n⚠️ 请在百度站长平台获取token后替换 YOUR_BAIDU_TOKEN")
        print("   步骤: 百度站长平台 → 站点管理 → 资源提交 → 普通收录 → API提交")
    else:
        print(f"\n推送 {len(urls)} 个URL...")
        push_urls(urls)
