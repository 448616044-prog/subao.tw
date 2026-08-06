#!/usr/bin/env python3
"""批量生成 subao.tw 品牌子页面（母婴奶粉 + 化妆品）"""
import os, json

SITE_DIR = "/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn/blog"

# ========== 品牌数据 ==========
BRANDS = {
    # --- 母婴奶粉 ---
    "quaker-formula-shipping": {
        "title": "桂格奶粉可以寄大陸嗎？金選/三益菌/成長奶粉寄送攻略 NT$290/kg起 | 速豹集運",
        "h1": "桂格奶粉可以寄大陸嗎？2026 完整寄送攻略",
        "desc": "桂格奶粉可以寄大陸嗎？可以！金選奶粉/三益菌/媽媽奶粉透過敏感貨專線NT$290/kg起包稅，最快5-7天（空運）。6罐約4.8kg運費約NT$1,392。LINE傳照片30秒確認！",
        "keywords": "桂格奶粉寄大陸,桂格奶粉可以寄大陸嗎,桂格金選寄大陸,台灣奶粉寄大陸",
        "pillar_name": "母嬰奶粉寄大陸",
        "pillar_url": "/blog/baby-formula-shipping-guide",
        "content": """<h2>🥛 桂格奶粉全系列寄送指南</h2>
<p>桂格（Quaker）是台灣市佔最高的嬰幼兒奶粉品牌，熱門品項：<strong>金選奶粉（1-3歲）、三益菌系列、成長奶粉（3歲以上）、媽媽奶粉（孕期營養）</strong>。全系列鋁箔密封包裝，走敏感貨專線均可寄送。</p>
<p>每罐約 800g，6 罐約 4.8kg，運費約 NT$1,392（NT$290×4.8kg）。單罐寄送最低 NT$290 起（未滿 1kg 以 1kg 計）。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>奶粉罐怕碰撞變形，每罐用氣泡紙獨立包裹</li>
<li>罐與罐之間用紙板隔開，防止運輸途中互相撞擊</li>
<li>外箱底部加一層防震泡棉，降低從高處摔落的風險</li>
<li><strong>關鍵：罐蓋用膠帶加固</strong>，防止氣壓變化導致爆蓋灑粉</li>
</ul>
<h3>🛒 購買建議</h3>
<p>桂格奶粉在全聯/家樂福/大潤發/藥局都能買到。大量採購建議去 Costco 買大罐裝，單價最低。買完直接寄到速豹倉庫（苗栗頭份），不必自己扛回家再寄一次。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>奶粉屬於食品類，走敏感貨專線可正常通關。<strong>建議控制每批在 6-12 罐以內（合理自用範圍）</strong>，超過 12 罐建議分批寄送、降低被海關抽查的機率。</p>"""
    },
    "abbott-formula-shipping": {
        "title": "亞培奶粉可以寄大陸嗎？心美力/小安素/安素寄送攻略 NT$290/kg起 | 速豹集運",
        "h1": "亞培奶粉可以寄大陸嗎？2026 完整寄送攻略",
        "desc": "亞培奶粉可以寄大陸嗎？可以！心美力/小安素/安素透過敏感貨專線NT$290/kg起包稅，最快5-7天（空運）。6罐約4.8kg運費約NT$1,392。LINE傳照片秒確認！",
        "keywords": "亞培寄大陸,亞培奶粉可以寄大陸嗎,亞培心美力寄大陸,小安素寄大陸,亞培安素寄大陸",
        "pillar_name": "母嬰奶粉寄大陸",
        "pillar_url": "/blog/baby-formula-shipping-guide",
        "content": """<h2>🍼 亞培全系列寄送指南</h2>
<p>亞培（Abbott）是全球前三大嬰幼兒營養品牌，台灣熱門品項：<strong>心美力（0-1歲）、小安素（1-10歲營養補充）、安素（成人營養）、盼納補（孕婦綜合維他命）</strong>。全系列工廠密封包裝，走敏感貨專線均可寄送。</p>
<p>每罐約 850-900g，6 罐約 5kg，運費約 NT$1,450。單罐寄送 NT$290 起。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>奶粉罐蓋子先用膠帶十字封口，防止運輸途中爆蓋</li>
<li>每罐獨立氣泡紙包裹，罐底罐頂各加一層防震</li>
<li>小安素是塑膠瓶裝，比鐵罐更耐用但仍須氣泡紙保護</li>
<li>外箱貼「易碎品」標籤有助降低粗魯搬運風險</li>
</ul>
<h3>🛒 購買建議</h3>
<p>亞培奶粉在各大藥局（大樹/杏一/丁丁）和全聯都能買到。小安素/安素在大潤發和 Costco 有大包裝，每 ml 成本最低。心美力建議在藥局買，經常有買 6 送 1 活動。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>心美力為 0-1 歲配方，大陸海關對嬰兒配方奶粉審查較嚴，建議搭配發票或購買證明，證明為個人自用、非商業販售。</p>"""
    },
    "snow-brand-formula-shipping": {
        "title": "雪印奶粉可以寄大陸嗎？強子/成長奶粉寄送攻略 NT$290/kg起 | 速豹集運",
        "h1": "雪印奶粉可以寄大陸嗎？2026 完整寄送攻略",
        "desc": "雪印奶粉可以寄大陸嗎？可以！強子奶粉/成長奶粉透過敏感貨專線NT$290/kg起包稅，最快5-7天（空運）。6罐約4.5kg運費約NT$1,305。LINE傳照片30秒確認！",
        "keywords": "雪印寄大陸,雪印奶粉可以寄大陸嗎,雪印強子寄大陸,台灣雪印寄大陸",
        "pillar_name": "母嬰奶粉寄大陸",
        "pillar_url": "/blog/baby-formula-shipping-guide",
        "content": """<h2>🇯🇵 雪印全系列寄送指南</h2>
<p>雪印（Snow Brand）是日本百年乳業品牌，台灣市場熱門品項：<strong>強子奶粉（1-3歲）、成長奶粉（3歲以上）、T3成長奶粉、MBP高鈣系列</strong>。全系列鐵罐密封包裝，走敏感貨專線均可寄送。</p>
<p>每罐約 750-900g，6 罐約 4.5kg，運費約 NT$1,305（NT$290×4.5kg）。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>雪印鐵罐較薄，比桂格更容易凹陷，氣泡紙至少包兩層</li>
<li>罐蓋用膠帶十字加固（和桂格一樣重要）</li>
<li>多罐寄送時橫放比直放更穩（降低重心）</li>
</ul>
<h3>🛒 購買建議</h3>
<p>雪印在藥局通路最齊全（大樹/杏一/啄木鳥），全聯也有但品項較少。強子奶粉建議直接去藥局買整箱，通常有會員折扣。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>雪印是日本品牌台灣製造，標籤為繁體中文，大陸海關無額外限制。建議控制在 6-12 罐以內合理自用範圍。</p>"""
    },
    "s26-formula-shipping": {
        "title": "S-26奶粉可以寄大陸嗎？金幼兒樂/金學兒樂寄送攻略 NT$290/kg起 | 速豹集運",
        "h1": "S-26奶粉可以寄大陸嗎？2026 完整寄送攻略",
        "desc": "S-26奶粉可以寄大陸嗎？可以！金幼兒樂/金學兒樂/惠氏媽咪透過敏感貨專線NT$290/kg起包稅，最快5-7天（空運）。6罐約5kg運費約NT$1,450。LINE傳照片秒確認！",
        "keywords": "S-26寄大陸,S-26奶粉可以寄大陸嗎,惠氏寄大陸,金幼兒樂寄大陸,金學兒樂寄大陸",
        "pillar_name": "母嬰奶粉寄大陸",
        "pillar_url": "/blog/baby-formula-shipping-guide",
        "content": """<h2>🧠 S-26 / 惠氏全系列寄送指南</h2>
<p>S-26 是惠氏（Wyeth）旗下嬰幼兒奶粉品牌，台灣熱門品項：<strong>金幼兒樂（1-3歲）、金學兒樂（3-7歲）、惠氏媽咪（孕期營養）、S-26 敏兒樂（水解配方）</strong>。全系列鋁箔密封+塑膠蓋包裝，走敏感貨專線均可寄送。</p>
<p>每罐約 800-900g，6 罐約 5kg，運費約 NT$1,450。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>S-26 是塑膠蓋+鋁箔封膜設計，塑膠蓋容易在運輸中彈開，務必用膠帶加固</li>
<li>附贈的湯匙放在罐內（不要黏在蓋子上），避免壓壞封膜</li>
<li>水解配方（敏兒樂）罐身較小（400g），多罐混寄時注意大小罐不要擠壓</li>
</ul>
<h3>🛒 購買建議</h3>
<p>S-26 在各大藥局和全聯都有，Costco 偶有大包裝優惠。金幼兒樂建議藥局買，通常有開罐價或滿額折扣。惠氏官網也有定期促銷。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>S-26 是大陸媽媽圈高知名度的台灣奶粉品牌，建議附購買證明證明自用。控制在 6-12 罐合理範圍內。</p>"""
    },
    "kabrita-formula-shipping": {
        "title": "金可貝可奶粉可以寄大陸嗎？羊奶粉寄送攻略 NT$290/kg起 | 速豹集運",
        "h1": "金可貝可奶粉可以寄大陸嗎？2026 完整寄送攻略",
        "desc": "金可貝可奶粉可以寄大陸嗎？可以！羊奶粉/成長奶粉透過敏感貨專線NT$290/kg起包稅，最快5-7天（空運）。6罐約5kg運費約NT$1,450。LINE傳照片30秒確認！",
        "keywords": "金可貝可寄大陸,金可貝可奶粉可以寄大陸嗎,羊奶粉寄大陸,台灣羊奶粉寄大陸,Kabrita寄大陸",
        "pillar_name": "母嬰奶粉寄大陸",
        "pillar_url": "/blog/baby-formula-shipping-guide",
        "content": """<h2>🐐 金可貝可全系列寄送指南</h2>
<p>金可貝可（Kabrita）是荷蘭品牌、台灣分裝的羊奶粉專家，熱門品項：<strong>金可貝可羊奶粉（1-3歲）、成長羊奶粉（3歲以上）</strong>。羊奶粉分子比牛奶粉更小、更接近母乳結構，是乳糖不耐受寶寶的首選。</p>
<p>每罐約 800-900g，6 罐約 5kg，運費約 NT$1,450。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>鐵罐包裝和一般奶粉相同，罐蓋膠帶加固</li>
<li>羊奶粉單價較高（一罐 NT$800-1,200），建議用泡棉+氣泡紙雙層保護</li>
<li>外箱加貼「易碎品」標籤</li>
</ul>
<h3>🛒 購買建議</h3>
<p>金可貝可在藥局和母嬰用品店（如奶娃的店/安琪兒）比較好買。全聯和家樂福不一定有。建議去藥局一次買整箱，通常有會員優惠。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>羊奶粉在大陸也是敏感貨，但需求很大（很多寶寶對牛奶蛋白過敏）。走專線通關正常，控制在 6-12 罐合理自用範圍即可。</p>"""
    },
    "meiji-formula-shipping": {
        "title": "明治奶粉可以寄大陸嗎？金選/樂樂Q貝寄送攻略 NT$290/kg起 | 速豹集運",
        "h1": "明治奶粉可以寄大陸嗎？2026 完整寄送攻略",
        "desc": "明治奶粉可以寄大陸嗎？可以！金選奶粉/樂樂Q貝方塊奶粉透過敏感貨專線NT$290/kg起包稅，最快5-7天（空運）。樂樂Q貝超輕便攜帶30條約1.2kg運費NT$348。LINE傳照片秒確認！",
        "keywords": "明治寄大陸,明治奶粉可以寄大陸嗎,明治金選寄大陸,樂樂Q貝寄大陸,台灣明治寄大陸",
        "pillar_name": "母嬰奶粉寄大陸",
        "pillar_url": "/blog/baby-formula-shipping-guide",
        "content": """<h2>🇯🇵 明治全系列寄送指南</h2>
<p>明治（Meiji）是日本食品巨頭，台灣市場熱門品項：<strong>金選奶粉（1-3歲）、樂樂Q貝方塊奶粉（外出神器，獨立條狀包裝）</strong>。樂樂Q貝每條 24g、一盒 30 條，不需量匙、直接撕開倒進奶瓶，是媽媽圈最愛的外出奶粉。</p>
<p>樂樂Q貝一盒 30 條約 720g，兩盒 1.44kg 運費 NT$418。金選奶粉每罐 800g，6 罐約 NT$1,392。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>樂樂Q貝是紙盒裝+獨立鋁箔條，本身已有雙層保護，外箱塞填充物即可</li>
<li>金選奶粉和一般奶粉罐相同包裝方式：膠帶加固罐蓋 + 氣泡紙包裹</li>
<li>樂樂Q貝特別適合寄送——重量輕、體積小、不怕爆罐</li>
</ul>
<h3>🛒 購買建議</h3>
<p>明治在藥局和全聯都很常見。樂樂Q貝建議在 Costco 或母嬰用品店買，單價最低。金選奶粉藥局常有促銷。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>樂樂Q貝是大陸媽媽圈代購熱門商品（便攜+日本品牌溢價），寄送無特殊限制，走敏感貨專線正常通關。</p>"""
    },

    # --- 化妆品品牌 ---
    "my-beauty-diary-shipping": {
        "title": "我的美麗日記可以寄大陸嗎？面膜/精華液寄送攻略 NT$290/kg起 | 速豹集運",
        "h1": "我的美麗日記可以寄大陸嗎？2026 完整寄送攻略",
        "desc": "我的美麗日記可以寄大陸嗎？可以！黑珍珠/納豆/玻尿酸面膜透過敏感貨專線NT$290/kg起包稅，最快5-7天（空運）。20片約0.6kg運費NT$290。LINE傳照片30秒確認！",
        "keywords": "我的美麗日記寄大陸,我的美麗日記面膜寄大陸,美麗日記寄大陸,台灣面膜寄大陸",
        "pillar_name": "化妝品寄大陸",
        "pillar_url": "/blog/cosmetics-shipping",
        "content": """<h2>💆‍♀️ 我的美麗日記全系列寄送指南</h2>
<p>我的美麗日記是統一藥品旗下、台灣最暢銷的平價面膜品牌。熱門系列：<strong>黑珍珠煥白面膜、納豆發酵保濕面膜、玻尿酸極效保濕面膜、蜂王乳面膜、膠原蛋白面膜</strong>。全系列鋁箔獨立包裝，走敏感貨專線均可寄送。</p>
<p>每片約 30g，20 片約 0.6kg，運費 NT$290。50 片約 1.5kg，運費約 NT$435。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>面膜輕薄不怕壓，用紙箱或快遞袋均可</li>
<li>若同時寄精華液（玻璃瓶裝），須用氣泡紙獨立包裹後再放入紙箱</li>
<li>夏天寄送無需冷藏，常溫保存即可</li>
</ul>
<h3>🛒 購買建議</h3>
<p>美麗日記在屈臣氏/康是美/寶雅最齊全，常有買一送一或第二件五折優惠。一次買大量建議去康是美官網訂購，直接寄到速豹倉庫最省事。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>面膜屬化妝品，走敏感貨專線正常通關。大陸海關對化妝品稅率較高（行郵稅 20%），但走包稅專線免關稅煩惱。建議每批控制在 50 片以內合理自用範圍。</p>"""
    },
    "dr-wu-shipping": {
        "title": "DR.WU可以寄大陸嗎？杏仁酸/玻尿酸精華寄送攻略 NT$350/kg起 | 速豹集運",
        "h1": "DR.WU可以寄大陸嗎？2026 完整寄送攻略",
        "desc": "DR.WU可以寄大陸嗎？可以！杏仁酸精華/玻尿酸精華/角鯊潤澤透過含液體特貨專線NT$350/kg起包稅，最快5-7天（空運）。3瓶約0.8kg運費NT$350。LINE傳照片30秒確認！",
        "keywords": "DR.WU寄大陸,DR.WU可以寄大陸嗎,杏仁酸寄大陸,DR.WU玻尿酸寄大陸,台灣醫美保養品寄大陸",
        "pillar_name": "化妝品寄大陸",
        "pillar_url": "/blog/cosmetics-shipping",
        "content": """<h2>🧪 DR.WU全系列寄送指南</h2>
<p>DR.WU 是台灣醫美保養品第一品牌，由台大皮膚科醫師吳英俊創立。大陸小紅書上討論度極高，熱門品項：<strong>杏仁酸溫和煥膚精華（6%/8%/18%）、玻尿酸保濕精華液、角鯊潤澤修復精華、超逆齡系列</strong>。</p>
<p>精華液每瓶約 15-30ml，體積小重量輕。3 瓶約 0.8kg，運費 NT$350（含液體特貨）。5-6 瓶約 1.2kg，運費約 NT$420。</p>
<h3>📦 包裝重點</h3>
<ul>
<li><strong>精華液是玻璃滴管瓶，包裝最關鍵！</strong>每瓶用氣泡紙單獨包裹至少兩層</li>
<li>瓶蓋用膠帶固定防止鬆開滲漏</li>
<li>多瓶寄送時中間用紙板隔開，瓶身不互相碰觸</li>
<li>外箱底部鋪防震泡棉，降低摔落衝擊</li>
<li>杏仁酸屬酸性液體，走含液體特貨 NT$350/kg 安全通關</li>
</ul>
<h3>🛒 購買建議</h3>
<p>DR.WU 在屈臣氏/康是美/寶雅都能買到，但官網和 momo 購物常有更低的組合價（如買精華送面膜）。建議先去官網看當期優惠再下單，直接寄到速豹倉庫。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>杏仁酸等含酸類產品屬敏感貨中的含液體特貨，運費 NT$350/kg。走專線包稅雙清，大陸海關無額外管制。控制在 6 瓶以內合理自用範圍即可。</p>"""
    },
    "morita-shipping": {
        "title": "森田藥粧可以寄大陸嗎？面膜/精華液寄送攻略 NT$290/kg起 | 速豹集運",
        "h1": "森田藥粧可以寄大陸嗎？2026 完整寄送攻略",
        "desc": "森田藥粧可以寄大陸嗎？可以！玻尿酸面膜/抗黑淨白面膜透過敏感貨專線NT$290/kg起包稅，最快5-7天（空運）。20片約0.5kg運費NT$290。LINE傳照片30秒確認！",
        "keywords": "森田藥粧寄大陸,森田藥粧面膜寄大陸,森田藥粧可以寄大陸嗎,台灣面膜寄大陸",
        "pillar_name": "化妝品寄大陸",
        "pillar_url": "/blog/cosmetics-shipping",
        "content": """<h2>🧖‍♀️ 森田藥粧全系列寄送指南</h2>
<p>森田藥粧是台灣開架面膜銷量冠軍品牌，以「藥粧店價格、專櫃品質」聞名。熱門系列：<strong>玻尿酸複合精華面膜、抗黑淨白面膜、蝸牛修護面膜、六重玻尿酸面膜、全日極效保濕系列</strong>。全系列鋁箔獨立包裝，常溫保存，走敏感貨專線均可寄送。</p>
<p>每片約 28g，20 片約 0.56kg，運費 NT$290。50 片約 1.4kg，運費約 NT$406。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>片狀面膜和美麗日記相同，輕薄不怕壓</li>
<li>若夾帶精華液（瓶裝），須用氣泡紙獨立包裹</li>
<li>夏天常溫寄送即可，無需冰袋</li>
</ul>
<h3>🛒 購買建議</h3>
<p>森田藥粧在屈臣氏/康是美/寶雅最常見，經常買一送一。官方蝦皮商城也常有超殺優惠。一次買大量建議直接去官網或蝦皮官方店下單寄倉庫。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>森田藥粧在大陸天貓/京東有官方旗艦店，但台灣版的配方和包裝不同，大陸消費者更偏愛台灣境內版。走敏感貨專線包稅通關，無需擔心關稅。</p>"""
    },
    "forbelovedone-shipping": {
        "title": "寵愛之名可以寄大陸嗎？生物纖維面膜寄送攻略 NT$290/kg起 | 速豹集運",
        "h1": "寵愛之名可以寄大陸嗎？2026 完整寄送攻略",
        "desc": "寵愛之名可以寄大陸嗎？可以！生物纖維面膜/亮白精華透過敏感貨專線NT$290/kg起包稅，最快5-7天（空運）。10片約0.5kg運費NT$290。LINE傳照片30秒確認！",
        "keywords": "寵愛之名寄大陸,寵愛之名面膜寄大陸,生物纖維面膜寄大陸,For Beloved One寄大陸,台灣專櫃面膜寄大陸",
        "pillar_name": "化妝品寄大陸",
        "pillar_url": "/blog/cosmetics-shipping",
        "content": """<h2>✨ 寵愛之名全系列寄送指南</h2>
<p>寵愛之名（For Beloved One）是台灣輕奢醫美品牌，以「生物纖維面膜」聞名——不同於一般不織布面膜，生物纖維材質像果凍一樣 Q 彈、服貼度和導入效果更好，是美妝部落客狂推的明星商品。熱門品項：<strong>亮白淨化生物纖維面膜、三分子玻尿酸藍銅面膜、極致保濕生物纖維面膜、抗皺精華系列</strong>。</p>
<p>每片約 35g（比一般面膜稍重），10 片約 0.35kg，運費 NT$290。20 片約 0.7kg，運費同樣 NT$290。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>生物纖維面膜內含較多精華液，鋁箔包比一般面膜更厚實，不易破</li>
<li>若同時寄精華液（玻璃瓶），務必分開包裝——玻璃瓶用氣泡紙+紙板隔層</li>
<li>寵愛之名單價較高（一片 NT$150-250），建議用紙箱而非塑膠袋寄送</li>
</ul>
<h3>🛒 購買建議</h3>
<p>寵愛之名在百貨專櫃（SOGO/新光三越）和屈臣氏/康是美都能買到。官網常有組合優惠（如買面膜送旅行組）。建議直接在官網或 momo 訂購後寄到倉庫。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>寵愛之名在大陸是輕奢定位，小紅書上「生物纖維面膜」的討論度很高。走敏感貨專線包稅通關正常，控制在 20-30 片以內合理自用範圍。</p>"""
    },
    "neogence-shipping": {
        "title": "霓淨思可以寄大陸嗎？玻尿酸精華/面膜寄送攻略 NT$350/kg起 | 速豹集運",
        "h1": "霓淨思可以寄大陸嗎？2026 完整寄送攻略",
        "desc": "霓淨思可以寄大陸嗎？可以！玻尿酸精華/N3面膜/粉刺精華透過含液體特貨專線NT$350/kg起包稅，最快5-7天（空運）。3瓶精華約0.6kg運費NT$350。LINE傳照片秒確認！",
        "keywords": "霓淨思寄大陸,霓淨思可以寄大陸嗎,Neogence寄大陸,玻尿酸精華寄大陸,台灣醫美寄大陸",
        "pillar_name": "化妝品寄大陸",
        "pillar_url": "/blog/cosmetics-shipping",
        "content": """<h2>🔬 霓淨思全系列寄送指南</h2>
<p>霓淨思（Neogence）是台灣醫美保養品牌，以玻尿酸精華液和粉刺代謝精華聞名。熱門品項：<strong>玻尿酸保濕精華液、粉刺淨化精華、N3面膜系列、全能緊緻精華</strong>。精華液含液體，走含液體特貨 NT$350/kg。</p>
<p>精華液每瓶約 30ml，3 瓶約 0.6kg，運費 NT$350。N3 面膜每片約 25g，40 片約 1kg 運費 NT$290。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>精華液是玻璃滴管瓶，處理方式和 DR.WU 相同：每瓶獨立氣泡紙包裹、瓶蓋膠帶固定</li>
<li>面膜和精華液分開包——精華液用紙箱+泡棉，面膜可用氣泡袋</li>
<li>粉刺精華含酸類成分，標籤保留清楚以便海關查驗</li>
</ul>
<h3>🛒 購買建議</h3>
<p>霓淨思在屈臣氏/康是美/寶雅都能買到，官網和蝦皮官方店常有買一送一或第二件半價優惠。CP 值最高的買法是等官網年度大促一次囤貨。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>含液體精華液走特貨 NT$350/kg。霓淨思在大陸天貓有官方旗艦店，但台灣版配方和包裝不同，許多大陸消費者仍偏好代購台灣境內版。控制在 6 瓶以內自用範圍為佳。</p>"""
    },

    # --- 电子产品返修 ---
    "phone-repair-shipping": {
        "title": "手機寄回大陸維修怎麼寄？含電池手機寄送攻略 NT$350/kg起 | 速豹集運",
        "h1": "手機寄回大陸維修怎麼寄？2026 完整攻略",
        "desc": "手機寄回大陸維修怎麼寄？含鋰電池走含電池特貨專線NT$350/kg起包稅雙清，最快5-7天。單支手機約0.3kg運費NT$350。iPhone/三星/華碩皆可寄，LINE傳照片30秒確認！",
        "keywords": "手機寄大陸維修,手機寄回大陸,台灣寄手機到大陸,含電池手機寄大陸,舊手機寄大陸",
        "pillar_name": "電子產品返修寄大陸",
        "pillar_url": "/blog/electronics-repair-return-shipping",
        "content": """<h2>📱 手機寄回大陸維修全攻略</h2>
<p>手機從台灣寄回大陸維修，最大的問題是<strong>鋰電池——郵局和一般快遞不收</strong>。速豹含電池特貨專線可以合法寄送，運費 NT$350/kg 起，包稅雙清。</p>
<p>單支手機約 0.2-0.3kg，運費最低 NT$350。2-3 支約 0.6-0.9kg，運費同樣 NT$350。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>手機務必關機後再寄送（開機狀態運輸有安全風險）</li>
<li>原廠盒子最理想；沒有盒子的話用氣泡紙包裹至少 3 層</li>
<li>螢幕面朝上、用硬紙板固定，防止運輸途中彎折壓碎</li>
<li>外箱貼「易碎品/內含電池」標籤，方便倉庫識別處理</li>
<li>充電線/充電頭可以一起寄，不額外收費</li>
</ul>
<h3>🔄 維修流程建議</h3>
<p>1. 先聯繫大陸維修點確認收件地址和維修費用<br>2. 包裝好後寄到速豹倉庫（苗栗頭份）<br>3. 速豹走含電池特貨專線寄往大陸（5-7天）<br>4. 大陸維修點收件→修好後可再走速豹寄回台灣</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>含鋰電池是航空禁運品，但走含電池特貨專線（海快+空運混合）可合法寄送。申報時需註明「舊手機維修/無商業價值」，降低大陸進口關稅風險。單次建議不超過 3 支。</p>"""
    },
    "laptop-repair-shipping": {
        "title": "筆電寄回大陸維修怎麼寄？含電池筆電寄送攻略 NT$350/kg起 | 速豹集運",
        "h1": "筆電寄回大陸維修怎麼寄？2026 完整攻略",
        "desc": "筆電寄回大陸維修怎麼寄？含鋰電池走含電池特貨專線NT$350/kg起包稅雙清，最快5-7天。一台筆電約2kg運費NT$700。華碩/宏碁/MSI皆可寄，LINE傳照片30秒確認！",
        "keywords": "筆電寄大陸維修,筆電寄回大陸,台灣寄筆電到大陸,含電池筆電寄大陸,筆記型電腦寄大陸維修",
        "pillar_name": "電子產品返修寄大陸",
        "pillar_url": "/blog/electronics-repair-return-shipping",
        "content": """<h2>💻 筆電寄回大陸維修全攻略</h2>
<p>筆電和手機一樣含鋰電池，郵局不收、順豐也不一定收。速豹含電池特貨專線可以寄送，運費 NT$350/kg。</p>
<p>一台筆電約 1.8-2.5kg，運費約 NT$630-875。建議用原廠盒子或專用筆電包。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>筆電務必關機後寄送</li>
<li>最佳包裝：原廠紙箱 + 原廠防震泡棉。如果沒有原廠盒：筆電用氣泡紙包裹 3-5 層 → 放入紙箱 → 四周塞填充物防止晃動</li>
<li>螢幕面朝上、鍵盤面朝下，避免重物壓壞螢幕</li>
<li><strong>重要：變壓器（充電器）含線圈，分開用氣泡紙包裹後和筆電放一起</strong></li>
<li>貼「易碎品/此面向上」標籤</li>
</ul>
<h3>🔄 維修流程建議</h3>
<p>台灣品牌的筆電（華碩/宏碁/MSI/技嘉）送回大陸原廠維修很常見，尤其是保固內的機型。流程：聯繫客服開維修單 → 包裝寄到速豹倉庫 → 含電池特貨 5-7 天 → 大陸維修中心收件。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>申報時寫「舊筆電維修/無商業價值」，附上維修單據更好。保固內維修建議走原廠 RMA 流程，進口關稅可以申請退回。單次建議不超過 2 台。</p>"""
    },
    "camera-repair-shipping": {
        "title": "相機寄回大陸維修怎麼寄？含電池相機寄送攻略 NT$350/kg起 | 速豹集運",
        "h1": "相機寄回大陸維修怎麼寄？2026 完整攻略",
        "desc": "相機寄回大陸維修怎麼寄？含鋰電池走含電池特貨專線NT$350/kg起包稅雙清，最快5-7天。單眼/微單/鏡頭分開包裝，LINE傳照片30秒確認運費！",
        "keywords": "相機寄大陸維修,相機寄回大陸,台灣寄相機到大陸,含電池相機寄大陸,單眼相機寄大陸維修,鏡頭寄大陸",
        "pillar_name": "電子產品返修寄大陸",
        "pillar_url": "/blog/electronics-repair-return-shipping",
        "content": """<h2>📷 相機寄回大陸維修全攻略</h2>
<p>相機（單眼/微單/數位相機）含鋰電池，走含電池特貨專線 NT$350/kg。鏡頭不含電池，走一般專線 NT$290/kg。機身+鏡頭分開包裝最安全。</p>
<p>一台單眼機身約 0.5-0.8kg + 一顆鏡頭約 0.5-1kg = 合計約 1.5kg，運費約 NT$435-525。</p>
<h3>📦 包裝重點</h3>
<ul>
<li><strong>機身和鏡頭一定要分開！</strong>卡口連接處是相機最脆弱的地方，運輸震動極易損壞</li>
<li>機身：用氣泡紙包裹 3-5 層 → 放入獨立小盒 → 再放進外箱</li>
<li>鏡頭：前後蓋蓋好 → 氣泡紙包裹 → 獨立小盒 → 鏡頭周圍至少留 3cm 緩衝空間</li>
<li>記憶卡和電池取出分開包裝（電池用獨立防靜電袋）</li>
<li>外箱貼「精密儀器/易碎品」標籤</li>
</ul>
<h3>🔄 維修流程建議</h3>
<p>Canon/Nikon/Sony 等大廠在大陸都有官方維修中心。建議先聯繫客服確認維修點地址和費用 → 包裝寄到速豹倉庫 → 特貨專線 5-7 天送達。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>高價值相機建議加保價（運費 × 20%）。申報時註明「舊相機維修/無商業價值」。附上購買證明有助降低關稅風險。單次建議不超過 1 組（機身+2 顆鏡頭）。</p>"""
    },
    "gaming-console-repair-shipping": {
        "title": "遊戲機寄回大陸維修怎麼寄？Switch/PS5/Steam Deck寄送攻略 NT$350/kg起 | 速豹集運",
        "h1": "遊戲機寄回大陸維修怎麼寄？2026 完整攻略",
        "desc": "遊戲機寄回大陸維修怎麼寄？Switch/PS5/Steam Deck含鋰電池走含電池特貨專線NT$350/kg起包稅雙清，最快5-7天。Switch約0.5kg運費NT$350。LINE傳照片30秒確認！",
        "keywords": "遊戲機寄大陸維修,Switch寄大陸維修,PS5寄大陸維修,Steam Deck寄大陸,含電池遊戲機寄大陸,遊戲主機寄大陸",
        "pillar_name": "電子產品返修寄大陸",
        "pillar_url": "/blog/electronics-repair-return-shipping",
        "content": """<h2>🎮 遊戲機寄回大陸維修全攻略</h2>
<p>Switch/PS5/Steam Deck 等遊戲機都含鋰電池，走含電池特貨專線 NT$350/kg。Switch 主機約 0.4-0.5kg，運費 NT$350。PS5 約 4.5kg，運費約 NT$1,575。</p>
<h3>📦 包裝重點</h3>
<ul>
<li><strong>Switch 最脆弱的是 Joy-Con 滑軌</strong>，建議 Joy-Con 拆下來分開用氣泡紙包裹，主機本體單獨包裝後再全部放進同一個紙箱</li>
<li>PS5 體積大重量重，包裝時底部和四周至少留 5cm 防震空間</li>
<li>Steam Deck 和 Switch 類似，主機+充電器分開包裝</li>
<li>所有遊戲卡帶/光碟片取出另外包裝，不要插在主機裡</li>
<li>外箱貼「易碎品/電子產品」標籤</li>
</ul>
<h3>🔄 維修流程建議</h3>
<p>Switch 在大陸有騰訊代理的官方維修中心（限國行版），水貨建議找民間信譽好的維修店。PS5 建議走 Sony 官方維修管道。流程：聯繫確認維修點 → 包裝寄倉庫 → 特貨 5-7 天 → 大陸收件維修。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>遊戲機價值較高，建議加保價。申報「舊遊戲機維修/無商業價值」。PS5 因體積大，運費較高，建議先評估維修費用是否值得（有時買新的比運費+維修費便宜）。</p>"""
    }
}

