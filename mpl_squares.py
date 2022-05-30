import matplotlib.pyplot as plt

#使用plot绘制折现时默认是从0开始的，
#这里要从1开始绘制，因此可将输入作为参数一并传给plot
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values,squares, linewidth=5)

# 设置图片标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis="both", labelsize=14)

plt.show()
