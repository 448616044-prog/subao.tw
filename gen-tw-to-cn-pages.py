#!/usr/bin/env python3
"""批量生成 subaotw.cn tw-to-cn 敏感货品类页面"""

import os

OUTPUT_DIR = "/Users/mac/WorkBuddy/Claw/物流項目/sites/subaotw-cn/tw-to-cn"

TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://www.subaotw.cn/tw-to-cn/{slug}">
  <style>
    :root{{--primary:#1a56db;--primary-dark:#1e40af;--accent:#f97316;--bg:#f8fafc;--card:#fff;--text:#1e293b;--text-light:#64748b;--border:#e2e8f0;--radius:12px}}
    *{{margin:0;padding:0;box-sizing:border-box}}
    body{{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;color:var(--text);line-height:1.7;background:var(--bg);-webkit-font-smoothing:antialiased}}
    .container{{max-width:900px;margin:0 auto;padding:0 20px}}
    .header{{background:rgba(255,255,255,0.95);backdrop-filter:blur(12px);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100}}
    .header .container{{display:flex;align-items:center;justify-content:space-between;height:64px;max-width:1200px}}
    .logo{{font-size:20px;font-weight:800;color:var(--primary);text-decoration:none}}
    .logo span{{color:var(--accent);font-size:12px;font-weight:500;margin-left:6px;padding:2px 8px;background:#fff7ed;border-radius:20px}}
    .breadcrumb{{padding:20px 0;font-size:14px;color:var(--text-light)}}
    .breadcrumb a{{color:var(--primary);text-decoration:none}}
    article{{padding-bottom:60px}}
    article h1{{font-size:32px;font-weight:800;margin-bottom:20px;line-height:1.3}}
    article h2{{font-size:24px;font-weight:700;margin:40px 0 16px;color:var(--primary);padding-bottom:8px;border-bottom:2px solid #dbeafe}}
    article h3{{font-size:18px;font-weight:700;margin:24px 0 12px}}
    article p{{font-size:16px;margin-bottom:16px;color:var(--text)}}
    article ul,article ol{{margin:12px 0 16px 24px;color:var(--text-light)}}
    article li{{margin-bottom:8px}}
    .info-box{{background:#fef3c7;border-left:4px solid #f59e0b;padding:16px 20px;border-radius:8px;margin:24px 0;font-size:14px}}
    .info-box strong{{display:block;margin-bottom:4px;color:#92400e}}
    .tip-box{{background:#f0fdf4;border-left:4px solid #10b981;padding:16px 20px;border-radius:8px;margin:24px 0;font-size:14px}}
    table{{width:100%;border-collapse:collapse;margin:20px 0;background:var(--card);border-radius:var(--radius);overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,0.06)}}
    th{{background:var(--primary);color:#fff;padding:12px 16px;text-align:left;font-size:14px}}
    td{{padding:12px 16px;border-bottom:1px solid var(--border);font-size:14px}}
    tr:last-child td{{border-bottom:none}}
    .faq-item{{background:var(--card);border-radius:var(--radius);padding:24px;margin-bottom:12px;box-shadow:0 1px 3px rgba(0,0,0,0.04);border:1px solid var(--border)}}
    .faq-q{{font-weight:700;margin-bottom:8px;color:var(--primary)}}
    .faq-a{{color:var(--text-light);font-size:15px}}
    .cta{{background:linear-gradient(135deg,var(--accent) 0%,#ea580c 100%);color:#fff;text-align:center;padding:48px 20px;border-radius:var(--radius);margin:40px 0}}
    .cta h2{{color:#fff;margin-top:0;border:none;padding:0}}
    .btn{{display:inline-block;padding:14px 32px;border-radius:10px;font-weight:700;font-size:16px;text-decoration:none;transition:all 0.2s}}
    .btn-primary{{background:#fff;color:var(--accent);box-shadow:0 4px 14px rgba(0,0,0,0.15)}}
    .btn-primary:hover{{transform:translateY(-2px)}}
    .footer{{background:#0f172a;color:#94a3b8;padding:40px 0 20px;text-align:center;font-size:13px}}
    .footer a{{color:#64748b;text-decoration:none}}
    @media(max-width:768px){{article h1{{font-size:26px}}table{{font-size:13px}}}}
  </style>
</head>
<body>
  <header class="header">
    <div class="container">
      <a href="/" class="logo">速豹集运<span>两岸集运</span></a>
    </div>
  </header>

  <div class="container">
    <div class="breadcrumb"><a href="/">首页</a> › <a href="/tw-to-cn/">台湾寄大陆</a> › {breadcrumb_name}</div>
  </div>

  <article>
    <div class="container">
      <h1>{h1}</h1>
      <p>{intro}</p>

      <h2>可寄品类与限制</h2>
      <table>
        <tr><th>品类</th><th>是否可寄</th><th>注意事项</th></tr>
        {table_rows}
      </table>

      <h2>寄送流程</h2>
      <ol>
        <li><strong>确认可寄：</strong>提供具体品名和数量给客服确认</li>
        <li><strong>包装准备：</strong>{packing_tip}</li>
        <li><strong>寄到集货仓：</strong>将包裹寄到速豹台湾集货站</li>
        <li><strong>集运发出：</strong>敏感货专线发往大陆，3-7天送达</li>
        <li><strong>清关派送：</strong>大陆清关后快递派送到收件地址</li>
      </ol>

      <div class="info-box"><strong>⚠️ 重要提示</strong>{tip}</div>

      <h2>费用参考</h2>
      <p>台湾寄大陆敏感货专线按重量计费，以下为参考价格（实际以客服报价为准）：</p>
      <table>
        <tr><th>重量区间</th><th>参考单价</th><th>时效</th></tr>
        <tr><td>1-5kg</td><td>NT$180-250/kg</td><td>5-7天</td></tr>
        <tr><td>5-10kg</td><td>NT$150-200/kg</td><td>5-7天</td></tr>
        <tr><td>10-20kg</td><td>NT$120-160/kg</td><td>5-7天</td></tr>
        <tr><td>20kg以上</td><td>请联系客服报价</td><td>5-7天</td></tr>
      </table>
      <p style="font-size:13px;color:var(--text-light)">※ 以上为参考价格，具体以实际货物和目的地为准。大件或特殊品类请联系客服获取精确报价。</p>

      <h2>常见问题</h2>
      {faq_items}

      <div class="cta">
        <h2>{cta_title}</h2>
        <p style="opacity:0.9">发送品名+重量，30分钟内获取报价</p>
        <a href="/contact" class="btn btn-primary">立即咨询</a>
      </div>
    </div>
  </article>

  <footer class="footer">
    <p>© 2026 速豹集运 Subao Logistics | 两岸集运专线</p>
    <p style="margin-top:8px"><a href="https://beian.miit.gov.cn/" target="_blank" rel="nofollow">湘ICP备2026016030号-2</a></p>
  </footer>
</body>
</html>'''

PAGES = [
    {
        "slug": "tea-shipping",
        "breadcrumb_name": "台湾茶叶寄大陆",
        "title": "台湾茶叶寄大陆 | 高山茶/冻顶乌龙/东方美人怎么寄 | 速豹集运",
        "description": "台湾茶叶寄大陆专线：高山茶、冻顶乌龙、东方美人、包种茶、红茶均可寄送。敏感货专线3-7天送达，真空包装更安全。LINE免费咨询！",
        "h1": "台湾茶叶寄大陆完整指南：高山茶、冻顶乌龙、东方美人怎么寄？",
        "intro": "台湾茶叶是大陆朋友最爱的伴手礼之一。高山茶、冻顶乌龙、东方美人、包种茶……各种好茶怎么寄到大陆才不会压碎、不会被海关扣？这篇整理了茶叶寄大陆的全部注意事项。",
        "table_rows": '''<tr><td>高山茶/乌龙茶</td><td>✅ 可寄</td><td>真空包装为佳，避免运输受潮</td></tr>
        <tr><td>冻顶乌龙</td><td>✅ 可寄</td><td>密封罐装或真空袋装均可</td></tr>
        <tr><td>东方美人茶</td><td>✅ 可寄</td><td>原厂密封包装，个人自用数量</td></tr>
        <tr><td>包种茶/绿茶</td><td>✅ 可寄</td><td>干燥密封即可</td></tr>
        <tr><td>红茶/普洱茶</td><td>✅ 可寄</td><td>茶饼需原包装完整</td></tr>
        <tr><td>散装茶叶</td><td>⚠️ 慎寄</td><td>建议密封分装，避免海关疑虑</td></tr>''',
        "packing_tip": "茶叶必须使用真空包装或密封罐装，外箱用气泡纸包裹防震，避免运输中压碎茶叶。",
        "tip": "茶叶本身属于干燥农产品，通关节风险相对较低。但散装茶叶容易被海关怀疑是商业用途，建议使用原厂密封包装。个人自用数量一般不超过2公斤。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">台湾茶叶寄大陆会被扣吗？</div><div class="faq-a">只要包装完整、数量在个人自用范围内（一般不超过2公斤），走敏感货专线通关节风险很低。散装或自行分装的茶叶更容易被查验。</div></div>
      <div class="faq-item"><div class="faq-q">茶叶寄大陆要几天？</div><div class="faq-a">速豹集运敏感货专线寄茶叶到大陆，正常时效为5-7个工作日。一、二线城市通常更快。</div></div>
      <div class="faq-item"><div class="faq-q">一次可以寄多少茶叶？</div><div class="faq-a">建议单次不超过2公斤。超出可能被认为是商业用途，需额外报关手续。</div></div>''',
        "cta_title": "有台湾茶叶要寄到大陆？",
    },
    {
        "slug": "health-products",
        "breadcrumb_name": "台湾保健品寄大陆",
        "title": "台湾保健品寄大陆 | 维他命/鱼油/叶黄素/益生菌怎么寄 | 速豹集运",
        "description": "台湾保健品寄大陆专线：维他命、鱼油、叶黄素、益生菌、胶原蛋白等均可寄送。个人自用数量通关稳定，敏感货专线3-7天送达。",
        "h1": "台湾保健品寄大陆完整指南：维他命、鱼油、叶黄素怎么寄？",
        "intro": "台湾的保健品品质好、价格实惠，很多大陆朋友喜欢在台湾购买。维他命、鱼油、叶黄素、益生菌这些常见保健品怎么寄到大陆？有哪些规定和限制？这篇全部告诉你。",
        "table_rows": '''<tr><td>维他命/综合维生素</td><td>✅ 可寄</td><td>个人自用3-6个月用量</td></tr>
        <tr><td>鱼油/Omega-3</td><td>✅ 可寄</td><td>保留原厂包装和说明</td></tr>
        <tr><td>叶黄素/护眼保健品</td><td>✅ 可寄</td><td>原包装未拆封</td></tr>
        <tr><td>益生菌/酵素</td><td>✅ 可寄</td><td>密封包装，防潮</td></tr>
        <tr><td>胶原蛋白</td><td>✅ 可寄</td><td>粉剂或胶囊均可</td></tr>
        <tr><td>中药材类保健品</td><td>⚠️ 需确认</td><td>确认是否含CITES保护药材成分</td></tr>''',
        "packing_tip": "保留原厂瓶装或盒装，外层用气泡纸包裹，玻璃瓶装的保健品要在瓶身周围加缓冲材料防止破损。",
        "tip": "保健品寄大陆的核心原则是「个人自用、合理数量」。单一种类3-6瓶通常没有问题，但如果同一种类寄10瓶以上，海关可能认为是商业行为要求补税。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">保健品寄大陆会被扣吗？</div><div class="faq-a">个人自用数量的保健品走敏感货专线基本不会被扣。关键在于数量控制在合理范围、保留原厂包装、如实际申报。</div></div>
      <div class="faq-item"><div class="faq-q">保健品寄大陆要交税吗？</div><div class="faq-a">个人自用保健品在合理数量范围内（货值1000元人民币以内）通常免税。超过可能需要补税，建议控制单次寄送的总货值。</div></div>
      <div class="faq-item"><div class="faq-q">日本/美国保健品也可以从台湾转寄吗？</div><div class="faq-a">只要是从台湾发出的正规产品就可以。但需确保产品包装完整、有中文或英文标签，方便海关识别内容。</div></div>''',
        "cta_title": "有台湾保健品要寄到大陆？",
    },
    {
        "slug": "cosmetics-shipping",
        "breadcrumb_name": "台湾化妆品寄大陆",
        "title": "台湾化妆品寄大陆 | 面膜/护肤品/彩妆怎么寄 | 速豹集运",
        "description": "台湾化妆品寄大陆专线：面膜、护肤品、彩妆、洗面奶等均可寄送。敏感货专线3-7天送达，非喷雾类个人自用数量通关稳定。",
        "h1": "台湾化妆品寄大陆完整指南：面膜、护肤品、彩妆怎么寄？",
        "intro": "台湾面膜和护肤品在亚洲口碑极佳，很多大陆消费者喜欢从台湾购买。化妆品寄大陆属于敏感货，但只要掌握正确的方法，完全不是问题。",
        "table_rows": '''<tr><td>面膜（片状/涂抹式）</td><td>✅ 可寄</td><td>原包装未拆封，非喷雾型</td></tr>
        <tr><td>护肤品（乳液/精华/面霜）</td><td>✅ 可寄</td><td>密封包装，防漏</td></tr>
        <tr><td>彩妆（口红/眼影/粉底）</td><td>✅ 可寄</td><td>原包装完好</td></tr>
        <tr><td>洗面奶/卸妆产品</td><td>✅ 可寄</td><td>瓶盖拧紧，防漏</td></tr>
        <tr><td>防晒喷雾/发胶</td><td>❌ 不可寄</td><td>高压罐属危险品禁运</td></tr>
        <tr><td>含酒精产品（>24%）</td><td>⚠️ 需确认</td><td>高浓度酒精属危险品</td></tr>''',
        "packing_tip": "液体类护肤品要确保瓶盖拧紧，瓶口用保鲜膜密封后再盖盖子，外层用气泡纸包裹。容易压碎的眼影等粉状彩妆要加足缓冲材料。",
        "tip": "化妆品寄大陆最容易出问题的是喷雾类和含酒精产品。高压罐（喷雾瓶）一律不能寄，属于航空危险品。面霜、乳液、面膜等非喷雾类产品一般没问题。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">面膜可以寄大陆吗？</div><div class="faq-a">完全可以。台湾面膜寄大陆是最常见的品类之一。只要不是喷雾型面膜，片状和涂抹式都可以正常寄送。</div></div>
      <div class="faq-item"><div class="faq-q">化妆品寄大陆会被税吗？</div><div class="faq-a">个人自用数量通常免税。如果一次寄几十盒同款面膜，海关可能认为商业用途会要求补税。建议品类分散、每种不要过多。</div></div>
      <div class="faq-item"><div class="faq-q">香水可以寄吗？</div><div class="faq-a">香水含酒精且通常是玻璃瓶，不建议寄送。酒精属于危险品，玻璃瓶破损风险高。建议走其他渠道确认。</div></div>''',
        "cta_title": "有台湾化妆品要寄到大陆？",
    },
    {
        "slug": "medicine-shipping",
        "breadcrumb_name": "台湾药品寄大陆",
        "title": "台湾药品寄大陆 | 一条根/撒隆巴斯/中药/成藥怎么寄 | 速豹集运",
        "description": "台湾药品寄大陆专线：一条根、撒隆巴斯、张国周强胃散、中药等均可寄送。个人自用数量通关稳定，需确认药品成分是否符合大陆规定。",
        "h1": "台湾药品寄大陆完整指南：一条根、撒隆巴斯、科学中药怎么寄？",
        "intro": "台湾的一些常用药品如一条根、撒隆巴斯、张国周强胃散等，在大陆也有不少忠实用户。但药品属于特殊敏感货，寄大陆需要特别注意成分和数量限制。",
        "table_rows": '''<tr><td>外用药品（一条根/撒隆巴斯）</td><td>✅ 可寄</td><td>原包装，个人自用数量</td></tr>
        <tr><td>肠胃药（张国周强胃散等）</td><td>✅ 可寄</td><td>保留说明书和原包装</td></tr>
        <tr><td>科学中药/中药丸</td><td>✅ 可寄</td><td>非CITES保护药材成分</td></tr>
        <tr><td>一般成藥（止痛药/感冒药）</td><td>⚠️ 需确认</td><td>确认成分不在大陆管制清单</td></tr>
        <tr><td>处方药</td><td>⚠️ 需确认</td><td>需确认大陆进口管制政策</td></tr>
        <tr><td>含麻黄碱/可待因药品</td><td>❌ 不可寄</td><td>管制成分严禁寄送</td></tr>''',
        "packing_tip": "保留原厂包装盒和药品说明书，瓶装药注意防震。药品外包装上最好有中文成分标签，方便海关识别。",
        "tip": "药品寄大陆最关键的是成分审查。含麻黄碱类、可待因类等管制成分的药品绝对不能寄。外用药品（贴布、药膏）比内服药品的通关节风险更低。建议寄之前先发成分表给客服确认。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">一条根和撒隆巴斯可以寄大陆吗？</div><div class="faq-a">可以。一条根和撒隆巴斯是外用贴布/药膏，属于比较安全的品类。个人自用数量（每种5-10盒以内）通关稳定。</div></div>
      <div class="faq-item"><div class="faq-q">哪些药品绝对不能寄？</div><div class="faq-a">含麻黄碱、可待因、吗啡等管制成分的药品绝对不能寄。CITES保护药材（虎骨、麝香、穿山甲鳞片等）制成品也严禁。不确定的先问客服。</div></div>
      <div class="faq-item"><div class="faq-q">大陆处方药可以从台湾寄吗？</div><div class="faq-a">不推荐。大陆对处方药进口管制较严，个人邮寄处方药可能被海关查扣。建议在大陆当地就医开药。</div></div>''',
        "cta_title": "有台湾药品要寄到大陆？",
    },
    {
        "slug": "mooncake-shipping",
        "breadcrumb_name": "台湾月饼寄大陆",
        "title": "台湾月饼寄大陆 | 蛋黄酥/凤梨酥/中秋礼盒邮寄攻略 | 速豹集运",
        "description": "台湾月饼寄大陆专线：蛋黄酥、月饼、凤梨酥等中秋礼盒均可寄送。敏感货专线5-7天送达，建议中秋前2-3周提前安排寄送。",
        "h1": "台湾月饼寄大陆指南：蛋黄酥、中秋礼盒怎么寄？",
        "intro": "每年中秋节，台湾的蛋黄酥和月饼是寄往大陆最热门的伴手礼之一。蛋黄酥、广式月饼、台式月饼……怎么寄才不会被压碎、不会因为蛋黄成分被卡关？这篇完整解析。",
        "table_rows": '''<tr><td>蛋黄酥</td><td>✅ 可寄</td><td>原包装，个人自用数量</td></tr>
        <tr><td>广式月饼</td><td>✅ 可寄</td><td>密封包装完好</td></tr>
        <tr><td>台式月饼/绿豆椪</td><td>✅ 可寄</td><td>无蛋黄成分更安全</td></tr>
        <tr><td>凤梨酥/太阳饼</td><td>✅ 可寄</td><td>无动物成分，通关最安全</td></tr>
        <tr><td>含肉月饼（鲜肉月饼）</td><td>⚠️ 需确认</td><td>肉类成分受检疫管制</td></tr>
        <tr><td>冰皮月饼</td><td>❌ 不可寄</td><td>需冷链，物流条件不允许</td></tr>''',
        "packing_tip": "月饼和蛋黄酥容易碎，一定要用原厂礼盒包装，外层再用气泡纸和硬纸箱加固。单个礼盒之间要塞缓冲材料防止碰撞。",
        "tip": "蛋黄酥中的蛋黄属于动物源性成分，虽经过烘焙处理通常可以通关，但海关对含蛋/含肉制品的检疫要求会严格一些。建议中秋节前至少2-3周安排寄送，留足时间。凤梨酥和绿豆椪等无动物成分的糕点通关最快。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">蛋黄酥可以寄大陆吗？</div><div class="faq-a">可以。含蛋黄的烘焙糕点一般可以寄大陆。但蛋黄属于动物源性成分，检验相对严格，走敏感货专线更稳定。</div></div>
      <div class="faq-item"><div class="faq-q">中秋节前多久寄比较合适？</div><div class="faq-a">建议提前2-3周安排寄送。中秋节前是物流高峰期，转运和清关时间会延长，提前安排才能保证节前收到。</div></div>
      <div class="faq-item"><div class="faq-q">月饼寄大陆会被税吗？</div><div class="faq-a">个人寄送礼盒月饼，自用合理数量一般不税。一次寄超过5-8盒可能被认定为商业用途。</div></div>''',
        "cta_title": "有台湾月饼要寄到大陆？",
    },
    {
        "slug": "clothing-shipping",
        "breadcrumb_name": "台湾服饰寄大陆",
        "title": "台湾服饰寄大陆 | 衣服/鞋子/包包/配件邮寄攻略 | 速豹集运",
        "description": "台湾服饰寄大陆专线：衣服、鞋子、包包、配件均可寄送。一般快件3-7天送达，费用透明。大牌商品需注意关税。",
        "h1": "台湾服饰寄大陆指南：衣服、鞋子、包包怎么寄最省钱？",
        "intro": "在台湾买了喜欢的衣服鞋子想寄回大陆？服饰类不属于敏感货，寄送相对简单，但重量和体积是影响运费的关键。这篇教你服饰寄大陆最省钱的方法。",
        "table_rows": '''<tr><td>衣服/外套/裤子</td><td>✅ 可寄</td><td>无特殊限制</td></tr>
        <tr><td>鞋子/运动鞋</td><td>✅ 可寄</td><td>鞋盒外需加外箱保护</td></tr>
        <tr><td>包包/皮具</td><td>✅ 可寄</td><td>奢侈品需注意关税</td></tr>
        <tr><td>首饰/手表</td><td>✅ 可寄</td><td>高价值建议投保</td></tr>
        <tr><td>品牌奢侈品</td><td>⚠️ 注意关税</td><td>高货值可能被税</td></tr>
        <tr><td>皮草/动物毛皮制品</td><td>⚠️ 需确认</td><td>CITES保护动物制品禁寄</td></tr>''',
        "packing_tip": "衣服用真空压缩袋节省体积，鞋子保留鞋盒但外箱加固。奢侈品建议用硬质纸箱加足缓冲，并购买运输保险。",
        "tip": "服饰类本身不是敏感货，通关比较简单。但如果是LV、Gucci等奢侈品牌，货值超过人民币1000元可能被征税。建议分散寄送或申报时控制货值。含动物毛皮的高端服饰需确认是否涉及CITES保护物种。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">衣服寄大陆怎么最省运费？</div><div class="faq-a">使用真空压缩袋可以大幅减少体积，体积越小运费越低。多件衣服集中寄比一件一件寄更划算。</div></div>
      <div class="faq-item"><div class="faq-q">品牌包包寄大陆会被税吗？</div><div class="faq-a">如果货值较高（超过1000元人民币），有可能被海关抽查征税。建议每个包裹价值不要过高，或购买运输保险。</div></div>
      <div class="faq-item"><div class="faq-q">鞋子可以带鞋盒一起寄吗？</div><div class="faq-a">可以，但鞋盒会增加体积从而提高运费。如果不在意鞋盒，去掉鞋盒可以省不少运费。</div></div>''',
        "cta_title": "有台湾服饰要寄到大陆？",
    },
    {
        "slug": "books-shipping",
        "breadcrumb_name": "台湾书籍寄大陆",
        "title": "台湾书籍寄大陆 | 繁体书/杂志/文具邮寄攻略 | 速豹集运",
        "description": "台湾书籍寄大陆专线：繁体中文书、杂志、漫画、文具均可寄送。注意内容审查，政治敏感类不可寄。一般快件5-7天送达。",
        "h1": "台湾书籍寄大陆指南：繁体书、杂志、漫画怎么寄？",
        "intro": "台湾出版的繁体中文书在内容和装帧上都有独特魅力，很多大陆书友喜欢从台湾购书。书籍寄大陆本身不是敏感货，但内容审查是必须注意的环节。",
        "table_rows": '''<tr><td>一般书籍/小说/散文</td><td>✅ 可寄</td><td>内容不涉及政治敏感</td></tr>
        <tr><td>学术/专业书籍</td><td>✅ 可寄</td><td>正常渠道通关</td></tr>
        <tr><td>漫画/绘本</td><td>✅ 可寄</td><td>内容健康即可</td></tr>
        <tr><td>杂志/期刊</td><td>⚠️ 注意内容</td><td>政治时事类需确认</td></tr>
        <tr><td>政治敏感类书籍</td><td>❌ 不可寄</td><td>海关会查扣</td></tr>
        <tr><td>文具/手账/贴纸</td><td>✅ 可寄</td><td>无特殊限制</td></tr>''',
        "packing_tip": "书籍非常重，运费主要按重量计算。建议用硬纸箱包装，箱内四角塞缓冲材料防止撞击伤角。精装书之间用纸板隔开。",
        "tip": "书籍寄大陆最大的风险是内容审查。涉及台湾政治、两岸关系等敏感话题的书籍可能被海关查扣。建议寄之前快速翻阅确认内容。纯文学、学术、生活类书籍一般没问题。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">繁体书寄大陆会被没收吗？</div><div class="faq-a">一般不会。只要书籍内容不涉及政治敏感话题，繁体中文的文学、学术、生活类书籍都可以正常寄送。大陆海关关注的是内容而非字体。</div></div>
      <div class="faq-item"><div class="faq-q">一次可以寄多少本书？</div><div class="faq-a">建议单次不超过10-15本。书籍重量大，超过这个量运费会明显增加，也容易被海关认为是商业用途。</div></div>
      <div class="faq-item"><div class="faq-q">二手书可以寄吗？</div><div class="faq-a">可以。个人自用的二手书可以寄送，包装完整即可。但二手书如果内容涉及政治敏感同样不行。</div></div>''',
        "cta_title": "有台湾书籍要寄到大陆？",
    },
    {
        "slug": "baby-products",
        "breadcrumb_name": "台湾母婴用品寄大陆",
        "title": "台湾母婴用品寄大陆 | 奶粉/尿布/婴儿辅食邮寄攻略 | 速豹集运",
        "description": "台湾母婴用品寄大陆专线：奶粉、尿布、婴儿辅食、奶瓶、玩具等均可寄送。个人自用数量通关稳定。敏感货专线3-7天送达。",
        "h1": "台湾母婴用品寄大陆指南：奶粉、尿布、婴儿辅食怎么寄？",
        "intro": "大陆宝妈对台湾和日本的母婴用品非常信任。奶粉、尿布、婴儿辅食……这些都是寄往大陆的高频品类。母婴用品涉及婴幼儿食品安全，寄送有一些特殊要求。",
        "table_rows": '''<tr><td>奶粉（婴儿配方）</td><td>✅ 可寄</td><td>未开封原罐，个人自用数量</td></tr>
        <tr><td>尿布/纸尿裤</td><td>✅ 可寄</td><td>体积大，建议集中寄送省运费</td></tr>
        <tr><td>婴儿辅食/米饼</td><td>✅ 可寄</td><td>原厂密封包装</td></tr>
        <tr><td>奶瓶/水杯</td><td>✅ 可寄</td><td>无特殊限制</td></tr>
        <tr><td>婴儿玩具/安抚巾</td><td>✅ 可寄</td><td>非电子类更简单</td></tr>
        <tr><td>电动吸奶器/电子体温计</td><td>⚠️ 注意电池</td><td>含锂电池需特殊处理</td></tr>''',
        "packing_tip": "奶粉罐要用气泡纸包裹防止凹罐，尿布原包装直接装箱即可。液体类产品（如婴儿沐浴露）瓶盖要拧紧密封。电子产品取出电池或做好绝缘。",
        "tip": "奶粉寄大陆需特别注意：大陆对进口婴幼儿配方奶粉有严格的注册要求。个人自用少量奶粉一般可以通关，但一次寄大量（10罐以上）可能被海关拦下。建议每次控制在3-6罐，分批次寄送。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">台湾奶粉可以寄大陆吗？</div><div class="faq-a">个人自用数量的奶粉可以寄送。建议每次不超过3-6罐，保留原厂包装和中文标签。大量寄送可能涉及进口注册问题。</div></div>
      <div class="faq-item"><div class="faq-q">尿布寄大陆划算吗？</div><div class="faq-a">尿布本身价格不贵但体积大、运费占比高。建议和其他母婴用品集中寄送，分摊运费。一整箱尿布走海运集运更划算。</div></div>
      <div class="faq-item"><div class="faq-q">婴儿辅食可以寄吗？</div><div class="faq-a">密封包装的婴儿米粉、果泥、饼干等可以寄送。含肉类成分的辅食需确认检疫要求。过期或临期产品不要寄。</div></div>''',
        "cta_title": "有台湾母婴用品要寄到大陆？",
    },
]

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for i, page in enumerate(PAGES, 1):
        html = TEMPLATE.format(**page)
        filepath = os.path.join(OUTPUT_DIR, page["slug"] + ".html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"[{i}/8] ✅ {filepath}")
    print(f"\n🎉 全部 8 个敏感货页面生成完成！")
