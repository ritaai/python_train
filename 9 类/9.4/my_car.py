# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月10日
"""
# from car import Car, ElectricCar
import car
from electric_car import ElectricCar as EC

# my_new_car = Car('audi', 'a4', 2019)
my_new_car = car.Car('audi', 'a4', 2019)

print(my_new_car.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'models', 2020)
my_tesla = EC('tesla', 'models', 2020)
print(my_tesla.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_doometer()
