import json

# 读取整个文件
with open('pi_digits') as file_object:
    contents = file_object.read()
    print(contents)
print()

# 文件路径
with open('text_files/test') as file_object:
    contents = file_object.read()
    print(contents)
print()

# 逐行读取
filename = 'pi_digits'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
print()

# 创建一个包含文件各行内容的列表
with open(filename) as file_object:
    # readlines()从文件中读取每一行，并将其存储在一个列表中
    lines = file_object.readlines()
print(lines)
for line in lines:
    print(line.rstrip())
print()

# 使用文件的内容
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))
print()

# 由于上述pi_string包含位于每行左边的空格，下边使用strip()来消除
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))
print()


# 写入文件
#   写入空文件
'''
注意：1.python只能将字符串写入文本文件。要将数值写入，必须先使用函数str()将其转换为字符串格式
　　　2.若文件已存在，则写入之后会覆盖之前的文本
'''
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
print()

#   附加到文件
'''
如果要给文件添加内容，而不是覆盖原有内容，可以附加模式打开文件
'''
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in datasets.\n")
print()

# 异常

'''
每当发生让python不知所措的错误时，它都会创建一个异常对象。若你编写了处理该异常的代码，程序将继续运行；否则程序将停止，
并显示一个traceback，包含有关异常报告
'''

# 处理ZeroDivisionError异常(除0异常)
#   使用try-except代码块
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")
print()

# # 使用异常来避免崩溃
# #   try-except-else代码块
# print("Give me two numbers,and I'll divide them.")
# print("Enter 'q' to quit")
# while True:
#     first_num = input("First number:")
#     if first_num == 'q':
#         break
#     second_num = input("Second number:")
#     if second_num == 'q':
#         break
#     try:
#         answer = int(first_num)/int(second_num)
#     except ZeroDivisionError:
#         print("You can't divide by zero")
#     else:
#         # 如果除法运算成功，我们就用else代码块来打印结果
#         print(answer)

# 处理FileNotFoundError异常
filename = 'Alice.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry,We can't find a file named "+filename
    print(msg)
print()


# 可以将这段代码写成以一个函数，调用起来会很方便
def judge(filename):
    try:
        with open(filename) as f_obj:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry,We can't find a file named " + filename
        print(msg)


judge('manage.txt')
print()


# 失败时一声不吭
def judge(filename):
    try:
        with open(filename) as f_obj:
            contents = file_object.read()
    except FileNotFoundError:
        # pass还充当了占位符，它提醒你在程序的某个地方什么都没有做，并且以后要在这里做些什么
        pass


judge('manage.txt')
print()

# 存储数据▲▲
numbers = [1, 2, 3, 4, 5]
filename = 'numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)

# 读取数据▲▲
with open(filename) as file_object:
    r_numbers = json.load(file_object)
print(r_numbers)
print()

# 保存和读取用户生成的数据
username = input("What's your name?")
filename = 'username.json'
with open(filename,  'w') as file_object:
    json.dump(username, file_object)
    print("We'll remember your name when you back,"+username+"!")
print()

with open(filename) as file_object:
    username = json.load(file_object)
    print("Welcome back,"+username)
print()

# 重构(见重构remember_me.py)
