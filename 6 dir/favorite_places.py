# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月14日
"""
favorite_places = {
    'qzl': ['xiann', 'dali', 'piking'],
    'qwe': ['chongqing', 'china', 'piking'],
    'asd': ['taiyuan'],
}
for name, places in favorite_places.items():
    print(f"{name} like to ")
    for place in places:
        print(f"\t{place}")