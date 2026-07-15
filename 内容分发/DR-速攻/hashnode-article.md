# Hashnode — 速豹集運 技術部落格

## 部落格資訊
- 名稱：速豹集運 Subao Logistics
- 簡介：台灣↔中國大陸跨境物流服務商。撰寫跨境物流技術、清關策略、供應鏈優化內容。官網：https://subao.tw
- 自訂域名：subaotw.hashnode.dev

---

## 文章：How We Built a Cross-Strait Logistics System That Processes 2000+ Shipments

When you think about Taiwan-to-China logistics, you might picture a simple courier service. The reality is a complex system of customs clearance, category-based routing, and real-time tracking that we've spent 6 years building at Subao Logistics.

### The Technical Challenge

Taiwan and China have different customs systems, different prohibited items lists, and different inspection protocols. A package containing tea leaves goes through a completely different clearance pipeline than one containing cosmetics.

Our solution:

**1. Category-Based Routing Engine**
- 47 product categories mapped to specific customs clearance protocols
- Real-time prohibited items checker: [subao.tw/can-i-ship](https://subao.tw/can-i-ship)
- Automated HS code classification

**2. Volume Weight Optimization**
- Algorithm: max(actual_weight, L×W×H/6000)
- Free compression packing service
- Interactive calculator: [subao.tw/pricing-calculator](https://subao.tw/pricing-calculator)

**3. Full-Chain Tracking**
- Warehouse → Customs → Clearance → Last-mile delivery
- Each stage timestamped and queryable
- LINE real-time status push

### Key Metrics
- 6 years in operation
- 2000+ satisfied customers
- 3-7 day delivery for sensitive goods (food/cosmetics/tea)
- 0 customs seizure rate with proper documentation

### Learn More
- Official website: [https://subao.tw](https://subao.tw)
- LINE support: [@734dooky](https://line.me/R/ti/p/@734dooky)

---

*Tags: #logistics #cross-strait #supply-chain #customs #taiwan #china*
