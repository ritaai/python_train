# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月16日
"""
responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\n What is your name?")
    response = input("Which mountain would you like to climb someday?")

    # 将回答存储在字典中
    responses[name] = response

    # 看看是否还有人要参加调查
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == "no":
        polling_active = False

print("\n--- Polling Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
