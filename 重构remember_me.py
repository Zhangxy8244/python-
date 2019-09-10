import json

'''
代码能够正确运行，但可做进一步的改进——将代码划分为一系列完成具体工作的函数。这样的过程称为重构。
重构让代码更清晰、更易于理解、更容易扩展
'''


def greet_user():
    filename = 'my_username.json'
    try:
        with open(filename) as file_object:
            r_username = json.load(file_object)
    except FileNotFoundError:
        username = input("what's your name?")
        with open(filename, 'w') as file_object:
            json.dump(username, file_object)
            print("We'll remember you when you come back," + username)
    else:
        print("Welcome back," + r_username)


greet_user()
print()

'''
上述函数greet_user()所做的不仅仅是问候用户，还存储了用户名时获取它，而在没有存储用户名时提示用户输入一个。
下面来重构greet_user(),让他不执行那么多任务
'''


def get_stored_username():
    filename = 'my_username.json'
    try:
        with open(filename) as file_object:
            r_username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return r_username


def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back,"+username+"!")
    else:
        username = input("What's your name?")
        filename = 'username.json'
        with open(filename, 'w') as file_object:
            json.dump(username, file_object)
            print("We'll remember you when you come back,"+username)


greet_user()
print()


def get_new_username():
    username = input("What's your name?")
    filename = 'username.json'
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back,"+username+"!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back," + username)


greet_user()
print()
