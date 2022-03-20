# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月12日
"""
available_toppings = ['mushrooms', 'olives',  'green peppers', 'extra cheese',
                      'pineapple', 'pepperoni']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping} right now.")


print("\nAre you sure you want a plain pizza")