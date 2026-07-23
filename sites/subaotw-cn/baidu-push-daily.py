#!/usr/bin/env python3
"""subaotw.cn 百度每日推送 — 从队列推10条最新URL，标记已推送"""
import requests, os
from datetime import date

BASE = os.path.dirname(os.path.abspath(__file__))
TOKEN = 'zjjGnbA2oufj2XmY'  # ✅ 有效token (2026-07-23)
API = f'http://data.zz.baidu.com/urls?site=www.subaotw.cn&token={TOKEN}'

QUEUE = os.path.join(BASE, 'baidu-push-queue.txt')
PUSHED = os.path.join(BASE, 'baidu-pushed.txt')

# Load queue (new URLs not yet pushed)
queue = []
if os.path.exists(QUEUE):
    with open(QUEUE) as f:
        queue = [line.strip() for line in f if line.strip()]

# Load pushed history
pushed_set = set()
if os.path.exists(PUSHED):
    with open(PUSHED) as f:
        pushed_set = set(line.strip() for line in f if line.strip())

# Filter: URLs not yet pushed
to_push = [u for u in queue if u not in pushed_set][:10]

if not to_push:
    print(f'{date.today()} Baidu Push: 队列已空，无新URL可推送')
    exit(0)

resp = requests.post(API, data='\n'.join(to_push), headers={'Content-Type': 'text/plain'}, timeout=15)
print(f'{date.today()} Baidu Push: {resp.text}')
print(f'  推送URL数: {len(to_push)}')

# Parse response
try:
    data = resp.json()
    success = data.get('success', 0)
    if success > 0:
        with open(PUSHED, 'a') as f:
            for u in to_push[:success]:
                f.write(u + '\n')
        print(f'  成功: {success}, 已标记')
    remain = data.get('remain', '?')
    print(f'  剩余配额: {remain}')
except:
    print(f'  响应: {resp.text[:200]}')
