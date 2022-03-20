# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月19日
"""


def make_pizza(size, *toppings):
    """打印顾客点的所有配料"""
    print(f"\nMaking a {size}-inch pizza with the folling topping:")
    for topping in toppings:
        print(f"- {topping}")



