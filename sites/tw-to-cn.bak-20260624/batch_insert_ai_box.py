#!/usr/bin/env python3
"""批量为 subao.tw blog 文章插入 AI Summary Box"""

import os
import re

BLOG_DIR = "/Users/mac/WorkBuddy/Claw/物流項目/sites/tw-to-cn/blog"

# 每个文件的配置: (文件名, 颜色主题, 盒子标题, 摘要内容)
BOXES = {
    "cosmetics-shipping.html": {
        "theme": "purple",
        "title": "化妝品快遞大陸",
        "content": (
            "<strong>台灣化妝品可以寄大陸！</strong>面膜、保養品、精華液、乳液都可以走敏感貨專線寄送。<br>\n"
            "<strong>需要注意</strong>：液體需做好防漏包裝、每件建議20件以內、保持原廠標籤完整。<br>\n"
            "<strong>不能寄</strong>：指甲油（易燃）、噴霧型防曬（壓縮氣體）。<br>\n"
            "<a href=\"https://line.me/ti/p/~mmmppp004\" style=\"color:#7B1FA2;font-weight:700\">化妝品能不能寄？傳產品包裝照片30分鐘內回覆 →</a>"
        ),
    },
    "mid-autumn-mooncake-shipping.html": {
        "theme": "orange",
        "title": "月餅快遞大陸",
        "content": (
            "<strong>台灣月餅可以寄大陸！</strong>傳統月餅、蛋黃酥、鳳梨酥均可走敏感貨專線寄送。<br>\n"
            "<strong>需要注意</strong>：肉鬆/蛋黃月餅屬肉類成分，無法寄送；月餅禮盒建議真空包裝防碎。<br>\n"
            "<strong>最佳時機</strong>：中秋節前2-3週寄出，確保親友準時收到。<br>\n"
            "<a href=\"https://line.me/ti/p/~mmmppp004\" style=\"color:#E65100;font-weight:700\">月餅能不能寄？傳包裝成分表30分鐘內回覆 →</a>"
        ),
    },
    "shopee-shipping.html": {
        "theme": "purple",
        "title": "蝦皮貨寄大陸",
        "content": (
            "<strong>蝦皮賣家可以把貨寄到大陸！</strong>台灣電商賣家出貨到大陸消費者，可走轉運集運模式。<br>\n"
            "<strong>關鍵步驟</strong>：將貨寄到台灣集運倉 → 合併包裹 → 敏感貨專線發往大陸。<br>\n"
            "<strong>適合商品</strong>：服飾、配件、化妝品（小量）、書籍、台灣特產。<br>\n"
            "<a href=\"https://line.me/ti/p/~mmmppp004\" style=\"color:#7B1FA2;font-weight:700\">想從蝦皮發貨到大陸？問集運運費 →</a>"
        ),
    },
    "taiwan-to-china-guide.html": {
        "theme": "blue",
        "title": "台灣寄大陸",
        "content": (
            "<strong>台灣寄東西到大陸，選對渠道就不難。</strong>不同商品適合不同線路：敏感貨（食品/保健品/茶葉）走專線，化妝品/藥品有特殊規範。<br>\n"
            "<strong>三步驟</strong>：確認物品可不可以寄 → 選對物流渠道 → 打包符合規範。<br>\n"
            "<a href=\"https://line.me/ti/p/~mmmppp004\" style=\"color:#1565C0;font-weight:700\">不知道寄什麼渠道？傳物品照片30分鐘內回覆 →</a>"
        ),
    },
    "tw-to-cn-shipping-methods.html": {
        "theme": "blue",
        "title": "快遞方式比較",
        "content": (
            "<strong>台灣寄大陸有四大方式：</strong>快遞專線（3-7天）、經濟線（7-15天）、空運（1-3天）、海運（15-30天）。<br>\n"
            "<strong>快速選擇指南</strong>：緊急文件選快遞專線、大量貨物選經濟線、貴重物品選空運、工廠大貨選海運。<br>\n"
            "<a href=\"https://line.me/ti/p/~mmmppp004\" style=\"color:#1565C0;font-weight:700\">不知道哪種方式適合我？提供物品資訊，速豹幫你推薦 →</a>"
        ),
    },
    "tw-to-cn-cost.html": {
        "theme": "blue",
        "title": "運費多少錢",
        "content": (
            "<strong>台灣寄大陸運費 NT$250 起。</strong>實際費用取決於：商品種類（普通/敏感貨）、重量、體積、選擇的服務等級。<br>\n"
            "<strong>計價原則</strong>：首重+續重，越重相對越划算；敏感貨比普通貨運費高20-50%。<br>\n"
            "<a href=\"https://line.me/ti/p/~mmmppp004\" style=\"color:#1565C0;font-weight:700\">查運費！提供：物品、重量、目的城市，30分鐘內報價 →</a>"
        ),
    },
    "birds-nest-ginseng-shipping.html": {
        "theme": "green",
        "title": "燕窩人蔘寄大陸",
        "content": (
            "<strong>燕窩、人蔘可以寄大陸！</strong>乾燕窩、即食燕窩、人蔘/高麗蔘、枸杞等養生食材均可走敏感貨專線。<br>\n"
            "<strong>需要注意</strong>：燕窩需乾燥密封包裝、人蔘建議真空包裝、數量不超過合理自用範圍。<br>\n"
            "<a href=\"https://line.me/ti/p/~mmmppp004\" style=\"color:#2E7D32;font-weight:700\">燕窩/人蔘能不能寄？傳包裝照片30分鐘內回覆 →</a>"
        ),
    },
    "taobao-consolidated-shipping.html": {
        "theme": "blue",
        "title": "淘寶集運",
        "content": (
            "<strong>台灣買淘寶可以集運回台灣，但subao.tw是反方向：台灣寄貨到大陸。</strong>如果你在大陸，想把台灣商品寄過去，我們提供台灣→大陸的敏感貨轉運服務。<br>\n"
            "<strong>適合場景</strong>：台灣親友寄大陸、跨境電商出貨、台商調貨。<br>\n"
            "<a href=\"https://line.me/ti/p/~mmmppp004\" style=\"color:#1565C0;font-weight:700\">需要從台灣寄東西到大陸？30分鐘內回覆運費 →</a>"
        ),
    },
    "tw-to-cn-shipping-guide.html": {
        "theme": "blue",
        "title": "寄件指南",
        "content": (
            "<strong>台灣寄大陸完整攻略：</strong>選對渠道 → 確認物品規範 → 正確打包 → 填寫申報。<br>\n"
            "<strong>最常見失敗原因</strong>：瞞報液體、使用普通快遞寄敏感貨、包裝不當導致退件。<br>\n"
            "<a href=\"https://line.me/ti/p/~mmmppp004\" style=\"color:#1565C0;font-weight:700\">第一次寄？不知道怎麼打包？速豹教你正確流程 →</a>"
        ),
    },
    "tw-to-cn-customs.html": {
        "theme": "orange",
        "title": "大陸海關報關",
        "content": (
            "<strong>大陸海關對個人包裹有免稅額：每次50元人民幣。</strong>超出需繳納行郵稅，稅率視品類而定（食品20%、化妝品50%等）。<br>\n"
            "<strong>如實申報是關鍵：</strong>瞞報被查到會罰款、課稅，甚至退件。<br>\n"
            "<a href=\"https://line.me/ti/p/~mmmppp004\" style=\"color:#E65100;font-weight:700\">想知道稅費怎麼算？提供物品名稱和價值，速豹幫你估算 →</a>"
        ),
    },
    "taiwan-to-china-shipping-time.html": {
        "theme": "blue",
        "title": "寄大陸時效",
        "content": (
            "<strong>台灣寄大陸時效3-15個工作天。</strong>快遞專線約3-7天，經濟線約7-15天。具體看商品種類和目的城市。<br>\n"
            "<strong>春節/五一/國慶</strong>期間海關清關慢，建議提前7-10天寄出。<br>\n"
            "<a href=\"https://line.me/ti/p/~mmmppp004\" style=\"color:#1565C0;font-weight:700\">現在寄，中秋節前能到嗎？速豹幫你評估時效 →</a>"
        ),
    },
    "taiwan-medicine-to-china.html": {
        "theme": "teal",
        "title": "藥品中藥寄大陸",
        "content": (
            "<strong>中藥（科學中藥、丸、散）和一般西藥（自用合理數量）可以寄大陸。</strong>需提供藥名、成分、工廠名稱。<br>\n"
            "<strong>禁寄</strong>：不明成分中草藥、需冷藏的胰島素、未經批准的新藥。<br>\n"
            "<a href=\"https://line.me/ti/p/~mmmppp004\" style=\"color:#00695C;font-weight:700\">藥品能不能寄？提供藥名和成分，30分鐘內回覆 →</a>"
        ),
    },
    "tw-to-cn-returned.html": {
        "theme": "orange",
        "title": "大陸退貨處理",
        "content": (
            "<strong>包裹被大陸海關退件怎麼辦？</strong>常見原因：敏感貨瞞報、包裝不合規範、申報不實。<br>\n"
            "<strong>速豹處理的退件流程</strong>：確認退件原因 → 提供解決方案（重新申報/轉運/報廢）→ 重新安排發貨。<br>\n"
            "<a href=\"https://line.me/ti/p/~mmmppp004\" style=\"color:#E65100;font-weight:700\">包裹被退件了？傳單號，速豹幫你查原因 →</a>"
        ),
    },
    "tw-to-cn-express-comparison.html": {
        "theme": "blue",
        "title": "快遞比較",
        "content": (
            "<strong>台灣寄大陸快遞：順豐 vs 中華郵政EMS vs 敏感貨專線。</strong>順豐對液體/食品有限制，EMS時效較慢，敏感貨專線最適合食品/保健品/茶葉。<br>\n"
            "<strong>選擇建議</strong>：普通文件→順豐；食品/保健品/茶葉→速豹敏感貨專線；不著急→EMS經濟線。<br>\n"
            "<a href=\"https://line.me/ti/p/~mmmppp004\" style=\"color:#1565C0;font-weight:700\">不知道哪個快遞適合？提供物品和目的地，30分鐘內推薦 →</a>"
        ),
    },
    "tw-to-cn-logistics-recommend.html": {
        "theme": "blue",
        "title": "物流推薦",
        "content": (
            "<strong>寄送台灣到大陸，最推薦敏感貨專線。</strong>我們熟悉兩岸海關規定，能最大化降低查扣風險，提供包稅通關選項。<br>\n"
            "<strong>不推薦</strong>：順豐寄液體/食品（多被扣關）、UPS/DHL（價格高且不承接敏感貨）。<br>\n"
            "<a href=\"https://line.me/ti/p/~mmmppp004\" style=\"color:#1565C0;font-weight:700\">速豹敏感貨專線多少錢？提供物品、重量、目的城市，速豹30分鐘內報價 →</a>"
        ),
    },
    "tw-to-cn-logistics-comparison.html": {
        "theme": "blue",
        "title": "物流比較",
        "content": (
            "<strong>主流台灣到大陸物流：敏感貨專線、EMS、航空小包。</strong>各有優劣——速度vs價格vs通關率。<br>\n"
            "<strong>敏感貨專線</strong>：速度中等（3-7天），通關率高，含包稅服務，性價比最高。<br>\n"
            "<a href=\"https://line.me/ti/p/~mmmppp004\" style=\"color:#1565C0;font-weight:700\">想寄東西到大陸但不知道選哪個？速豹根據你的物品和需求推薦最適方案 →</a>"
        ),
    },
    "taiwan-products-jd-tmall.html": {
        "theme": "blue",
        "title": "京東天貓台灣商品",
        "content": (
            "<strong>台灣商品入駐京東/天貓門檻高，但個人寄送可以。</strong>無論是工廠出貨還是個人禮品，速豹都提供台灣→大陸轉運服務。<br>\n"
            "<strong>暢銷品類</strong>：台灣茶葉、保養品、零食、特產禮盒在京東/小紅書需求旺盛。<br>\n"
            "<a href=\"https://line.me/ti/p/~mmmppp004\" style=\"color:#1565C0;font-weight:700\">想把台灣商品發到大陸？提供品名和數量，速豹評估能否寄送 →</a>"
        ),
    },
}

