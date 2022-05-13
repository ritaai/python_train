# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月11日
"""
# 写入文件
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 10.2.3 附加到文件
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")