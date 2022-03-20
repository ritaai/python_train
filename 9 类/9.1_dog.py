# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月19日
"""
class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令后蹲下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令后打滚"""
        print(f"{self.name} rolled over.")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")
my_dog.sit()
my_dog.roll_over()

print(f"Your dog's name is {your_dog.name}")
print(f"My dog's age is {your_dog.age}")
your_dog.sit()
your_dog.roll_over()
