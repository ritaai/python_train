# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月14日
"""
import json


# love_num = input("please input your love num")
# filename = 'lovenum.json'
# with open(filename, 'w') as f:
#     json.dump(love_num, f)

filename = 'lovenum.json'

try:
    with open(filename) as f:
        loves = json.load(f)
except FileNotFoundError:
    love_num = input("please input your love num")
    with open(filename, 'w') as f:
        json.dump(love_num, f)
else:
    print(f"i know your favorite number! it's{loves}")