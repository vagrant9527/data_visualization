import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]
# matplotlib默认以蓝色点，黑色轮廓绘制
# edgecolors是将数据点的轮廓删除,在2.0.0版本中默认为none

# c可以设置颜色，既可以设置单个色彩c=‘red’，
# 也可以自定义c=(0,0,0.8),这里是一个元组，包含三个0~1之间的小数值，分别是红色、绿色和蓝色分量

# cmap是指颜色映射。颜色映射是一系列颜色，它们从起始颜色渐变到结束颜色。
# 将c设置成一个y值列表，并使用cmap告诉pyplot使用哪个颜色映射。
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# 设置图片标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记大小
# Change the appearance of ticks, tick labels, and gridlines.
# 更改刻度、刻度标签和网格线的外观。
# axis:x,y,both.含义：将参数应用到哪个轴，默认时both
# which：major, minor, both.含义：将参数应用到哪个刻度，主刻度线、副刻度线还是二者都是。默认是major
plt.tick_params(axis="both", which='minor', labelsize=44)

# 设置每个坐标轴的取值范围
# 这里提供的四个值是x和y坐标轴的最小值和最大值
plt.axis([0, 1100, 0, 1100000])

# plt.show()
# 保存图表。第一个参数是保存下来的名字，第二个参数指定将图表多余的空白区域裁剪掉
# 如果有plot.show()在就保存不到东西
plt.savefig('squares_plot.png', bbox_inches='tight')
