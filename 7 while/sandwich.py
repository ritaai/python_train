# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月16日
"""
sandwich_orders = ['fish', 'apple', 'banana']
finished_sandwish = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwish.append(sandwich)

for i in finished_sandwish:
    print(i)

sandwich_orders = ['fish', 'pastrami', 'apple', 'pastrami', 'banana', 'pastrami']
print("'pastrami' mai wan le ")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