# 主题颜色配置
THEMES = {
    "blue":    {"gradient": "#E3F2FD 0%,#BBDEFB 100%", "border": "#1976D2", "badge": "#1976D2", "text": "#1565C0"},
    "purple":  {"gradient": "#F3E5F5 0%,#E1BEE7 100%", "border": "#7B1FA2", "badge": "#7B1FA2", "text": "#7B1FA2"},
    "orange":  {"gradient": "#FFF3E0 0%,#FFE0B2 100%", "border": "#E65100", "badge": "#E65100", "text": "#E65100"},
    "green":   {"gradient": "#E8F5E9 0%,#C8E6C9 100%", "border": "#388E3C", "badge": "#388E3C", "text": "#2E7D32"},
    "teal":    {"gradient": "#E0F2F1 0%,#B2DFDB 100%", "border": "#00695C", "badge": "#00695C", "text": "#00695C"},
}


def make_box(filename, config):
    """生成 AI Summary Box HTML"""
    theme = THEMES[config["theme"]]
    content = config["content"]
    title = config["title"]
    return f'''    <!-- AI摘要盒 -->
    <div style="background:linear-gradient(135deg,{theme["gradient"]});border-left:4px solid {theme["border"]};border-radius:8px;padding:20px 24px;margin-bottom:32px">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px">
        <span style="background:{theme["badge"]};color:#fff;font-size:12px;font-weight:700;padding:2px 10px;border-radius:12px">速豹集運</span>
        <span style="background:{theme["badge"]};color:#fff;font-size:11px;font-weight:500;padding:2px 8px;border-radius:10px;opacity:0.85">✨ AI協助總結</span>
      </div>
      <p style="font-size:16px;line-height:1.8;margin:0;color:#333">
        {content}
      </p>
    </div>
'''


