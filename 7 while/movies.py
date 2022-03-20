# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月16日
"""
movies = input("How are you age?")
movies = int(movies)

while True:
    if movies < 3:
        print("you don't pay")
    elif movies < 12:
        print("you need 10")
    else:
        print("you need 15")
    continue