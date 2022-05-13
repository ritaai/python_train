# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月17日
"""
class Employee:
    """雇员的名字和年薪"""
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount


