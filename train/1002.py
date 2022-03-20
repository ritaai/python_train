# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月19日
"""


def num(list_n, n):

    m = 0
    for i in n:
        i = int(i)
        m = m + i

    new_list =[]
    for i in str(m):
        new_list.append(list_n[int(i)])
    return " ".join(new_list)


list_n = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
n = input()
result = num(list_n, n)
print(result)
