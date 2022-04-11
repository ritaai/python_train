# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月10日
"""
from car import ElectricCar
my_tesla = ElectricCar('tesla', 'models', 2020)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()