# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月19日
"""


def bulid_profile(first, last, **user_info):
    """创建一个字典，其中包括我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = bulid_profile('qin', 'zilu',
                             location='xian',
                             filed='student')
print(user_profile)
