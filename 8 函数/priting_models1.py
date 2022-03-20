# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月18日
"""
def print_models(unprinted_designs,completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其一道列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Priting models: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe folling models have benen prited:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 切片表示法[:] 创建列表的副本 function_name(list_name_[:])
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)