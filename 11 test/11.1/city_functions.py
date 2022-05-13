# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月17日
"""


def city_country(city, country, population=0):
    full = f"{city.title()}, {country.title()}"
    if population:
        full += f" - population {population}"
    return full


