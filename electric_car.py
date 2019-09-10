from car import Car


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
