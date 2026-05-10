# TRAE网站实现提示词

直接复制下面的内容到TRAE，即可生成完整网站。

---

## 提示词

```
请帮我实现两个独立的两岸物流网站，要求如下：

## 品牌信息
- 品牌名：速豹集运（SUBAO EXPRESS）
- 业务：台灣↔大陸雙向物流（普通貨+敏感貨）
- 核心定位：專業兩岸物流服務商
- Slogan：兩岸物流，一站搞定

## 两个独立站点

### 站点A（台湾发大陆方向）
- 域名：subaotw.cn（已购）
- 语言：全站正体中文（臺灣/台灣繁體）
- 目标用户：台湾卖家/个人寄货到大陆

### 站点B（大陆发台湾方向）
- 域名：subao.tw（待购）
- 语言：全站简体中文
- 目标用户：大陆卖家/个人寄货到台湾

---

## 网站A（subaotw.cn）- 台湾发大陆

### 页面结构（4个页面）
1. index.html - 首页（台湾发大陆入口）
2. pricing.html - 运费报价
3. faq.html - 常见问题
4. about.html - 关于我们

### 设计规范
- 主色-蓝：#0066CC（信任蓝）
- 辅色-橙：#FF6600（行动橙）
- LINE绿：#00B900
- 背景：#FFFFFF / #F5F7FA
- 文字：#333333 / #666666
- 字体：Google Fonts Noto Sans TC / 备选 PingFang TC, Microsoft JhengHei
- 移动端优先 + 响应式设计
- 右下角悬浮LINE按钮

### 首页结构
1. Hero区域：蓝色渐变背景，品牌标语 + CTA按钮 + 运费计算器入口
2. 服务介绍：台湾发大陆专线（海快/空运/敏感货）
3. 四大优势：敏感货专线 | 价格实惠 | 时效稳定 | 一对一客服
4. 服务流程：4步骤图示（注册→预报→打包→发货）
5. 运费计算器：表单 + 结果展示
6. FAQ折叠区（5个问题）
7. CTA区域
8. Footer（含LINE/电话/邮箱）

---

## 网站B（subao.tw）- 大陆发台湾

### 页面结构（4个页面）
1. index.html - 首页（大陆发台湾入口）
2. pricing.html - 运费报价
3. faq.html - 常见问题
4. about.html - 关于我们

### 设计规范
- 主色-蓝：#0066CC（信任蓝）
- 辅色-橙：#FF6600（行动橙）
- 背景：#FFFFFF / #F5F7FA
- 文字：#333333 / #666666
- 字体：Google Fonts Noto Sans SC / 备选 PingFang SC, Microsoft YaHei
- 移动端优先 + 响应式设计
- 右下角悬浮客服按钮（微信/电话）

### 首页结构
1. Hero区域：蓝色渐变背景，品牌标语 + CTA按钮 + 运费计算器入口
2. 服务介绍：大陆发台湾专线（海运/空运/集运）
3. 四大优势：敏感货专线 | 价格实惠 | 时效稳定 | 一对一客服
4. 服务流程：4步骤图示
5. 运费计算器：表单 + 结果展示
6. FAQ折叠区（5个问题）
7. CTA区域
8. Footer（含微信/电话/邮箱）

---

## 交互功能（两站通用）
1. Header滚动时添加阴影
2. 手机端汉堡菜单
3. FAQ点击折叠/展开
4. 运费计算器：输入重量和物品类型，计算预估价格（价格是示例数据）
5. 滚动动画（fadeInUp）

## 技术要求
- 纯HTML + CSS + 原生JavaScript（无框架）
- 使用FontAwesome图标
- 每个站点独立完整

## 需要完成的文件

### 网站A（/Users/mac/WorkBuddy/Claw/物流項目/subao-tw/）
1. index.html - 首页
2. pricing.html - 运费报价
3. faq.html - 常见问题
4. about.html - 关于我们

### 网站B（/Users/mac/WorkBuddy/Claw/物流項目/subao-cn/）
1. index.html - 首页
2. pricing.html - 运费报价
3. faq.html - 常见问题
4. about.html - 关于我们

请帮我生成完整的两个网站代码！
```

---

## 快速修改说明

网站上线前需要修改的内容：

| 位置 | 修改内容 | 示例 |
|:---|:---|:---|
| Logo | 品牌名 | 已确认为"速豹集运"，需提供矢量文件 |
| LINE链接 | 所有"LINE連結" | 替换为真实LINE链接（仅TW站） |
| 微信二维码 | 右下角悬浮按钮（仅CN站） | 替换为真实微信二维码 |
| 电话 | Footer联系信息 | "XXX-XXXX-XXXX" |
| 邮箱 | Footer联系信息 | "info@xxx.com" |
| 运费价格 | 计算器JS | 根据实际价格表调整 |
| 公司信息 | About页面 | 统一编号、地址等 |

---

## 文件位置

```
/Users/mac/WorkBuddy/Claw/物流項目/
├── TRAE-網站實現提示詞.md   ← 本提示词
├── subaotw/                 ← 台湾发大陆站（繁体）
│   ├── index.html
│   ├── pricing.html
│   ├── faq.html
│   └── about.html
└── subao-tw/                ← 大陆发台湾站（简体）
    ├── index.html
    ├── pricing.html
    ├── faq.html
    └── about.html
```

---

## 域名对应关系

| 站点 | 域名 | 语言 | 方向 |
|:---|:---|:---:|:---|
| A | subaotw.cn | 正体中文 | 台湾→大陆 |
| B | subao.tw | 简体中文 | 大陆→台湾 |