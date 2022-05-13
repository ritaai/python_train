# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月17日
"""
import unittest
from city_functions import city_country


class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        full = city_country('santiago', 'chile')
        self.assertEqual(full, 'Santiago, Chile')

    def test_city_population(self):
        full = city_country('santiago', 'chile', 5000000)
        self.assertEqual(full, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main
