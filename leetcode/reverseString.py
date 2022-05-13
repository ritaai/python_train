# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年05月13日
"""
s = ["H", "a", "n", "n", "a", "h"]
n = len(s)
#
# temp = ''
# i = 0
# j = n - 1
# m = n // 2
# while i != m:
#     temp = s[i]
#     s[i] = s[n - i - 1]
#     s[n - i - 1] = temp
#     i += 1
#     j -= 1
for i in range(n//2):
    temp = s[i]
    s[i] = s[n-i-1]
    s[n-i-1] = temp
print(s)
