# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月14日
"""
import json

username = input("What is your name?")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remebmber you when you come back, {username}")