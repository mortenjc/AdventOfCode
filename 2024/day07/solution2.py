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
    return solve(res, [a+b] + rest) or solve(res, [a*b] + rest)


def solve2(res, lst):
    if len(lst) == 1:
        return res == lst[0]

    a = lst[0]
    b = lst[1]
    rest = lst[2:]
    #print('x',a,b, int(str(a)+str(b)))
    return solve2(res, [a+b] + rest) or solve2(res, [a*b] + rest) or \
        solve2(res, [int(str(a)+str(b))] + rest)


with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


for line in lines:
    val, nums = line.split(':')
    val = int(val)

    nums = list(map(int, nums.split()))
    #print(val, nums)

    if solve(val, nums):
        S1 += val
    if solve2(val, nums):
        S2 += val


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
