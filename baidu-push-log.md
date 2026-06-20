# subaotw.cn 百度主动推送日志

> 每天5条URL，轮转式推送
> 
> API: data.zz.baidu.com
> Token: K4kVPs6NwjtWr4ij

## 2026-06-14 00:05
- **推送URL数**: 5
- **起点索引**: 0
- [0] https://www.subaotw.cn/
- [1] https://www.subaotw.cn/equipment/
- [2] https://www.subaotw.cn/tw-to-cn/
- [3] https://www.subaotw.cn/tw-to-cn/complete-guide
- [4] https://www.subaotw.cn/guide/
- **API返回**: `{'remain': 5, 'success': 5}`

## 2026-06-16 23:55
- **推送URL数**: 5（尝试）
- **起点索引**: 5
- [5] https://www.subaotw.cn/faq
- [6] https://www.subaotw.cn/pricing-calculator
- [7] https://www.subaotw.cn/volume-calculator
- [8] https://www.subaotw.cn/about
- [9] https://www.subaotw.cn/contact
- **API返回**: `{"error":400,"message":"over quota"}`
- **状态**: ⚠️ 配额已满，索引未推进

## 2026-06-17 23:55
- **推送URL数**: 5 ✅
- **起点索引**: 5（重试上轮因配额未推的URL）
- [5] https://www.subaotw.cn/faq
- [6] https://www.subaotw.cn/pricing-calculator
- [7] https://www.subaotw.cn/volume-calculator
- [8] https://www.subaotw.cn/about
- [9] https://www.subaotw.cn/contact
- **API返回**: `{"remain":5,"success":5}`
- **状态**: ✅ 全部推送成功


## 2026-06-18 23:59
- **推送URL数**: 5
- **起点索引**: 11
- [11] https://www.subaotw.cn/tw-to-cn
- [12] https://www.subaotw.cn/tw-to-cn/food-shipping
- [13] https://www.subaotw.cn/guide/equipment-export-process
- [14] https://www.subaotw.cn/equipment/cnc-export-taiwan
- [15] https://www.subaotw.cn/equipment/injection-molding
- **API返回**: `{'remain': 5, 'success': 5}`


## 2026-06-20 00:01
- **推送URL数**: 5
- **起点索引**: 17
- [17] https://www.subaotw.cn/equipment/cnc-export-taiwan
- [18] https://www.subaotw.cn/equipment/construction-machinery
- [19] https://www.subaotw.cn/equipment/food-processing
- [20] https://www.subaotw.cn/equipment/injection-molding
- [21] https://www.subaotw.cn/equipment/mechanical-parts
- **API返回**: `{'remain': 5, 'success': 5}`


## 2026-06-20 00:11 batch
- **推送URL数**: 5
- **起点索引**: 22
- [22] https://www.subaotw.cn/equipment/mining-equipment
- [23] https://www.subaotw.cn/equipment/mold-tooling
- [24] https://www.subaotw.cn/equipment/packaging-equipment
- [25] https://www.subaotw.cn/equipment/plastic-machinery
- [26] https://www.subaotw.cn/equipment/press-machine
- **API返回**: {"remain": 0, "success": 5}


## 2026-06-20 08:07 batch (继续)
- **推送**: 5
- **起点**: 22
- **返回**: {"error": 400, "message": "over quota"}
- [22] https://www.subaotw.cn/equipment/mining-equipment
- [23] https://www.subaotw.cn/equipment/mold-tooling
- [24] https://www.subaotw.cn/equipment/packaging-equipment
- [25] https://www.subaotw.cn/equipment/plastic-machinery
- [26] https://www.subaotw.cn/equipment/press-machine


## 06-20 auto
- **27**: 5 URLs
- **return**: {"error": 400, "message": "over quota"}
- https://www.subaotw.cn/equipment/printing-equipment
- https://www.subaotw.cn/equipment/textile-machinery
- https://www.subaotw.cn/equipment/woodworking
- https://www.subaotw.cn/faq
- https://www.subaotw.cn/furniture-shipping


## 2026-06-21 00:03
- **推送URL数**: 5
- **起点索引**: 27
- [27] https://www.subaotw.cn/equipment/mining-equipment.html
- [28] https://www.subaotw.cn/equipment/mold-tooling.html
- [29] https://www.subaotw.cn/equipment/ningbo-export-taiwan.html
- [30] https://www.subaotw.cn/equipment/packaging-equipment.html
- [31] https://www.subaotw.cn/equipment/plastic-machinery.html
- **API返回**: `{'remain': 5, 'success': 5}`
- **状态**: ✅ 推送成功

## next_start: 32
