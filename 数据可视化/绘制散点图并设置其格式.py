import matplotlib.pyplot as plt

# plt.scatter(2, 4)

# 添加标题，给轴加上标签
plt.scatter(2, 4, s=200)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
