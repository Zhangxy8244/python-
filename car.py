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
