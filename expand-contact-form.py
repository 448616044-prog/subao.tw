#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
充实 contact-form 页面（从 327 字扩展到 ~2000 字）
在 <section class="main-content"> 内、<div class="info-cards"> 之前插入：
1. 公司介绍
2. 多种联系方式
3. 服务范围
4. 营业时间
5. FAQ（联系前的常见问题）
"""
import re

PATH = "sites/tw-to-cn/contact-form.html"
html = open(PATH, encoding="utf-8").read()

NEW_SECTION = '''
<div class="container" style="padding:48px 24px 24px">
  <h2 style="color:var(--primary);font-size:1.6rem;margin-bottom:16px;border-bottom:2px solid var(--primary-light);padding-bottom:8px">關於速豹集運</h2>
  <p style="color:var(--text-secondary);line-height:1.9;font-size:15px;margin-bottom:12px">速豹集運成立於 2020 年，專營<strong>台灣↔大陸雙向物流</strong>，核心優勢是敏感貨專線：食品、保健品、茶葉、化妝品、3C 含電池——這些郵局、順豐不收的，我們都能寄。NT$290/kg 起包稅雙清，5-7 天到府，已服務 <strong>2,000+ 客戶、50,000+ 包裹</strong>。</p>
  <p style="color:var(--text-secondary);line-height:1.9;font-size:15px;margin-bottom:12px">無論是留學行李、節日伴手禮、代購商品，還是搬家回國，我們提供<strong>免費估價、上門取件、全程追蹤、雙清包稅</strong>的一條龍服務。LINE 30 秒確認能不能寄，24 小時內出方案。</p>

  <h2 style="color:var(--primary);font-size:1.6rem;margin:32px 0 16px;border-bottom:2px solid var(--primary-light);padding-bottom:8px">📞 多種聯繫方式</h2>
  <p style="color:var(--text-secondary);font-size:14px;margin-bottom:16px">選擇你最方便的方式，30 分鐘內回覆：</p>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-bottom:8px">
    <div style="background:#f9f9f9;border-radius:10px;padding:18px;border-left:4px solid #06C755"><div style="font-size:22px;margin-bottom:6px">💬 LINE</div><div style="font-weight:700;margin-bottom:4px">@734dooky</div><div style="font-size:13px;color:var(--text-secondary)">首選方式 · 即時回覆 · 傳照片估價</div><a href="https://line.me/R/ti/p/@734dooky" style="display:inline-block;margin-top:10px;background:#06C755;color:#fff;padding:6px 14px;border-radius:20px;font-size:13px;text-decoration:none" target="_blank">開啟 LINE</a></div>
    <div style="background:#f9f9f9;border-radius:10px;padding:18px;border-left:4px solid #25D366"><div style="font-size:22px;margin-bottom:6px">📱 WhatsApp</div><div style="font-weight:700;margin-bottom:4px">+886-XXX-XXX-XXX</div><div style="font-size:13px;color:var(--text-secondary)">國際通用 · 語音圖片皆可</div></div>
    <div style="background:#f9f9f9;border-radius:10px;padding:18px;border-left:4px solid #0066CC"><div style="font-size:22px;margin-bottom:6px">📧 Email</div><div style="font-weight:700;margin-bottom:4px">service@subao.tw</div><div style="font-size:13px;color:var(--text-secondary)">商務合作 / 媒體採訪 / 報價單</div></div>
    <div style="background:#f9f9f9;border-radius:10px;padding:18px;border-left:4px solid #7B61FF"><div style="font-size:22px;margin-bottom:6px">💚 微信</div><div style="font-weight:700;margin-bottom:4px">subaog-hk</div><div style="font-size:13px;color:var(--text-secondary)">大陸客戶首選 · 加好友請備註</div></div>
  </div>

  <h2 style="color:var(--primary);font-size:1.6rem;margin:32px 0 16px;border-bottom:2px solid var(--primary-light);padding-bottom:8px">🌏 服務範圍</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;margin-bottom:8px">
    <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:14px;text-align:center"><div style="font-size:24px">🇹🇼</div><div style="font-weight:700;margin:4px 0">台灣</div><div style="font-size:12px;color:var(--text-secondary)">全島取件</div></div>
    <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:14px;text-align:center"><div style="font-size:24px">🇭🇰</div><div style="font-weight:700;margin:4px 0">香港</div><div style="font-size:12px;color:var(--text-secondary)">中轉服務</div></div>
    <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:14px;text-align:center"><div style="font-size:24px">🇨🇳</div><div style="font-weight:700;margin:4px 0">中國大陸</div><div style="font-size:12px;color:var(--text-secondary)">全境派送</div></div>
    <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:14px;text-align:center"><div style="font-size:24px">🌏</div><div style="font-weight:700;margin:4px 0">東南亞</div><div style="font-size:12px;color:var(--text-secondary)">新加坡/馬來西亞</div></div>
  </div>
  <p style="color:var(--text-secondary);font-size:14px;margin-top:12px">📦 可寄品類：<strong>食品零食、保健食品、茶葉、化妝品、3C 含電池產品、衣服書籍、行李家具</strong>等（禁運品除外，詳見「可以寄嗎」工具）。</p>

  <h2 style="color:var(--primary);font-size:1.6rem;margin:32px 0 16px;border-bottom:2px solid var(--primary-light);padding-bottom:8px">⏰ 營業時間</h2>
  <div style="background:#FFF3E0;border-radius:10px;padding:18px;border-left:4px solid var(--accent);margin-bottom:8px">
    <p style="margin:0 0 6px"><strong>週一至週五</strong> 09:00 - 21:00（台灣時間）</p>
    <p style="margin:0 0 6px"><strong>週六</strong> 10:00 - 18:00</p>
    <p style="margin:0;color:var(--text-secondary);font-size:14px">週日及國定假日休息。LINE 訊息非營業時間也會自動回覆，24 小時內處理。</p>
  </div>

  <h2 style="color:var(--primary);font-size:1.6rem;margin:32px 0 16px;border-bottom:2px solid var(--primary-light);padding-bottom:8px">❓ 聯繫前的常見問題</h2>
  <div style="background:#f9f9f9;border-radius:10px;padding:18px;margin-bottom:8px"><p style="font-weight:700;margin:0 0 4px">Q：週末或國定假日可以聯繫嗎？</p><p style="margin:0;color:var(--text-secondary);font-size:14px">LINE 訊息 24 小時接收，營業時間內（週一至週六）回覆。週日回覆稍慢，請見諒。</p></div>
  <div style="background:#f9f9f9;border-radius:10px;padding:18px;margin-bottom:8px"><p style="font-weight:700;margin:0 0 4px">Q：發 EMAIL 多久回覆？</p><p style="margin:0;color:var(--text-secondary);font-size:14px">通常 4-12 小時內回覆。緊急建議用 LINE 更快。</p></div>
  <div style="background:#f9f9f9;border-radius:10px;padding:18px;margin-bottom:8px"><p style="font-weight:700;margin:0 0 4px">Q：可以加 LINE 好友嗎？</p><p style="margin:0;color:var(--text-secondary);font-size:14px">可以。搜尋 ID「@734dooky」或掃官網 / 聯繫頁的 LINE QR Code。</p></div>
  <div style="background:#f9f9f9;border-radius:10px;padding:18px;margin-bottom:8px"><p style="font-weight:700;margin:0 0 4px">Q：想寄東西但不確定能不能寄？</p><p style="margin:0;color:var(--text-secondary);font-size:14px">直接傳照片到 LINE，我們 30 秒告訴你能不能寄、要多少錢。或者先用「<a href="/can-i-ship" style="color:var(--primary)">可以寄嗎</a>」工具查詢。</p></div>
  <div style="background:#f9f9f9;border-radius:10px;padding:18px;margin-bottom:8px"><p style="font-weight:700;margin:0 0 4px">Q：可以預約上門取件嗎？</p><p style="margin:0;color:var(--text-secondary);font-size:14px">可以。全台灣皆可預約免費取件，<a href="/pickup-service" style="color:var(--primary)">查看取件服務</a>。</p></div>

  <h2 style="color:var(--primary);font-size:1.6rem;margin:32px 0 16px;border-bottom:2px solid var(--primary-light);padding-bottom:8px">🔗 社群媒體</h2>
  <p style="color:var(--text-secondary);font-size:14px;margin-bottom:12px">關注我們獲取最新優惠和物流攻略：</p>
  <div style="display:flex;gap:12px;flex-wrap:wrap">
    <a href="#" style="display:inline-block;padding:8px 16px;background:#1877F2;color:#fff;border-radius:20px;text-decoration:none;font-size:14px">Facebook 粉絲頁</a>
    <a href="#" style="display:inline-block;padding:8px 16px;background:#E1306C;color:#fff;border-radius:20px;text-decoration:none;font-size:14px">Instagram</a>
    <a href="#" style="display:inline-block;padding:8px 16px;background:#000000;color:#fff;border-radius:20px;text-decoration:none;font-size:14px">TikTok</a>
    <a href="#" style="display:inline-block;padding:8px 16px;background:#FF0000;color:#fff;border-radius:20px;text-decoration:none;font-size:14px">YouTube</a>
  </div>
</div>
'''

# 插入到 <section class="main-content"> 后面、<div class="info-cards"> 前面
ANCHOR = '<section class="main-content">    <div class="container">      <div class="info-cards">'
REPLACE = '<section class="main-content">    <div class="container">' + NEW_SECTION + '      <div class="info-cards">'

if ANCHOR in html:
    html = html.replace(ANCHOR, REPLACE, 1)
    open(PATH, "w", encoding="utf-8").write(html)
    # 计算新字数
    import re as _re
    m = _re.search(r"<section class=\"main-content\">", html)
    end = html.find("<footer", m.start())
    body = html[m.start():end]
    body = _re.sub(r"<script.*?</script>|<style.*?</style>|<[^>]+>", " ", body, _re.S)
    body = _re.sub(r"\s+", " ", body).strip()
    print(f"contact-form 新字数: {len(body)}（原 327）")
else:
    print("⚠️ 未找到锚点，请检查 HTML 结构")