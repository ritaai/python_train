# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月17日
"""
def make_album(name, album, cout = None):
    full = {'name': name, 'album': album}
    if cout:
        full['cout'] = cout
    return full

full1 = make_album('qzl', 'wrer',1)
full2 = make_album('qqaz', 'weerr', 2)
full3 = make_album('okm', 'qwrdf')

print(full1)
print(full2)
print(full3)

while True:
    print("if your enter 'q' quit!")
    f_name = input("input your name:")
    if f_name == 'q':
        break
    l_name = input("input zhuanjiming:")
    if l_name == 'q':
        break
    full = make_album(f_name, l_name)
    print(full)