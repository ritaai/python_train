# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月17日
"""


def describe_pet(animal_type, pet_name='dog'):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"my {animal_type}'s name is {pet_name.title()}.")


describe_pet('dog', 'willie')
describe_pet('hamster', 'harry')

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(animal_type='hamster')
