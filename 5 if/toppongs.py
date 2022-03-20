# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月08日
"""
requested_toppings = ['mushronns', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinishedmaking your pizza!")
# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")
