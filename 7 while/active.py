# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月16日
"""
prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program."

# active = True
# while active:
#     message = input(prompt)
#
#     if message == "quit":
#         active = False
#     else:
#         print(message)

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")