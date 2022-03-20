# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月07日
"""
my_foods = ['pizza', 'flafel', 'carrot',  'cake']
firend_foods = my_foods[:]

my_foods.append('cannili')
firend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\n My firend's favorite foods are:")
print(firend_foods)

print("The first three items in the list are:")
print(my_foods[:3])
print(my_foods[1:3])
print(my_foods[-3:])