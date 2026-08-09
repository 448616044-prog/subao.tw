#!/usr/bin/env python3
"""批量生成 subao.tw 品牌子页面 v2 — 奶粉扩展 + 化妆品扩展 + 手机扩展"""
import os

SITE_DIR = "/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn/blog"

# ========== 新增品牌数据 ==========
BRANDS = {
    # --- 母婴奶粉扩展（+3） ---
    "nestle-nan-formula-shipping": {
        "title": "雀巢能恩奶粉可以寄大陸嗎？水解配方/能恩全護寄送攻略 NT$290/kg起 | 速豹集運",
        "h1": "雀巢能恩奶粉可以寄大陸嗎？2026 完整寄送攻略",
        "desc": "雀巢能恩奶粉可以寄大陸嗎？可以！能恩水解/能恩全護透過敏感貨專線NT$290/kg起包稅，最快5-7天（空運）。台灣市佔第一水解配方，6罐約5kg運費約NT$1,450。LINE傳照片秒確認！",
        "keywords": "雀巢寄大陸,雀巢能恩寄大陸,能恩水解寄大陸,能恩全護寄大陸,雀巢奶粉寄大陸,Nestle NAN寄大陸,水解奶粉寄大陸",
        "pillar_name": "母嬰奶粉寄大陸",
        "pillar_url": "/blog/baby-formula-shipping-guide",
        "content": """<h2>🍼 雀巢能恩全系列寄送指南</h2>
<p>雀巢能恩（Nestlé NAN）是台灣市佔第一的水解配方奶粉品牌，根據 Kantar 凱度市調，能恩水解3是三階水解配方市場銷售金額冠軍。熱門品項：<strong>能恩水解3（1-3歲）、能恩全護3（含羅伊氏菌+HMO）、能恩水解1/2（0-1歲）</strong>。全系列鐵罐密封包裝，走敏感貨專線均可寄送。</p>
<p>每罐約 800-900g，6 罐約 5kg，運費約 NT$1,450。能恩水解是許多對牛奶蛋白過敏寶寶的首選，大陸媽媽圈討論度極高。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>鐵罐包裝與桂格/亞培相同，罐蓋用膠帶十字加固防止爆蓋</li>
<li>每罐獨立氣泡紙包裹，罐與罐之間用紙板隔開</li>
<li>水解配方奶粉單價較高（一罐 NT$700-900），建議雙層氣泡紙保護</li>
<li>開罐後的奶粉不要寄——已開封的奶粉容易受潮變質</li>
</ul>
<h3>🛒 購買建議</h3>
<p>能恩在各大藥局（大樹/杏一/丁丁）和母嬰用品店都能買到。Costco 有大罐裝能恩水解3，單價最低。雀巢官網有試用罐申請（NT$550/400g），但不適合大量採購。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>水解配方奶粉屬特殊醫療用途食品，建議附上兒科醫師建議或過敏診斷證明，通關更順利。控制在 6-12 罐合理自用範圍。</p>"""
    },
    "meadjohnson-formula-shipping": {
        "title": "美強生奶粉可以寄大陸嗎？優生/A+/親舒水解寄送攻略 NT$290/kg起 | 速豹集運",
        "h1": "美強生奶粉可以寄大陸嗎？2026 完整寄送攻略",
        "desc": "美強生奶粉可以寄大陸嗎？可以！優生/A+/親舒水解透過敏感貨專線NT$290/kg起包稅，最快5-7天（空運）。6罐約5kg運費約NT$1,450。LINE傳照片30秒確認！",
        "keywords": "美強生寄大陸,美強生奶粉可以寄大陸嗎,優生寄大陸,A+寄大陸,美強生親舒寄大陸,Mead Johnson寄大陸",
        "pillar_name": "母嬰奶粉寄大陸",
        "pillar_url": "/blog/baby-formula-shipping-guide",
        "content": """<h2>👶 美強生全系列寄送指南</h2>
<p>美強生（Mead Johnson）是全球嬰幼兒營養領導品牌，旗下產品線齊全。台灣熱門品項：<strong>優生奶粉（1-3歲）、A+系列、親舒水解配方、安敏健高度水解配方</strong>。全系列鐵罐密封包裝，走敏感貨專線均可寄送。</p>
<p>每罐約 800-900g，6 罐約 5kg，運費約 NT$1,450。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>鐵罐包裝與一般奶粉相同，罐蓋膠帶十字加固</li>
<li>親舒水解是部分水解配方，適用輕度過敏寶寶，罐身標示清楚可輔助通關</li>
<li>安敏健是高度水解配方（醫療級），建議附醫師證明更穩妥</li>
</ul>
<h3>🛒 購買建議</h3>
<p>美強生在藥局和全聯都能買到。Costco 有大罐裝優生系列。親舒水解建議在藥局購買，藥師可以幫忙確認配方適用性。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>美強生是大陸知名度極高的國際品牌，天貓/京東有官方旗艦店，但台灣版的配方和成分標示不同。控制在 6-12 罐合理自用範圍即可。</p>"""
    },
    "karihome-formula-shipping": {
        "title": "卡洛塔妮奶粉可以寄大陸嗎？羊奶粉寄送攻略 NT$290/kg起 | 速豹集運",
        "h1": "卡洛塔妮奶粉可以寄大陸嗎？2026 完整寄送攻略",
        "desc": "卡洛塔妮奶粉可以寄大陸嗎？可以！羊奶粉/牛奶粉透過敏感貨專線NT$290/kg起包稅，最快5-7天（空運）。台灣本土羊奶粉品牌，6罐約5kg運費約NT$1,450。LINE傳照片30秒確認！",
        "keywords": "卡洛塔妮寄大陸,卡洛塔妮奶粉可以寄大陸嗎,卡洛塔妮羊奶粉寄大陸,Karihome寄大陸,台灣羊奶粉寄大陸",
        "pillar_name": "母嬰奶粉寄大陸",
        "pillar_url": "/blog/baby-formula-shipping-guide",
        "content": """<h2>🐐 卡洛塔妮全系列寄送指南</h2>
<p>卡洛塔妮（Karihome）是台灣本土羊奶粉品牌，1986年由友華生技與紐西蘭乳羊合作社合資成立，在台灣和亞太市場深耕近40年。熱門品項：<strong>卡洛塔妮羊奶粉（1-3歲）、成長羊奶粉（3歲以上）、牛奶粉系列</strong>。台灣唯一自有研發+紐西蘭原裝進口的羊奶粉品牌。</p>
<p>每罐約 800-900g，6 罐約 5kg，運費約 NT$1,450。羊奶粉分子比牛奶更小、更接近母乳結構，適合乳糖不耐受和對牛奶蛋白過敏的寶寶。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>鐵罐包裝，罐蓋膠帶十字加固</li>
<li>羊奶粉在台灣單價約 NT$800-1,000/罐，比牛奶粉貴，雙層氣泡紙保護更穩妥</li>
<li>卡洛塔妮的罐身設計較方正，多罐堆疊時穩定度好</li>
</ul>
<h3>🛒 購買建議</h3>
<p>卡洛塔妮在藥局和母嬰用品店為主，全聯不一定有。建議去大樹/杏一藥局購買，通常有會員折扣。官網和 momo 也有直營店。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>卡洛塔妮 2008 年進入中國市場，天貓有官方旗艦店，但台灣版的配方和價格可能不同。控制在 6-12 罐合理自用範圍。羊奶粉在大陸需求旺盛（乳糖不耐受寶寶多），寄送無特殊限制。</p>"""
    },

    # --- 化妆品品牌扩展（+5） ---
    "ttm-mask-shipping": {
        "title": "提提研面膜可以寄大陸嗎？生物纖維面膜寄送攻略 NT$290/kg起 | 速豹集運",
        "h1": "提提研面膜可以寄大陸嗎？2026 完整寄送攻略",
        "desc": "提提研面膜可以寄大陸嗎？可以！TTM生物纖維面膜/黑蜂蜜/向日葵系列透過敏感貨專線NT$290/kg起包稅，最快5-7天（空運）。10片約0.4kg運費NT$290。LINE傳照片30秒確認！",
        "keywords": "提提研寄大陸,提提研面膜寄大陸,TTM寄大陸,Timeless Truth Mask寄大陸,生物纖維面膜寄大陸,台灣面膜寄大陸",
        "pillar_name": "化妝品寄大陸",
        "pillar_url": "/blog/cosmetics-shipping",
        "content": """<h2>🏆 提提研全系列寄送指南</h2>
<p>提提研（Timeless Truth Mask，簡稱 TTM）是台灣頂級面膜品牌，連續6年獲得英國 Pure Beauty Awards 美妝大賞，2020年獲法國 Élu Produit de l'Année 年度創品獎。熱門系列：<strong>黑蜂蜜活源新肌生物纖維面膜、向日葵光透白皙面膜、希俄斯乳香柔衡面膜、永生苔修護面膜</strong>。全系列鋁箔獨立包裝，走敏感貨專線均可寄送。</p>
<p>每片約 35g（生物纖維材質較重），10片約 0.35kg，運費 NT$290。20片約 0.7kg，運費同樣 NT$290。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>生物纖維面膜含精華液較多（每片約 28-30ml），鋁箔包比一般面膜厚實</li>
<li>面膜不怕壓，用紙箱或快遞袋均可</li>
<li>提提研單價較高（一片 NT$150-250），建議用紙箱寄送</li>
</ul>
<h3>🛒 購買建議</h3>
<p>提提研在屈臣氏/康是美/寶雅都能買到，官網常有組合優惠和新品首發。黑蜂蜜系列是明星商品，建議直接在官網或 momo 購買寄到倉庫。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>提提研在中國大陸沒有官方旗艦店，但小紅書上「TTM提提研」的討論度很高，尤其是生物纖維面膜。走敏感貨專線包稅通關正常，控制在 20-30 片合理自用範圍。</p>"""
    },
    "mirae-mask-shipping": {
        "title": "未來美面膜可以寄大陸嗎？8分鐘/PDRN外泌體面膜寄送攻略 NT$290/kg起 | 速豹集運",
        "h1": "未來美面膜可以寄大陸嗎？2026 完整寄送攻略",
        "desc": "未來美面膜可以寄大陸嗎？可以！8分鐘微分子/專業院線PDRN外泌體面膜透過敏感貨專線NT$290/kg起包稅，最快5-7天（空運）。20片約0.6kg運費NT$290。LINE傳照片30秒確認！",
        "keywords": "未來美寄大陸,未來美面膜寄大陸,8分鐘面膜寄大陸,PDRN面膜寄大陸,台灣面膜寄大陸",
        "pillar_name": "化妝品寄大陸",
        "pillar_url": "/blog/cosmetics-shipping",
        "content": """<h2>⏱️ 未來美全系列寄送指南</h2>
<p>未來美（Mirae）是台灣成長最快的平價面膜品牌，以「8分鐘面膜」聞名——主打快速吸收、懶人保養。近期更大推「專業院線PDRN外泌體新生面膜」，結合韓國醫美成份，一片等於30ml水光精華。熱門系列：<strong>8分鐘微分子面膜（玻尿酸保濕/淨白）、PDRN外泌體新生面膜、胜肽抗皺面膜</strong>。全系列鋁箔獨立包裝，走敏感貨專線均可寄送。</p>
<p>每片約 25-30g，20片約 0.6kg，運費 NT$290。40片約 1.2kg，運費約 NT$348。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>片狀面膜輕薄不怕壓，一般紙箱或快遞袋即可</li>
<li>8分鐘系列是紙盒+鋁箔獨立包裝，雙層保護很穩固</li>
<li>PDRN精華液面膜含水量較高，同樣常溫寄送即可</li>
</ul>
<h3>🛒 購買建議</h3>
<p>未來美在屈臣氏/康是美/寶雅都很常見，常有限時特價。蝦皮官方旗艦店也常有買一送一活動。建議一次囤貨後直接寄到倉庫。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>未來美在大陸知名度快速上升，8分鐘面膜是很多美妝博主的推薦。走敏感貨專線包稅通關正常，控制在 40-50 片合理自用範圍。</p>"""
    },
    "drsatin-shipping": {
        "title": "Dr. Satin可以寄大陸嗎？魚子精華/膠原蛋白面膜寄送攻略 NT$290/kg起 | 速豹集運",
        "h1": "Dr. Satin可以寄大陸嗎？2026 完整寄送攻略",
        "desc": "Dr. Satin可以寄大陸嗎？可以！頂級魚子膠原面膜/胜肽精華透過敏感貨專線NT$290/kg起包稅，最快5-7天（空運）。10片約0.4kg運費NT$290。LINE傳照片30秒確認！",
        "keywords": "Dr. Satin寄大陸,Dr Satin可以寄大陸嗎,魚子面膜寄大陸,魚子精華寄大陸,台灣醫美面膜寄大陸",
        "pillar_name": "化妝品寄大陸",
        "pillar_url": "/blog/cosmetics-shipping",
        "content": """<h2>🐟 Dr. Satin 全系列寄送指南</h2>
<p>Dr. Satin 是台灣醫美級平價保養品牌，以「魚子精華」系列聞名，屈臣氏熱銷排行榜常客。熱門品項：<strong>頂級魚子膠原面膜、魚子精華保濕系列、胜肽抗皺精華</strong>。全系列工廠密封包裝，走敏感貨專線均可寄送。</p>
<p>面膜每片約 30g，10片約 0.3kg，運費 NT$290。精華液（含液體）走含液體特貨 NT$350/kg。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>面膜片狀包裝不怕壓，一般紙箱即可</li>
<li>若同時寄精華液（玻璃瓶），分開氣泡紙包裹後放入紙箱</li>
<li>魚子系列包裝質感好（藍色瓶身），送禮也體面</li>
</ul>
<h3>🛒 購買建議</h3>
<p>Dr. Satin 主要在屈臣氏販售，經常買一送一。官網和蝦皮也有直營店。魚子面膜 3入 NT$299，CP值很高，適合大量囤貨。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>Dr. Satin 在中國大陸知名度一般，但「魚子精華」這個成分在大陸保養圈很受追捧。走敏感貨專線包稅通關正常。</p>"""
    },
    "my-scheming-shipping": {
        "title": "我的心機面膜可以寄大陸嗎？玻色因/玻尿酸面膜寄送攻略 NT$290/kg起 | 速豹集運",
        "h1": "我的心機面膜可以寄大陸嗎？2026 完整寄送攻略",
        "desc": "我的心機面膜可以寄大陸嗎？可以！石墨烯玻色因/玻尿酸/黑珍珠面膜透過敏感貨專線NT$290/kg起包稅，最快5-7天（空運）。20片約0.5kg運費NT$290。LINE傳照片30秒確認！",
        "keywords": "我的心機寄大陸,我的心機面膜寄大陸,玻色因面膜寄大陸,石墨烯面膜寄大陸,台灣面膜寄大陸",
        "pillar_name": "化妝品寄大陸",
        "pillar_url": "/blog/cosmetics-shipping",
        "content": """<h2>💎 我的心機全系列寄送指南</h2>
<p>我的心機（My Scheming）是台灣開架面膜人氣品牌，以高CP值和多元功效聞名。熱門系列：<strong>石墨烯玻色因彈潤面膜、玻尿酸保濕面膜、黑珍珠煥白面膜、蝸牛修護面膜</strong>。全系列鋁箔獨立包裝，走敏感貨專線均可寄送。</p>
<p>每片約 25g，20片約 0.5kg，運費 NT$290。40片約 1kg，運費同樣 NT$290。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>片狀面膜輕薄，一般快遞袋或紙箱即可</li>
<li>石墨烯系列採用特殊膜布材質，和一般面膜一樣常溫保存</li>
<li>多口味混寄無影響，一箱多種系列</li>
</ul>
<h3>🛒 購買建議</h3>
<p>我的心機在屈臣氏/康是美/寶雅都能買到，蝦皮官方旗艦店常有買二送一優惠。玻色因系列是抗老新寵，建議在官網或蝦皮趁活動時囤貨。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>我的心機在大陸天貓有官方旗艦店，但台灣版的配方和包裝不同，大陸消費者仍偏愛台灣境內版。走敏感貨專線包稅通關正常。</p>"""
    },
    "shirojyun-shipping": {
        "title": "自白肌可以寄大陸嗎？玻尿酸保濕/美白精華寄送攻略 NT$290/kg起 | 速豹集運",
        "h1": "自白肌可以寄大陸嗎？2026 完整寄送攻略",
        "desc": "自白肌可以寄大陸嗎？可以！玻尿酸保濕精華/美白系列透過敏感貨專線NT$290/kg起包稅，最快5-7天（空運）。3瓶精華約0.5kg運費NT$290。LINE傳照片30秒確認！",
        "keywords": "自白肌寄大陸,自白肌可以寄大陸嗎,自白肌玻尿酸寄大陸,自白肌美白寄大陸,台灣醫美保養品寄大陸",
        "pillar_name": "化妝品寄大陸",
        "pillar_url": "/blog/cosmetics-shipping",
        "content": """<h2>💧 自白肌全系列寄送指南</h2>
<p>自白肌（Shirojyun）是台灣醫美保養品牌，以「高濃度玻尿酸」和「美白」系列聞名，主打成分單純、溫和不刺激，特別適合敏感肌。熱門品項：<strong>玻尿酸保濕精華液、美白淡斑精華、玻尿酸化妝水、美白乳液</strong>。</p>
<p>精華液每瓶約 30-50ml，3瓶約 0.5kg，運費 NT$290。化妝水含液體較多，走含液體特貨 NT$350/kg。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>精華液是塑膠瓶裝，比玻璃瓶耐撞，但仍建議氣泡紙包裹</li>
<li>化妝水是大瓶裝（200-500ml），瓶蓋用膠帶加固以防滲漏</li>
<li>乳液瓶也建議單獨氣泡紙包裹</li>
</ul>
<h3>🛒 購買建議</h3>
<p>自白肌在屈臣氏/康是美銷量穩定，經常買一送一。官網和蝦皮旗艦店也有獨家組合。保濕精華是入門首選，建議先試一瓶確認適合膚質後再大量購買。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>自白肌在中國大陸知名度中等，但因成分單純溫和，適合敏感肌，小紅書上討論度持續上升。走敏感貨專線包稅通關正常。</p>"""
    },

    # --- 电子产品返修扩展（+3） ---
    "tablet-repair-shipping": {
        "title": "平板寄回大陸維修怎麼寄？iPad/安卓平板含電池寄送攻略 NT$350/kg起 | 速豹集運",
        "h1": "平板寄回大陸維修怎麼寄？2026 完整攻略",
        "desc": "平板寄回大陸維修怎麼寄？iPad/安卓平板含鋰電池走含電池特貨專線NT$350/kg起包稅雙清，最快5-7天。iPad約0.5kg運費NT$350。LINE傳照片30秒確認運費！",
        "keywords": "平板寄大陸維修,iPad寄大陸維修,平板寄回大陸,含電池平板寄大陸,iPad寄回大陸維修,安卓平板寄大陸",
        "pillar_name": "電子產品返修寄大陸",
        "pillar_url": "/blog/electronics-repair-return-shipping",
        "content": """<h2>📱 平板寄回大陸維修全攻略</h2>
<p>iPad 和安卓平板都含鋰電池，郵局不收、順豐不一定收。走含電池特貨專線 NT$350/kg，單台平板約 0.5-0.7kg，運費 NT$350。iPad Pro 12.9吋約 0.7kg，運費同樣 NT$350。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>平板螢幕是最脆弱的部分，務必用硬紙板固定螢幕面</li>
<li>原廠盒子最佳；沒有的話用氣泡紙包裹至少3層 → 放入紙箱 → 四周塞填充物</li>
<li>Apple Pencil/觸控筆分開用氣泡紙包裹後和平板放一起</li>
<li>充電器和充電線可以一起寄，不額外收費</li>
<li>外箱貼「易碎品/此面向上」標籤</li>
</ul>
<h3>🔄 維修流程建議</h3>
<p>iPad 送回大陸維修建議走第三方專業維修店（換螢幕/換電池比蘋果官方便宜很多）。流程：確認維修點 → 包裝寄倉庫 → 含電池特貨 5-7天 → 大陸收件維修 → 修好後可再走速豹寄回台灣。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>iPad 需關閉「尋找我的 iPad」後再寄送（否則大陸維修點無法操作）。申報「舊平板維修/無商業價值」。單次建議不超過 2 台。</p>"""
    },
    "headphones-repair-shipping": {
        "title": "耳機寄回大陸維修怎麼寄？AirPods/藍牙耳機含電池寄送攻略 NT$350/kg起 | 速豹集運",
        "h1": "耳機寄回大陸維修怎麼寄？2026 完整攻略",
        "desc": "耳機寄回大陸維修怎麼寄？AirPods/藍牙耳機含鋰電池走含電池特貨專線NT$350/kg起包稅雙清，最快5-7天。一副AirPods約0.2kg運費NT$350。LINE傳照片30秒確認！",
        "keywords": "耳機寄大陸維修,AirPods寄大陸維修,藍牙耳機寄大陸維修,耳機寄回大陸,含電池耳機寄大陸,Beats寄大陸",
        "pillar_name": "電子產品返修寄大陸",
        "pillar_url": "/blog/electronics-repair-return-shipping",
        "content": """<h2>🎧 耳機寄回大陸維修全攻略</h2>
<p>AirPods/藍牙耳機都含微型鋰電池，走含電池特貨專線 NT$350/kg。一副 AirPods Pro 含充電盒約 0.15kg，運費最低 NT$350。頭戴式耳機（如 AirPods Max/Sony WH-1000）約 0.4kg，運費同樣 NT$350。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>AirPods 體積小、容易遺失，務必放入小盒後再放進外箱</li>
<li>充電盒用氣泡紙獨立包裹，防止刮傷</li>
<li>頭戴式耳機用原廠盒最理想；沒有的話用氣泡紙包裹耳罩和頭梁</li>
<li>充電線可以一起寄，不額外收費</li>
</ul>
<h3>🔄 維修流程建議</h3>
<p>AirPods 常見問題：單耳不響/電池衰退/充電盒不充電。大陸華強北有大量專業維修店，換電池 NT$300-500 比蘋果官方 NT$2,290 便宜很多。流程：確認維修點 → 包裝寄倉庫 → 含電池特貨 5-7天 → 大陸收件。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>AirPods 需在 iPhone 上「忘記此裝置」解除配對後再寄出。Beats 耳機流程相同。單次建議不超過 3 副。</p>"""
    },
    "smartwatch-repair-shipping": {
        "title": "智慧手錶寄回大陸維修怎麼寄？Apple Watch/三星含電池寄送攻略 NT$350/kg起 | 速豹集運",
        "h1": "智慧手錶寄回大陸維修怎麼寄？2026 完整攻略",
        "desc": "智慧手錶寄回大陸維修怎麼寄？Apple Watch/三星手錶含鋰電池走含電池特貨專線NT$350/kg起包稅雙清，最快5-7天。單支Apple Watch約0.1kg運費NT$350。LINE傳照片秒確認！",
        "keywords": "智慧手錶寄大陸維修,Apple Watch寄大陸維修,三星手錶寄大陸,手錶寄回大陸維修,含電池手錶寄大陸,Garmin寄大陸",
        "pillar_name": "電子產品返修寄大陸",
        "pillar_url": "/blog/electronics-repair-return-shipping",
        "content": """<h2>⌚ 智慧手錶寄回大陸維修全攻略</h2>
<p>Apple Watch/三星 Galaxy Watch/Garmin 等智慧手錶都含鋰電池，走含電池特貨專線 NT$350/kg。單支手錶約 0.05-0.1kg，運費最低 NT$350。手錶體積小價值高，包裝務必謹慎。</p>
<h3>📦 包裝重點</h3>
<ul>
<li>手錶本體用氣泡紙包裹至少 3 層 → 放入小硬盒（如首飾盒）→ 再放進外箱</li>
<li>錶帶和充電器分開包裝後和手錶放一起</li>
<li>Apple Watch 螢幕容易刮傷，建議貼一層保護膜再包裝</li>
<li>外箱貼「易碎品」標籤，並建議加保價</li>
</ul>
<h3>🔄 維修流程建議</h3>
<p>智慧手錶常見問題：電池老化/螢幕碎裂/進水/無法開機。Apple Watch 官方換電池 NT$3,290，第三方維修約 NT$800-1,200。流程：確認維修點 → 解鎖配對 → 寄倉庫 → 含電池特貨 5-7天 → 大陸收件。</p>
<h3>⚠️ 寄大陸注意事項</h3>
<p>Apple Watch 需先在 iPhone 上解除配對並關閉「啟用鎖定」，否則大陸維修點無法操作。高價值手錶（Apple Watch Ultra 等）建議加保價。單次建議不超過 2 支。</p>"""
    },
}


