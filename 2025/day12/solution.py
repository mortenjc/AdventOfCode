#!/usr/local/bin/python3

import numpy as np
import sys
#import portion as p
from collections import defaultdict
from functools import cache
import math


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

if infile == 'test.txt':
    pass
else:
    pass

S1 = 0
S2 = 0

with open(infile) as fin:
    blocks = ((fin.read().strip()).split('\n\n'))

SIZE ={}
for block in blocks[:-1]:
    sz = block.count('#')
    SIZE[int(block[0])] = sz

for line in blocks[-1].split('\n'):
    reg, nums = line.split(':')
    x, y = [int(x) for x in reg.split('x')]
    nums = [int(x) for x in nums.split()]
    reg_size = x * y
    block_size = sum(b * SIZE[i] for i, b in enumerate(nums))

    if reg_size > block_size: # unfounded heuristic
        S1 += 1

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
