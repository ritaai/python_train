# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月10日
"""
from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        for i in range(10):
            print(randint(1, self.sides))


my_die = Die()
my_die.roll_die()
my_die = Die(10)
my_die.roll_die()
my_die = Die(20)
my_die.roll_die()



