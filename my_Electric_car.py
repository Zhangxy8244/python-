from car import ElectricCar

my_new_electric_car = ElectricCar('tesla', 'model s', 2019)
my_new_electric_car.modify_odometer(200)
print(my_new_electric_car.get_description_name())
my_new_electric_car.read_odometer()
