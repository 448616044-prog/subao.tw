# subao.tw 台湾站 YouTube 视频/链接完整清单

> 扫描日期：2026-08-19 | 数据源：本地源码 + 线上验证（HTTP 200 一致）
> 全站共 **13 个唯一视频**，分布在 6 个页面；另有 1 个无链接占位按钮（见文末注意事项）。

---

## 一、核心视频（3 个，用于 5 个页面）

| # | 视频 ID | 页面内名称（Schema） | 视频下方名称 | 链接 | 使用页面 |
|:---:|:---|:---|:---|:---|:---|
| 1 | `DEraXkkT2Fs` | 速豹倉庫實拍 1 | **貨物分類作業** | https://www.youtube.com/watch?v=DEraXkkT2Fs | about / tw-to-cn / pickup-service / bulk-shipping / daigou-service |
| 2 | `MlpXMKRhqNk` | 速豹倉庫實拍 2 | **包裹裝箱出貨** | https://www.youtube.com/watch?v=MlpXMKRhqNk | about / pickup-service / bulk-shipping / daigou-service |
| 3 | `Ara0yCCTc34` | 速豹倉庫實拍 3 | **包裹出貨前檢查** | https://www.youtube.com/watch?v=Ara0yCCTc34 | about / tw-to-cn / pickup-service / bulk-shipping / daigou-service |

> ⚠️ 特例：`tw-to-cn.html` 第 2 个视频用 **`gLbGftgU8ss`（客戶自行封箱）** 替代了 `MlpXMKRhqNk`（包裹裝箱出貨），Schema 名称仍写「速豹倉庫實拍 2」。

---

## 二、倉庫頁專用（warehouse.html，13 个视频全量）

| # | 视频 ID | 页面内名称（Schema） | 视频下方名称 | 链接 |
|:---:|:---|:---|:---|:---|
| 1 | `20_Cjw6iXDE` | 速豹倉庫實拍 1 | **包裝材料展示** | https://www.youtube.com/watch?v=20_Cjw6iXDE |
| 2 | `5O-ffvD9nKY` | 速豹倉庫實拍 2 | **倉庫包裝區** | https://www.youtube.com/watch?v=5O-ffvD9nKY |
| 3 | `64TfffE6yCY` | 速豹倉庫實拍 3 | **批量包裹整理** | https://www.youtube.com/watch?v=64TfffE6yCY |
| 4 | `AbLfBU1_rPc` | 速豹倉庫實拍 4 | **包裹整理中** | https://www.youtube.com/watch?v=AbLfBU1_rPc |
| 5 | `Ara0yCCTc34` | 速豹倉庫實拍 5 | **包裹出貨前檢查** | https://www.youtube.com/watch?v=Ara0yCCTc34 |
| 6 | `DEraXkkT2Fs` | 速豹倉庫實拍 6 | **貨物分類作業** | https://www.youtube.com/watch?v=DEraXkkT2Fs |
| 7 | `FZd2LrrZQbI` | 速豹倉庫實拍 7 | **貨物上架準備** | https://www.youtube.com/watch?v=FZd2LrrZQbI |
| 8 | `MlpXMKRhqNk` | 速豹倉庫實拍 8 | **包裹裝箱出貨** | https://www.youtube.com/watch?v=MlpXMKRhqNk |
| 9 | `QM6kUlckZaU` | 速豹倉庫實拍 9 | **貨物堆疊整理** | https://www.youtube.com/watch?v=QM6kUlckZaU |
| 10 | `W6YN6_0Jn3w` | 速豹倉庫實拍 10 | **倉庫貨物包裝** | https://www.youtube.com/watch?v=W6YN6_0Jn3w |
| 11 | `fa7A1AnfcuU` | 速豹倉庫實拍 11 | **貨物秤重作業** | https://www.youtube.com/watch?v=fa7A1AnfcuU |
| 12 | `gLbGftgU8ss` | 速豹倉庫實拍 12 | **封箱出貨** | https://www.youtube.com/watch?v=gLbGftgU8ss |
| 13 | `qasnknA6VCE` | 速豹倉庫實拍 13 | **倉庫作業日常** | https://www.youtube.com/watch?v=qasnknA6VCE |

---

## 三、视频在页面上的使用分布

| 页面 | 视频数 | 实际引用的视频 ID |
|:---|:---:|:---|
| about.html | 3 | DEraXkkT2Fs, MlpXMKRhqNk, Ara0yCCTc34 |
| tw-to-cn.html | 3 | DEraXkkT2Fs, **gLbGftgU8ss**, Ara0yCCTc34 |
| pickup-service.html | 3 | DEraXkkT2Fs, MlpXMKRhqNk, Ara0yCCTc34 |
| bulk-shipping.html | 3 | DEraXkkT2Fs, MlpXMKRhqNk, Ara0yCCTc34 |
| daigou-service.html | 3 | DEraXkkT2Fs, MlpXMKRhqNk, Ara0yCCTc34 |
| warehouse.html | 13 | 全部 13 个 |

---

## 四、⚠️ 发现的问题（2026-08-19 已修复）

1. ~~**contact-form.html 有 YouTube 按钮但无链接**~~ → ✅ **已修复**（commit 068a5d2d）：发现该页「🔗 社群媒體」区 4 个按钮（Facebook/Instagram/TikTok/YouTube）**全部是 href="#" 死链**，且全站无任何真实 FB/IG/TikTok/YT 频道外链。已将死链区改为 **LINE 官方帳號入口**（https://line.me/R/ti/p/@734dooky），既清除死链又强化唯一有效转化渠道。线上验证：0 死链残留。
2. ~~**tw-to-cn.html Schema 名称不一致**~~ → ✅ **已修复**：第 2 个视频 Schema name 改为「速豹倉庫實拍 2 — 客戶自行封箱」，与 iframe title 及内容对齐（与第 3 个「速豹倉庫實拍 3 — 出貨前檢查」命名风格统一），JSON-LD 全部有效。线上验证通过。
3. **无频道级链接**（维持现状）：全站未发现 youtube.com/@频道、/channel/、/shorts/ 等链接，13 个视频均为单条 watch/embed 链接。若速豹开通官方 YouTube 频道，可后续补充。

---

## 五、可复用链接速查（视频 ID → 链接）

```
速豹倉庫實拍 1  (貨物分類作業)  https://www.youtube.com/watch?v=DEraXkkT2Fs
速豹倉庫實拍 2  (包裹裝箱出貨)  https://www.youtube.com/watch?v=MlpXMKRhqNk
速豹倉庫實拍 3  (包裹出貨前檢查) https://www.youtube.com/watch?v=Ara0yCCTc34
客戶自行封箱                     https://www.youtube.com/watch?v=gLbGftgU8ss
包裝材料展示                     https://www.youtube.com/watch?v=20_Cjw6iXDE
倉庫包裝區                       https://www.youtube.com/watch?v=5O-ffvD9nKY
批量包裹整理                     https://www.youtube.com/watch?v=64TfffE6yCY
包裹整理中                       https://www.youtube.com/watch?v=AbLfBU1_rPc
貨物上架準備                     https://www.youtube.com/watch?v=FZd2LrrZQbI
貨物堆疊整理                     https://www.youtube.com/watch?v=QM6kUlckZaU
倉庫貨物包裝                     https://www.youtube.com/watch?v=W6YN6_0Jn3w
貨物秤重作業                     https://www.youtube.com/watch?v=fa7A1AnfcuU
倉庫作業日常                     https://www.youtube.com/watch?v=qasnknA6VCE
```
