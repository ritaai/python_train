# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月11日
"""
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# 10.3.3 使用异常避免崩溃
print("Give me two numbers, and I will divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input('\nFirst number：')
    if first_number == 'q':
        break
    second_number = input("\nSecond number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
