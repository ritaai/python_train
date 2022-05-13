# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月11日
"""
# 10-3访客
filename = 'guest.txt'
with open(filename, 'w') as f:
    user = input("please input your name: ")
    f.write(f"{user}\n")

# 10-4 访客名单
filename = 'guest_book.txt'
with open(filename, 'a') as f:
    while True:
        user = input("please input your name: ")
        if user == 'exit':
            break
        print(f"Hello,{user}")
        f.write(f"{user}\n")

# 10-5 调查
survey = 'survey.txt'
with open(survey, 'a') as f:
    reason = input("why your like programming?")
    while True:
        if reason == 'exit':
            break
        f.write(f"{reason}\n")
