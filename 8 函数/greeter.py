# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月17日
"""


def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# 这是一个无限的循环
while True:
    print("\nPlease tell me you name:")
    print("(enter 'q' at any time to quit!)")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")


