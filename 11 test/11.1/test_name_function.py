# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月15日
"""
import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地像Janis Joplin这样大的姓名？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_frist_last_middle_name(self):
        """能够正确地处理像wolfgang Amadeus Mozart这样地名字嘛？"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main
