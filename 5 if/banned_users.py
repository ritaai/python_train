# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月08日
"""
banned_users = ['andrew', 'carollina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post  a response if you wish.")

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("Is car == 'audi'? I predict False.")
print(car == 'audi')