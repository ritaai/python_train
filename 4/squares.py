# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月07日
"""
# squares = []
# for value in range(1, 11):
#     # square = value ** 2
#     # squares.append(square)
#     squares.append(value ** 2)
#
# print(squares)
#
# squares = [value ** 2 for value in range(1, 11)]
# print(squares)
#
# numbers = range(1, 21)
# for number in numbers:
#     print(number)

numbers = list(range(1, 1000000))
# print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

numbers = list(range(1, 21, 2))
for number in numbers:
    print(number)


lists = range(1,11)
for i in lists:
    print(i **3)

squaress = [value ** 3 for value in range(1, 11)]
print(squaress)