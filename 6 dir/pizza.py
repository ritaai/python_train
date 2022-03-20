# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月14日
"""
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print(f"You ordered a {pizza['crust']}-ceust pizza"
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\f"+topping)