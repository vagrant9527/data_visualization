import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取日期、最高气温、最低气温
# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # 为了更清楚的显示第一行数据的内容，可以用如下for循环进行读取显示。
    # 显示结果发现，第0列和第1列存储了日期和最高气温，为了研究这些数据，我们将处理这个csv中的每行数据，并提取其中索引值为0和为1的值
    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,"missing date")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # 阅读器将从停留的地方继续往下读csv文件，由于已经读取了头行，因此将从第二行开始
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')  # 在同一个窗口中添加一个折线图
# plt.fill_between接受一个x值和一个y值，它用来填充两个y值之间的区域
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.5)

# 设置图形格式
# plt.title("Daily high and low temperatures - 2014", fontsize=24)
title="Daily high and low temperatures - 2014\nDeath Valley,CA"
plt.title(title,fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # 绘制斜的日期标签，避免重叠
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
