# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月19日
"""


def num(n=0, m=0):
    n = int(input())
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n + 1) / 2
        m = m + 1
    print(m)

num()
