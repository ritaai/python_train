# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月17日
"""
import unittest
from employee import Employee

class EmplyeeTestCase(unittest.TestCase):
    """测试employee.py"""
    def setUp(self):
        """创建一个Employee实例，以便在测试中使用"""
        self.eric = Employee('eric', 'matthes', 65_000)

    def test_give_default_raise(self):
        """c测试使用默认的年薪增长量是否可"""
        self.eric.give_raise()
        self.assertEqual(self.eric.salary, 70000)

    def test_give_custom_raise(self):
        """测试给定增长量是否可行"""
        self.eric.give_raise(amount=10000)
        self.assertEqual(self.eric.salary, 75000)

if __name__ == '__main__':
    unittest.main