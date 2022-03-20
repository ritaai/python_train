# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月14日
"""
car = input("What are you runt car?")
print(f"Let me see if i can find a {car.title()}")

number = input("How many people for dinner?")
number = int(number)
if number > 8:
    print("Sorry, we haven't zhuozi.")
else:
    print("OK!")

number = input("Please input a number:")
number = int(number)
if number % 10 == 0:
    print(f"{number} is 10 de zheng shu bei")
else:
    print(f"{number} is not 10 de zheng shu bei")