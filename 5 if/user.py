# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月12日
"""
users = ['admin', 'qwe', 'asd', 'sdf', 'ffg']
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you logging in again.")
else:
    print("We need to find some users!")