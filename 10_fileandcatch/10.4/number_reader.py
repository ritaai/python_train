# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月14日
"""
import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)