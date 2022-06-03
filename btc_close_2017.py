import json
import pygal
from matplotlib import pyplot as plt
import math
from itertools import groupby

# 将数据加载到一个列表中
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

dates = []
months = []
weeks = []
weekdays = []
closes = []
# 打印每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    closes.append(int(float(btc_dict['close'])))
    # print("{} is month {} week {} ,{},the close price is {} RMB".format(date,month,week,weekday,close))

# line_chart = pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
# #x_label_rotation:让标签旋转20°，show_minor_x_labels：不用显示所有的x轴标签
# line_chart.title='收盘价（¥）'
# line_chart.x_labels=dates
# N=20 #x坐标轴每隔20天显示一次
# line_chart.x_labels_major = dates[::N] #列表的切片写法，每第N个序列项目
# line_chart.add('收盘价',closes)
# line_chart.render_to_file('收盘价折线图（¥）.svg')

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价对数变换（¥）'
line_chart.x_labels = dates
N = 20  # x坐标轴每隔20天显示一次
line_chart.x_labels_major = dates[::N]  # 列表的切片写法，每第N个序列项目
close_log = [math.log10(_) for _ in closes]
# 用对数变换剔除非线性趋势。结果发现在每个季度末有显著的周期性
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('收盘价对数变换折线图（¥）.svg')


def draw_line(x_data, y_data, title, y_lenged):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        # sorted() 函数对所有可迭代的对象进行排序操作.内建函数 sorted 方法返回的是一个新的 list.
        # 这里每给出排序方式，所以sorted根据第一个元素进行排序, 第一个元素相同则根据第二个元素排序
        # lambda:匿名函数
        # groupby分组函数：分组的依据由key决定, 而key则使用了lambda函数。 key具体函数的参数取自于可迭代对象中，
        # 指定可迭代对象中的一个元素进行排序. 也就是把可迭代对象sorted_object作为参数, 传递给lambda函数,
        # 然后进行分组, 分组的依据为第0号索引的元素。
        # groupby分组函数在使用时要注意先排序。
        y_list = [v for _, v in y]
        # 这里就是只取出了同一个月的收盘价进行计算。
        # _表示没有用到的值
        xy_map.append([x, sum(y_list) / len(y_list)])
        # 这里就是将月份和计算出来的均值组成了一个列表，加到了xy_map中
    x_unique, y_mean = [*zip(*xy_map)]
    # [*zip(*xy_map)], 逐层来看, *xy_map,  *号的作用就是把列表的[]
    # 去掉了，比如[(1, 1203), (2, 1340), (3, 1245)], 变成(1, 1203) (2, 1340) (3, 1245)，
    # 然后对这些元素进行一次zip()操作, 就会得到(1, 2, 3), (1203, 1340, 1245),
    # 但是由于此时的zip是迭代对象, 他的值不能直接取出, 所以需要再在前面加一个 * 号, 并且用[]
    # 将其包裹起来, 让两个多元元素分别作为列表的0号和1号元素赋给x_unique和y_mean.
    # 此时x_unique是月份数, y_mean是各月的收盘均值,

    # https://www.jianshu.com/p/3df2357b8812
    # https: // zhuanlan.zhihu.com / p / 128670021
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_lenged, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart


idx_mouth = dates.index('2017-12-01')
# index函数为返回列表的索引值.用于从列表中找出某个值第一个匹配项的索引位置.
line_chart_month = draw_line(months[:idx_mouth], closes[:idx_mouth], '收盘价月日均值（￥）', '月日均值')

idx_week=dates.index('2017-12-11')
line_chart_week=draw_line(weeks[1:idx_week],closes[1:idx_week],'收盘价周日均值（¥）','周日均值')

idx_week=dates.index('2017-12-11')
wd=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekdays_int=[wd.index(w)+1 for w in weekdays[1:idx_week]]
line_chart_weekday=draw_line(weekdays_int,closes[1:idx_week],'收盘价星期均值（¥）','星期均值')
line_chart_weekday.x_labels=['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line_chart_weekday.render_to_file('收盘价星期均值（¥）.svg')
#这段代码是为了将2017年的收盘价格按照周几来计算均值。如：全年周一的均值，全年周二的均值......
#weekday列表中存放的是周几的英文单词，为了方便，将它的内容替换为1~7的整数，也就是weekdays_int,
#函数draw_ine在处理数据时按周几的顺序排列，就会将周一放在列表的第一位，周日放在列表的第七位。
#图形生成后再将x轴的标签替换成中文


with open('收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write(
        '<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in [
        '收盘价折线图（¥）.svg', '收盘价对数变换折线图（¥）.svg', '收盘价月日均值（￥）.svg',
        '收盘价周日均值（¥）.svg', '收盘价星期均值（¥）.svg'
    ]:
        html_file.write(
            '    <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))  # 1
    html_file.write('</body></html>')


