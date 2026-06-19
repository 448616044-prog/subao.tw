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

## next_start: 16
