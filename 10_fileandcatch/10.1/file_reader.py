# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月11日
"""
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

# 10.1.3 逐行读取
# filename = 'pi_digits.txt'
#
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# 10.1.4 创建一个包含文件各行内容的列表

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())