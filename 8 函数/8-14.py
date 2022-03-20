# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月19日
"""


def make_car(people, num, **info):
    info['people'] = people
    info['num'] = num
    return info


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
