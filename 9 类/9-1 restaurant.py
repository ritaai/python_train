# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月19日
"""


class Resturant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")


restaurant = Resturant('wanjiahe', 'zhongcan')
restaurant2 = Resturant('basihixing', 'xican')
restaurant3 = Resturant('weiterui', 'facan')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
restaurant3.describe_restaurant()
restaurant3.open_restaurant()
