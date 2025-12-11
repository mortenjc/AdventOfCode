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
    lines = ((fin.read().strip()).split('\n'))

D = {}
for line in lines:
    a, b = line.split(':')
    b = b.split()
    D[a] = b


def dp(s1):
    if s1 == 'out':
        return 1
    else:
        return sum(dp(x) for x in D[s1])

S1 = dp('you')


@cache
def dp2(s1, seen_dac, seen_fft):
    #print(s1, seen_dac, seen_fft)
    if s1 == 'out':
        return 1 if seen_dac and seen_fft else 0
    else:
        ans = 0
        for x in D[s1]:
            new_seen_dac = seen_dac or x == 'dac'
            new_seen_fft = seen_fft or x == 'fft'
            ans += dp2(x, new_seen_dac, new_seen_fft)
        return ans


S2 = dp2('svr', False, False)


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
