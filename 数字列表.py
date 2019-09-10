# range函数：1-4依次打印出来
for value in range(1, 5):
    print(value)

# 使用range()创建数字列表
numbers = list(range(1, 5))
print(numbers)

# 使用range()函数还可以指定步长
numbers = list(range(1, 11, 2))
print(numbers)

# 将前十个整数的平方加入到一个列表
squares = []
for value in range(1, 10):
    square = value**2
    squares.append(square)
    # squares.append(value**2) 此段代码也可直接将得到的值附加到列表末尾
print(squares)

# 对数字列表进行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 求最小值
print(min(digits))
# 求最大值
print(max(digits))
# 求和
print(sum(digits))

# 列表解析：只需编写一行代码即可生成一个上述数字列表
new_squares = [value**2 for value in range(1, 10)]
print(new_squares)

