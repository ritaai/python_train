# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月11日
"""
# 10.1.5 使用文件的内容
#
# filename = 'pi_digits.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
#
# print(pi_string)
# print(len(pi_string))

# 圆周率中包含你的生日嘛

filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday odes not appear in the first million digits if pi.")