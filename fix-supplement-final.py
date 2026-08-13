#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""最终清理 supplement-customs-guide.html 残留：Breadcrumb 乱码 + 相关文章区"""
import re

PATH = "sites/tw-to-cn/blog/supplement-customs-guide.html"
html = open(PATH, encoding="utf-8").read()

# 1. Breadcrumb name（含乱码 \ufffd）→ 保健品清关
html = re.sub(
    r'"name":"[^"]*鞋子寄大陸攻略"',
    '"name":"保健品寄大陸海關指南"',
    html,
)

# 2. 相關文章区：鞋子/包包/配饰 → 保健品相关
old_related = (
    '<strong>相關文章：</strong>'
    '    <a href="/blog/clothing-shoes-shipping" style="color:var(--primary);margin-left:8px">台灣服飾鞋子寄大陸【必備懶人包】</a>'
    '    <a href="/blog/bags-shipping" style="color:var(--primary);margin-left:12px">台灣包包寄大陸攻略</a>'
    '    <a href="/blog/accessories-shipping" style="color:var(--primary);margin-left:12px">配飾寄大陸指南</a>'
)
new_related = (
    '<strong>相關文章：</strong>'
    '    <a href="/blog/health-products-shipping" style="color:var(--primary);margin-left:8px">保健品寄大陸完整攻略</a>'
    '    <a href="/blog/health-supplement-shipping" style="color:var(--primary);margin-left:12px">保健食品寄大陸指南</a>'
    '    <a href="/blog/medicine-health-supplements-shipping" style="color:var(--primary);margin-left:12px">藥品保健食品寄大陸說明</a>'
)
if old_related in html:
    html = html.replace(old_related, new_related)
    print("相關文章区已替换")
else:
    print("相關文章区未精确匹配，尝试正则替换")
    # 兜底：正则替换整个相關文章 div 内的链接
    html = re.sub(
        r'<strong>相關文章：</strong>.*?</div></main>',
        '<strong>相關文章：</strong>    <a href="/blog/health-products-shipping" style="color:var(--primary);margin-left:8px">保健品寄大陸完整攻略</a>    <a href="/blog/health-supplement-shipping" style="color:var(--primary);margin-left:12px">保健食品寄大陸指南</a>    <a href="/blog/medicine-health-supplements-shipping" style="color:var(--primary);margin-left:12px">藥品保健食品寄大陸說明</a>  </div></main>',
        html,
        flags=re.S,
    )

open(PATH, "w", encoding="utf-8").write(html)

# 校验
print("鞋子残留:", html.count("鞋子"))
print("球鞋残留:", html.count("球鞋"))
print("NIKE残留:", html.count("NIKE"))
print("亂碼残留:", html.count("\ufffd"))
print("保健品FAQ:", html.count("魚油、葉黃素寄大陸會被扣嗎"))
print("Breadcrumb 保健品:", html.count("保健品寄大陸海關指南"))
