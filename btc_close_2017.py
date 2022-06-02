import json
import pygal
from matplotlib import pyplot as plt

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



line_chart = pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
#x_label_rotation:让标签旋转20°，show_minor_x_labels：不用显示所有的x轴标签
line_chart.title='收盘价（¥）'
line_chart.x_labels=dates
N=20 #x坐标轴每隔20天显示一次
line_chart.x_labels_major = dates[::N] #列表的切片写法，每第N个序列项目
line_chart.add('收盘价',closes)
line_chart.render_to_file('收盘价折线图（¥）.svg')


