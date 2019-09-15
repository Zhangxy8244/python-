import matplotlib.pyplot as plt

x_value = [1, 2, 3, 4, 5]
y_value = [1, 4, 9, 16, 25]

# 自动计算数据
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=6)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 自定义颜色
plt.scatter(x_values, y_values, c='red', s=6)
# 还可以使用RGB颜色模式自定义有颜色
plt.scatter(x_values, y_values, c=(0, 0, 0.8), s=8)
# 使用颜色映射（颜色渐变）
plt.scatter(x_values, y_values, c=y_values, s=8, cmap=plt.cm.Blues)
# 自动保存图表
plt.savefig("Squares_plot.png", bbox_inch='tight')  # 第二个实参指定将图表多余的空白区域剪掉
plt.show()
