# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月17日
"""
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印没个设计， 知道没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Priting model: {current_design}")
    completed_models.append(current_design)

# 显示打印好的模型
print("\nTHe folling models have benn printed:")
for completed_model in completed_models:
    print(completed_model)

