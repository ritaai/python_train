# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月17日
"""
def city_country(city, country):
    full = f"{city.title()}, {country.title()}"
    return full

city1 = city_country('beijjing', 'china')
city2 = city_country('santiago', 'chile')
city3 = city_country('ostylie', 'sffg')
print(city1)
print(city2)
print(city3)



