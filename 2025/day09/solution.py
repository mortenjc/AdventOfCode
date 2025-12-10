#!/usr/local/bin/python3

import numpy as np
import sys
import portion as p
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

P = []
for line in lines:
    x,y = map(int, line.split(','))
    P.append([x,y])

print(P)
max = 0
for i in range(len(P)):
    for j in range(i+1, len(P)):
        if i != j:
            p1 = P[i]
            p2 = P[j]
            d = abs((p1[0]-p2[0] +1) * (p1[1]-p2[1] +1))
            if d > max:
                max = d

S1 = max



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
