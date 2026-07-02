# subao.tw 全站移动端适配审计与修复 — 2026-07-02

## 修复前状态
- 129 HTML 页面
- 15 个页面存在移动端严重问题（无 @media 响应式 / 无移动导航）
- 1 个页面依赖外部 style.css（违反自包含规则）
- 104 个页面存在 hamburger 按钮但缺失点击事件 JS（按钮可见、点了没反应）

## 修复后状态
- 🔴 P0 致命问题：0
- 🟡 P1 体验问题：0
- 🔵 P2 优化建议：107 页（`overflow-x:hidden` 缺失，非关键）
- ✅ 豁免：3 页（404.html + widget/ × 2）

## 修复明细

### 批量修复（12 页 P0）
| 类型 | 数量 | 页面 | 修复内容 |
|:---|:---:|:---|:---|
| navbar 型（无 @media） | 7 | clothing-shoes, books-culture, post-office-rejected, post-office-vs-subao, post-office-vs-express, medical-supplies, baby-products | 添加完整移动端 CSS + menu-toggle + mobile-menu + JS |
| header 型（无 @media） | 3 | audio-equipment-repair, multi-parcel-consolidation, bamboo-agricultural | 添加 @media 规则 + mobile-menu + JS |
| header 型（最小 @media） | 1 | taiwan-snack-shipping | 替换为完整移动端 CSS + toggle + menu + JS |
| 外部 CSS 依赖 | 1 | line.html | 将 14 条缺失规则内联化，移除 style.css 引用 |

### 批量注入 mobile-menu div（36 页 P1）
含 toggle 按钮但缺少 mobile-menu div → hamburger 点击无效

### 批量修复缺少 toggle 按钮（15 页 P1）
navbar 型和 root 页面缺少 `id="menuToggle"` 的 HTML 元素

### 批量注入 menuToggle 点击事件 JS（104 页 P1）
大量"黄金页面"有完整的 HTML 结构但缺失 `menuToggle.addEventListener('click', ...)` 代码

### 文件恢复（3 页）
`tw-to-cn-prohibited-items` / `cosmetics-shipping` / `tea-shipping-guide` 在修复过程中被损坏（缺失 `</body>`），从 git 恢复后重新应用移动端修复

## 移动端标准模板（每页注入）

```
CSS: .menu-toggle + .mobile-menu + .m-dropdown + @media(992px/768px)
HTML: <button id="menuToggle"> + <div id="mobileMenu">
JS: menuToggle click → mobileMenu.classList.toggle('active')
```

## 备份
原文件备份：`/tmp/subao-mobile-backup/`（12 个文件）
Git 工作树：所有修改已就绪，待 commit + push
