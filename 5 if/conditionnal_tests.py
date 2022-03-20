# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月08日
"""
a = 'abc'
b = 'def'
print(a == b)
c = 'DEF'
print(b == c.lower())

print(3 == 3)
print(3 != 4)
print(3 > 2)
print(3 >= 3)

print(a == c.lower() or b == c.lower())
print(a == c.lower() and b == c.lower())
f = [3, 4, 5, 6, 6]
print(3 in f)
print(8 not in f)