# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月14日
"""
import json

filename = 'lovenum.json'
with open(filename) as f:
    loves = json.load(f)
    print(f"i know your favorite number! it's{loves}")