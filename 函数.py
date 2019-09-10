import pizza


# 定义函数
def great_user():
    print("hello!")


great_user()


# 关键字实参
def describe_pet(animal_type, pet_name):
    print("I have a "+animal_type+'.')
    print("my "+animal_type+"'s name is "+pet_name+'.')


describe_pet(pet_name='harry', animal_type='hamster')
print()


# 返回值
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
print()


# 让实参变成可选的
def get_formatted_name2(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name2('join', 'lee', 'snow')
print(musician)


def get_formatted_name3(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name3('Zhang', 'Xiangyang')
print(musician)
musician = get_formatted_name3('Zhang', 'Yang', 'Xiang')
print(musician)
print()


# # 结合使用函数和while循环
# def get_full_name():
#     while True:
#         print("Please tell me your name(input 'q' to quit):")
#         first_name = input("first name:")
#         if first_name == 'q':
#             break
#         last_name = input("last name:")
#         if last_name == 'q':
#             break
#         print("hello,"+first_name + ' ' + last_name + '\n')
#
#
# get_full_name()
# print()


# 传递列表
def greet_users(names):
    for name in names:
        print("hello," + name + '.')


names = ["Zhang", "Wang", "Li"]
greet_users(names)
print()


# 在函数中修改列表
def print_models(unprinted_designs, finished_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("printing:"+current_design)
        finished_models.append(current_design)
    print()
    print("The models we have printed as follows:")
    for finished_model in finished_models:
        print(finished_model)


unprinted_designs = ['Big Data', 'ML', 'Computer']
finished_models = []
print_models(unprinted_designs, finished_models)
print()
# 注意：在函数体内会永久改变列表的值
print(unprinted_designs)
print(finished_models)
print()

# 禁止函数修改列表
unprinted_designs = ['Big Data', 'ML', 'Computer']
finished_models = []
print_models(unprinted_designs[:],finished_models[:])
print()
# 此次未改变列表的值
print(unprinted_designs)
print(finished_models)
print()


# 传递任意数量的实参
def make_pizza(*toppings):
    for topping in toppings:
        print(topping)


make_pizza('pepperoni')
print()
make_pizza('mushroom', 'onion')
print()


# 结合使用位置实参和任意数量实参(注：必须将接纳任意数量实参的形参放在最后)
def make_pizza2(size, *toppings):
    print("Make a "+str(size)+"-inch pizza with the following toppings:")
    for my_topping in toppings:
        print(my_topping)


toppings = ['french fries', 'mushroom', 'peanut']
make_pizza2(10, toppings)
print()


# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
print()

# 将函数存储在模块中
pizza.make_pizza3(20, 'mushroom', 'green peppers')
print()
