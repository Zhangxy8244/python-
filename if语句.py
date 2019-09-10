# 判断元素是否在列表中
letters = ['a', 'b', 'c']
if 'c' in letters:
    print('true')

# 判断元素是否不在列表中
if 'd' not in letters:
    print('true')

'''
注意：在使用if-elif-else时候，由于else是一条包罗万象的语句，只要不满足if或者elif的条件测试，其中的代码可能引来无效甚至恶意的数
据，若知道最终要测试的条件，应该考虑使用elif代码块
'''

'''
if-elif-else结构，每次只能有一个测试通过，即只能有一个符合条件，若要测试多个条件，应该使用多个if语句 （P74）
'''

# 确定列表不是空的
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding '+requested_topping+'.')
    print('\nFinish your piezza!')
else:
    print('Are you sure you need a plain pizza?')

# 使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers']
requested_toppings = ['mushrooms', 'french fries']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding '+requested_topping+'.')
    else:
        print("Sorry,We don't have "+requested_topping+".")
print('Finished your pizza!')
