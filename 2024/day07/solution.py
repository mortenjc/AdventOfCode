#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import copy
import itertools

import sys
import re


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


for line in lines:
    val, nums = line.split(':')
    val = int(val)

    nums = list(map(int, nums.split()))

    gaps = len(nums)-1

    combs = [''.join(x) for x in itertools.product('+*|', repeat=gaps)]


    for p in combs:
        a = nums[0]
        for i in range(gaps):
            b = nums[i+1]
            if p[i] == '+':
                v  = a + b
            elif p[i] == '*':
                v = a * b
            else: # assuming '|'
                v = int(str(a)+str(b))
            a = v

        if v == val:
            print(line, p)
            if '|' not in p:
                S1 += val
            S2 += val
            break


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
