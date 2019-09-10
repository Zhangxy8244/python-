letters = ['a', 'b', 'c', 'd']
print(letters)
letters.append('f')  # 在列表后插入字符
print(letters)
letters.insert(4, 'e')  # 在制定位置插入字符
print(letters)
del letters[-1]  # 删除指定位置字符
print(letters)
my_pop_letter = letters.pop()  # 出栈一个字符存入变量
print(letters)
print(my_pop_letter)
letters.remove("d")  # 根据值删除字符，一次只能删除第一个指定的值，若要全部删除，则要使用循环来解决
# letters.remove("d") 注：若指定值不在列表中，则会报错
print(letters)
del_value = 'c'
letters.remove(del_value)  # 也可以将指定值存入变量中删除
print(letters)
letters.pop(0)  # 弹出index为1的值
print(letters)

# 永久排序
cars = ['BMW', 'AUDI', 'TOYOTA', 'SUBARU']
cars.sort()  # 对列表从小到大永久排序
print(cars)
cars.sort(reverse=True)  # 对列表反向永久排序
print(cars)

# 临时排序
books = ['math', 'English', 'physics', 'chemical']
print(books)  # 原始序列
print(sorted(books))  # 临时从小到大排序
print(books)  # 临时序列
print(sorted(books, reverse=True))  # 临时从大到小排序
books.reverse()  # 永久反转列表中元素
print(books)
print(len(books))  # 打印出books列表的长度