# ========== 生成函数 ==========
def generate_brand_page(key, data):
    """基于模板生成品牌页面"""
    title = data["title"]
    h1 = data["h1"]
    desc = data["desc"]
    keywords = data["keywords"]
    content = data["content"]
    pillar_name = data["pillar_name"]
    pillar_url = data["pillar_url"]

    page = f'''<!DOCTYPE html><html lang="zh-TW"><head>
  <meta charset="UTF-8">
  <link rel="icon" href="/favicon.ico">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{keywords}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="https://subao.tw/images/subao-logo-new.webp">
  <meta property="og:url" content="https://subao.tw/blog/{key}">
  <meta property="og:type" content="article">
  <meta property="og:locale" content="zh_TW">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="canonical" href="https://subao.tw/blog/{key}">
  <meta name="lastmod" content="2026-08-06">
  <style>
    :root{{--primary:#1a56db;--primary-light:#e8f0fe;--text-dark:#1a1a2e;--text-light:#64748b;--bg:#f8fafc;--white:#fff;--border:#e2e8f0;--green:#059669;--amber:#d97706;--radius:12px;--shadow:0 2px 8px rgba(0,0,0,.08)}}
    *{{margin:0;padding:0;box-sizing:border-box}}
    body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang TC","Microsoft JhengHei",sans-serif;color:var(--text-dark);background:var(--bg);line-height:1.7}}
    .container{{max-width:800px;margin:0 auto;padding:0 20px}}
    header{{background:var(--white);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100}}
    nav{{display:flex;align-items:center;justify-content:space-between;max-width:1200px;margin:0 auto;padding:12px 20px}}
    .logo{{font-size:22px;font-weight:800;color:var(--primary);text-decoration:none}}
    .nav-links{{display:flex;gap:20px;align-items:center}}
    .nav-links a{{color:var(--text-light);text-decoration:none;font-size:14px;font-weight:500}}
    .nav-links a:hover{{color:var(--primary)}}
    .btn-line{{background:var(--green);color:var(--white)!important;padding:8px 16px;border-radius:20px;font-weight:600;text-decoration:none;display:inline-flex;align-items:center;gap:6px;font-size:14px}}
    .top-promo{{background:linear-gradient(135deg,#1a56db,#2563eb);color:var(--white);text-align:center;padding:8px 16px;font-size:13px;position:relative;display:flex;align-items:center;justify-content:center;gap:12px;flex-wrap:wrap}}
    .top-promo a{{color:var(--white);background:rgba(255,255,255,.2);padding:4px 14px;border-radius:16px;text-decoration:none;font-weight:600;font-size:12px;white-space:nowrap}}
    .top-promo-close{{position:absolute;right:12px;background:none;border:none;color:var(--white);font-size:20px;cursor:pointer}}
    .article-header{{background:var(--white);padding:40px 0 30px;border-bottom:1px solid var(--border);margin-bottom:30px}}
    .article-header h1{{font-size:28px;line-height:1.4;margin-bottom:12px;color:var(--text-dark)}}
    .article-meta{{color:var(--text-light);font-size:13px}}
    .article-body{{background:var(--white);padding:30px 0;border-radius:var(--radius);box-shadow:var(--shadow);margin-bottom:30px}}
    .article-body .container{{padding:0 24px}}
    .article-body h2{{font-size:22px;margin:30px 0 14px;color:var(--text-dark);padding-bottom:8px;border-bottom:2px solid var(--primary-light)}}
    .article-body h3{{font-size:18px;margin:22px 0 10px;color:var(--text-dark)}}
    .article-body p{{margin:10px 0;color:#334155}}
    .article-body ul{{margin:10px 0;padding-left:24px}}
    .article-body li{{margin:6px 0;color:#334155}}
    .article-body li strong{{color:var(--text-dark)}}
    .cta-box{{background:linear-gradient(135deg,#eff6ff,#dbeafe);border:2px solid var(--primary);border-radius:var(--radius);padding:24px;margin:30px 0;text-align:center}}
    .cta-box p{{font-size:16px;margin-bottom:14px}}
    .cta-box .btn{{display:inline-block;background:var(--green);color:var(--white);padding:12px 28px;border-radius:24px;text-decoration:none;font-weight:700;font-size:16px}}
    .pillar-nav{{background:var(--white);border-radius:var(--radius);box-shadow:var(--shadow);padding:20px 24px;margin-bottom:30px}}
    .pillar-nav strong{{display:block;margin-bottom:10px;color:var(--primary)}}
    .pillar-nav a{{color:var(--primary);text-decoration:none;font-size:14px;font-weight:500}}
    .pillar-nav a:hover{{text-decoration:underline}}
    .internal-links{{background:var(--white);border-radius:var(--radius);box-shadow:var(--shadow);padding:20px 24px;margin-bottom:30px}}
    .internal-links p{{margin:0 0 10px;font-weight:700;color:var(--text-dark);font-size:15px}}
    .internal-links a{{display:inline-block;background:var(--primary-light);color:var(--primary);padding:6px 12px;border-radius:6px;text-decoration:none;font-size:13px;margin:4px 6px 4px 0;font-weight:500}}
    .internal-links a:hover{{background:var(--primary);color:var(--white)}}
    .faq-section{{background:var(--white);border-radius:var(--radius);box-shadow:var(--shadow);padding:24px;margin-bottom:30px}}
    .faq-section h2{{margin-top:0!important;border-bottom:none!important}}
    .faq-item{{border-bottom:1px solid var(--border);padding:14px 0}}
    .faq-item:last-child{{border-bottom:none}}
    .faq-question{{font-weight:700;color:var(--text-dark);margin-bottom:6px;font-size:15px}}
    .faq-answer{{color:#475569;font-size:14px}}
    footer{{background:var(--text-dark);color:var(--white);padding:40px 0 20px;margin-top:40px}}
    footer a{{color:#94a3b8;text-decoration:none;font-size:13px;display:block;margin:4px 0}}
    footer a:hover{{color:var(--white)}}
    footer .footer-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:24px;max-width:1200px;margin:0 auto;padding:0 20px}}
    footer h3{{font-size:16px;margin-bottom:10px;color:var(--white)}}
    .footer-bottom{{text-align:center;padding-top:20px;margin-top:20px;border-top:1px solid #334155;color:#64748b;font-size:13px;max-width:1200px;margin-left:auto;margin-right:auto;padding-left:20px;padding-right:20px}}
    .float-bar{{position:fixed;bottom:0;left:0;right:0;background:var(--white);border-top:2px solid var(--primary);padding:12px 20px;display:flex;align-items:center;justify-content:space-between;z-index:200;box-shadow:0 -4px 16px rgba(0,0,0,.08);flex-wrap:wrap;gap:8px}}
    .float-bar-text{{font-size:13px;line-height:1.4}}
    .float-bar-text strong{{color:var(--primary)}}
    .float-bar-text small{{display:block;color:var(--text-light);font-size:11px}}
    .float-bar-close{{position:absolute;top:4px;right:12px;background:none;border:none;font-size:18px;cursor:pointer;color:var(--text-light)}}
  </style>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-X2T4LGTKJ1"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-X2T4LGTKJ1');</script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"首頁","item":{{"@id":"https://subao.tw/","name":"首頁"}}}},{{"@type":"ListItem","position":2,"name":"{pillar_name}","item":{{"@id":"https://subao.tw{pillar_url}","name":"{pillar_name}"}}}},{{"@type":"ListItem","position":3,"name":"{h1}"}}]}}</script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"{h1}","acceptedAnswer":{{"@type":"Answer","text":"可以寄！走敏感貨專線 NT$290/kg 起包稅雙清，最快5-7天送達。需注意包裝方式和合理自用數量。詳細寄送攻略請看本文完整教學。"}}}},{{"@type":"Question","name":"運費怎麼算？","acceptedAnswer":{{"@type":"Answer","text":"普貨NT$290/kg起、含液體/電池特貨NT$350/kg起，最低收費NT$290/350。包稅雙清、無隱藏費用。用我們的運費計算器試算準確價格。"}}}},{{"@type":"Question","name":"會不會被海關扣？","acceptedAnswer":{{"@type":"Answer","text":"走包稅專線基本上不會。控制在合理自用數量範圍內（一般單次6-12件以內），申報為個人自用、非商業販售。遇到特殊情況我們會協助處理通關。"}}}},{{"@type":"Question","name":"寄送需要多久？","acceptedAnswer":{{"@type":"Answer","text":"敏感貨專線空運 5-7 天送達大陸主要城市（廣東/福建/上海/北京），偏遠地區加 2-3 天。全程物流追蹤可查。"}}}}]}}</script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{h1}","description":"{desc}","datePublished":"2026-08-06","dateModified":"2026-08-06","author":{{"@type":"Organization","name":"速豹集運","url":"https://subao.tw"}},"publisher":{{"@type":"Organization","name":"速豹集運","url":"https://subao.tw","logo":{{"@type":"ImageObject","url":"https://subao.tw/images/subao-logo-new.webp"}}}},"image":"https://subao.tw/images/subao-logo-new.webp","mainEntityOfPage":{{"@type":"WebPage","@id":"https://subao.tw/blog/{key}"}}}}</script>
</head>
<body>
  <header>
    <nav>
      <a href="/" class="logo">速豹集運</a>
      <div class="nav-links">
        <a href="/tw-to-cn">台灣寄大陸</a>
        <a href="/pricing">運費說明</a>
        <a href="/article-list">文章攻略</a>
        <a href="/faq">常見問題</a>
        <a href="https://line.me/R/ti/p/@734dooky" class="btn-line" target="_blank" onclick="gtag('event','line_click',{{event_category:'conversion',event_label:'nav'}});gtag('event','generate_lead',{{event_category:'lead',event_label:'line'}})">💬 LINE 咨詢</a>
      </div>
    </nav>
  </header>

  <div class="top-promo" id="topPromo">
    <span>📦 不確定能不能寄？</span>
    <a href="https://line.me/R/ti/p/@734dooky" target="_blank" onclick="gtag('event','line_click',{{event_category:'conversion',event_label:'top_promo'}});gtag('event','generate_lead',{{event_category:'lead',event_label:'line'}})">LINE 免費估價 →</a>
    <button class="top-promo-close" onclick="this.parentElement.style.display='none'" aria-label="關閉">×</button>
  </div>

  <div class="article-header">
    <div class="container">
      <h1>{h1}</h1>
      <div class="article-meta">📅 2026-08-06 更新 · 速豹集運 · 5-7天送達</div>
    </div>
  </div>

  <div class="article-body">
    <div class="container">
      <div class="pillar-nav">
        <strong>📌 返回主題總覽：</strong>
        <a href="{pillar_url}">{pillar_name}完整攻略 →</a>
      </div>
{content}

      <div class="cta-box">
        <p>📦 <strong>不確定能不能寄？傳照片給我們免費評估</strong></p>
        <p style="font-size:14px;color:var(--text-light)">LINE @734dooky · 平均30分鐘內回覆 · 無隱藏費用</p>
        <a href="https://line.me/R/ti/p/@734dooky" class="btn" target="_blank" onclick="gtag('event','line_click',{{event_category:'conversion',event_label:'cta_box'}});gtag('event','generate_lead',{{event_category:'lead',event_label:'line'}})">💬 LINE 立即咨詢</a>
      </div>

      <div class="internal-links">
        <p>🔗 相關寄送指南</p>
        <a href="{pillar_url}">{pillar_name}</a>
        <a href="/pricing">運費查詢</a>
        <a href="/blog/tw-to-cn-shipping-guide">台灣寄大陸全攻略</a>
        <a href="/blog/tw-to-cn-customs">海關通關指南</a>
      </div>
    </div>
  </div>

  <div class="faq-section">
    <div class="container">
      <h2>❓ 常見問題</h2>
      <div class="faq-item">
        <div class="faq-question">Q: {h1}</div>
        <div class="faq-answer">A: 可以寄！走敏感貨專線 NT$290/kg 起（含液體/電池特貨 NT$350/kg），包稅雙清、最快5-7天送達。需注意包裝方式（防撞/防漏/防爆罐），且控制在合理自用數量範圍內。不確定的話直接 LINE 傳照片，30 秒內回覆。</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Q: 運費怎麼算？最低多少？</div>
        <div class="faq-answer">A: 普貨 NT$290/kg 起、含液體/電池特貨 NT$350/kg 起，最低收費 NT$290/350（不滿 1kg 以 1kg 計）。包稅雙清、無隱藏費用。用網站運費計算器可以試算準確價格。</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Q: 會不會被海關扣押或退運？</div>
        <div class="faq-answer">A: 走包稅專線基本上不會。關鍵是控制在合理自用數量、如實申報。遇到特殊情況我們有專人協助處理通關，不會直接退運。</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Q: 寄到大陸要多久？</div>
        <div class="faq-answer">A: 敏感貨專線空運 5-7 天送達大陸主要城市（廣東/福建/上海/北京等），偏遠地區（新疆/西藏/內蒙）加 2-3 天。全程物流追蹤可查。</div>
      </div>
    </div>
  </div>

  <footer>
    <div class="footer-grid">
      <div>
        <h3>速豹集運</h3>
        <p style="font-size:13px;color:#94a3b8">台灣寄大陸專家，專營敏感貨、保健品、茶葉、化妝品等兩岸快遞服務。</p>
        <p style="font-size:13px;color:#94a3b8">LINE：<a href="https://line.me/R/ti/p/@734dooky" target="_blank" style="color:#60a5fa;display:inline">@734dooky</a></p>
      </div>
      <div>
        <h3>服務項目</h3>
        <a href="/tw-to-cn">台灣發大陸</a>
        <a href="/pricing">運費說明</a>
        <a href="/article-list">文章攻略</a>
        <a href="/pickup-service">上門取貨</a>
        <a href="/faq">常見問題</a>
      </div>
      <div>
        <h3>寄送指南</h3>
        <a href="/blog/tea-shipping-guide">茶葉寄送</a>
        <a href="/blog/cosmetics-shipping">化妝品寄送</a>
        <a href="/blog/health-products-shipping">保健品寄送</a>
        <a href="/blog/food-shipping-guide">食品寄送</a>
      </div>
      <div>
        <h3>幫助中心</h3>
        <a href="/about">關於我們</a>
        <a href="/pricing">運費查詢</a>
        <a href="https://line.me/R/ti/p/@734dooky" target="_blank">LINE 客服</a>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2026 速豹集運 Subao.tw All rights reserved.</p>
    </div>
  </footer>

  <div class="float-bar" id="floatBar">
    <button class="float-bar-close" onclick="this.parentElement.style.display='none'" aria-label="關閉">×</button>
    <div class="float-bar-text">
      <p>📦 不確定能不能寄？<strong>傳照片免費評估</strong></p>
      <small>LINE：@734dooky　平均30分鐘內回覆</small>
    </div>
    <a href="https://line.me/R/ti/p/@734dooky" class="btn-line" target="_blank" onclick="gtag('event','line_click',{{event_category:'conversion',event_label:'float_bar'}});gtag('event','generate_lead',{{event_category:'lead',event_label:'line'}})">💬 LINE 咨詢</a>
  </div>
</body></html>'''
    return page


# ========== 生成所有品牌页 ==========
if __name__ == "__main__":
    generated = []
    for key, data in BRANDS.items():
        filepath = os.path.join(SITE_DIR, f"{key}.html")
        content = generate_brand_page(key, data)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        generated.append(f"{key}.html")
        print(f"✅ {key}.html")

    print(f"\n🎉 共生成 {len(generated)} 个品牌页:")
    for g in generated:
        print(f"   - {g}")
