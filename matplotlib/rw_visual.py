import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态，就不断的模拟随机漫步
while True:
    #创建一个RandomWalk的实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()
    
    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))

    #给点着色
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers, cmap = plt.cm.Blues, edgecolors= 'none',s = 1)

    # plt.scatter(rw.x_values, rw.y_values, s = 15)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors= 'none', s = 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s = 100)

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    break
    # keep_runnig = input("Make another walk? (y/n):")
    # if keep_runnig == 'n':
    #     break