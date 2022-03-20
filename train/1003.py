# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月20日
"""

import re

n = input()
for i in range(int(n)):
    s = input()
    if re.match(r'A*PA+TA*', s):  # 在字符串中进行匹配
        a = re.split(r'[P|T]', s)
        if a[0] * len(a[1]) == a[2]:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
