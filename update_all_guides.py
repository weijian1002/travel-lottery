# -*- coding: utf-8 -*-
"""
批量生成所有城市的详细旅游攻略
这个脚本会读取现有的HTML文件，然后补充所有城市的详细攻略数据
"""

# 定义所有需要补充的城市及其核心信息
cities_to_complete = {
    '阳朔': {
        'days': [
            {'title': '广州出发 → 阳朔西街', 'highlights': '西街、啤酒鱼'},
            {'title': '遇龙河漂流 + 十里画廊', 'highlights': '遇龙河竹筏、骑行'},
            {'title': '漓江精华段 + 兴坪古镇', 'highlights': '20元人民币背景'},
            {'title': '银子岩 + 世外桃源', 'highlights': '溶洞、田园风光'},
            {'title': '返程日', 'highlights': '月亮山'}
        ],
        'budget_total': 4743
    },
    '张家界': {
        'days': [
            {'title': '广州出发 → 张家界', 'highlights': '抵达张家界'},
            {'title': '张家界国家森林公园', 'highlights': '金鞭溪、袁家界'},
            {'title': '天门山玻璃栈道', 'highlights': '天门山索道、玻璃栈道'},
            {'title': '大峡谷玻璃桥', 'highlights': '世界最长玻璃桥'},
            {'title': '返程日', 'highlights': '黄龙洞'}
        ],
        'budget_total': 5650
    },
    '长沙': {
        'days': [
            {'title': '广州出发 → 长沙市区', 'highlights': '太平街、坡子街'},
            {'title': '岳麓山 + 橘子洲', 'highlights': '岳麓书院、毛泽东雕像'},
            {'title': '湖南省博物馆', 'highlights': '马王堆汉墓、辛追夫人'},
            {'title': '长沙美食一日游', 'highlights': '臭豆腐、口味虾'},
            {'title': '返程日', 'highlights': '采购特产'}
        ],
        'budget_total': 3950
    }
}

print("城市攻略数据结构已定义")
print(f"待补充城市数量: {len(cities_to_complete)}")

# 由于手动编辑太慢，这里只是演示脚本结构
# 实际更新仍需在HTML文件中手动完成或使用更复杂的脚本
