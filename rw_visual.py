import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw=RandomWalk()
    rw.fill_walk()

    #设置绘图窗口的尺寸
    plt.figure(figsize=(10,6))
    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,s=15)
    #突出起点和终点
    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

    #隐藏坐标轴
    #todo:
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    # plt.axis('off')
    # ax = plt.gca()
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running=input("Mask another walk?(y/n):")
    if keep_running=='n':
        break