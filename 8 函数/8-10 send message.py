# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月19日
"""


def show_message(messages):
    for message in messages:
        print(message)


def send_message(messages, send_message):
    while messages:
        message = messages.pop()
        send_message.append(message)
    print(send_messages)



messages = ['you beautiful', 'oh no', 'take easy', 'en?', 'oh my god']
send_messages = []
show_message(messages)
send_message(messages[:], send_messages)
print(messages)