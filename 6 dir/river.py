# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月14日
"""
rivers = {
    'nile': 'egypt',
    'yellow river': 'china',
    'changjiang': 'china',
}
for keys, value in rivers.items():
    print(f"The {keys.title()} runs through {value.title()}")
for keys in rivers.keys():
    print(keys)
for value in set(rivers.values()):
    print(value)