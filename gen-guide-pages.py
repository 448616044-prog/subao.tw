#!/usr/bin/env python3
"""批量生成 subaotw.cn guide/ 知识权威页"""

import os

OUTPUT_DIR = "/Users/mac/WorkBuddy/Claw/物流項目/sites/subaotw-cn/guide"

TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://www.subaotw.cn/guide/{slug}">
  <style>
    :root{{--primary:#1a56db;--accent:#f97316;--bg:#f8fafc;--card:#fff;--text:#1e293b;--text-light:#64748b;--border:#e2e8f0;--radius:12px}}
    *{{margin:0;padding:0;box-sizing:border-box}}
    body{{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;color:var(--text);line-height:1.8;background:var(--bg)}}
    .container{{max-width:900px;margin:0 auto;padding:0 20px}}
    .header{{background:rgba(255,255,255,0.95);backdrop-filter:blur(12px);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100}}
    .header .container{{display:flex;align-items:center;justify-content:space-between;height:64px;max-width:1200px}}
    .logo{{font-size:20px;font-weight:800;color:var(--primary);text-decoration:none}}
    .logo span{{color:var(--accent);font-size:12px;font-weight:500;margin-left:6px;padding:2px 8px;background:#fff7ed;border-radius:20px}}
    .breadcrumb{{padding:20px 0;font-size:14px;color:var(--text-light)}}.breadcrumb a{{color:var(--primary);text-decoration:none}}
    article{{padding-bottom:60px}}
    article h1{{font-size:32px;font-weight:800;margin-bottom:20px;line-height:1.3}}
    article h2{{font-size:22px;font-weight:700;margin:36px 0 14px;color:var(--primary);padding-bottom:8px;border-bottom:2px solid #dbeafe}}
    article h3{{font-size:18px;font-weight:700;margin:24px 0 10px}}
    article p{{font-size:16px;margin-bottom:14px;color:var(--text)}}
    article ul,article ol{{margin:10px 0 14px 24px;color:var(--text-light)}}article li{{margin-bottom:6px}}
    .info-box{{background:#eff6ff;border-left:4px solid var(--primary);padding:16px 20px;border-radius:8px;margin:20px 0;font-size:14px}}
    .info-box strong{{display:block;margin-bottom:4px;color:var(--primary)}}
    table{{width:100%;border-collapse:collapse;margin:20px 0;background:var(--card);border-radius:var(--radius);overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,0.06)}}
    th{{background:var(--primary);color:#fff;padding:12px 16px;text-align:left;font-size:14px}}
    td{{padding:12px 16px;border-bottom:1px solid var(--border);font-size:14px}}tr:last-child td{{border-bottom:none}}
    .cta{{background:linear-gradient(135deg,var(--accent) 0%,#ea580c 100%);color:#fff;text-align:center;padding:48px 20px;border-radius:var(--radius);margin:40px 0}}
    .cta h2{{color:#fff;margin-top:0;border:none;padding:0;font-size:24px}}
    .btn{{display:inline-block;padding:14px 32px;background:#fff;color:var(--accent);border-radius:10px;font-weight:700;font-size:16px;text-decoration:none;transition:all .2s}}.btn:hover{{transform:translateY(-2px)}}
    .footer{{background:#0f172a;color:#94a3b8;padding:40px 0 20px;text-align:center;font-size:13px}}
    .footer a{{color:#64748b;text-decoration:none}}
    @media(max-width:768px){{article h1{{font-size:26px}}}}
  </style>
</head>
<body>
  <header class="header"><div class="container"><a href="/" class="logo">速豹集运<span>两岸物流</span></a></div></header>
  <div class="container"><div class="breadcrumb"><a href="/">首页</a> › <a href="/guide/">物流指南</a> › {breadcrumb_name}</div></div>
  <article><div class="container">
    <h1>{h1}</h1>
    <p>{intro}</p>
    {body}
    <div class="cta"><h2>{cta_title}</h2><p style="opacity:0.9">发送货物信息，30分钟内获取方案和报价</p><a href="/contact" class="btn">立即咨询</a></div>
  </div></article>
  <footer class="footer"><p>© 2026 速豹集运 Subao Logistics | 两岸物流专线</p><p style="margin-top:8px"><a href="https://beian.miit.gov.cn/" target="_blank" rel="nofollow">湘ICP备2026016030号-2</a></p></footer>
</body>
</html>'''

PAGES = [
    {
        "slug": "customs-documents",
        "breadcrumb_name": "报关文件清单",
        "title": "设备出口台湾报关文件清单 | 商业发票/装箱单/原产地证 | 速豹集运",
        "description": "设备出口台湾需要准备哪些报关文件？商业发票、装箱单、原产地证明、设备技术参数表等详细清单。速豹集运提供一站式报关服务。",
        "h1": "大件设备出口台湾报关文件完整清单及准备指南",
        "intro": "大件设备出口台湾涉及复杂的报关手续，文件准备是否齐全直接影响通关效率。我们整理了设备出口台湾的全套报关文件清单和每份文件的具体要求。",
        "body": '''<h2>必备文件清单</h2>
<table><tr><th>文件名称</th><th>用途</th><th>准备要点</th></tr>
<tr><td><strong>商业发票</strong></td><td>申报货值和交易信息</td><td>需注明设备名称、型号、数量、单价、总价、贸易条款（FOB/CIF）</td></tr>
<tr><td><strong>装箱单</strong></td><td>核对货物明细</td><td>列明每件货物的重量、尺寸、包装方式，与发票信息一致</td></tr>
<tr><td><strong>设备技术参数表</strong></td><td>HS编码归类依据</td><td>注明设备功能、功率、重量、尺寸、材质等技术指标</td></tr>
<tr><td><strong>原产地证明</strong></td><td>ECFA关税优惠</td><td>由贸促会或海关签发，证明设备产自中国大陆</td></tr>
<tr><td><strong>出口报关委托书</strong></td><td>授权报关</td><td>委托报关行代理出口报关手续</td></tr>
<tr><td><strong>合同/订单</strong></td><td>证明交易真实性</td><td>买卖双方签字盖章的贸易合同</td></tr></table>

<h2>可选文件（视情况需要）</h2>
<table><tr><th>文件</th><th>何时需要</th></tr>
<tr><td>旧设备装运前检验报告</td><td>出口旧机电产品时</td></tr>
<tr><td>出口许可证</td><td>涉及两用物项管制的设备</td></tr>
<tr><td>危险品运输声明</td><td>含油/含电池设备</td></tr>
<tr><td>木质包装熏蒸证明</td><td>使用实木包装时（ISPM 15）</td></tr>
<tr><td>保险单</td><td>需要投保高价值设备时</td></tr></table>

<h2>HS编码归类建议</h2>
<p>设备出口最关键的一步是确定正确的HS编码。HS编码决定了适用关税税率和是否需要特殊许可。以下是常见设备的HS编码范围：</p>
<ul>
<li><strong>CNC加工中心</strong>：8457-8459系列</li>
<li><strong>注塑机</strong>：8477系列</li>
<li><strong>冲床/折弯机</strong>：8462系列</li>
<li><strong>包装机械</strong>：8422系列</li>
</ul>
<p>建议在发货前由专业报关行确认HS编码，避免归类错误导致退单或罚款。</p>

<div class="info-box"><strong>💡 我们提供的服务</strong>速豹集运提供一站式报关服务：协助准备全套文件、HS编码归类、原产地证明办理。您只需提供设备基本信息和贸易合同即可。</div>''',
        "cta_title": "需要设备出口报关协助？",
    },
    {
        "slug": "taiwan-import-tax",
        "breadcrumb_name": "台湾进口关税",
        "title": "台湾进口关税计算 | 设备出口台湾税率查詢 | 速豹集运",
        "description": "设备出口台湾要交多少关税？台湾进口关税计算方法、HS编码查詢、ECFA优惠税率详解。速豹集运6年两岸物流经验。",
        "h1": "台湾进口关税计算指南：设备出口台湾税率详解",
        "intro": "设备出口台湾时，了解台湾的关税政策可以帮助你更准确地预估总成本。本文详细介绍台湾进口关税的计算方法、常见设备的税率范围以及如何利用ECFA框架享受关税优惠。",
        "body": '''<h2>台湾进口关税基本结构</h2>
<p>台湾对进口货物征收的主要税费包括：</p>
<ul><li><strong>进口关税</strong>：按CIF完税价格的百分比征收</li><li><strong>营业税（VAT）</strong>：目前为5%（2026年），按CIF价+关税后的金额计算</li><li><strong>货物税</strong>：特定商品（如汽车）额外征收</li></ul>

<h2>关税计算公式</h2>
<div class="info-box"><strong>标准公式</strong>
总税费 = 进口关税 + 营业税<br>
进口关税 = CIF价 × 关税率<br>
营业税 = (CIF价 + 进口关税) × 5%</div>

<h2>常见设备关税参考</h2>
<table><tr><th>设备类型</th><th>HS编码范围</th><th>台湾关税率</th></tr>
<tr><td>CNC加工中心</td><td>8457-8459</td><td>0-5%</td></tr>
<tr><td>注塑机</td><td>8477.10</td><td>0-2.5%</td></tr>
<tr><td>冲床</td><td>8462</td><td>0-5%</td></tr>
<tr><td>包装机械</td><td>8422</td><td>0-5%</td></tr>
<tr><td>纺织机械</td><td>8445-8447</td><td>0-3%</td></tr></table>
<p style="font-size:13px;color:var(--text-light)">※ 以上为参考范围，具体以HS编码实际归类为准。关税政策可能调整。</p>

<h2>ECFA关税优惠</h2>
<p>在ECFA框架下，部分大陆制造的设备出口台湾可享受零关税或优惠税率。申请ECFA优惠关税需要提供：</p>
<ul><li>ECFA原产地证明书（Form ECFA）</li><li>设备必须满足ECFA原产地规则（大陆增值≥一定比例）</li><li>在报关时主动申报ECFA优惠</li></ul>
<p>并非所有设备都在ECFA清单中，需逐项确认HS编码是否在早期收获清单内。</p>''',
        "cta_title": "需要确认设备关税？",
    },
    {
        "slug": "packaging-standard",
        "breadcrumb_name": "设备包装标准",
        "title": "设备出口包装标准 | 木箱熏蒸/防震防潮/ISPM15 | 速豹集运",
        "description": "大件设备出口台湾的包装标准详解：ISPM15熏蒸木箱、防震包装、防潮处理、重型设备固定方案。速豹集运专业包装服务。",
        "h1": "大件设备出口台湾木箱包装标准全解：熏蒸/防震/防潮",
        "intro": "设备包装直接关系到运输安全——包装不当轻则设备损坏、重则被海关退运。本文详解设备出口台湾的包装标准，包括ISPM 15熏蒸要求、防震方案和防潮措施。",
        "body": '''<h2>木箱包装的四大标准</h2>

<h3>1. ISPM 15 熏蒸标准</h3>
<p>所有出口的实木包装必须经过ISPM 15国际标准熏蒸处理，并加施IPPC标识。这是国际通用的检疫要求，缺少标识将被退运或销毁。</p>
<ul><li>熏蒸方式：热处理（HT）或溴甲烷熏蒸（MB）</li><li>IPPC标识需清晰可辨，包含国家代码、处理方式代码和熏蒸企业编号</li><li>胶合板/免熏蒸板材不需要额外熏蒸处理</li></ul>

<h3>2. 防震包装</h3>
<p>精密设备的核心部件需要特别防震保护：</p>
<ul><li>主轴/导轨等精密部件：加装防震支撑块或运输锁止装置</li><li>控制面板/显示屏：拆卸后独立防震包装</li><li>整机：钢架底座+弹性缓冲垫+螺栓固定</li><li>推荐使用高密度泡沫定制模腔，贴合设备外形</li></ul>

<h3>3. 防潮处理</h3>
<ul><li>木箱内部放置硅胶干燥剂（用量按箱体容积计算）</li><li>箱体内壁覆盖防潮PE膜</li><li>金属加工面涂抹防锈油并用防锈纸包裹</li><li>海运集装箱内额外放置干燥剂</li></ul>

<h3>4. 重型设备固定</h3>
<ul><li>设备重心务必在木箱中央，防止运输倾倒</li><li>使用M12以上螺栓将设备底座与木箱底板连接</li><li>超过5吨的设备需钢架底座+焊接固定</li><li>箱体外部标注吊装点和重心位置</li></ul>

<h2>包装材料选择</h2>
<table><tr><th>材料</th><th>适用场景</th><th>特点</th></tr>
<tr><td>实木（松木/杨木）</td><td>重型设备、出口要求熏蒸</td><td>强度高、成本适中</td></tr>
<tr><td>胶合板</td><td>中型设备、免熏蒸</td><td>免熏蒸、外观好、价格较高</td></tr>
<tr><td>钢架</td><td>超重设备（>10吨）</td><td>强度最高、可重复使用</td></tr>
<tr><td>气泡膜/泡沫</td><td>精密部件缓冲</td><td>轻量、可定制模腔</td></tr></table>''',
        "cta_title": "需要专业设备包装？",
    },
    {
        "slug": "oversize-permit",
        "breadcrumb_name": "超限货物运输",
        "title": "超限货物运输许可 | 超高超重设备出口台湾 | 速豹集运",
        "description": "超限货物出口台湾需要什么许可？超高超重设备运输申报流程、特种柜选择、路线规划。速豹集运超限货运输专家。",
        "h1": "超限货物运输许可指南：超高超重设备出口台湾全流程",
        "intro": "设备超出标准集装箱尺寸时，就进入了「超限货物」范畴。超限运输需要额外的申报许可、特殊运输工具和路线规划。本文详解超限设备出口台湾的完整流程。",
        "body": '''<h2>什么是超限货物？</h2>
<p>在集装箱运输中，超过以下任一标准的货物被视为超限货：</p>
<table><tr><th>参数</th><th>标准集装箱限制</th></tr>
<tr><td>长度</td><td>超过12米（40尺柜）/ 6米（20尺柜）</td></tr>
<tr><td>宽度</td><td>超过2.35米</td></tr>
<tr><td>高度</td><td>超过2.39米（标准柜）/ 2.69米（高柜）</td></tr>
<tr><td>单件重量</td><td>超过25吨</td></tr></table>

<h2>超限货物运输方案</h2>
<table><tr><th>方案</th><th>适用场景</th><th>优缺点</th></tr>
<tr><td><strong>框架箱（Flat Rack）</strong></td><td>超宽超高，10-40吨</td><td>最常用方案，灵活可靠</td></tr>
<tr><td><strong>平板柜（Platform）</strong></td><td>超重超大型，>30吨</td><td>无侧壁限制，需特殊吊装</td></tr>
<tr><td><strong>开顶柜（Open Top）</strong></td><td>超高但宽度正常</td><td>顶部可开启，便于吊装</td></tr>
<tr><td><strong>件杂货船（Break Bulk）</strong></td><td>超大超重无法装箱</td><td>按件运输，费用较高</td></tr>
<tr><td><strong>滚装船（RORO）</strong></td><td>自走式设备</td><td>自行开上船，无需吊装</td></tr></table>

<h2>超限货物申报流程</h2>
<ol><li><strong>提前申报</strong>：在订舱时提供设备的详细尺寸、重量和图纸</li><li><strong>船公司审批</strong>：船公司根据货物参数确认是否可以承运及费用</li><li><strong>码头协调</strong>：协调起运港和目的港的吊装设备（需确认吊机能力）</li><li><strong>特殊许可</strong>：部分超限货物需要海事部门审批</li><li><strong>保险安排</strong>：超限设备建议单独购买运输险</li></ol>

<div class="info-box"><strong>⚠️ 特别提醒</strong>台湾主要港口（基隆、台中、高雄）均有100吨以上岸边吊机，可处理大型超限设备。但在订舱时必须确认目的港吊装能力，避免到港后无法卸货。</div>''',
        "cta_title": "有超限设备要运？",
    },
    {
        "slug": "ecfa-tariff",
        "breadcrumb_name": "ECFA关税优惠",
        "title": "ECFA设备关税优惠 | 哪些设备出口台湾可以零关税 | 速豹集运",
        "description": "ECFA框架下设备出口台湾关税优惠详解：哪些设备享受零关税、原产地证明办理流程、HS编码确认方法。",
        "h1": "ECFA框架下设备出口台湾关税优惠指南",
        "intro": "ECFA（海峡两岸经济合作框架协议）为大陆设备出口台湾提供了关税减免机会。了解哪些设备在ECFA清单内、如何申请零关税，可以显著降低台湾买家的采购成本。",
        "body": '''<h2>ECFA对设备出口的意义</h2>
<p>ECFA早期收获清单中包含了部分机械设备，符合条件的设备凭ECFA原产地证明可享受<strong>零关税或大幅降低的优惠税率</strong>。这对于台湾买家来说是实实在在的成本优势。</p>

<h2>哪些设备在ECFA清单内？</h2>
<table><tr><th>设备类别</th><th>HS编码范围</th><th>ECFA优惠</th></tr>
<tr><td>数控加工中心</td><td>8457.10</td><td>零关税</td></tr>
<tr><td>数控车床</td><td>8458.11</td><td>零关税</td></tr>
<tr><td>注塑成型机</td><td>8477.10</td><td>零关税</td></tr>
<tr><td>纺织机械</td><td>8445-8447</td><td>零关税</td></tr>
<tr><td>包装机械</td><td>8422.30/8422.40</td><td>零关税</td></tr>
<tr><td>模具（注塑/冲压）</td><td>8480.71</td><td>零关税</td></tr></table>

<h2>申请ECFA关税优惠的条件</h2>
<ol><li><strong>原产地规则</strong>：设备必须在大陆完成主要制造工序，大陆增值比例不低于一定标准</li><li><strong>原产地证明</strong>：需向当地贸促会或海关申请ECFA专用原产地证明（Form ECFA）</li><li><strong>直接运输</strong>：设备须从大陆直接运至台湾，不得经第三地中转加工</li><li><strong>主动申报</strong>：台湾进口报关时须主动申报ECFA优惠并提供原产地证</li></ol>

<h2>ECFA原产地证明办理流程</h2>
<ol><li>企业向当地贸促会或海关提交申请</li><li>提供出口发票、生产流程说明、原材料来源证明</li><li>审核通过后签发ECFA原产地证书（通常3-5个工作日）</li><li>证书有效期一般为一年</li></ol>''',
        "cta_title": "需要协助申请ECFA关税优惠？",
    },
    {
        "slug": "shipping-methods",
        "breadcrumb_name": "运输方式对比",
        "title": "设备运输方式对比 | 海运/空运/陆运/铁路怎么选 | 速豹集运",
        "description": "设备出口台湾运输方式全面对比：海运整柜、拼柜、空运、框架箱。成本、时效、适用设备类型详细对照表，帮你选出最佳方案。",
        "h1": "设备出口台湾运输方式全面对比：海运、空运、陆运怎么选？",
        "intro": "设备出口台湾有海运、空运、陆运和铁路运输等多种方式。不同运输方式在成本、时效和适用设备类型上差异巨大。本文帮你快速选出最适合的运输方案。",
        "body": '''<h2>四种运输方式对比</h2>
<table><tr><th>方式</th><th>时效</th><th>成本</th><th>适用设备</th></tr>
<tr><td><strong>海运整柜</strong></td><td>5-7天</td><td>NT$30,000-80,000/柜</td><td>大型设备，重量>3吨</td></tr>
<tr><td><strong>海运拼柜</strong></td><td>7-10天</td><td>NT$800-1,500/立方米</td><td>小型设备，<3立方米</td></tr>
<tr><td><strong>空运</strong></td><td>2-3天</td><td>NT$80-150/kg</td><td>紧急配件、精密仪器</td></tr>
<tr><td><strong>框架箱/特种柜</strong></td><td>5-7天</td><td>NT$40,000-60,000</td><td>超宽超高大型设备</td></tr></table>

<h2>各方式详细分析</h2>
<h3>海运整柜 — 大型设备首选</h3>
<ul><li>20尺柜约28立方米，适合单台中型设备</li><li>40尺柜约58立方米，适合多台设备或大型机台</li><li>费用含两端码头操作费（THC）和文件费</li><li>航线成熟，每周多个船期</li></ul>

<h3>海运拼柜 — 小型设备省成本</h3>
<ul><li>适合体积小于3立方米的设备</li><li>需等待拼柜集货（3-5天），总时效较长</li><li>中途可能经多次装卸，精密设备不推荐</li></ul>

<h3>空运 — 紧急和高精密设备</h3>
<ul><li>适合重量轻、价值高、时效紧急的设备</li><li>重量和尺寸限制严格（单件通常不超过300kg）</li><li>航空安检对含油/含电池设备有特殊要求</li></ul>

<h3>框架箱 — 超限设备专用</h3>
<ul><li>无顶或无侧壁，适合超宽超高设备</li><li>需要码头有相应吊装设备</li><li>费用比标准柜高30-50%</li></ul>''',
        "cta_title": "不确定选哪种运输方式？",
    },
    {
        "slug": "insurance-guide",
        "breadcrumb_name": "设备运输保险",
        "title": "设备运输保险指南 | 货运险怎么买/理赔流程 | 速豹集运",
        "description": "设备出口运输保险怎么买？货运险类型、保额计算、保费费率、理赔流程详解。高价值精密设备运输必备保障。",
        "h1": "设备运输保险指南：货运险怎么买？保多少？理赔怎么办？",
        "intro": "高价值设备在运输途中的风险不容忽视——碰撞、倾覆、海水侵蚀……一份合适的运输保险可以在意外发生时保护你的利益。本文详解设备运输保险的选择和购买。",
        "body": '''<h2>设备运输常见的保险类型</h2>
<table><tr><th>险种</th><th>保障范围</th><th>推荐度</th></tr>
<tr><td><strong>平安险（FPA）</strong></td><td>全损+部分自然灾害</td><td>★★ 基础保障</td></tr>
<tr><td><strong>水渍险（WA）</strong></td><td>平安险+海水损害</td><td>★★★ 海运推荐</td></tr>
<tr><td><strong>一切险（All Risks）</strong></td><td>除免责外的所有意外损失</td><td>★★★★★ 强烈推荐</td></tr>
<tr><td><strong>战争险/罢工险</strong></td><td>战争/罢工造成的损失</td><td>★ 特殊航线需要</td></tr>
</table>

<h2>保费怎么算？</h2>
<div class="info-box"><strong>标准公式</strong>
保费 = 保险金额 × 保险费率<br>
保险金额 = 货值 × (1 + 加成率)<br>
通常加成率10%，即按货值的110%投保</div>

<h2>保费费率参考</h2>
<table><tr><th>设备类型</th><th>费率范围</th></tr>
<tr><td>普通机械设备</td><td>货值的0.2%-0.3%</td></tr>
<tr><td>精密仪器/CNC设备</td><td>货值的0.3%-0.5%</td></tr>
<tr><td>二手/旧设备</td><td>货值的0.5%-0.8%</td></tr>
<tr><td>超限超重设备</td><td>需单独核保报价</td></tr>
</table>

<h2>理赔流程</h2>
<ol><li><strong>发现损失</strong>：收货时如发现外包装破损，当场拍照并保留证据</li><li><strong>通知保险公司</strong>：48小时内书面通知保险公司或代理</li><li><strong>申请检验</strong>：由保险公司指定的第三方检验机构进行残损鉴定</li><li><strong>提交索赔材料</strong>：保单、提单、发票、装箱单、检验报告</li><li><strong>保险公司核赔</strong>：核定损失金额后赔付（通常30天内）</li></ol>''',
        "cta_title": "需要设备运输保险报价？",
    },
    {
        "slug": "weight-calculation",
        "breadcrumb_name": "计费重计算",
        "title": "物流计费重量计算 | 实重vs体积重/海运空运怎么算 | 速豹集运",
        "description": "物流计费重量怎么算？了解实重和体积重的区别，海运和空运的计算方法，大件设备最优计费策略。少花冤枉运费。",
        "h1": "物流计费重量全解：实重vs体积重，海运空运怎么算最省钱",
        "intro": "物流行业的计费规则并不简单——有时按实际重量，有时按体积重量，取两者中较大的那个。了解这些规则可以帮助你优化包装方案，避免多花冤枉钱。",
        "body": '''<h2>为什么要区分实重和体积重？</h2>
<p>运输工具的承载限制包含两个维度：<strong>重量限制</strong>和<strong>空间限制</strong>。棉花很轻但占空间，钢铁很重但体积小。为公平收费，物流商按重量和体积中较大的那个计费。</p>

<h2>计费公式</h2>
<div class="info-box"><strong>空运计费重公式</strong>
体积重(kg) = 长(cm) × 宽(cm) × 高(cm) ÷ 6000<br>
计费重 = max(实重, 体积重)<br><br>
<strong>海运计费重公式</strong>
体积重(吨) = 长(m) × 宽(m) × 高(m) ÷ 1<br>
即：1立方米 = 1计费吨</div>

<h2>常见案例</h2>
<table><tr><th>案例</th><th>实际重量</th><th>尺寸</th><th>计费重</th></tr>
<tr><td>大型注塑机</td><td>5吨</td><td>3×2×2m=12m³</td><td>12计费吨（按体积）</td></tr>
<tr><td>小型CNC</td><td>2吨</td><td>1.5×1×1m=1.5m³</td><td>2计费吨（按实重）</td></tr>
<tr><td>精密仪器</td><td>50kg</td><td>60×50×40=0.12m³</td><td>50kg（按实重）</td></tr>
</table>

<h2>省钱策略：优化包装降低体积</h2>
<ul><li>拆卸可分离的部件单独包装，降低主体尺寸</li><li>使用真空包装/压缩减少软质附件体积</li><li>精密设备使用定制尺寸木箱，避免过大包装</li><li>多件小设备集中装箱，减少空隙浪费</li></ul>''',
        "cta_title": "发尺寸来算最省运费的方案？",
    },
    {
        "slug": "tw-cn-logistics-terms",
        "breadcrumb_name": "两岸物流术语",
        "title": "两岸物流术语表 | CIF/FOB/THC/提单/报关 | 速豹集运",
        "description": "两岸物流常用术语详解：FOB、CIF、THC、提单、报关、清关、整柜、拼柜等专业术语。一次看懂物流单据和专业词汇。",
        "h1": "两岸物流术语表：看懂CIF、FOB、THC等专业词汇",
        "intro": "跨境物流涉及大量的专业术语和英文缩写——FOB、CIF、THC、BL……这些词汇让很多初次出口设备的客户头疼。本文整理了两岸物流最常用的术语，帮你快速入门。",
        "body": '''<h2>贸易条款</h2>
<table><tr><th>术语</th><th>全称</th><th>含义</th></tr>
<tr><td><strong>FOB</strong></td><td>Free On Board</td><td>船上交货：卖方负责将货物装上船，之后的运费和风险由买方承担</td></tr>
<tr><td><strong>CIF</strong></td><td>Cost, Insurance, Freight</td><td>到岸价：卖方承担运费和保险费，直到货物抵达目的港</td></tr>
<tr><td><strong>EXW</strong></td><td>Ex Works</td><td>工厂交货：买方承担所有运输和风险</td></tr>
<tr><td><strong>DAP</strong></td><td>Delivered at Place</td><td>目的地交货：卖方承担到指定地点的全部费用和风险</td></tr>
</table>

<h2>运输术语</h2>
<table><tr><th>术语</th><th>含义</th></tr>
<tr><td><strong>FCL</strong></td><td>整柜（Full Container Load）：一个货柜只装一家客户的货物</td></tr>
<tr><td><strong>LCL</strong></td><td>拼柜（Less than Container Load）：多个客户的货物共用一个货柜</td></tr>
<tr><td><strong>THC</strong></td><td>码头操作费（Terminal Handling Charge）：码头装卸的基本费用</td></tr>
<tr><td><strong>BL (B/L)</strong></td><td>提单（Bill of Lading）：海运最重要的运输单据，代表货物所有权</td></tr>
<tr><td><strong>Telex Release</strong></td><td>电放：不用正本提单提货，由起运港通知目的港放货</td></tr>
</table>

<h2>报关术语</h2>
<table><tr><th>术语</th><th>含义</th></tr>
<tr><td><strong>报关</strong></td><td>向海关申报进出口货物的行为</td></tr>
<tr><td><strong>清关</strong></td><td>完成海关所有手续，货物放行</td></tr>
<tr><td><strong>HS编码</strong></td><td>海关商品编码，决定税率和监管条件</td></tr>
<tr><td><strong>关税</strong></td><td>海关对进口货物征收的税费</td></tr>
</table>

<h2>费用术语</h2>
<table><tr><th>术语</th><th>含义</th></tr>
<tr><td><strong>海运费</strong></td><td>船公司收取的基本运输费</td></tr>
<tr><td><strong>BAF</strong></td><td>燃油附加费（Bunker Adjustment Factor）</td></tr>
<tr><td><strong>文件费</strong></td><td>制作和传递提单等文件的手续费</td></tr>
<tr><td><strong>报关费</strong></td><td>代理报关服务的费用</td></tr>
</table>''',
        "cta_title": "有设备运输问题需要咨询？",
    },
]

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for i, page in enumerate(PAGES, 1):
        html = TEMPLATE.format(**page)
        filepath = os.path.join(OUTPUT_DIR, page["slug"] + ".html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"[{i}/9] ✅ {filepath}")
    print(f"\n🎉 全部 9 个知识页生成完成！")
