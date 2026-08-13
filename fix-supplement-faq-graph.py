#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复 supplement-customs-guide.html 中 @graph 里的 FAQPage 鞋子残留"""
import re

PATH = "sites/tw-to-cn/blog/supplement-customs-guide.html"
html = open(PATH, encoding="utf-8").read()

main_entity = [
    ("魚油、葉黃素寄大陸會被扣嗎？", "成分單純的膳食補充劑（魚油/葉黃素/維他命）通關率高。個人自用合理數量、原廠密封包裝、成分標示完整，基本不會被扣。"),
    ("台灣的保健食品可以寄到大陸嗎？", "可以。標示為保健食品/膳食補充劑的產品走敏感貨專線可寄，NT$290/kg起包稅雙清。標示為藥品的不行。"),
    ("含中藥成分的保健品能寄嗎？", "看成分。純草本萃取（如葉黃素、花青素）可寄；含人參、當歸、黃芪等中藥材的需單獨確認，部分屬管控品。"),
    ("一次可以寄多少保健品？", "個人自用合理數量，單次建議6-12瓶/罐，總值在免稅額度內。超過合理數量海關會懷疑商業用途。"),
    ("保健品寄大陸要申報成分嗎？", "要。原廠包裝+成分標示完整是通關關鍵。拆封、無標示的散裝保健品最容易被扣。申報品名寫清楚。"),
    ("藥品可以寄大陸嗎？", "處方藥、注射劑不能寄，需藥監備案個人無法清關。常見保健品（魚油/維他命/膠原蛋白）走專線可寄。"),
]

qjson = ",".join(
    '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q, a)
    for q, a in main_entity
)
new_faq_graph = '{"@type":"FAQPage","mainEntity":[' + qjson + ']}'

# 替换 @graph 里的 FAQPage（无空格形式 "FAQPage"）
html, n = re.subn(
    r'\{"@type":"FAQPage","mainEntity":\[.*?\]\}',
    new_faq_graph,
    html,
    flags=re.S,
)

open(PATH, "w", encoding="utf-8").write(html)
print("替换次数:", n)
print("NIKE 残留:", html.count("NIKE"))
print("球鞋 残留:", html.count("球鞋"))
print("高跟鞋 残留:", html.count("高跟鞋"))
print("FAQPage 总数:", html.count("FAQPage"))
print("保健品FAQ:", html.count("魚油、葉黃素寄大陸會被扣嗎"))
