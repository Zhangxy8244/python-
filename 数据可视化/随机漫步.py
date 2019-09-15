import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建一个RandomWalk实例，并将包含的点都绘制出来
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))

    # 给点着色，渐变显示
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1)
    # plt.scatter(rw.x_values, rw.y_values, s=10)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=50)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
