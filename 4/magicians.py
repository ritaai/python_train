# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月07日
"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you!")

pizzas = ['pepperoni', 'chicken', 'apple']
for pizza in pizzas:
    print(f"i like {pizza} pizza.")
print("I really love pizza")

firend_pizzas = pizzas[:]
pizzas.append('oragin')
firend_pizzas.append('blue')
for pizza in pizzas:
    print(f"i like {pizza} pizza.")
print("My firend's favoriate pizzas are:")
for firend_pizza in firend_pizzas:
    print(firend_pizza)