def find_insertion_point(lines):
    """找最佳插入点：在 <main class="article-content"> 或 <div class="article-content"> 之后，第一个非空内容标签之前"""
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        # 匹配主内容容器开始标签
        if re.search(r'<main\s+class="article-content"', line_stripped) or \
           re.search(r'<div\s+class="article-content"', line_stripped) or \
           re.search(r'<article\s+class="article-content"', line_stripped):
            # 找这个标签之后的第一个块级内容元素（p, div, h2, h3, table, ul, ol, blockquote）
            for j in range(i + 1, len(lines)):
                after = lines[j].strip()
                if after and re.match(r'<(p|div|h[1-6]|table|ul|ol|blockquote|hr)[>\s]', after):
                    return j, lines[j]
            # 如果没找到块级元素但在闭合标签之前，就插在容器开始标签后面
            return i + 1, lines[i + 1] if i + 1 < len(lines) else ""
    return None, None


def inject_box(filepath, config):
    """向单个文件插入 AI Summary Box"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 检查是否已有 AI 摘要盒
    if "<!-- AI摘要盒 -->" in content:
        print(f"  ⏭️  已存在，跳过: {os.path.basename(filepath)}")
        return False

    lines = content.split("\n")
    idx, first_elem = find_insertion_point(lines)

    if idx is None:
        print(f"  ❌ 未找到插入点: {os.path.basename(filepath)}")
        return False

    box_html = make_box(os.path.basename(filepath), config)

    # 在 idx 位置插入（插入在第一个内容元素之前）
    lines.insert(idx, box_html)

    new_content = "\n".join(lines)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"  ✅ 已插入 AI摘要盒[{config['theme']}] → {os.path.basename(filepath)}")
    return True


def main():
    print("🚀 批量插入 AI Summary Box 開始\n")
    changed = 0

    for filename, config in BOXES.items():
        filepath = os.path.join(BLOG_DIR, filename)
        if not os.path.exists(filepath):
            print(f"  ❌ 文件不存在: {filename}")
            continue
        if inject_box(filepath, config):
            changed += 1

    print(f"\n📊 完成：{changed}/{len(BOXES)} 個文件已插入 AI Summary Box")
    print("\n📋 主題顏色對照：")
    for name, theme in THEMES.items():
        print(f"   {name:8s} → 邊框 {theme['border']}")

if __name__ == "__main__":
    main()
