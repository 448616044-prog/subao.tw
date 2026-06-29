# subao.tw LINE Login OAuth — 主動獲客方案

## 🎯 目標
用戶在網站點「LINE 授權聯繫」→ 自動成為 LINE OA 好友 + 你收到通知 → 客服立刻跟單

---

## 📐 技術架構

```
subao.tw (Cloudflare Pages)
  ├─ [LINE 授權聯繫] 按鈕（全站高流量頁面嵌入）
  │   └─ 點擊 → LINE OAuth 授權頁
  │
  ├─ Cloudflare Worker (/api/line-callback)
  │   └─ 接收 OAuth 回調 → 調 LINE API → 發郵件通知
  │
  └─ 郵件通知 → business@videotvai.com
      ├─ 標題：[速豹LEAD] {暱稱} - {來源頁面}
      └─ 內容：LINE User ID / 暱稱 / 頭像 / 時間 / 來源URL
```

---

## 👤 你需要做的事

### Step 1: 下載 LINE Official Account APP
- iOS: App Store 搜「LINE Official Account」
- Android: Google Play 搜「LINE Official Account」
- 用管理員帳號登入（已有 subaotw5988 的 OA）

### Step 2: 登入 LINE Developers 後台
- 網址：https://developers.line.biz
- 用**同一個 LINE 帳號**登入（必須是 OA 管理員）
- 左側選「Providers」→ 如果沒有，建一個（名稱：速豹集運）

### Step 3: 創建 LINE Login Channel
1. 在 Provider 下 → Create a new channel → 選 **LINE Login**
2. 填寫：
   - Channel name: `速豹集運 Login`
   - Channel description: `速豹集運官網 LINE 授權登入`
   - App types: 勾選 **Web app**
   - Email address: `business@videotvai.com`
   - Privacy policy URL: `https://subao.tw/about`
   - Terms of use URL: `https://subao.tw/about`
3. 創建後，進 Settings：
   - 記下 **Channel ID**（一串數字）和 **Channel secret**
   - **Callback URL**：先留空（等我 Cloudflare Worker 部署後補上）
   - 在「Linked OA」選項 → 選擇 `subaotw5988` 的 LINE OA → 勾選「自動加好友」

### Step 4: 給我的資訊
把以下三個值發給我：
- LINE Login Channel ID：`16xxxxxxx`
- LINE Login Channel Secret：`xxxxx`
- 確認已在後台連結 OA（subaotw5988）並開啟自動加好友

---

## 🤖 我會做的事

### 1. 部署 Cloudflare Worker
- 寫一個 ~50 行 JS Worker，處理 OAuth 回調
- 功能：
  - 接收 LINE OAuth callback（code → access_token → User ID + 暱稱 + 頭像）
  - 調 LINE API 獲取用戶資料
  - 發郵件通知到 business@videotvai.com（含 User ID、暱稱、來源頁）
  - 重定向用戶回 subao.tw 完成頁
- 部署到 Cloudflare Workers（免費方案，每日 10 萬次請求）

### 2. 製作前端 LINE 授權按鈕組件
- 一個可複用的 HTML 片段，嵌入到高流量頁面
- 包含：
  - LINE 綠色授權按鈕
  - 簡短說明文字
  - GA4 點擊事件追蹤 (`line_login_click`)
  - 自帶內聯 CSS，不依賴外部樣式表

### 3. 全站批量嵌入
- 嵌入目標頁面：food-shipping-guide、cosmetics-shipping、tea-shipping-guide、battery-products-shipping、首頁、pricing
- 每個頁面 H1 下方 + 文末 FAQ 區上方各放一個

### 4. 測試驗證
- 用測試 LINE 帳號完整走一遍授權流程
- 確認郵件通知送達
- 確認 OA 後台出現新好友

---

## 📊 預期效果

| 指標 | 預估 |
|------|:---:|
| 每 100 次瀏覽 → 點擊授權 | 3-5 次 |
| 每 100 次點擊 → 完成授權+加好友 | 85-95 次 |
| 每週新增可跟進客戶 | 15-25 人 |
| 客服主動跟進率 | 100%（不再被動等） |

---

## 🔗 相關連結
- LINE Developers: https://developers.line.biz
- LINE OA 管理後台: https://manager.line.biz
- Cloudflare Dashboard: https://dash.cloudflare.com
- subao.tw GitHub: https://github.com/448616044-prog/subao.tw
