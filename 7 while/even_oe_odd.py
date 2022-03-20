# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月16日
"""
number = input("Enter a number, and i'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"th number {number} is odd.")