#!/usr/local/bin/python3

#from collections import deque
from collections import defaultdict

import sys


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

l1 = []
l2 = []
D = defaultdict(int)

for line in lines:
    a, b = list(map(int, line.split()))
    l1.append(a)
    l2.append(b)
    print(a,b)
    D[b] += 1

for x, y in zip(sorted(l1),sorted(l2)):
    print(x,y, D[y])
    S1 += abs(x-y)
    S2 += x * D[x]


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
