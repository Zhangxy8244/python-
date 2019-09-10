# 列表切片
letters = ['a', 'b', 'c', 'd', 'e']
print(letters[0:3])
print(letters[1:])
print(letters[-1:])

# 遍历切片
for letter in letters[0:3]:
    print(letter)

# 复制列表
my_letters = ['x', 'y', 'z']
# 简单复制，样本只有一个
friend_letters = my_letters
my_letters.append('w')
print(my_letters)
print(friend_letters)
# 深度复制，样本有两个
friend_letters = my_letters[:]
my_letters.append('v')
friend_letters.append('u')
print(my_letters)
print(friend_letters)

