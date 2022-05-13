# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月11日
"""

"""
练习10-6：加法运算 　提示用户提供数值输入时，常出现的一个问题是，用户
提供的是文本而不是数。在此情况下，当你尝试将输入转换为整数时，将引发
ValueError 异常。编写一个程序，提示用户输入两个数，再将其相加并打印
结果。在用户输入的任何一个值不是数时都捕获ValueError 异常，并打印一
条友好的错误消息。对你编写的程序进行测试：先输入两个数，再输入一些文
本而不是数
"""
print("Give me two numbers, and I will sum them.")
print("Enter 'q' to quit.")

while True:
    first_number = input('\nFirst number：')
    if first_number == 'q':
        break
    second_number = input("\nSecond number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You must input value!")
    else:
        print(answer)
