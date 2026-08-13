#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
contact-form 页面 3 项修正：
1. hero 蓝色区域太空（padding 140+80 + min-height 600）→ 紧凑化
2. 微信 ID subaog-hk → Bao13026603164
3. 服务范围：删除香港、东南亚，只留台湾+中国大陆
"""
import re

PATH = "sites/tw-to-cn/contact-form.html"
html = open(PATH, encoding="utf-8").read()

# 1. hero 紧凑化（删 min-height、减小 padding）
hero_old = ".hero { padding: 140px 0 80px; background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%); color: var(--text-white); min-height: 600px; display: flex; align-items: center; }"
hero_new = ".hero { padding: 100px 0 40px; background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%); color: var(--text-white); display: flex; align-items: center; }"
if hero_old in html:
    html = html.replace(hero_old, hero_new, 1)
    print("1. ✅ hero CSS 紧凑化")
else:
    print("1. ⚠️ hero CSS 锚点未匹配")

# 2. 微信 ID 修正
if "subaog-hk" in html:
    html = html.replace("subaog-hk", "Bao13026603164", 1)
    print("2. ✅ 微信 ID 已更新")
else:
    print("2. ⚠️ subaog-hk 未找到")

# 3. 服务范围：删除香港和东南亚两个 div
# 香港 div（精确匹配）
hk_div = '<div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:14px;text-align:center"><div style="font-size:24px">🇭🇰</div><div style="font-weight:700;margin:4px 0">香港</div><div style="font-size:12px;color:var(--text-secondary)">中轉服務</div></div>'
seasia_div = '<div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:14px;text-align:center"><div style="font-size:24px">🌏</div><div style="font-weight:700;margin:4px 0">東南亞</div><div style="font-size:12px;color:var(--text-secondary)">新加坡/馬來西亞</div></div>'
removed = 0
if hk_div in html:
    html = html.replace(hk_div, "", 1)
    removed += 1
if seasia_div in html:
    html = html.replace(seasia_div, "", 1)
    removed += 1
if removed:
    print(f"3. ✅ 服务范围：删除{removed}个地区，只留台灣+中國大陸")
else:
    print("3. ⚠️ 服务范围div未找到")

# 4. 同步：FAQ里关于品类的描述也精简（如有「東南亞」等），以及「可寄品類」描述保持
# 当前可寄品类那段没问题，保留

open(PATH, "w", encoding="utf-8").write(html)
print("\n3 项修正完成")