# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月14日
"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
for name in favorite_languages.keys():
    print(name)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")


for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

for language in set(favorite_languages.values()):
    print(language.title())

people = ['jen', 'sarah', 'edward', 'phil', 'wc', 'zzh']
for name in people:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you")
    else:
        print(f"{name.title()}, can you come?")


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': 'c',
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite languages is:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")