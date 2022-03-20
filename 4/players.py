# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月07日
"""
players =['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

players =['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three palyers on my team")
for player in players[:3]:
    print(player.title())
