#!/usr/local/bin/python3

import unittest
from solution2 import MMap


class MapMethodsTest(unittest.TestCase):
    def setUp(self):
        self.m = MMap(4, 'test.txt')

    def test_regions(self):
        for x in [0, 7, 12, 15]:
            assertEqual(self.m.region(x,0), 0)
            assertEqual(self.m.region(x,3), 0)
        assertEqual(self.m.region(8,0), 1)
        assertEqual(self.m.region(11,0), 1)
        assertEqual(self.m.region(8,3), 1)
        assertEqual(self.m.region(11,3), 1)

        assertEqual(self.m.region(0,4), 2)
        assertEqual(self.m.region(4,4), 3)
        assertEqual(self.m.region(8,4), 4)
        assertEqual(self.m.region(8,8), 5)
        assertEqual(self.m.region(12,8), 6)
        assertEqual(self.m.region(15,8), 6)


    def test_rotate(self):
        ds = [ (1,0), (-1,0), (0,1), (0,-1)]
        for d0 in ds:
            dir = d0
            for i in range(4):
                dir = self.m.rotate(dir[0], dir[1], 'R')
            assert dir == d0


    def test_boundary(self):
        x, y = [7,0]
        r = self.m.region(x,y)
        assertFalse(self.m.boundary(r, x  , y))
        assertTrue(self.m.boundary(r, x+1, y))
        assertTrue(self.m.boundary(r, x+4, y))


    def test_move(self):
        assertTrue(True)


if __name__ == '__main__':
    unittest.main()
