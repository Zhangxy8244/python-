# 函数input()工作原理,input()接受一个参数,即向用户显示的提示或说明
message = input("Tell me something,and I will repeat it back to you:")
print(message)
print()
# 编写清晰的程序
#   有时候提示可能超过一行，在此情况下，你可以将提示存储在一个变量之中
prompt = "If you tell us who are you,we can personalize the message you see."
prompt += "\nWhat is your first name?"
name = input(prompt)
print("\nHello,"+name+'.')
print()

# 使用int()来获取数值输入
age = input("How old are you?")
age = int(age)
print(age >= 18)
print()

# while循环
#   注：如果遇到无限循环，可按Ctrl+C
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
print()

# 在列表之间移动元素
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user:"+current_user)
    confirmed_users.append(current_user)
print()
print(unconfirmed_users)
print(confirmed_users)
print()

# 删除包含特定值的所有列表元素(若不用循环，则只能删除一个)
pets = ['cat', 'dog', 'cat', 'goldfish', 'rabbit']
while 'cat' in pets:
    pets.remove('cat')
print(pets)
print()

# 使用标志来结束循环
active = True
while active:
    message = input("Are you wanna to quit?")
    if message == 'yes':
        active = False

# 使用break退出循环
while True:
    message = input("Are you wanna to quit?")
    if message == 'yes':
        break
print()

# 使用continue结束本次循环
print()

# 使用while循环来处理列表和字典
