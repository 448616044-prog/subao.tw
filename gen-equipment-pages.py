#!/usr/bin/env python3
"""批量生成 subaotw.cn 设备品类页面"""

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
      <p>设备抵达台湾港口后，办理进口清关手续，安排专车（带吊装设备）派送到客户工厂。全程可在线追踪运输状态。</p>

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
    <p>© 2026 速豹集运 Subao Logistics | 大件设备两岸专线</p>
  </footer>
</body>
</html>'''

PAGES = [
    {
        "slug": "textile-machinery",
        "breadcrumb_name": "纺织设备出口台湾",
        "title": "纺织设备出口台湾 | 纺纱机/织布机/印染设备运输 | 速豹集运",
        "description": "纺织机械出口台湾专线：纺纱机、织布机、针织机、印染设备、无纺布设备运输。专业木箱包装、报关清关、门到门服务，6年设备运输经验。",
        "h1": "纺织机械设备出口台湾全流程指南：运输、包装、报关",
        "intro": "纺织机械设备种类繁多，从纺纱、织造到印染后整理，设备体积大、精度要求高。出口台湾涉及特殊包装、防潮运输和报关流程。作为专注两岸设备运输的服务商，我们整理了纺织设备出口台湾的完整操作指南。",
        "table_rows": '''<tr><td>纺纱机（环锭纺/气流纺/紧密纺）</td><td>3-15吨</td><td>整柜</td></tr>
        <tr><td>织布机（喷气/剑杆/喷水）</td><td>1-5吨/台</td><td>整柜/拼柜</td></tr>
        <tr><td>针织机（圆机/横机/经编机）</td><td>0.5-3吨</td><td>拼柜</td></tr>
        <tr><td>印染设备（染色机/印花机）</td><td>2-8吨</td><td>整柜</td></tr>
        <tr><td>无纺布生产线</td><td>5-20吨</td><td>整柜/框架箱</td></tr>
        <tr><td>缝纫/刺绣设备</td><td>50-500kg</td><td>拼柜/空运</td></tr>''',
        "step1": "提供设备的技术参数（型号、尺寸、重量、货值），我们根据设备特性制定运输方案。大型纺纱设备建议海运整柜，小型缝纫设备可选拼柜或空运。",
        "tip": "纺织设备出口台湾需注意：部分旧纺织机械可能涉及进口管制，建议提前确认HS编码。精密电子控制部件（如电子提花机）需特别防震包装。",
        "step2": "纺织设备包装要点：定制实木熏蒸木箱，符合ISPM 15标准；精密部件（提花装置、电子控制系统）加装防震支撑和防潮处理；设备活动部件固定，防止运输位移；电气控制柜单独固定并用防静电材料包裹。",
        "step3": "我们办理出口报关，准备商业发票、装箱单、设备技术参数表、原产地证明。整柜装运后经由厦门/宁波/深圳等口岸发往台湾基隆/台中/高雄港。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">旧纺织设备可以出口台湾吗？</div><div class="faq-a">可以，但旧纺织设备需确认是否属于台湾进口管制范围。部分旧设备需要办理装运前检验。建议提前确认设备的HS编码和进口要求。</div></div>
      <div class="faq-item"><div class="faq-q">纺织设备出口需要哪些认证？</div><div class="faq-a">一般不需要特殊认证，但电气设备需符合台湾电压和频率标准。如涉及环保要求的印染设备，需确认台湾环保署的相关规范。</div></div>
      <div class="faq-item"><div class="faq-q">设备运输途中如何防潮？</div><div class="faq-a">木箱内放置干燥剂，箱体做防水处理。海运全程使用防水帆布，仓库中转确保不露天存放。</div></div>''',
        "cta_title": "有纺织设备需要运到台湾？",
    },
    {
        "slug": "printing-equipment",
        "breadcrumb_name": "印刷机械出口台湾",
        "title": "印刷机械出口台湾 | 印刷机/装订设备/印后加工运输 | 速豹集运",
        "description": "印刷机械出口台湾专线：胶印机、数码印刷机、柔印机、凹印机、切纸机、装订设备运输。精密防震包装、报关清关、门到门，6年设备运输经验。",
        "h1": "印刷机械设备出口台湾全流程指南：运输、报关、精密包装",
        "intro": "印刷机械是高精度设备，胶印机、数码印刷机等核心设备对运输过程中的震动、湿度极为敏感。出口台湾需要专业的包装方案和可靠的物流渠道。我们整理了印刷设备出口台湾的完整操作指南。",
        "table_rows": '''<tr><td>胶印机（单色/多色）</td><td>3-20吨</td><td>整柜</td></tr>
        <tr><td>数码印刷机</td><td>0.3-3吨</td><td>拼柜/空运</td></tr>
        <tr><td>柔印机/凹印机</td><td>2-10吨</td><td>整柜</td></tr>
        <tr><td>切纸机/模切机</td><td>1-5吨</td><td>整柜/拼柜</td></tr>
        <tr><td>装订设备（胶装/骑订/锁线）</td><td>0.5-3吨</td><td>拼柜</td></tr>
        <tr><td>CTP制版机</td><td>100-500kg</td><td>空运/拼柜</td></tr>''',
        "step1": "提供设备型号、尺寸、重量和货值，评估最佳运输方案。大型胶印机建议40尺整柜+气囊减震，小型数码设备可选空运。精密光学部件（如CTP激光头）需要特殊包装。",
        "tip": "印刷设备含精密滚筒、齿轮和电子控制系统，运输中需特别注意防震、防潮和防倾斜。建议全程使用气囊减震运输方案。",
        "step2": "印刷设备包装标准：定制钢架木箱，滚筒和压印机构加装固定支架；精密部件（墨路系统、润版系统）拆卸单独包装；控制柜用防静电防潮材料包裹；箱体标注'精密仪器、防震、防潮'标识。",
        "step3": "办理出口报关，准备商业发票、装箱单、设备说明。整柜装运后经由厦门/深圳等口岸发往台湾基隆/台中/高雄港。全程GPS追踪。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">二手印刷机可以出口台湾吗？</div><div class="faq-a">可以出口，但需确认设备是否属于管制范围。建议提前提供设备型号和HS编码，我们协助确认进口管制和关税政策。</div></div>
      <div class="faq-item"><div class="faq-q">印刷机运输需要拆解吗？</div><div class="faq-a">根据设备尺寸决定。大型胶印机通常需要拆卸进纸单元和收纸单元，我们提供专业拆装指导和包装方案。</div></div>
      <div class="faq-item"><div class="faq-q">运输时间需要多久？</div><div class="faq-a">海运整柜从大陆主要港口到台湾约5-7天，加上两端清关和派送，全程约10-14天。空运2-3天。</div></div>''',
        "cta_title": "有印刷设备需要运到台湾？",
    },
    {
        "slug": "electrical-equipment",
        "breadcrumb_name": "电力设备出口台湾",
        "title": "电力设备出口台湾 | 变压器/开关柜/电缆/配电设备运输 | 速豹集运",
        "description": "电力设备出口台湾专线：变压器、高低压开关柜、配电箱、电缆、发电机组运输。专业超限货物运输、吊装、报关清关、门到门服务。",
        "h1": "电力设备出口台湾全流程指南：超限运输、报关、安装协调",
        "intro": "电力设备通常体积庞大、重量惊人——大型变压器可达数十吨，高低压开关柜和电缆盘也需要特殊运输工具。出口台湾涉及超限货物申报、专业吊装和台湾当地电力规范协调。我们整理了电力设备出口台湾的完整指南。",
        "table_rows": '''<tr><td>变压器（油浸/干式）</td><td>5-80吨</td><td>特种柜/框架箱</td></tr>
        <tr><td>高低压开关柜</td><td>0.5-3吨/台</td><td>整柜/拼柜</td></tr>
        <tr><td>配电箱/配电盘</td><td>100-1000kg</td><td>拼柜</td></tr>
        <tr><td>电力电缆/电缆盘</td><td>1-10吨</td><td>平板柜/框架箱</td></tr>
        <tr><td>变频器/软启动器</td><td>50-500kg</td><td>拼柜/空运</td></tr>
        <tr><td>电抗器/电容器组</td><td>0.5-3吨</td><td>拼柜</td></tr>''',
        "step1": "提供设备的详细技术参数（型号、尺寸、重量、电压等级、货值）。大型变压器需要评估超限运输方案（是否需要特种柜/分体运输），开关柜和配电箱评估整柜或拼柜方案。",
        "tip": "电力设备出口台湾需特别注意：① 台湾电力系统为110V/220V、60Hz，需确认设备兼容性；② 大型变压器运输属超限货物，需提前申报；③ 含油设备（油浸变压器）需符合危险品运输规范。",
        "step2": "电力设备包装要点：变压器使用定制钢架+防震木箱，充氮保护防止绝缘受潮；开关柜使用木箱+防震垫，内部元件加固；电缆盘使用专用托架固定；所有设备标注重量和吊装点。",
        "step3": "办理出口报关，大型变压器需提前申报超限货物运输许可。提供商业发票、装箱单、设备技术规范和电气参数表。整柜装运后经深圳/厦门发往台湾。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">大型变压器可以用普通集装箱运输吗？</div><div class="faq-a">超宽超高的大型变压器通常无法装入标准集装箱，需要使用平板柜或框架箱。我们会根据实际尺寸评估最佳运输方案。</div></div>
      <div class="faq-item"><div class="faq-q">电力设备出口台湾需要什么认证？</div><div class="faq-a">台湾对电力设备有BSMI认证要求，具体取决于设备类型。我们建议提前与台湾收货方确认所需的进口认证和检验要求。</div></div>
      <div class="faq-item"><div class="faq-q">含油变压器如何运输？</div><div class="faq-a">油浸变压器需按危险品管理规范运输，排放或保留绝缘油需根据运输方案决定。我们提供合规的危险品申报和专项运输服务。</div></div>''',
        "cta_title": "有电力设备需要运到台湾？",
    },
    {
        "slug": "construction-machinery",
        "breadcrumb_name": "工程机械出口台湾",
        "title": "工程机械出口台湾 | 挖掘机/装载机/推土机/起重机运输 | 速豹集运",
        "description": "工程机械出口台湾专线：挖掘机、装载机、推土机、压路机、起重机、混凝土设备运输。超限货物运输、滚装船、报关清关、门到门服务。",
        "h1": "工程机械设备出口台湾全流程指南：超大件运输、报关、门到门",
        "intro": "工程机械是典型的超大件货物——挖掘机、装载机、起重机等设备体积庞大、自重大，运输需要特种车辆和专业的超限货物操作经验。出口台湾涉及滚装船运输、超限申报和台湾当地的道路许可。我们整理了工程机械出口台湾的完整操作指南。",
        "table_rows": '''<tr><td>挖掘机（小型/中型/大型）</td><td>5-50吨</td><td>滚装船/框架箱</td></tr>
        <tr><td>装载机（轮式/履带式）</td><td>5-30吨</td><td>滚装船/框架箱</td></tr>
        <tr><td>推土机</td><td>8-40吨</td><td>滚装船/特种柜</td></tr>
        <tr><td>压路机</td><td>3-20吨</td><td>框架箱/滚装船</td></tr>
        <tr><td>汽车起重机/履带起重机</td><td>20-200吨</td><td>滚装船/分体运输</td></tr>
        <tr><td>混凝土泵车/搅拌车</td><td>10-40吨</td><td>滚装船</td></tr>''',
        "step1": "提供设备型号、整机尺寸、工作重量等参数。根据设备规格选择运输方式：整机适合滚装船（RORO），部分拆卸后可用框架箱。超大型设备可能需要分体运输。",
        "tip": "工程机械出口台湾关键注意事项：① 设备需清洗干净，无泥土残留（检疫要求）；② 履带式设备需确认是否可以在台湾道路行驶或需要平板车转运；③ 大型设备到港后需协调台湾当地吊车和平板车。",
        "step2": "工程机械包装要点：整机运输无需木箱，但需做好驾驶室和仪表盘防护；液压油缸需收缩到位并固定；电瓶断开，燃油排空或留少量；活动部件（动臂、铲斗）锁定；整车防水防锈处理。",
        "step3": "办理出口报关和超限货物运输申报。准备商业发票、装箱单、设备出厂合格证、发动机号/车架号信息。滚装船运输经由上海/深圳/厦门发往台湾基隆/台中/高雄。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">二手工程机械可以出口台湾吗？</div><div class="faq-a">可以，但台湾对进口二手工程机械有排放标准要求。柴油发动机需符合台湾环保署排放标准，建议提前确认设备是否符合进口条件。</div></div>
      <div class="faq-item"><div class="faq-q">挖掘机用滚装船还是集装箱？</div><div class="faq-a">绝大多数挖掘机使用滚装船（RORO）运输，自行开上船、到达后开下船，是最经济高效的方式。小型挖掘机也可以用框架箱运输。</div></div>
      <div class="faq-item"><div class="faq-q">工程机械到台湾后如何提货？</div><div class="faq-a">我们可安排台湾端的清关和派送，协调平板车和吊车将设备直接送到工地，实现真正的门到门服务。</div></div>''',
        "cta_title": "有工程机械需要运到台湾？",
    },
    {
        "slug": "food-processing",
        "breadcrumb_name": "食品加工设备出口台湾",
        "title": "食品加工设备出口台湾 | 食品生产线/包装机/烘焙设备运输 | 速豹集运",
        "description": "食品加工设备出口台湾专线：食品生产线、灌装机、包装机、烘焙设备、饮料设备运输。食品级包装标准、报关清关、门到门服务。",
        "h1": "食品加工设备出口台湾全流程指南：卫生运输、食品级包装、报关",
        "intro": "食品加工设备对卫生条件有严格要求——从食品生产线到包装机、烘焙设备，运输过程中必须保持洁净、防污染。台湾对食品设备进口有严格的卫生检验标准。我们整理了食品加工设备出口台湾的完整操作指南。",
        "table_rows": '''<tr><td>食品生产线（饼干/方便面/膨化食品）</td><td>2-20吨</td><td>整柜</td></tr>
        <tr><td>灌装/封口设备</td><td>0.5-3吨</td><td>拼柜/整柜</td></tr>
        <tr><td>包装机（枕式/立式/真空）</td><td>0.3-2吨</td><td>拼柜</td></tr>
        <tr><td>烘焙设备（烤炉/醒发箱/搅拌机）</td><td>0.2-3吨</td><td>拼柜</td></tr>
        <tr><td>饮料生产设备（灌装线/杀菌设备）</td><td>1-10吨</td><td>整柜</td></tr>
        <tr><td>肉类/水产加工设备</td><td>0.5-5吨</td><td>拼柜/整柜</td></tr>''',
        "step1": "提供设备型号、材质（不锈钢等级）、尺寸、重量和货值。评估运输方案：大型生产线需整柜运输，小型单机可拼柜。食品接触面材质需确认符合台湾食品容器卫生标准。",
        "tip": "食品设备出口台湾特别要求：① 设备需彻底清洁，无食品残留；② 与食品接触的不锈钢部件需为SUS304或更高等级；③ 台湾对食品机械有卫生安全检验要求，建议提前了解TFDA规范。",
        "step2": "食品设备包装标准：定制木箱（内部覆PE膜防污染），食品接触面额外包裹保鲜膜；设备内部彻底清洁干燥，防锈处理；不锈钢表面覆保护膜防止划伤；箱内放置干燥剂和防霉剂。",
        "step3": "办理出口报关，准备商业发票、装箱单、设备材质证明（不锈钢等级证书）。整柜经由深圳/厦门/宁波等口岸发往台湾。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">食品设备出口台湾需要卫生许可吗？</div><div class="faq-a">食品加工设备本身不需要进口卫生许可，但设备与食品接触的材料需符合台湾食品容器卫生标准。建议提供不锈钢材质证明。</div></div>
      <div class="faq-item"><div class="faq-q">旧食品设备可以出口吗？</div><div class="faq-a">可以，但旧设备需彻底清洁消毒处理，无任何食品残留。台湾海关对旧食品设备会严格检查卫生状况。</div></div>
      <div class="faq-item"><div class="faq-q">设备运输过程中如何保证洁净？</div><div class="faq-a">设备包装前彻底清洁并干燥，食品接触面覆PE膜保护，木箱内部覆防潮膜，全程使用密闭集装箱运输。</div></div>''',
        "cta_title": "有食品加工设备需要运到台湾？",
    },
    {
        "slug": "plastic-machinery",
        "breadcrumb_name": "塑料机械出口台湾",
        "title": "塑料机械出口台湾 | 注塑机/挤出机/吹塑机/回收设备运输 | 速豹集运",
        "description": "塑料机械出口台湾专线：注塑机（已完成）、挤出机、吹塑机、吹膜机、造粒机、回收设备运输。大型注塑机整柜、报关清关、门到门服务。",
        "h1": "塑料机械设备出口台湾全流程指南：大型注塑机、挤出机运输",
        "intro": "塑料机械是两岸贸易中最常见的设备品类之一。注塑机、挤出机、吹塑机等设备重量大、体积大，出口台湾需要专业的运输方案。我们整理了除注塑机外的其他塑料设备出口台湾的完整操作指南。（注塑机详见专用页）",
        "table_rows": '''<tr><td>挤出机（单螺杆/双螺杆）</td><td>1-8吨</td><td>整柜/拼柜</td></tr>
        <tr><td>吹塑机（中空成型机）</td><td>2-10吨</td><td>整柜</td></tr>
        <tr><td>吹膜机</td><td>1-5吨</td><td>整柜/拼柜</td></tr>
        <tr><td>造粒机/回收设备</td><td>1-6吨</td><td>整柜/拼柜</td></tr>
        <tr><td>热成型机（吸塑机）</td><td>0.5-3吨</td><td>拼柜</td></tr>
        <tr><td>塑料破碎机/粉碎机</td><td>0.3-2吨</td><td>拼柜</td></tr>''',
        "step1": "提供设备型号、锁模力（注塑机）/螺杆直径（挤出机）、尺寸、重量等参数。大型吹塑机需评估是否需要拆卸模具头和合模机构，挤出机需确认螺杆是否需要单独保护。",
        "tip": "塑料机械出口台湾提示：① 注塑机通常需拆卸模具头/料筒方便运输；② 液压系统需排空或固定，避免运输泄漏；③ 控制柜需防震防潮处理。",
        "step2": "塑料设备包装标准：大型设备使用定制钢架木箱，精密部件（螺杆、模具头）单独包装固定；液压管路排空或关闭阀门；控制柜用防静电防潮材料包裹；所有活动部件锁定并用防震垫隔离。",
        "step3": "办理出口报关，准备商业发票、装箱单、设备参数表。整柜经由深圳/厦门发往台湾基隆/台中/高雄港。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">注塑机和挤出机可以拼柜运输吗？</div><div class="faq-a">小型注塑机（100吨以下）和挤出机可以和其他设备拼柜运输。大型设备建议整柜运输以确保安全。</div></div>
      <div class="faq-item"><div class="faq-q">塑料机械出口台湾需要什么认证？</div><div class="faq-a">一般需要提供设备CE认证或ISO标准合规文件。台湾对注塑机安全有CNS标准要求，建议确认设备是否符合。</div></div>
      <div class="faq-item"><div class="faq-q">设备运输保险怎么买？</div><div class="faq-a">建议按设备货值的110%投保货物运输险，我们可以协助办理。费率约货值的0.3%-0.5%。</div></div>''',
        "cta_title": "有塑料设备需要运到台湾？",
    },
    {
        "slug": "woodworking",
        "breadcrumb_name": "木工机械出口台湾",
        "title": "木工机械出口台湾 | 封边机/开料机/砂光机/数控雕刻机运输 | 速豹集运",
        "description": "木工机械出口台湾专线：数控开料机、封边机、砂光机、钻孔中心、CNC雕刻机、木工生产线运输。精密包装、报关清关、门到门服务。",
        "h1": "木工机械设备出口台湾全流程指南：运输、包装、报关一站式",
        "intro": "木工机械涵盖从板材开料到成品加工的全系列设备，数控化程度高，设备精度直接影响加工品质。出口台湾需要专业的防震包装和可靠的物流渠道。我们整理了木工设备出口台湾的完整操作指南。",
        "table_rows": '''<tr><td>数控开料机/裁板锯</td><td>1-4吨</td><td>整柜/拼柜</td></tr>
        <tr><td>自动封边机</td><td>0.5-2吨</td><td>拼柜</td></tr>
        <tr><td>CNC雕刻机/加工中心</td><td>0.3-3吨</td><td>拼柜/整柜</td></tr>
        <tr><td>砂光机（宽带/异形）</td><td>1-5吨</td><td>整柜/拼柜</td></tr>
        <tr><td>六面钻/排钻</td><td>0.5-2吨</td><td>拼柜</td></tr>
        <tr><td>木工生产线（板式/实木定制）</td><td>5-15吨</td><td>整柜</td></tr>''',
        "step1": "提供设备型号、加工尺寸、重量、数控系统品牌等参数。板式家具生产线设备较多，建议整柜集中运输；单台CNC雕刻机可拼柜。",
        "tip": "木工设备运输注意事项：① 数控设备需做好控制系统防震，建议拆卸控制面板单独包装；② 精密导轨和丝杆需涂抹防锈油并固定；③ 刀具需拆卸单独装箱。",
        "step2": "木工设备包装标准：定制实木熏蒸木箱，台面和导轨面加装防护垫；控制系统和显示屏用防震泡沫单独包装；刀具和配件用工具箱集中装箱；整线设备统一编号便于台湾端安装对位。",
        "step3": "办理出口报关，准备商业发票、装箱单、设备参数表。整柜经由深圳/厦门/宁波等口岸发往台湾。到港后协调派送到工厂。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">木工设备出口台湾需要熏蒸吗？</div><div class="faq-a">是的，实木包装箱必须经过熏蒸处理并加施IPPC标识，符合ISPM 15国际标准。我们使用的所有木箱都已熏蒸达标。</div></div>
      <div class="faq-item"><div class="faq-q">家具生产线如何整体运输？</div><div class="faq-a">整线设备建议使用多个集装箱集中运输，每台设备独立木箱包装并编号。台湾端按编号顺序拆箱安装，效率最高。</div></div>
      <div class="faq-item"><div class="faq-q">数控雕刻机运输需要注意什么？</div><div class="faq-a">关键在主轴和导轨保护：主轴需用专用支架固定，导轨涂抹防锈油并加装保护罩，控制系统做好防震防潮。</div></div>''',
        "cta_title": "有木工设备需要运到台湾？",
    },
    {
        "slug": "metal-processing",
        "breadcrumb_name": "金属加工设备出口台湾",
        "title": "金属加工设备出口台湾 | 剪板机/折弯机/激光切割/焊接设备运输 | 速豹集运",
        "description": "金属加工设备出口台湾专线：激光切割机、剪板机、折弯机、冲床、焊接设备、钣金加工线运输。重型设备专业包装、报关清关、门到门。",
        "h1": "金属加工设备出口台湾全流程指南：重型运输、专业包装、报关",
        "intro": "金属加工设备通常重量大、体积大，是典型的工业重型设备。剪板机、折弯机、激光切割机等设备出口台湾，需要专业的吊装、运输和包装方案。我们整理了金属加工设备出口台湾的完整操作指南（冲床/折弯机详见专用页面）。",
        "table_rows": '''<tr><td>光纤激光切割机</td><td>1-8吨</td><td>整柜</td></tr>
        <tr><td>剪板机（液压/数控）</td><td>2-10吨</td><td>整柜</td></tr>
        <tr><td>卷板机</td><td>1-5吨</td><td>整柜/拼柜</td></tr>
        <tr><td>焊接设备（氩弧/二保/激光焊）</td><td>50-1000kg</td><td>拼柜</td></tr>
        <tr><td>钣金加工生产线</td><td>5-20吨</td><td>整柜（多柜）</td></tr>
        <tr><td>型材弯曲机/弯管机</td><td>0.5-3吨</td><td>拼柜</td></tr>''',
        "step1": "提供设备型号、加工能力（如折弯吨位、切割幅面）、尺寸、重量。大型剪板机和激光切割机建议整柜运输，小型焊接设备可拼柜。",
        "tip": "金属加工设备运输要点：① 激光切割机激光器和切割头是最精密的部件，需单独拆卸包装；② 重型设备吊装需确认吊点位置和重心；③ 油压系统需排空或密封处理。",
        "step2": "金属加工设备包装：重型设备使用钢架+木箱双重结构，设备与底座用螺栓固定；精密部件（激光器、光学镜片）防震箱独立包装；液压系统密封处理防止泄漏；控制柜防潮防静电包装。",
        "step3": "办理出口报关，准备商业发票、装箱单、设备技术参数。大型设备需提供吊装方案和重心图。整柜经由深圳/厦门发往台湾。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">激光切割机运输如何保护激光器？</div><div class="faq-a">激光器和切割头是核心精密部件，建议拆卸下来独立用防震箱包装，到达台湾后再安装调试。</div></div>
      <div class="faq-item"><div class="faq-q">超长剪板机怎么运输？</div><div class="faq-a">超长剪板机（6m以上）可使用框架箱或平板柜运输，超出标准集装箱尺寸的需申报超限货物。</div></div>
      <div class="faq-item"><div class="faq-q">焊接设备需要特殊运输条件吗？</div><div class="faq-a">一般不需要。但含气瓶的焊接设备需排空气体，电子控制部分做好防潮处理即可。</div></div>''',
        "cta_title": "有金属加工设备需要运到台湾？",
    },
    {
        "slug": "mining-equipment",
        "breadcrumb_name": "矿山设备出口台湾",
        "title": "矿山设备出口台湾 | 破碎机/筛分设备/球磨机/输送设备运输 | 速豹集运",
        "description": "矿山设备出口台湾专线：颚式破碎机、圆锥破碎机、振动筛、球磨机、输送机、分级设备运输。超重件特种运输、报关清关、门到门服务。",
        "h1": "矿山设备出口台湾全流程指南：超重运输、分体方案、特种物流",
        "intro": "矿山设备是工业运输中最具挑战性的品类——破碎机、球磨机等单件重量可达数十吨，对运输工具和吊装设备要求极高。出口台湾往往需要分体运输或特种柜方案。我们整理了矿山设备出口台湾的完整操作指南。",
        "table_rows": '''<tr><td>颚式破碎机</td><td>5-50吨</td><td>框架箱/分体运输</td></tr>
        <tr><td>圆锥破碎机</td><td>3-30吨</td><td>框架箱/特种柜</td></tr>
        <tr><td>反击式破碎机</td><td>3-25吨</td><td>框架箱</td></tr>
        <tr><td>振动筛/圆振筛</td><td>1-10吨</td><td>整柜/框架箱</td></tr>
        <tr><td>球磨机/棒磨机</td><td>10-80吨</td><td>分体运输/特种柜</td></tr>
        <tr><td>输送机/提升机</td><td>2-15吨</td><td>框架箱</td></tr>''',
        "step1": "提供设备型号、生产能力、整体尺寸和重量、是否需要分体运输。超大型球磨机和破碎机通常分体运输（筒体、传动装置分别装箱），需制定详细的拆解和组装方案。",
        "tip": "矿山设备出口台湾关键事项：① 超重件需确认台湾港口卸货能力（基隆/台中/高雄港均有重型吊机）；② 分体运输需编制详细的装箱清单和安装指引；③ 旧矿山设备需彻底清洗，无矿渣残留。",
        "step2": "矿山设备包装：超重件使用钢架底座+螺栓固定，精密轴承部位加装防护罩；分体部件按装配顺序编号装箱；易损件（衬板、筛网）独立包装并标注；所有金属加工面涂抹防锈油。",
        "step3": "办理出口报关，超限货物提前申报。准备商业发票、装箱单、设备图纸和吊装方案。经由上海/深圳等深水港发往台湾。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">50吨以上的矿山设备能运到台湾吗？</div><div class="faq-a">可以，但需要分体运输。我们将设备拆解为可运输的模块，到达台湾后在现场组裝。需提前制定详细的分体方案和组裝计划。</div></div>
      <div class="faq-item"><div class="faq-q">台湾港口能卸重型设备吗？</div><div class="faq-a">台湾基隆、台中、高雄等主要港口均有100吨以上的岸边吊机，可以处理大型重型设备卸货。</div></div>
      <div class="faq-item"><div class="faq-q">矿山设备出口台湾有什么环保要求？</div><div class="faq-a">设备需清洁无尘，旧设备特别需要彻底清洗，去除矿渣和粉尘残留。台湾海关会对设备清洁度进行检查。</div></div>''',
        "cta_title": "有矿山设备需要运到台湾？",
    },
    {
        "slug": "generator",
        "breadcrumb_name": "发电机出口台湾",
        "title": "发电机/发电机组出口台湾 | 柴油发电机/燃气发电机/变压器运输 | 速豹集运",
        "description": "发电机出口台湾专线：柴油发电机组、燃气发电机、备用电源系统、变压器运输。超重设备运输、报关清关、门到门安装协调服务。",
        "h1": "发电机及变压器出口台湾全流程指南：超重运输、报关、安装协调",
        "intro": "柴油发电机组和大型变压器属于工业和基础设施核心设备，通常重量大、价值高。出口台湾涉及超重运输、危险品管理（燃油系统）和台湾当地的电气规范协调。我们整理了发电机及变压器出口台湾的完整操作指南。",
        "table_rows": '''<tr><td>柴油发电机组（50-2000kW）</td><td>1-20吨</td><td>整柜/框架箱</td></tr>
        <tr><td>燃气发电机组</td><td>3-15吨</td><td>整柜/框架箱</td></tr>
        <tr><td>静音/防雨型发电机组</td><td>1-10吨</td><td>框架箱</td></tr>
        <tr><td>ATS自动转换柜</td><td>100-500kg</td><td>拼柜</td></tr>
        <tr><td>变压器（油浸/干式/箱变）</td><td>2-30吨</td><td>框架箱/特种柜</td></tr>
        <tr><td>高低压配电柜组</td><td>0.5-2吨/台</td><td>整柜</td></tr>''',
        "step1": "提供发电机组型号、功率、尺寸、重量、燃料类型等参数。大型发电机组建议框架箱运输，小型机组可用标准柜。变压器需确认是否含油及油量。",
        "tip": "发电机出口台湾特别注意事项：① 柴油发电机需排空燃油（或封闭燃油系统）；② 蓄电池需断开并做好绝缘保护；③ 台湾电压频率为60Hz，需确认设备兼容性或加配变频器。",
        "step2": "发电机组包装标准：钢架底座+防震木箱，机组与底座螺栓固定；散热器和控制面板加装防护；蓄电池拆卸单独防震包装；排气管道端口封堵防异物进入。",
        "step3": "办理出口报关，含油设备需额外危险品申报。准备商业发票、装箱单、设备技术参数和出厂测试报告。整柜经由厦门/深圳发往台湾。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">柴油发电机运输需要排空燃油吗？</div><div class="faq-a">是的，运输安全规范要求柴油发电机排空燃油或封闭燃油系统。蓄电池也需要断开连接。我们会在发货前指导完成这些准备工作。</div></div>
      <div class="faq-item"><div class="faq-q">大陆50Hz发电机在台湾60Hz能用吗？</div><div class="faq-a">这取决于具体设备。部分发电机组可以通过调速器调整频率，但额定50Hz的电机在60Hz下转速和功率都会变化。建议在发货前与制造商确认兼容性。</div></div>
      <div class="faq-item"><div class="faq-q">发电机组出口需要CE认证吗？</div><div class="faq-a">台湾对发电机组有BSMI电磁兼容和安规要求。建议提供设备的CE证书或等同的测试报告，以便顺利清关。</div></div>''',
        "cta_title": "有发电机组需要运到台湾？",
    },
    {
        "slug": "pump-valve",
        "breadcrumb_name": "泵阀设备出口台湾",
        "title": "泵阀设备出口台湾 | 水泵/阀门/管道/流体设备运输 | 速豹集运",
        "description": "泵阀设备出口台湾专线：离心泵、化工泵、阀门、管道管件、流体控制系统运输。专业防震包装、报关清关、门到门服务。",
        "h1": "泵阀设备出口台湾全流程指南：精密泵阀运输、包装、报关",
        "intro": "泵阀设备是工业流体系统的核心部件，涵盖了从水泵、化工泵到各类阀门和管道管件。虽然单件重量相对可控，但精密泵阀对运输中的震动和污染非常敏感。我们整理了泵阀设备出口台湾的完整操作指南。",
        "table_rows": '''<tr><td>离心泵（单级/多级）</td><td>50-3000kg</td><td>拼柜/整柜</td></tr>
        <tr><td>化工泵（耐腐蚀/磁力驱动）</td><td>30-2000kg</td><td>拼柜</td></tr>
        <tr><td>潜水泵/深井泵</td><td>50-1000kg</td><td>拼柜</td></tr>
        <tr><td>阀门（闸阀/截止阀/球阀/蝶阀）</td><td>5-500kg/个</td><td>拼柜</td></tr>
        <tr><td>管道管件（碳钢/不锈钢）</td><td>批量不等</td><td>整柜/拼柜</td></tr>
        <tr><td>流体控制/计量系统</td><td>100-2000kg</td><td>拼柜</td></tr>''',
        "step1": "提供泵型、流量、扬程、材质、重量等参数。批量管件和阀门可以拼柜运输降低成本，大型工业泵组建议整柜。精密泵需要防震包装方案。",
        "tip": "泵阀设备运输要点：① 泵体和电机联轴器需要固定或拆卸运输；② 阀门密封面需加保护盖或垫片；③ 不锈钢管件需做表面防护防止刮伤；④ 机械密封属于精密部件需特别保护。",
        "step2": "泵阀设备包装：泵体和电机底座用螺栓固定在木箱底板；法兰面和密封面加装保护盖；精密部件（机械密封、轴承）独立包装；不锈钢管件端口封堵，管体用缠绕膜保护；多品种配件按清单编号装箱。",
        "step3": "办理出口报关，准备商业发票、装箱单和材质证明（如需要）。拼柜货物经由深圳/厦门/宁波发往台湾。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">化工泵出口台湾需要什么认证？</div><div class="faq-a">一般工业泵阀不需要特殊认证。但用于食品、医疗或危险化学品场合的泵阀可能需要相应的材质认证和合规声明。</div></div>
      <div class="faq-item"><div class="faq-q">大批量阀门和管件如何运输最经济？</div><div class="faq-a">批量货物建议拼柜或整柜海运。按重量和体积综合计费，大宗货物整柜运输通常成本更低。</div></div>
      <div class="faq-item"><div class="faq-q">泵阀设备运输容易损坏吗？</div><div class="faq-a">密封面和精密部件最容易损坏。我们使用专业包装方案：法兰面加保护盖、泵体固定、精密部件独立包装，运输损坏率极低。</div></div>''',
        "cta_title": "有泵阀设备需要运到台湾？",
    },
    {
        "slug": "mold-tooling",
        "breadcrumb_name": "模具工装出口台湾",
        "title": "模具工装出口台湾 | 注塑模具/冲压模具/压铸模具/检具运输 | 速豹集运",
        "description": "模具工装出口台湾专线：注塑模具、冲压模具、压铸模具、检具、夹具运输。精密防锈防震包装、报关清关、门到门，6年设备运输经验。",
        "h1": "模具工装出口台湾全流程指南：精密模具运输、防锈包装、报关",
        "intro": "模具是制造业的'工业之母'，注塑模具、冲压模具等高精度工装价值高、精度要求极高。出口台湾需要专业的防锈、防震包装方案，确保模具在运输途中不受任何损伤。我们整理了模具工装出口台湾的完整操作指南。",
        "table_rows": '''<tr><td>注塑模具（单穴/多穴）</td><td>100kg-5吨</td><td>拼柜/整柜</td></tr>
        <tr><td>冲压模具（单工序/级进模）</td><td>200kg-8吨</td><td>拼柜/整柜</td></tr>
        <tr><td>压铸模具</td><td>200kg-5吨</td><td>拼柜/整柜</td></tr>
        <tr><td>检具/测量工装</td><td>50-500kg</td><td>拼柜</td></tr>
        <tr><td>夹具/治具</td><td>10-200kg</td><td>拼柜/空运</td></tr>
        <tr><td>热流道系统</td><td>20-200kg</td><td>空运/拼柜</td></tr>''',
        "step1": "提供模具类型、尺寸、重量、模穴数、货值等参数。大型冲压模具建议整柜运输，中小型注塑模具可拼柜。高价值精密模具建议全程投保。",
        "tip": "模具运输核心要点：① 型腔面和分型面是高精度表面，必须彻底防锈处理并加保护；② 滑块、顶针等活动部件需锁定或拆卸单独包装；③ 模具严禁叠压——每套模具独立底座固定。",
        "step2": "模具包装标准：模具型腔和分型面涂抹防锈油+覆保护膜；模具使用专用底座固定在木箱内，严禁悬挂；活动部件（滑块/斜顶）用支撑块锁定；冷却水道端口封堵，排水彻底；每套模具附带水路图和顶针图。",
        "step3": "办理出口报关，准备商业发票、装箱单。模具HTS编码相对统一（8480系列），清关流程成熟。经由深圳/厦门等地发往台湾。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">模具出口台湾需要熏蒸木箱吗？</div><div class="faq-a">是的，实木包装箱必须经过熏蒸处理并加施IPPC标识。我们使用的所有木箱均符合ISPM 15国际标准。</div></div>
      <div class="faq-item"><div class="faq-q">模具运输如何防止生锈？</div><div class="faq-a">模具型腔和分型面涂抹优质防锈油，包裹防锈纸，木箱内放置干燥剂。海运集装箱做好防水密封，确保全程干燥环境。</div></div>
      <div class="faq-item"><div class="faq-q">模具出口台湾关税是多少？</div><div class="faq-a">模具HS编码多在8480系列，台湾对该类产品关税较低，部分在ECFA早期收获清单中可享受零关税。具体以HS编码确认为准。</div></div>''',
        "cta_title": "有模具工装需要运到台湾？",
    },
    {
        "slug": "lab-equipment",
        "breadcrumb_name": "实验室设备出口台湾",
        "title": "实验室设备出口台湾 | 分析仪器/实验设备/科研仪器运输 | 速豹集运",
        "description": "实验室设备出口台湾专线：色谱仪、光谱仪、显微镜、离心机、培养箱、实验台运输。精密仪器防震防潮包装、报关清关、门到门服务。",
        "h1": "实验室设备出口台湾全流程指南：精密仪器运输、防震包装、报关",
        "intro": "实验室仪器设备属于高精密、高价值货物——色谱仪、光谱仪、显微镜等仪器对运输条件要求极为苛刻。震动、温差、湿度都可能影响仪器的精度和校准状态。我们整理了实验室设备出口台湾的完整操作指南。",
        "table_rows": '''<tr><td>液相色谱/气相色谱仪</td><td>50-200kg</td><td>空运/拼柜</td></tr>
        <tr><td>光谱仪（ICP/AAS/UV-Vis）</td><td>30-150kg</td><td>空运/拼柜</td></tr>
        <tr><td>电子显微镜（SEM/TEM）</td><td>100-500kg</td><td>空运/拼柜</td></tr>
        <tr><td>离心机（高速/超高速）</td><td>50-300kg</td><td>空运/拼柜</td></tr>
        <tr><td>恒温培养箱/灭菌器</td><td>50-400kg</td><td>拼柜</td></tr>
        <tr><td>实验室家具/通风系统</td><td>批量不等</td><td>整柜</td></tr>''',
        "step1": "提供仪器型号、品牌、尺寸、重量、货值、是否含易损部件等参数。精密分析仪器强烈建议空运以缩短运输时间、减少震动累积。大型实验台和通风系统可海运整柜。",
        "tip": "精密仪器运输核心要求：① 部分仪器需要原厂运输锁止装置，确保内部光学/机械组件在运输中不位移；② 含光源（激光/紫外灯）的仪器需特别注意防震；③ 部分仪器可能需要恒温运输或防静电包装。",
        "step2": "实验室设备包装标准：优先使用原厂包装箱（如可用）；精密仪器使用双层防震箱：外层木箱+内层高密度泡沫定制模腔；光学部件和电极等耗材独立包装；箱体标注'精密仪器、向上、防潮、易碎'。",
        "step3": "办理出口报关，高价值仪器建议购买全程运输保险。准备商业发票、装箱单。空运经由深圳/上海机场发往台湾桃园/松山机场，时效2-3天。",
        "faq_items": '''<div class="faq-item"><div class="faq-q">精密实验室仪器建议空运还是海运？</div><div class="faq-a">强烈建议空运。虽然费用较高，但运输时间短（2-3天 vs 7-10天），震动累积少，温湿度变化小，对精密仪器的保护效果远优于海运。</div></div>
      <div class="faq-item"><div class="faq-q">仪器运输保险怎么买？</div><div class="faq-a">建议按仪器货值的110%投保。我方合作的保险公司提供专门的精密仪器运输险，费率约货值的0.3%-0.5%。</div></div>
      <div class="faq-item"><div class="faq-q">二手实验室设备可以出口吗？</div><div class="faq-a">可以，但需确认设备是否属于出口管制范围（如涉及敏感技术的质谱仪）。一般实验室设备出口台湾无特殊管制。</div></div>''',
        "cta_title": "有实验室设备需要运到台湾？",
    },
]

def generate_page(data):
    """生成单个设备品类页面"""
    html = TEMPLATE.format(
        title=data["title"],
        description=data["description"],
        slug=data["slug"],
        breadcrumb_name=data["breadcrumb_name"],
        h1=data["h1"],
        intro=data["intro"],
        table_rows=data["table_rows"],
        step1=data["step1"],
        tip=data["tip"],
        step2=data["step2"],
        step3=data["step3"],
        faq_items=data["faq_items"],
        cta_title=data["cta_title"],
    )
    filepath = os.path.join(OUTPUT_DIR, data["slug"] + ".html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    return filepath


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for i, page in enumerate(PAGES, 1):
        filepath = generate_page(page)
        print(f"[{i:2d}/13] ✅ {filepath}")
    print("\n🎉 全部13个设备品类页生成完成！")
