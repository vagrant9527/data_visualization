import csv
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row = next(reader)
    # 为了更清楚的显示第一行数据的内容，可以用如下for循环进行读取显示。
    #显示结果发现，第0列和第1列存储了日期和最高气温，为了研究这些数据，我们将处理这个csv中的每行数据，并提取其中索引值为0和为1的值
    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)

    highs=[]
    for row in reader:
        high=int(row[1])
        highs.append(high)
    #阅读器将从停留的地方继续往下读csv文件，由于已经读取了头行，因此将从第二行开始
fig =plt.figure(dpi=128,figsize=(10,6))
plt.plot(highs,c='red')
#设置图形格式
plt.title("Daily high temperatures, July 2014",fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()