# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月06日
"""
bicycle = ['trek', 'cannondale', 'redline', 'spacialized']
print(bicycle)
print(bicycle[0])
print(bicycle[-1])
print(bicycle[0].title())
message = f"My first bicycle was a {bicycle[0].title()}"
print(message)

names = ['李爽', '张三', '李斯', '宛平', '伟岸']

for i in names:
    messages = f"Hello {i}, we are family"
    print(messages)