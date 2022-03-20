# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月16日
"""
pizza = "Please input your pizza:"
pizza += "when you input 'quit', you will exit"
# message = input(pizza)
# while True:
#     message = input(pizza)
#     if message == 'quit':
#         break
#     print(message)



# message = ''
# while message != 'quit':
#     message = input(pizza)
#
#     if message != 'quit':
#         print(message)


active = True
while active:
    message = input(pizza)

    if message == 'quit':
        active = False
    else:
        print(message)