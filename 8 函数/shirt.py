# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月17日
"""


def make_shirt(shirt_xxl, shirt_xyz='I love Python'):
    print(f"this shirt is {shirt_xxl} and {shirt_xyz}")


make_shirt('xl', 'yy')
make_shirt('xll')
make_shirt('s')


def describe_city(city, country):
    print(f"{city.title()} is in {country.title()}")


describe_city('reykjavik', 'iceland')
