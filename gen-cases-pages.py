#!/usr/bin/env python3
"""批量生成 subaotw.cn cases/ 案例页"""

import os

OUTPUT_DIR = "/Users/mac/WorkBuddy/Claw/物流項目/sites/subaotw-cn/cases"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- 案例总览 ---
with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write('''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>设备运输案例 | CNC/注塑机/冲床出口台湾成功案例 | 速豹集运</title>
  <meta name="description" content="速豹集运设备出口台湾真实案例：CNC机床→东莞、注塑机→深圳、冲床→佛山。6年两岸物流经验，服务500+工厂客户。">
  <link rel="canonical" href="https://www.subaotw.cn/cases/">
  <style>
    :root{--p:#1a56db;--a:#f97316;--bg:#f8fafc;--c:#fff;--t:#1e293b;--l:#64748b;--b:#e2e8f0;--r:12px;--shadow-sm:0 1px 2px rgba(0,0,0,0.05);--shadow-md:0 4px 12px rgba(0,0,0,0.08)}
    *{margin:0;padding:0;box-sizing:border-box}
    body{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;color:var(--t);line-height:1.7;background:var(--bg)}
    .container{max-width:1200px;margin:0 auto;padding:0 24px}
    .header{background:rgba(255,255,255,0.95);backdrop-filter:blur(12px);border-bottom:1px solid var(--b);position:sticky;top:0;z-index:100}
    .header .container{display:flex;align-items:center;justify-content:space-between;height:64px}
    .logo{font-size:20px;font-weight:800;color:var(--p);text-decoration:none}.logo span{color:var(--a);font-size:12px;margin-left:8px;padding:2px 8px;background:#fff7ed;border-radius:20px}
    .nav{display:flex;gap:8px}.nav a{color:var(--l);font-weight:500;font-size:14px;text-decoration:none;padding:6px 14px;border-radius:8px}.nav a:hover{color:var(--p);background:#eff6ff}
    .hero{background:linear-gradient(135deg,#0f766e 0%,#115e59 100%);color:#fff;padding:72px 0 52px;text-align:center}
    .hero h1{font-size:36px;font-weight:800;margin-bottom:14px}.hero p{font-size:17px;opacity:0.9}
    .section{padding:60px 0}.section-title{font-size:28px;font-weight:800;text-align:center;margin-bottom:12px}.section-subtitle{text-align:center;color:var(--l);margin-bottom:40px}
    .case-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px}
    .case-card{background:var(--c);border-radius:14px;padding:32px;text-decoration:none;color:inherit;box-shadow:var(--shadow-sm);border:1px solid var(--b);transition:all .25s}
    .case-card:hover{transform:translateY(-4px);box-shadow:var(--shadow-md);border-color:#93c5fd}
    .case-card h3{font-size:18px;color:var(--p);margin-bottom:8px}.case-card .tag{display:inline-block;padding:2px 8px;background:#f0fdf4;color:#0f766e;border-radius:6px;font-size:12px;margin-bottom:12px}
    .case-card p{font-size:14px;color:var(--l)}
    .stats{background:var(--c);padding:48px 0;display:flex;justify-content:center;gap:80px}
    .stat{text-align:center}.stat-num{font-size:32px;font-weight:800;color:var(--a)}.stat-label{font-size:14px;color:var(--l);margin-top:4px}
    .cta{background:linear-gradient(135deg,var(--a),#ea580c);color:#fff;text-align:center;padding:56px 0}
    .cta h2{font-size:28px;margin-bottom:12px}.cta p{margin-bottom:24px;opacity:0.9}
    .btn{display:inline-block;padding:14px 32px;background:#fff;color:var(--a);border-radius:10px;font-weight:700;font-size:16px;text-decoration:none}.btn:hover{transform:translateY(-2px)}
    .footer{background:#0f172a;color:#94a3b8;padding:40px 0 20px;text-align:center;font-size:13px}
    @media(max-width:768px){.case-grid{grid-template-columns:1fr}.stats{flex-wrap:wrap;gap:32px}}
  </style>
</head>
<body>
  <header class="header"><div class="container"><a href="/" class="logo">速豹集运<span>两岸物流</span></a><nav class="nav"><a href="/equipment/">设备运输</a><a href="/tw-to-cn/">台湾寄大陆</a><a href="/guide/">物流指南</a><a href="/contact">联系我们</a></nav></div></header>
  <section class="hero"><h1>设备运输成功案例</h1><p>6年两岸物流经验，服务500+工厂客户 — 真实案例，真实数据</p></section>
  <div class="stats"><div class="stat"><div class="stat-num">500+</div><div class="stat-label">服务工厂客户</div></div><div class="stat"><div class="stat-num">6年</div><div class="stat-label">两岸物流经验</div></div><div class="stat"><div class="stat-num">99%</div><div class="stat-label">准时交付率</div></div></div>
  <section class="section"><div class="container"><h2 class="section-title">精选案例</h2><p class="section-subtitle">以下案例均已脱敏处理，保护客户隐私</p>
    <div class="case-grid">
      <a href="/cases/case-cnc-dongguan" class="case-card"><span class="tag">CNC设备</span><h3>CNC加工中心 → 东莞工厂</h3><p>8吨数控加工中心，东莞→台湾基隆港，20尺整柜+专业木箱包装</p></a>
      <a href="/cases/case-injection-shenzhen" class="case-card"><span class="tag">注塑机</span><h3>注塑机 → 深圳工厂</h3><p>5吨注塑成型机，深圳→台湾台中港，40尺柜+防震钢架</p></a>
      <a href="/cases/case-press-foshan" class="case-card"><span class="tag">冲床</span><h3>数控冲床 → 佛山工厂</h3><p>12吨大型冲床，佛山→台湾高雄港，框架箱特种运输</p></a>
      <a href="/cases/case-textile-xiamen" class="case-card"><span class="tag">纺织设备</span><h3>纺纱设备线 → 厦门工厂</h3><p>整线纺纱设备，厦门→台湾基隆港，多柜集中运输</p></a>
      <a href="/cases/case-mold-kunshan" class="case-card"><span class="tag">模具</span><h3>精密模具组 → 昆山工厂</h3><p>8套注塑模具，昆山→台湾台中港，精密防锈包装+保险</p></a>
    </div></div></section>
  <section class="cta"><h2>有设备需要运到台湾？</h2><p>发送设备参数，30分钟内获取方案和报价</p><a href="/contact" class="btn">立即咨询</a></section>
  <footer class="footer"><p>© 2026 速豹集运 Subao Logistics | 两岸物流专线</p><p style="margin-top:8px"><a href="https://beian.miit.gov.cn/" target="_blank" rel="nofollow" style="color:#64748b">湘ICP备2026016030号-2</a></p></footer>
</body>
</html>''')

