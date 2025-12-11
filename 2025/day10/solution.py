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

FS = []
BTN = []
for line in lines:
    x = line.split()

    FS.append(x[0][1:-1])
    BTN.append(x[1:-1])
print(FS)
print(BTN)

for i in range(len(lines)):
    for a in range(2**len(BTN[i])):
        print(i, a)

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
