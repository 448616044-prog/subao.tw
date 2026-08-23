#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补完 8月重点目标品牌清单缺失的 2 页：義美(yimei) + 科學麵(kexue-mian)
克隆 guai-guai-shipping.html 模板，替换 head 元数据 / h1 / 正文 / FAQ JSON-LD / breadcrumb。
"""
import re, json, os

BASE = '/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn/blog'
SITEMAP = '/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn/sitemap.xml'
TPL = os.path.join(BASE, 'guai-guai-shipping.html')
TODAY = '2026-08-23'

tpl = open(TPL, encoding='utf-8').read()

def build(slug, brand, h1, title, desc, kw, faqs, body, article_headline, article_desc):
    p = tpl
    url = f'https://subao.tw/blog/{slug}'
    # head meta
    p = re.sub(r'<title>[^<]*</title>', f'<title>{title}</title>', p, count=1)
    p = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{desc}"', p, count=1)
    p = re.sub(r'<meta name="keywords" content="[^"]*"', f'<meta name="keywords" content="{kw}"', p, count=1)
    p = re.sub(r'<link rel="canonical" href="[^"]*"', f'<link rel="canonical" href="{url}"', p, count=1)
    p = re.sub(r'<meta property="og:title" content="[^"]*"', f'<meta property="og:title" content="{title}"', p, count=1)
    p = re.sub(r'<meta property="og:description" content="[^"]*"', f'<meta property="og:description" content="{desc[:200]}"', p, count=1)
    p = re.sub(r'<meta property="og:url" content="[^"]*"', f'<meta property="og:url" content="{url}"', p, count=1)
    p = re.sub(r'<meta name="lastmod" content="[^"]*"', f'<meta name="lastmod" content="{TODAY}"', p, count=1)
    p = re.sub(r'"(datePublished|dateModified)":\s*"[^"]*"', lambda m: f'"{m.group(1)}": "{TODAY}"', p)
    # breadcrumb name (JSON-LD)
    p = re.sub(r'"name":"乖乖寄大陸"', f'"name":"{brand}寄大陸"', p, count=1)
    # Article JSON-LD headline + description
    p = re.sub(r'"headline":\s*"[^"]*"', f'"headline": "{article_headline}"', p, count=1)
    p = re.sub(r'"description":\s*"[^"]*"', f'"description": "{article_desc}"', p, count=1)
    # 可见面包屑 HTML
    p = re.sub(r'<strong>乖乖寄大陸</strong>', f'<strong>{brand}寄大陸</strong>', p, count=1)
    # h1
    p = re.sub(r'<h1[^>]*>.*?</h1>', f'<h1>{h1}</h1>', p, count=1)
    # body: 替换 </h1> 到 <footer 之间，保留原 LINE CTA(<p>📱)
    h1end = p.find('</h1>')
    fstart = p.find('<footer')
    body_old = p[h1end:fstart]
    cta_i = body_old.find('<p>📱')
    cta = body_old[cta_i:] if cta_i > 0 else ''
    p = p[:h1end] + '</h1>' + body + cta + p[fstart:]
    # FAQ JSON-LD
    faq_json = json.dumps(
        [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}}
         for q, a in faqs],
        ensure_ascii=False)
    new_faq = ('<script type="application/ld+json">{"@context": "https://schema.org", '
               f'"@type": "FAQPage", "mainEntity": {faq_json}}}</script>')
    p = re.sub(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "FAQPage".*?</script>',
               new_faq, p, count=1, flags=re.DOTALL)
    out = os.path.join(BASE, f'{slug}.html')
    open(out, 'w', encoding='utf-8').write(p)
    # 校验整段 FAQ JSON-LD 可解析（含闭合大括号）
    fb = re.search(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "FAQPage".*?</script>',
                   p, re.DOTALL)
    json.loads(fb.group(0)[len('<script type="application/ld+json">'):-len('</script>')])
    print(f'✅ {slug}.html ({len(p)} bytes) FAQ items={len(faqs)}')
    return url

# ═══ 義美 (I-Mei) ═══
yimei_body = '''
<p>義美是台灣人從小吃到大的國民食品品牌，從義美蛋捲、小泡芙到牛乳糖、米果，都是送禮自用的經典。<strong>想把義美寄給大陸的親友？答案是：可以！</strong></p>
<table><thead><tr><th>項目</th><th>說明</th></tr></thead><tbody>
<tr><td><strong>可否寄送</strong></td><td>✅ 可以！義美蛋捲、小泡芙、牛乳糖、米果等烘焙零食，走敏感貨專線可寄</td></tr>
<tr><td><strong>運費</strong></td><td>蛋捲禮盒約0.3kg，NT$290起（含包稅雙清）</td></tr>
<tr><td><strong>時效</strong></td><td>空運最快5-7天（實際時效請加LINE確認）</td></tr>
</tbody></table>
<h2>義美哪些品項可以寄大陸？</h2>
<p>義美蛋捲、義美小泡芙、義美牛乳糖、義美米果、義美餅乾都屬於一般烘焙零食，走敏感貨專線沒問題。其中<strong>義美蛋捲禮盒</strong>和<strong>小泡芙</strong>最適合送禮。</p>
<h2>義美寄大陸運費怎麼算？</h2>
<p>以1盒義美蛋捲（約0.3kg）為例，敏感貨專線NT$290/kg起，最低消費NT$290（含包稅雙清）。一次寄2-3盒或搭配其他零食最經濟。</p>
<h2>寄送義美要注意什麼？</h2>
<ul><li>義美蛋捲易碎，建議原盒包裝外加氣泡膜（我們提供專業包裝）</li><li>小泡芙為常溫烘焙點心（非冷藏），奶油內餡可正常通關</li><li>冷藏類如義美布丁、鮮奶不建議海運寄送，應選常溫品項</li><li>送禮推薦蛋捲禮盒＋小泡芙組合，最有面子</li></ul>
<p>相關：<a href="/blog/taiwan-snack-shipping">台灣零食寄大陸完整攻略</a> | <a href="/blog/taiwan-snack-recommend">台灣零食推薦清單</a> | <a href="/blog/guai-guai-shipping">乖乖寄大陸</a> | <a href="/blog/cola-guo-shipping">可樂果寄大陸</a></p>
'''
yimei_faq = [
    ('義美可以寄大陸嗎？', '✅ 可以。義美蛋捲、小泡芙、牛乳糖、米果等烘焙零食，走敏感貨專線即可寄送。NT$290/kg起包稅雙清，5-7天到大陸。冷藏類（布丁、鮮奶）不建議寄。'),
    ('義美寄大陸運費多少？', '以1盒義美蛋捲（約0.3kg）為例，運費約NT$290-390（含NT$100派送費）。滿10kg免派送費，建議和其他零食一起寄更划算。'),
    ('義美小泡芙有奶油能寄嗎？', '可以。義美小泡芙是常溫保存的烘焙點心（非冷藏），奶油內餡屬一般食品成分，走專線通關沒問題。'),
]
build('yimei-shipping', '義美',
      '義美可以寄大陸嗎？2026運費+品項教學',
      '義美可以寄大陸嗎？義美寄送攻略 2026 | 速豹集運',
      '義美可以寄大陸嗎？可以！義美蛋捲、小泡芙、牛乳糖、米果等烘焙零食，走敏感貨專線NT$290/kg起包稅，5-7天。2026完整攻略：價格/包裝/通關一次搞定。LINE @734dooky 免費估價。',
      '義美寄大陸,義美可以寄大陸嗎,義美蛋捲寄大陸,義美小泡芙寄大陸,台灣義美零食寄大陸',
      yimei_faq, yimei_body,
      '義美可以寄大陸嗎？義美寄送攻略',
      '義美可以寄大陸嗎？可以！義美蛋捲、小泡芙等烘焙零食走敏感貨專線NT$290/kg起包稅，5-7天。2026完整攻略。')

# ═══ 科學麵 (Science Noodle / 統一) ═══
kexue_body = '''
<p>科學麵是台灣點心麵的始祖，1969年問世以來一直是國小生最愛的零食。<strong>科學麵可以寄大陸嗎？答案是：可以！</strong></p>
<table><thead><tr><th>項目</th><th>說明</th></tr></thead><tbody>
<tr><td><strong>可否寄送</strong></td><td>✅ 可以！科學麵為素食點心麵（不含肉類），走敏感貨專線可寄</td></tr>
<tr><td><strong>運費</strong></td><td>1包約40g，10包約0.4-0.5kg，NT$290起（含包稅雙清）</td></tr>
<tr><td><strong>時效</strong></td><td>空運最快5-7天（實際時效請加LINE確認）</td></tr>
</tbody></table>
<h2>科學麵為什麼能寄大陸？</h2>
<p>科學麵是油炸麵體加上調味粉的點心麵，<strong>不含肉類、不含高風險動物性成分</strong>，屬於一般零食，走敏感貨專線通關很順利。統一旗下還有許多類似點心麵也都能寄。</p>
<h2>科學麵寄大陸運費怎麼算？</h2>
<p>1包科學麵約40g，10包約0.4-0.5kg，敏感貨專線NT$290/kg起，最低消費NT$290（含包稅雙清）。湊滿10kg免派送費，建議和其他零食一起寄。</p>
<h2>寄送科學麵要注意什麼？</h2>
<ul><li>科學麵為油炸點心，怕壓怕潮，建議原包裝外加夾鏈袋防潮</li><li>大包裝（100g）比小包裝更省運費，送禮可選大袋</li><li>統一旗下科學麵、統一麵等點心麵都能走同一專線</li><li>一次寄20-30包最經濟（約1-1.5kg）</li></ul>
<p>相關：<a href="/blog/taiwan-snack-shipping">台灣零食寄大陸完整攻略</a> | <a href="/blog/taiwan-snack-recommend">台灣零食推薦清單</a> | <a href="/blog/tongyi-noodles-shipping">統一麵寄大陸</a> | <a href="/blog/guai-guai-shipping">乖乖寄大陸</a></p>
'''
kexue_faq = [
    ('科學麵可以寄大陸嗎？', '✅ 可以。科學麵是素食點心麵（不含肉類），走敏感貨專線完全沒問題。NT$290/kg起包稅雙清，5-7天到大陸主要城市。'),
    ('科學麵寄大陸運費多少？', '1包科學麵約40g，10包約0.4-0.5kg，運費約NT$290-390。滿10kg免派送費，建議湊重量和其他零食一起寄。'),
    ('科學麵為什麼能寄？含調味粉嗎？', '科學麵是油炸麵體＋調味粉的點心麵，不含肉類、不含動物性高風險成分，屬一般零食，專線通關順利。'),
]
build('kexue-mian-shipping', '科學麵',
      '科學麵可以寄大陸嗎？2026運費+品項教學',
      '科學麵可以寄大陸嗎？科學麵寄送攻略 2026 | 速豹集運',
      '科學麵可以寄大陸嗎？可以！科學麵為素食點心麵（不含肉類），走敏感貨專線NT$290/kg起包稅，5-7天。2026完整攻略：價格/包裝/通關全包。LINE @734dooky 免費估價。',
      '科學麵寄大陸,科學麵可以寄大陸嗎,統一科學麵寄大陸,台灣科學麵零食寄大陸,點心麵寄大陸',
      kexue_faq, kexue_body,
      '科學麵可以寄大陸嗎？科學麵寄送攻略',
      '科學麵可以寄大陸嗎？可以！科學麵為素食點心麵走敏感貨專線NT$290/kg起包稅，5-7天。2026完整攻略。')

# ═══ 入 sitemap ═══
sm = open(SITEMAP, encoding='utf-8').read()
for slug in ['yimei-shipping', 'kexue-mian-shipping']:
    url = f'https://subao.tw/blog/{slug}'
    if url not in sm:
        entry = (f'  <url><loc>{url}</loc><lastmod>{TODAY}</lastmod>'
                 f'<changefreq>weekly</changefreq><priority>0.7</priority></url>\n')
        sm = sm.replace('</urlset>', entry + '</urlset>', 1)
        print(f'✅ sitemap + {slug}')
open(SITEMAP, 'w', encoding='utf-8').write(sm)
print('\n📊 完成：義美 + 科學麵 2 頁已生成並入 sitemap')
