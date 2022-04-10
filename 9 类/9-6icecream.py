# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月08日
"""


class Resturant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_severd = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")


class IceCreamStand(Resturant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['apple', 'bnana', 'origin']

    def read_flavors(self):
        for i in self.flavors:
            print(i)


my_ice = IceCreamStand('i ice you', 'ice cream')
my_ice.describe_restaurant()
my_ice.read_flavors()
