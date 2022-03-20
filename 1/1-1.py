# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年03月06日
"""
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

print("Language:\n\tPython\n\tC\n\tJavaScript")

favorite_language = '  python '
print(favorite_language.lstrip())
print(favorite_language.rstrip())
print(favorite_language.strip())
print(favorite_language)