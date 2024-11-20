#!/usr/local/bin/python3

import unittest
from solution import AOC2022

class MapMethodsTest(unittest.TestCase):
    def setUp(self):
        self.m = AOC2022('test.txt')

    def test_dummy(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
