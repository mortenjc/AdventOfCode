#!/usr/local/bin/python3

import sys
from collections import Counter


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

for l in lines:
    d = list(map(int, l.split('x')))
    d.sort()
    print(d)
    S1 += 2 * (d[0]*d[1] + d[1]*d[2] + d[0]*d[2]) + d[0]*d[1]
    S2 += 2*(d[0] + d[1]) + d[0]*d[1]*d[2]


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
