# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月14日
"""
cities = {
    'piking': {
        'country': 'china',
        'population': '500million',
        'fact': 'big',
    },
    'paris': {
        'country': 'french',
        'population': '5million',
        'fact': 'beautiful',
    },
    'tokyo': {
        'country': 'japan',
        'population': 50,
        'fact': 'small',
    },
}
for city, values in cities.items():
    print(f"{city.title()} :")
    for value, w in values.items():
        print('\t'+f"{value}:{w}")