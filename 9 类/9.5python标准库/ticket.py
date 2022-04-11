# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月10日
"""
from random import randint, sample, choices

# tickets = ['1', '2', '3', '44', '5', '66', '7', '8', '9', '10', 'a', 'b', 'c', 'd', 'r']
lottery = []
tickets = list(range(10)) + ['a', 'b', 'c', 'd', 'r']
# for i in range(4):
#     lottery_ticket = randint(0, 14)
#     lottery.append(tickets[lottery_ticket])
# print(f'if your ticket is {lottery}, you win!')
# my_ticket = []
# lottery_ticket = ['1', '5', 'a', 'r']
# while my_ticket != lottery_ticket:
lottery_tickets = sample(tickets, k=4)

n = 1
while True:
    my_tickets = choices(tickets, k=4)
    if lottery_tickets != my_tickets:
        n += 1
        continue
    else:
        print(n)
        break



