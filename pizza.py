# 将函数存储在模块中
def make_pizza3(size, *toppings):
    print("--------此段代码导入模块--------")
    print("Making a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print(topping)
