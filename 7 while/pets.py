# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月16日
"""
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)