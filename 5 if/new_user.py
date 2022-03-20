# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月12日
"""
current_users = ['admin', 'qwe', 'asd', 'zxc', 'rty']
new_users = ['admin', 'qwe', 'ASD', 'tightly']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("You must use other names!")
    else:
        print("this name OK!")