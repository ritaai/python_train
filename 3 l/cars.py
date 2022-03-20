# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月07日
"""

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("Here is the sorted list")
print(sorted(cars))

print("Here is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

tours = ['重庆', '大理', '西安', '杭州', '三亚']
print(sorted(tours))
print(sorted(tours, reverse=True))
tours.reverse()
print(tours)
tours.reverse()
print(tours)
tours.sort()
print(tours)
tours.sort(reverse=True)
print(tours)