import car
from electric_car import ElectricCar

my_car = car.Car('bwm', 'sl', 2019)
print(my_car.get_description_name())
my_car.read_odometer()
print()

my_electric_car = ElectricCar('tesla', 'model s',2019)
print(my_electric_car.get_description_name())
my_electric_car.read_odometer()
