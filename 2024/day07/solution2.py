#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import copy
import itertools

import sys
import re

# Also solves dat 07 but with recursion

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


def solve(res, lst):
    if len(lst) == 1:
        return res == lst[0]
    a = lst[0]
    b = lst[1]
    rest = lst[2:]

    if part == 1:
        return solve(res, [a+b] + rest) or solve(res, [a*b] + rest)
    elif part == 2:
        return solve(res, [a+b] + rest) or solve(res, [a*b] + rest) or \
            solve(res, [int(str(a)+str(b))] + rest)
    else:
        assert False


with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


for part in [1,2]:
    for line in lines:
        val, nums = line.split(':')
        val = int(val)
        nums = list(map(int, nums.split()))

        if solve(val, nums):
            if part == 1:
                S1 += val
            else:
                S2 += val

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
