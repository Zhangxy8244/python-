# 一个简单的字典,字典alien_0存储了外星人的颜色和点数
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print()

# 添加键值对(注意：字典中的键值对不分先后顺序)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print()

# 修改字典中的值
print("this alien's color is "+alien_0['color'])
alien_0['color'] = 'blue'
print("this alien's color is now "+alien_0['color'])
print()

# 删除键值对(注意：删除的键值对永久消失)
print(alien_0)
del alien_0['points']
print(alien_0)
print()

'''
上述字典存储的是一个对象的多种信息，但是也可以使用字典存储众多对象的同一种信息
'''
favorite_language = {
    'Zhang': 'python',
    'Wang': 'C',
    'Li': 'ruby',
    'Zhao': 'python'
}
print(favorite_language)
print("Zhang's favorite language is " +
      favorite_language['Zhang'] +
      '.')
print()

# 遍历字典
# 遍历所有的键值对
user_0 = {
    'username': 'Zxy',
    'first': 'Xiangyang',
    'last': 'Zhang'
}
for key, value in user_0.items():
    print('Key:'+key)
    print('Value:'+value)
    print()

# 优化显示键值对
for name, language in favorite_language.items():
    print(name.title()+"'s favorite language is "+language.title()+'.')
print()

# 遍历字典中的所有键
for name in favorite_language.keys():
    print(name.title())
print()

# 遍历字典中的键的应用
friends = ['Zhang', 'Wang']
for name in favorite_language.keys():
    print(name)
    if name in friends:
        print(name+"'s favorite language is "+favorite_language[name]+".")
print()

# 方法keys()可以返回一个列表，因此可以核实字典中是否含有某个键
if 'Yang' not in favorite_language.keys():
    print("Yang,please take our pool")
print()

# 按顺序遍历字典中的所有键
for name in sorted(favorite_language.keys()):
    print(name)
print()

# 遍历字典中的所有值
print("The following languages are mentioned:")
print()
print("before:")
for language in favorite_language.values():
    print(language)
print()
# 由于列表中可能包含重复的值，为剔除重复项，可使用集合(set)
print("after:")
for language in set(favorite_language.values()):
    print(language)
print()

# 嵌套
#   字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'blue', 'points': 6}
alien_2 = {'color': 'yellow', 'points': 7}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print()
#   使用range()函数生成30个外星人
for alien_number in range(30):
    new_alien = {'color': 'white', 'points': 5}
    aliens.append(new_alien)
for alien in aliens[3:8]:
    print(alien)
print('...')
print('The total number of aliens:'+str(len(aliens)))
print()

# 在字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print("You ordered a "+pizza['crust']+"-crust pizza"+"with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)
print()

favorite_languages = {
    'Sam': ['python', 'C'],
    'Anny': ['C++', 'Java'],
    'Bob': ['C#', 'Go']
}

for name, languages in favorite_languages.items():
    print(name.title()+"'s favorite languages are:")
    for language in languages:
        print("\t"+language)
print()

# 在字典中嵌套字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mucurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}
for username, user_info in users.items():
    print("Username:"+username)
    fullname = user_info['first']+" "+user_info['last']
    location = user_info['location']
    print("\tFull name:"+fullname)
    print("\tLocation:"+location)
    print()
print()


