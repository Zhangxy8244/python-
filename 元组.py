'''
创建一系列可以修改的元素可以使用列表，创建一系列不可变的列表可以使用元组
'''

# 创建一个大小不应改变的矩形，将长和宽存储在元组中
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# 下边的代码会报错,因为元组元素不可被改变
# dimensions[0] = 300
# 遍历元组元素
for dimension in dimensions:
    print(dimension)

# 修改元组变量：虽然不能修改元组的元素，但是可以给存储元组的变量赋值
print('原始元组：')
print(dimensions)
dimensions = (300, 100)
print('修改后的元组：')
print(dimensions)



