#!/usr/bin/env python3
"""百度主动推送脚本 — 通知百度爬虫立即抓取新URL"""
import urllib.request
import os

API = "http://data.zz.baidu.com/urls?site=https://www.subaotw.cn&token=2zqNR8QtonmBaAF4"

def push_urls(url_list):
    """推送URL列表到百度，返回结果"""
    data = "\n".join(url_list).encode('utf-8')
    req = urllib.request.Request(API, data=data, 
                                  headers={"Content-Type": "text/plain"})
    resp = urllib.request.urlopen(req, timeout=30)
    return resp.read().decode()

def collect_all_urls():
    """收集站点所有页面URL（不含index/404）"""
    urls = []
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in ('.git',)]
        for f in files:
            if f.endswith('.html') and f != '404.html':
                path = os.path.join(root, f).replace('./', '')
                if path.endswith('/index.html'):
                    # /equipment/index.html → /equipment/
                    path = path.replace('/index.html', '/')
                else:
                    path = path.replace('.html', '')
                urls.append(f"https://www.subaotw.cn/{path}")
    return sorted(urls)

if __name__ == "__main__":
    all_urls = collect_all_urls()
    print(f"Total: {len(all_urls)} URLs")
    
    # Baidu free tier: ~10 URLs per push, resets daily
    # Push ALL URLs in batches of 10
    batch = 10
    for i in range(0, len(all_urls), batch):
        chunk = all_urls[i:i+batch]
        try:
            result = push_urls(chunk)
            print(f"Batch {i//batch + 1} ({len(chunk)} URLs): {result}")
        except Exception as e:
            print(f"Batch {i//batch + 1} error: {e}")
