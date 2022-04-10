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
    def restanrant(self):
        print(f"Had {self.number_severd} come here for food.")
    def set_number_severd(self,num):
        self.number_severd = num
    def increment_number_severd(self, n):
        self.number_severd += n

restaurant = Resturant('wanjiahe', 'zhongcan')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_severd(30)
restaurant.restanrant()
restaurant.increment_number_severd(12)
restaurant.restanrant()