# --- 5个案例详情 ---
CASES = [
    ("case-cnc-dongguan", "CNC加工中心→东莞", "CNC加工中心出口台湾 | 东莞→基隆 8吨设备运输案例 | 速豹集运",
     "8吨CNC数控加工中心从东莞出口至台湾基隆港的完整运输案例。20尺整柜+专业木箱+防震包装，5天送达。",
     "CNC加工中心出口台湾运输案例：东莞→基隆港",
     '''<p>东莞某精密机械制造厂接到台湾客户订单，需要将一台重8吨的CNC立式加工中心运至台湾基隆附近的工厂。</p>
<h2>客户需求</h2><ul><li>设备：CNC立式加工中心（某国产品牌）</li><li>尺寸：3.2m × 2.1m × 2.5m</li><li>重量：8吨</li><li>目的地：台湾基隆市</li><li>要求：门到门服务，含包装和报关</li></ul>
<h2>我们的方案</h2><ol><li><strong>运输方式：</strong>20尺整柜海运，东莞港→基隆港</li><li><strong>包装方案：</strong>定制实木熏蒸木箱（ISPM 15），主轴和导轨加装防震支撑块</li><li><strong>报关：</strong>协助准备全套文件（商业发票/装箱单/设备参数表/原产地证），3个工作日完成出口报关</li><li><strong>保险：</strong>按货值110%投保一切险</li></ol>
<h2>运输数据</h2><table><tr><th>环节</th><th>时间</th></tr><tr><td>设备包装</td><td>2天</td></tr><tr><td>报关+装柜</td><td>1天</td></tr><tr><td>海运</td><td>3天</td></tr><tr><td>台湾清关+派送</td><td>2天</td></tr><tr><td><strong>全程总计</strong></td><td><strong>8个工作日</strong></td></tr></table>
<h2>客户反馈</h2><p>"第一次做设备出口到台湾，本来很担心手续复杂。速豹全程代办，我们只需提供设备参数和合同，其他都不用操心。设备到达后完好无损，台湾客户非常满意。"</p>'''),
    ("case-injection-shenzhen", "注塑机→深圳", "注塑机出口台湾 | 深圳→台中 5吨注塑机运输案例 | 速豹集运",
     "5吨卧式注塑机从深圳出口至台湾台中港的真实运输案例。40尺整柜+防震钢架底座+防锈处理，7天送达。",
     "注塑机出口台湾运输案例：深圳→台中港",
     '''<p>深圳某注塑机制造商需要将一台卧式注塑机出口至台湾台中工业区。</p>
<h2>客户需求</h2><ul><li>设备：卧式注塑机（锁模力800吨）</li><li>尺寸：4.5m × 1.8m × 2.2m</li><li>重量：5吨</li><li>目的地：台湾台中市</li><li>要求：含台湾端派送到工厂</li></ul>
<h2>我们的方案</h2><ol><li><strong>运输方式：</strong>40尺整柜海运，深圳蛇口港→台中港</li><li><strong>包装方案：</strong>钢架底座+防震木箱，液压系统排油密封，料筒模具头拆卸单独包装</li><li><strong>报关：</strong>注塑机HS编码8477.10，ECFA零关税，协助申请原产地证明</li></ol>
<h2>运输数据</h2><table><tr><th>环节</th><th>时间</th></tr><tr><td>设备拆解+包装</td><td>2天</td></tr><tr><td>报关+装柜</td><td>1天</td></tr><tr><td>海运</td><td>3天</td></tr><tr><td>台湾清关+派送</td><td>2天</td></tr><tr><td><strong>全程总计</strong></td><td><strong>8个工作日</strong></td></tr></table>
<h2>成本亮点</h2><p>凭借ECFA原产地证明，该注塑机享受零关税优惠，为台湾客户节省了约NT$8万元关税成本。</p>'''),
    ("case-press-foshan", "冲床→佛山", "数控冲床出口台湾 | 佛山→高雄 12吨冲床运输案例 | 速豹集运",
     "12吨大型数控冲床从佛山出口至台湾高雄港的运输案例。超限货物框架箱运输+专业吊装，10天送达。",
     "冲床出口台湾运输案例：佛山→高雄港",
     '''<p>佛山某冲压设备厂需要将一台12吨的大型数控冲床出口至台湾高雄。</p>
<h2>客户需求</h2><ul><li>设备：数控液压冲床</li><li>尺寸：5.2m × 2.8m × 3.1m（超宽超高）</li><li>重量：12吨</li><li>目的地：台湾高雄市</li><li>要求：超限货物特种运输</li></ul>
<h2>我们的方案</h2><ol><li><strong>运输方式：</strong>框架箱海运，深圳港→高雄港</li><li><strong>包装方案：</strong>钢架焊接底座+螺栓固定，重心标注清晰，液压油缸收缩锁定</li><li><strong>特殊申报：</strong>提前14天向船公司申报超限货物，协调码头吊装方案</li><li><strong>台湾端：</strong>协调高雄港100吨岸边吊机卸货，平板车转运到工厂</li></ol>
<h2>运输数据</h2><table><tr><th>环节</th><th>时间</th></tr><tr><td>超限申报+订舱</td><td>3天</td></tr><tr><td>包装+吊装</td><td>2天</td></tr><tr><td>海运</td><td>4天</td></tr><tr><td>清关+派送</td><td>2天</td></tr><tr><td><strong>全程总计</strong></td><td><strong>11个工作日</strong></td></tr></table>
<h2>挑战与解决</h2><p>该冲床宽度2.8米超出标准框架箱宽度2.4米。我们与船公司协商使用了加宽型框架箱（3.5m宽），确保设备安全装载。超额运输费用比标准方案高约35%，但在客户预算范围内。</p>'''),
    ("case-textile-xiamen", "纺织设备→厦门", "纺织设备出口台湾 | 厦门→基隆 整线纺纱设备案例 | 速豹集运",
     "厦门某纺织机械厂整线纺纱设备出口台湾的运输案例。多台设备集中运输，3个40尺柜同步发运。",
     "纺纱设备出口台湾案例：厦门→基隆港",
     '''<p>厦门某纺织机械制造商需要将一整套纺纱设备（含梳棉机、并条机、粗纱机、细纱机共12台）出口至台湾纺织厂。</p>
<h2>客户需求</h2><ul><li>设备：纺纱整线设备共12台</li><li>单台尺寸：1-3m³不等</li><li>总重量：约18吨</li><li>目的地：台湾彰化</li></ul>
<h2>我们的方案</h2><ol><li><strong>运输方式：</strong>3个40尺整柜集中发运，厦门港→基隆港</li><li><strong>包装方案：</strong>每台设备独立木箱包装+编号，精密部件（罗拉、锭子）防锈油+防潮包装</li><li><strong>交付：</strong>3柜同步发运，到港后按编号顺序拆箱，协助台湾端安装定位</li></ol>
<h2>运输数据</h2><table><tr><th>环节</th><th>时间</th></tr><tr><td>包装+装箱</td><td>3天</td></tr><tr><td>报关+发运</td><td>1天</td></tr><tr><td>海运</td><td>3天</td></tr><tr><td>清关+派送</td><td>3天</td></tr><tr><td><strong>全程总计</strong></td><td><strong>10个工作日</strong></td></tr></table>'''),
    ("case-mold-kunshan", "模具→昆山", "注塑模具出口台湾 | 昆山→台中 精密模具组运输案例 | 速豹集运",
     "昆山某模具厂8套精密注塑模具出口台湾的完整案例。专业防锈防震包装+全程保险，零损伤交付。",
     "精密模具出口台湾案例：昆山→台中港",
     '''<p>昆山某精密模具制造商需要将8套注塑模具出口至台湾台中的注塑厂。</p>
<h2>客户需求</h2><ul><li>货品：注塑模具8套（单穴至4穴不等）</li><li>单套重量：200kg-1.5吨</li><li>总重：约7吨</li><li>关键要求：零损伤（型腔面精度要求±0.01mm）</li></ul>
<h2>我们的方案</h2><ol><li><strong>运输方式：</strong>40尺整柜拼装，上海港→台中港</li><li><strong>包装方案：</strong>每套模具型腔面涂抹防锈油→覆PE保护膜→独立底座螺栓固定→定制木箱，严禁叠压</li><li><strong>保险：</strong>按货值110%投保精密仪器运输险</li></ol>
<h2>运输数据</h2><table><tr><th>环节</th><th>时间</th></tr><tr><td>模具防锈+包装</td><td>2天</td></tr><tr><td>报关+发运</td><td>1天</td></tr><tr><td>海运</td><td>3天</td></tr><tr><td>清关+派送</td><td>2天</td></tr><tr><td><strong>全程总计</strong></td><td><strong>8个工作日</strong></td></tr></table>
<h2>客户反馈</h2><p>"模具精度是我们最关心的问题。速豹的防锈防震包装方案非常专业，8套模具全部完好到达，型腔面无任何损伤。后续的5套模具也继续用他们。"</p>'''),
]

TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="https://www.subaotw.cn/cases/{slug}">
  <style>
    :root{{--p:#1a56db;--a:#f97316;--bg:#f8fafc;--c:#fff;--t:#1e293b;--l:#64748b;--b:#e2e8f0;--r:12px}}
    *{{margin:0;padding:0;box-sizing:border-box}}
    body{{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;color:var(--t);line-height:1.8;background:var(--bg)}}
    .container{{max-width:900px;margin:0 auto;padding:0 20px}}
    .header{{background:rgba(255,255,255,0.95);backdrop-filter:blur(12px);border-bottom:1px solid var(--b);position:sticky;top:0;z-index:100}}
    .header .container{{display:flex;align-items:center;justify-content:space-between;height:64px;max-width:1200px}}
    .logo{{font-size:20px;font-weight:800;color:var(--p);text-decoration:none}}.logo span{{color:var(--a);font-size:12px;margin-left:6px}}
    .breadcrumb{{padding:20px 0;font-size:14px;color:var(--l)}}.breadcrumb a{{color:var(--p);text-decoration:none}}
    article{{padding-bottom:60px}}
    article h1{{font-size:32px;font-weight:800;margin-bottom:20px;line-height:1.3}}
    article h2{{font-size:22px;font-weight:700;margin:36px 0 14px;color:var(--p);padding-bottom:8px;border-bottom:2px solid #dbeafe}}
    article p{{font-size:16px;margin-bottom:14px}}
    article ul,article ol{{margin:10px 0 14px 24px;color:var(--l)}}article li{{margin-bottom:6px}}
    table{{width:100%;border-collapse:collapse;margin:20px 0;background:var(--c);border-radius:var(--r);overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,0.06)}}
    th{{background:var(--p);color:#fff;padding:12px 16px;text-align:left}}td{{padding:12px 16px;border-bottom:1px solid var(--b)}}
    .cta{{background:linear-gradient(135deg,var(--a),#ea580c);color:#fff;text-align:center;padding:48px 20px;border-radius:var(--r);margin:40px 0}}
    .cta h2{{color:#fff;margin-top:0;border:none;padding:0}}.btn{{display:inline-block;padding:14px 32px;background:#fff;color:var(--a);border-radius:10px;font-weight:700;font-size:16px;text-decoration:none}}.btn:hover{{transform:translateY(-2px)}}
    .footer{{background:#0f172a;color:#94a3b8;padding:40px 0 20px;text-align:center;font-size:13px}}@media(max-width:768px){{article h1{{font-size:26px}}}}
  </style>
</head>
<body>
  <header class="header"><div class="container"><a href="/" class="logo">速豹集运<span>两岸物流</span></a></div></header>
  <div class="container"><div class="breadcrumb"><a href="/">首页</a> › <a href="/cases/">客户案例</a> › {case_name}</div></div>
  <article><div class="container"><h1>{h1}</h1>{body}
    <div class="cta"><h2>有类似设备需要运输？</h2><p style="opacity:0.9">发送设备参数，30分钟内获取方案</p><a href="/contact" class="btn">立即咨询</a></div>
  </div></article>
  <footer class="footer"><p>© 2026 速豹集运 Subao Logistics | 两岸物流专线</p><p style="margin-top:8px"><a href="https://beian.miit.gov.cn/" target="_blank" rel="nofollow" style="color:#64748b">湘ICP备2026016030号-2</a></p></footer>
</body>
</html>'''

for slug, case_name, title, desc, h1, body in CASES:
    html = TEMPLATE.format(slug=slug, case_name=case_name, title=title, desc=desc, h1=h1, body=body)
    with open(os.path.join(OUTPUT_DIR, slug + ".html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ {slug}")

print("\n🎉 全部 6 个案例页生成完成！")
