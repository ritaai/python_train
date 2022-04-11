# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月11日
"""
filename = 'learning_python.txt'


# 打印整个文件
# with open(filename) as file_object:
#     contens = file_object.read()
# print(contens)

# # 打印时遍历文件对象
# with open(filename) as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.strip())


# # 打印时将各行存储再一个列表中
# with open(filename) as file_object:
#     lines = file_object.readlines()
# line_str = ''
# for line in lines:
#     line_str += line
# print(line_str)

# 将python 换成C
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    # line.replace('Python', 'C')
    print(line.replace('Python', 'C').strip())

