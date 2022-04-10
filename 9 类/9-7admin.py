# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月08日
"""


class User:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def greet_user(self):
        print(f"Hello! {self.first} {self.last}")


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"you can {privilege}")


admin = Admin('q', 'zl')
admin.greet_user()
admin.show_privileges()
