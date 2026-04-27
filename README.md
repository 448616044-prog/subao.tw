# subao.tw 台灣到大陸物流

靜態網站，部署於 Cloudflare Pages。

---

## 🚀 部署方式

### 方式一：Cloudflare Pages Git 集成（推薦）

1. 登入 [dash.cloudflare.com](https://dash.cloudflare.com) → **Pages** → **Create a project**
2. 選擇 **Connect to Git**
3. 授權 GitHub，選擇 `448616044-prog/subao.tw` 倉庫
4. 設定：
   - **Project name**: `subao-tw`
   - **Build command**: （留空，純靜態）
   - **Build output directory**: `/`（根目錄）
   - **Root directory**: `/`
5. 點擊 **Save and Deploy**

，以後 push 到 main 分支會自動部署

### 方式二：手動上傳

直接把 `台灣到大陸` 資料夾的內容上傳到 Cloudflare Pages。

---

## 📁 檔案結構

```
台灣到大陸/
├── index.html        # 首頁
├── tw-to-cn.html     # 台灣到大陸服務頁
├── pricing.html      # 運費查詢
├── about.html        # 關於我們
├── faq.html          # 常見問題
├── style.css         # 樣式
└── logo.png          # Logo
```

---

## 🌐 域名解析設定

1. Cloudflare Pages 部署完成後，複製部署 URL（如 `https://xxxx.pages.dev`）
2. 在 DNS 管理處新增 CNAME 記錄：
   - **Type**: CNAME
   - **Name**: `@`（或 `www`）
   - **Target**: `xxxx.pages.dev`
   - **Proxy status**: DNS only（先這樣，等 Cloudflare 自動切換）

---

## 🔄 更新網站

```bash
# 1. 修改代碼
# 2. 提交
git add .
git commit -m "更新說明"
git push origin main
# Cloudflare Pages 自動部署（約 1-2 分鐘）
```
