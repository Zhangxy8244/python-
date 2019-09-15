import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

# 绘制简单折线图
# plt.plot(squares)
# 改变线条粗细

# plt.plot(squares, linewidth=5)
# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

# 矫正图案
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

plt.show()
