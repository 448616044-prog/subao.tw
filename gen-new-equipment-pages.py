#!/usr/bin/env python3
"""生成农业机械 + 汽车发动机 + 机械配件 三个页面"""

import os

OUTPUT_DIR = "/Users/mac/WorkBuddy/Claw/物流項目/sites/subaotw-cn/equipment"

TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://subaotw.cn/equipment/{slug}">
  <style>
    :root{{--primary:#1a56db;--primary-dark:#1e40af;--accent:#f97316;--bg:#f8fafc;--card:#fff;--text:#1e293b;--text-light:#64748b;--border:#e2e8f0;--radius:12px}}
    *{{margin:0;padding:0;box-sizing:border-box}}
    body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;color:var(--text);line-height:1.7;background:var(--bg)}}
    .container{{max-width:900px;margin:0 auto;padding:0 20px}}
    .header{{background:var(--card);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100}}
    .header .container{{display:flex;align-items:center;justify-content:space-between;height:64px;max-width:1200px}}
    .logo{{font-size:20px;font-weight:800;color:var(--primary);text-decoration:none}}
    .logo span{{color:var(--accent);font-size:12px;font-weight:500;margin-left:6px}}
    .breadcrumb{{padding:20px 0;font-size:14px;color:var(--text-light)}}
    .breadcrumb a{{color:var(--primary);text-decoration:none}}
    article{{padding-bottom:60px}}
    article h1{{font-size:32px;font-weight:800;margin-bottom:20px;line-height:1.3}}
    article h2{{font-size:24px;font-weight:700;margin:40px 0 16px;color:var(--primary)}}
    article h3{{font-size:18px;font-weight:700;margin:24px 0 12px}}
    article p{{font-size:16px;margin-bottom:16px;color:var(--text)}}
    .info-box{{background:var(--card);border-left:4px solid var(--primary);border-radius:var(--radius);padding:20px 24px;margin:24px 0}}
    .info-box strong{{display:block;margin-bottom:8px;color:var(--primary)}}
    table{{width:100%;border-collapse:collapse;margin:20px 0;background:var(--card);border-radius:var(--radius);overflow:hidden}}
    th{{background:var(--primary);color:#fff;padding:12px 16px;text-align:left;font-size:14px}}
    td{{padding:12px 16px;border-bottom:1px solid var(--border);font-size:14px}}
    tr:last-child td{{border-bottom:none}}
    .faq-item{{background:var(--card);border-radius:var(--radius);padding:24px;margin-bottom:12px;box-shadow:0 1px 3px rgba(0,0,0,0.06)}}
    .faq-q{{font-weight:700;margin-bottom:8px}}
    .faq-a{{color:var(--text-light);font-size:15px}}
    .cta{{background:linear-gradient(135deg,var(--accent) 0%,#ea580c 100%);color:#fff;text-align:center;padding:48px 20px;border-radius:var(--radius);margin:40px 0}}
    .cta h2{{color:#fff;margin-top:0}}
    .btn{{display:inline-block;padding:14px 32px;border-radius:8px;font-weight:700;font-size:16px;text-decoration:none;transition:all 0.2s}}
    .btn-primary{{background:#fff;color:var(--accent)}}
    .btn-primary:hover{{transform:translateY(-2px)}}
    .footer{{background:#1e293b;color:#94a3b8;padding:40px 0 20px;text-align:center;font-size:14px}}
    @media(max-width:768px){{article h1{{font-size:26px}}table{{font-size:13px}}}}
  </style>
</head>
<body>
  <header class="header">
    <div class="container">
      <a href="/" class="logo">速豹集运<span>大件设备专线</span></a>
    </div>
  </header>

  <div class="container">
    <div class="breadcrumb"><a href="/">首页</a> › <a href="/equipment/">设备运输</a> › {breadcrumb_name}</div>
  </div>

  <article>
    <div class="container">
      <h1>{h1}</h1>
      <p>{intro}</p>

      <h2>可运输的设备类型</h2>
      <table>
        <tr><th>设备类型</th><th>典型重量</th><th>运输方式</th></tr>
        {table_rows}
      </table>

      <h2>设备出口台湾四步流程</h2>
      <h3>第1步：设备评估与方案制定</h3>
      <p>{step1}</p>
      <div class="info-box"><strong>重要提示</strong>{tip}</div>
      <h3>第2步：专业包装与固定</h3>
      <p>{step2}</p>
      <h3>第3步：报关与运输</h3>
      <p>{step3}</p>
      <h3>第4步：台湾清关与派送</h3>
      <p>设备抵达台湾港口后，办理进口清关手续，安排专车派送到客户指定地点。全程可在线追踪运输状态。</p>

      <h2>运费参考</h2>
      <table>
        <tr><th>运输方式</th><th>参考费用</th><th>时效</th><th>适用场景</th></tr>
        <tr><td>20尺整柜海运</td><td>约NT$30,000-50,000</td><td>5-7天</td><td>单台中型设备</td></tr>
        <tr><td>40尺整柜海运</td><td>约NT$50,000-80,000</td><td>5-7天</td><td>多台设备或大型机台</td></tr>
        <tr><td>拼柜/散货</td><td>约NT$800-1,500/立方米</td><td>7-10天</td><td>小型设备</td></tr>
        <tr><td>空运</td><td>按实际重量/体积重计费</td><td>2-3天</td><td>紧急配件</td></tr>
      </table>
      <p style="font-size:13px;color:var(--text-light)">※ 费用含基本报关和派送，不含关税和设备保险。精确报价请联系客服。</p>

      <h2>常见问题</h2>
      {faq_items}

      <div class="cta">
        <h2>{cta_title}</h2>
        <p style="opacity:0.9">发送设备参数，30分钟内获取运输方案和报价</p>
        <a href="/contact" class="btn btn-primary">立即咨询</a>
      </div>
    </div>
  </article>

  <footer class="footer">
    <p>&copy; 2026 速豹集运 Subao Logistics | 大件设备两岸专线</p>
  </footer>
</body>
</html>'''

PAGES = [
    {
        "slug": "agricultural-machinery",
        "breadcrumb_name": "农业机械出口台湾",
        "title": "农业机械出口台湾 | 旋耕机/割草机/小挖机/铲车运输 | 速豹集运",
        "description": "农业机械出口台湾专线：旋耕机、割草机、小型铲车、微型挖掘机、农用拖拉机运输。专业清洗包装、报关清关、门到门服务，6年设备运输经验。",
        "h1": "农业机械设备出口台湾全流程指南：旋耕机、割草机、小挖机、铲车运输",
        "intro": "农业机械种类繁多，从农田作业的旋耕机、割草机到小型工程用的铲车、微型挖掘机，设备自重大、体积特殊，出口台湾需要专业的运输方案和严格的检疫处理。作为专注两岸设备运输的服务商，我们整理了农业机械出口台湾的完整操作指南。",
        "table_rows": '''<tr><td>旋耕机</td><td>200-800kg</td><td>拼柜/整柜</td></tr>
        <tr><td>割草机（手推/乘坐式/碎枝机）</td><td>50-500kg</td><td>拼柜</td></tr>
        <tr><td>小型铲车/滑移装载机</td><td>1-5吨</td><td>框架箱/整柜</td></tr>
        <tr><td>微型挖掘机（1-3吨）</td><td>1-3吨</td><td>框架箱/整柜</td></tr>
        <tr><td>农用拖拉机（小型/中型）</td><td>1-8吨</td><td>整柜/框架箱</td></tr>
        <tr><td>播种机/插秧机/收割机</td><td>0.5-5吨</td><td>整柜/拼柜</td></tr>''',
        "step1": "提供设备型号、尺寸、重量和货值，评估运输方案。微型挖掘机和小型铲车通常使用框架箱或滚装船运输，旋耕机、割草机等小型设备可拼柜。自走式设备可自行开进集装箱固定。",
        "tip": "农业机械出口台湾需特别注意：① 设备需彻底清洗，无泥土、杂草残留（检疫强制要求，不合格会退运）；② 燃油需排空，蓄电池断开；③ 台湾对进口农用机械有排放和安全标准要求，建议提前确认是否合规。",
        "step2": "农业设备包装要点：自走式设备直接进集装箱，轮胎用楔块+绑带固定；小型设备（旋耕机、割草机）木箱包装，活动部件锁定；刀片和旋转部件拆卸或装保护套；液压系统密封，发动机排气管封堵。",
        "step3": "办理出口报关，准备商业发票、装箱单、设备出厂合格证。自走式设备提供发动机号和车架号。整柜经由深圳/厦门发往台湾基隆/台中/高雄港。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">旋耕机和割草机可以拼柜运输吗？</div><div class="faq-a">完全可以。旋耕机和割草机属于中小型设备，可与其它农业机械拼柜运输以降低成本。设备需清洗干净，刀片卸下或加保护套。</div></div>
      <div class="faq-item"><div class="faq-q">微型挖掘机如何运输？</div><div class="faq-a">1-3吨微型挖掘机可用框架箱运输，也可用滚装船自行开上船。框架箱方案更灵活，不需要等待滚装船班期。</div></div>
      <div class="faq-item"><div class="faq-q">农业设备出口台湾需要检疫吗？</div><div class="faq-a">台湾对进口农用机械有严格的检疫要求，设备必须彻底清洗，无泥土和植物残留。我们会发货前指导清洁标准，确保顺利通过检疫。</div></div>''',
        "cta_title": "有农业机械需要运到台湾？",
    },
    {
        "slug": "car-engine",
        "breadcrumb_name": "汽车发动机出口台湾",
        "title": "汽车发动机出口台湾 | 发动机总成/缸体/变速箱/涡轮增压器运输 | 速豹集运",
        "description": "汽车发动机出口台湾专线：发动机总成、缸体缸盖、变速箱、涡轮增压器、差速器运输。精密防锈防震包装、报关清关、门到门服务。",
        "h1": "汽车发动机及动力总成出口台湾全流程指南：运输、防锈包装、报关",
        "intro": "汽车发动机属于高精度、高价值的核心部件，出口台湾需要专业的防锈、防震包装和可靠的物流方案。无论是全新发动机总成还是二手拆车发动机，都需要严格的运输保护措施。我们整理了汽车发动机出口台湾的完整操作指南。",
        "table_rows": '''<tr><td>发动机总成（四缸/V6/V8）</td><td>150-400kg</td><td>拼柜/空运</td></tr>
        <tr><td>缸体/缸盖（铸铁/铝合金）</td><td>30-150kg</td><td>拼柜</td></tr>
        <tr><td>变速箱（手动/自动/CVT）</td><td>50-120kg</td><td>拼柜/空运</td></tr>
        <tr><td>涡轮增压器</td><td>5-20kg</td><td>空运/拼柜</td></tr>
        <tr><td>差速器/分动箱</td><td>20-80kg</td><td>拼柜</td></tr>
        <tr><td>发动机线束/ECU控制模块</td><td>1-15kg</td><td>空运</td></tr>''',
        "step1": "提供发动机型号、排量、燃料类型（汽油/柴油）、是否为旧件等参数。全新发动机建议使用原厂包装箱+木箱外箱，二手发动机需彻底排空机油冷却液并做防锈处理。高价值发动机总成建议空运。",
        "tip": "发动机出口台湾重要提示：① 二手发动机需彻底排空所有油液（机油、冷却液、燃油），否则属于危险品影响运输；② 旧发动机可能涉及台湾进口旧机电管制，需提前确认HS编码；③ ECU等电子部件需防静电包装。",
        "step2": "发动机包装标准：优先使用原厂包装箱；二手发动机使用定制木箱+发泡缓冲，所有油液排空，进排气口和油管接口封堵；缸体加工面涂抹防锈油并加保护垫；火花塞孔/喷油嘴孔封堵防止异物进入。",
        "step3": "办理出口报关，准备商业发票、装箱单。如有旧设备，准备设备新旧状态说明。经由深圳/厦门/上海发往台湾。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">二手发动机可以出口台湾吗？</div><div class="faq-a">可以，但需确认台湾进口旧机电产品的管制要求。建议提前提供发动机型号和HS编码，我们协助确认进口条件和关税政策。</div></div>
      <div class="faq-item"><div class="faq-q">发动机运输需要排空所有油液吗？</div><div class="faq-a">是的，二手发动机必须排空机油、冷却液和燃油。全新原厂发动机出厂时已做好了防锈处理，无需额外处理。</div></div>
      <div class="faq-item"><div class="faq-q">发动机建议空运还是海运？</div><div class="faq-a">全新高价值发动机总成建议空运（时效快、震动少）。二手发动机或大批量运输可选海运拼柜，成本更低。</div></div>''',
        "cta_title": "有汽车发动机需要运到台湾？",
    },
    {
        "slug": "mechanical-parts",
        "breadcrumb_name": "机械配件出口台湾",
        "title": "机械配件出口台湾 | 轴承/齿轮/液压件/气动元件/紧固件运输 | 速豹集运",
        "description": "机械配件出口台湾专线：轴承、齿轮、液压缸、气缸、泵阀、紧固件、传动件、密封件运输。批量配件整柜/拼柜、报关清关、门到门服务。",
        "h1": "机械配件出口台湾全流程指南：批量配件运输、包装、报关一站式",
        "intro": "机械配件是两岸贸易中量最大、品类最杂的货物类型——从轴承齿轮到液压气动元件、从紧固件密封件到传动链条，涉及面广、批量差异大。小到几公斤的精密轴承，大到几十吨的批量配件，出口台湾需要灵活的运输方案和专业的分类包装。我们整理了机械配件出口台湾的完整操作指南。",
        "table_rows": '''<tr><td>轴承（滚动/滑动/关节轴承）</td><td>0.1-500kg/批</td><td>拼柜/整柜</td></tr>
        <tr><td>齿轮/齿条/蜗轮蜗杆</td><td>0.5-2000kg/批</td><td>拼柜/整柜</td></tr>
        <tr><td>液压缸/气缸/油泵</td><td>5-500kg/件</td><td>拼柜/整柜</td></tr>
        <tr><td>紧固件（螺栓/螺母/垫圈）</td><td>批量不等</td><td>拼柜/整柜</td></tr>
        <tr><td>传动件（链条/同步带/联轴器）</td><td>批量不等</td><td>拼柜</td></tr>
        <tr><td>密封件/O型圈/油封</td><td>批量不等</td><td>拼柜/空运</td></tr>''',
        "step1": "提供配件清单（品名、材质、数量、总重量、总货值），我们评估最优运输方案。小批量精密配件（轴承、密封件）可拼柜或空运，大批量重型配件（齿轮、液压缸）建议整柜运输。",
        "tip": "机械配件出口台湾要点：① 不同材质（钢件/铸铁/铜件/铝合金）需分类包装，防止电化学腐蚀；② 精密轴承需防锈油+防锈纸+独立包装；③ 液压件需排空液压油并封堵接口；④ 批量配件建议按类别编号装箱，便于台湾端分拣入库。",
        "step2": "机械配件包装标准：精密件（轴承、密封件）使用防锈纸+独立小盒+外箱，标注'精密件、防潮'；重型件（齿轮、液压缸）木箱固定，加工面涂防锈油+保护垫；紧固件按规格分类装入编织袋或纸箱，标注规格和数量；整批配件按装箱清单分类编号。",
        "step3": "办理出口报关，配件品类多时需准备详细的装箱清单，申报时按主要材质和用途归类。大批量配件整柜经由深圳/厦门发往台湾基隆/台中/高雄港。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">配件品类多、数量杂怎么报关？</div><div class="faq-a">提供详细的装箱清单，我们可以按主要用途和材质归类报关。建议发货前将配件分类编号装箱，既方便报关也方便台湾端收货核对。</div></div>
      <div class="faq-item"><div class="faq-q">精密轴承怎么防锈运输？</div><div class="faq-a">精密轴承需涂抹优质防锈油，用防锈纸包裹，装入独立防潮盒。海运集装箱内放置干燥剂，确保全程防潮防锈。</div></div>
      <div class="faq-item"><div class="faq-q">批量配件走拼柜还是整柜？</div><div class="faq-a">总货量5立方米以下建议拼柜（成本最低），5-15立方米视货物密度决定，15立方米以上建议整柜（单价更低且减少中转损耗）。</div></div>''',
        "cta_title": "有机械配件需要运到台湾？",
    },
]

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for page in PAGES:
        html = TEMPLATE.format(**page)
        filepath = os.path.join(OUTPUT_DIR, page["slug"] + ".html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ {filepath}")
    print(f"\n🎉 全部 {len(PAGES)} 个页面生成完成！")
