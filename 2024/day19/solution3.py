#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import sys
import re
import math
import random
import heapq



infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

if infile == 'puzzle.txt':
    pass
else:
    pass

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

designs = lines[0].split(',')
designs = [x.strip() for x in designs]


DP = {}
def ways(designs, l):
    if l in DP:
        return DP[l]
    ans = 0
    if not l:
        ans = 1
    for des in designs:
        if l.startswith(des):
            ans += ways(designs, l[len(des):])
    DP[l] = ans
    return ans


for line in lines[2:]:
    print(f'*** {line} ***')
    S2 += ways(designs, line)



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
