#!/usr/bin/env python3
"""subaotw.cn 百度每日推送 — 自动推送10条最新URL"""
import requests, glob, re, os
from datetime import date

BASE = '/Users/mac/WorkBuddy/Claw/物流項目/sites/subaotw-cn'
TOKEN = 'UAVg0xt7rxpTjzaL'
API = f'http://data.zz.baidu.com/urls?site=www.subaotw.cn&token={TOKEN}'

# 收集全站URL
urls = []
for f in glob.glob(f'{BASE}/**/*.html', recursive=True):
    if '404' in f or 'google' in f: continue
    path = f.replace(BASE, '').replace('/index.html', '/').replace('.html', '')
    if path == '/index': path = '/'
    urls.append(f'https://www.subaotw.cn{path}')

# 推送前10条（优先核心页+最新更新）
priority = sorted(urls, key=lambda u: 0 if '/' == u or '/blog/' in u or '/guide/' in u else 1)[:10]
resp = requests.post(API, data='\n'.join(priority), headers={'Content-Type': 'text/plain'}, timeout=15)
print(f'{date.today()} Baidu Push: {resp.text}')
