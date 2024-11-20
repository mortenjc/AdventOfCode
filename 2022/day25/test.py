#!/usr/local/bin/python3

import unittest
from solution import AOC2022

class MapMethodsTest(unittest.TestCase):
    def setUp(self):
        self.m = AOC2022('test.txt')

    def test_numbers(self):
        for i in range(1,1000):
            S = self.m.to_snafu(i)
        self.assertTrue(S != 0)


if __name__ == '__main__':
    unittest.main()
