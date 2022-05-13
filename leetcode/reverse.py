# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年05月13日
"""
x = 123
# sign = 1
# if x < 0:
#     sign = -1
#     x = -x
# x = str(x)
# x = x[-1::-1]
# x = int(x)
# if (-2) ** 31 < x < 2 ** 31 - 1:
#     print(sign * x)
res = 0
while x != 0:
    res = res * 10 + x % 10
    x = x // 10
print(res)