# ========== 生成函数 ==========
def generate_brand_page(key, data):
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
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"{h1}","acceptedAnswer":{{"@type":"Answer","text":"可以寄！走敏感貨專線 NT$290/kg 起包稅雙清，最快5-7天送達。需注意包裝方式和合理自用數量。詳細攻略請看本文完整教學。"}}}},{{"@type":"Question","name":"運費怎麼算？","acceptedAnswer":{{"@type":"Answer","text":"普貨NT$290/kg起、含液體/電池特貨NT$350/kg起，最低收費NT$290/350。包稅雙清、無隱藏費用。用網站運費計算器試算準確價格。"}}}},{{"@type":"Question","name":"會不會被海關扣？","acceptedAnswer":{{"@type":"Answer","text":"走包稅專線基本上不會。控制在合理自用數量範圍內，申報為個人自用。遇到特殊情況我們會協助處理通關。"}}}},{{"@type":"Question","name":"寄送需要多久？","acceptedAnswer":{{"@type":"Answer","text":"敏感貨專線空運 5-7 天送達大陸主要城市，偏遠地區加 2-3 天。全程物流追蹤可查。"}}}}]}}</script>
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
      <div class="faq-item"><div class="faq-question">Q: {h1}</div><div class="faq-answer">A: 可以寄！走敏感貨專線 NT$290/kg 起（含液體/電池特貨 NT$350/kg），包稅雙清、最快5-7天送達。需注意包裝方式且控制在合理自用數量範圍內。不確定的話直接 LINE 傳照片，30 秒內回覆。</div></div>
      <div class="faq-item"><div class="faq-question">Q: 運費怎麼算？最低多少？</div><div class="faq-answer">A: 普貨 NT$290/kg 起、含液體/電池特貨 NT$350/kg 起，最低收費 NT$290/350（不滿 1kg 以 1kg 計）。包稅雙清、無隱藏費用。</div></div>
      <div class="faq-item"><div class="faq-question">Q: 會不會被海關扣押或退運？</div><div class="faq-answer">A: 走包稅專線基本上不會。關鍵是控制在合理自用數量、如實申報。遇到特殊情況我們有專人協助處理通關。</div></div>
      <div class="faq-item"><div class="faq-question">Q: 寄到大陸要多久？</div><div class="faq-answer">A: 敏感貨專線空運 5-7 天送達大陸主要城市，偏遠地區加 2-3 天。全程物流追蹤可查。</div></div>
    </div>
  </div>

  <footer>
    <div class="footer-grid">
      <div><h3>速豹集運</h3><p style="font-size:13px;color:#94a3b8">台灣寄大陸專家，專營敏感貨兩岸快遞服務。</p><p style="font-size:13px;color:#94a3b8">LINE：<a href="https://line.me/R/ti/p/@734dooky" target="_blank" style="color:#60a5fa;display:inline">@734dooky</a></p></div>
      <div><h3>服務項目</h3><a href="/tw-to-cn">台灣發大陸</a><a href="/pricing">運費說明</a><a href="/article-list">文章攻略</a><a href="/pickup-service">上門取貨</a><a href="/faq">常見問題</a></div>
      <div><h3>寄送指南</h3><a href="/blog/tea-shipping-guide">茶葉寄送</a><a href="/blog/cosmetics-shipping">化妝品寄送</a><a href="/blog/health-products-shipping">保健品寄送</a><a href="/blog/food-shipping-guide">食品寄送</a></div>
      <div><h3>幫助中心</h3><a href="/about">關於我們</a><a href="/pricing">運費查詢</a><a href="https://line.me/R/ti/p/@734dooky" target="_blank">LINE 客服</a></div>
    </div>
    <div class="footer-bottom"><p>© 2026 速豹集運 Subao.tw All rights reserved.</p></div>
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
