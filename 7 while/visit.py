# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月16日
"""
dir = {}
active = True

while active:
    name = input("what are you name?")
    city = input("\nwhere are you city?")

    dir[name] = city
    res = input("you hai yao xie ma?")
    if res == 'no':
        active = False

for name, city in dir.items():
    print(f"{name} would like {city}.")