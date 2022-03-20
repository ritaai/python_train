# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月06日
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'tomoto')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")

motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")


dinners = ['张三', '里斯', '王五', '马六']
print(f"I will invite {dinners} for dinner")
print(f" But now {dinners[-1]} can't to the dinner")
dinners[-1] = '克鲁'
for i in dinners:
    print(f"{i}, can i invited you for dinner")

dinners.insert(0, '微风')
dinners.append('刀锋')
dinners.insert(3, '得分')
print(dinners)
for i in dinners:
    print(f"{i}, can i invited you for dinner")
print("sorry everyone, now i only have two dinner")

print(f"sorry, {dinners.pop()}, you will back")
print(f"sorry, {dinners.pop()}, you will back")
print(len(dinners ))
print(f"sorry, {dinners.pop()}, you will back")
print(f"sorry, {dinners.pop()}, you will back")
print(f"sorry, {dinners.pop()}, you will back")
print(dinners)
for i in dinners:
    print(f"{i}, can i invited you for dinner")

dinners.remove('微风')
dinners.remove('张三')

print(dinners)









