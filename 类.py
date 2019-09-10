# 创建Dog类
class Love:
    def __init__(self, name, age):
        self.name = name  # 以self为前缀的变量可供类中所有方法使用，我们还可以通过类的任何实例访问这些变量
        self.age = age

    def kiss(self):
        print(self.name.title() + " is now kissing me❤！")

    def hug(self):
        print(self.name + " gave me a big hug❤！")


# 根据类创建实例
my_love = Love('jinqinyuan', 23)
print("My love's name is "+my_love.name.title()+".")
my_love.kiss()
my_love.hug()
print()


# Car类
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_description_name(self):
        long_name = str(self.year)+" "+self.make+" "+self.model
        return long_name.title()


my_car = Car('audi', 'a8', 2019)
print(my_car.get_description_name())
print()


# 给属性指定默认值
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description_name(self):
        long_name = str(self.year)+" "+self.make+" "+self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")


my_car = Car('audi', 'a8', 2019)
print(my_car.get_description_name())
my_car.read_odometer()
print()

# 修改属性的值
#   直接修改属性的值
my_car.odometer_reading = 100
my_car.read_odometer()
print()


#   通过方法修改属性的值
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description_name(self):
        long_name = str(self.year)+" "+self.make+" "+self.model
        return long_name.title()

    def modify_odometer(self, update_odometer):
        self.odometer_reading = update_odometer

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")


my_car = Car('audi', 'a9', 2020)
my_car.modify_odometer(200)
my_car.read_odometer()
print()


# 继承
class ElectricCar(Car):
    def __init__(self, make, model, year):
        # 初始化父类的属性
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_description_name())
my_tesla.read_odometer()
print()


# 给子类定义属性和方法
class ElectricCar(Car):
    def __init__(self, make, model, year):
        # 初始化父类的属性
        super().__init__(make, model, year)
        self.battery_size = 100

    def describe_battery(self):
        print("This electric car's battery is "+str(self.battery_size)+"-KWh.")


my_new_tesla = ElectricCar('tesla', 'model s', 2020)
my_new_tesla.describe_battery()
print()


# 重写父类的方法
#   若要重写父类的方法，只需要它的名字与父类方法同名即可，到时候调用的时候就会调用子类的方法，忽略父类方法
print()


# 将实例用作属性
class Battery:
    # 一次模拟电动汽车电瓶的简单尝试
    def __init__(self, battery_size=100):
        # 初始化电瓶的属性
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-KWh battery.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        # 初始化父类的属性
        super().__init__(make, model, year)
        # 将实例用作属性
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2020)
my_tesla.battery.describe_battery()
print()


# 导入类（见my_car.py）

#
