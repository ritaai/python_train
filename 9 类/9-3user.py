# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月19日
"""


class User:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def greet_user(self):
        print(f"Hello! {self.first} {self.last}")


user1 = User('qin', 'zilch')
user2 = User('while', 'died')
user3 = User('wee', 'wee')

user1.greet_user()
user2.greet_user()
user3.greet_user()
