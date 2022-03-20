# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月17日
"""


def get_formatted_name(first_name,  last_name, minddile_name=''):
    """返回整洁的姓名"""
    if minddile_name:
        full_name = f"{first_name} {minddile_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'lee', 'hendrix')
print(musician)
musician = get_formatted_name('jimi', 'lee')
print(musician)