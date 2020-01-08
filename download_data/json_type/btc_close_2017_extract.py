import json

# 数据加载到一个列表
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

#创建5个列表，分别存储日期和收盘价
dates, months, weeks, weekdays, close = [],[],[],[],[]

# 打印每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
    # print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))

import pygal

# line_chart = pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
# 折线图
# line_chart.title = '收盘价（￥）'
# line_chart.x_labels = dates
# N = 20 # x坐标轴每隔20天显示一次
# line_chart.x_label_major = dates[::N]
# line_chart.add('收盘价', close)
# line_chart.render_to_file('收盘价折线图（￥）.svg')
# 对数变换折线图（周期性假设，消除非线性趋势，使用对数变换--log_transformation，以10为底的对数函数math.log10计算收盘价，这种方式被称为半对数变换）
# import math

# line_chart.title = '收盘价对数变换（￥）'
# line_chart.x_labels = dates
# N = 20
# line_chart.x_label_major = dates[::N]
# close_log = [math.log10(_) for _ in close]
# line_chart.add('log收盘价', close_log)
# line_chart.render_to_file('收盘价对数变换折线图（￥）.svg')

# 均值
from itertools import groupby

# def draw_line(x_data, y_data, title, y_legend):
#     xy_map = []
#     for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
#         y_list = [v for _,v in y]
#         xy_map.append([x, sum(y_list) / len(y_list)])
#     x_unique, y_mean = [*zip(*xy_map)]
#     line_chart = pygal.Line()
#     line_chart.title = title
#     line_chart.x_labels = x_unique
#     line_chart.add(y_legend, y_mean)
#     line_chart.render_to_file(title + '.svg')
#     return line_chart

def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):  # 2
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])  # 3
    x_unique, y_mean = [*zip(*xy_map)]  # 4
    # 转换的x_unique和y_mean是一个集合，需要转成list,并且新坐标不知道为什么只能传入str类型
    x_unique = list(map(str,list(x_unique)))
    y_mean = list(y_mean)
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    # line_chart.render_to_file(title + '.svg')
    return line_chart


# idx_mouth = dates.index('2017-12-01')
# line_chart_mouth = draw_line(months[:idx_mouth], close[:idx_mouth], '收盘价月日均值（￥）', '月日均值')
# line_chart_mouth.render_to_file('收盘价月日均值（￥）.svg')

idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week], close[1:idx_week], '收盘价周日均值（￥）', '周日均值')
line_chart_week.render_to_file('收盘价周日均值（￥）.svg')

# idx_week = dates.index('2017-12-11')
# wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
# line_chart_weekday = draw_line(weekdays_int, close[1:idx_week], '收盘价星期均值（￥）', '星期均值')
# line_chart_weekday.x_labels = ['周一','周二', '周三', '周四', '周五', '周六', '周日']
# line_chart_weekday.render_to_file('收盘价星期均值（￥）.svg')