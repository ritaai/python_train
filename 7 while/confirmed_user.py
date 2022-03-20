# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月16日
"""
# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

# 验证每个用户， 直到没有未验证用户为止
# 将每个经过验证的用户都一道已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been cionfirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())