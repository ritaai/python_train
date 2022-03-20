# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月17日
"""
def  greet_users(names):
    """向列表中的美味用户发出简单的问候"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['hannah', 'ty', 'margot', 'qzf']
greet_users(usernames)