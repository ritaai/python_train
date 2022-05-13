# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月14日
"""
import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")