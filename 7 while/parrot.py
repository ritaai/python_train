# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月16日
"""
message = input("Tell me something, and i wll repeat it back to you.")
print(message)

prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
