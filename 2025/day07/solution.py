#!/usr/local/bin/python3

import numpy as np
import sys
import portion as p
from collections import defaultdict


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

G = [ [c for c in r ] for r in lines]

R = len(G)
C = len(G[0])
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            r0 = r
            c0 = c


Q = [(r0+1,c0)]
seen = set()
while len(Q) != 0:
    r,c = Q.pop(0)
    if (r,c) in seen:
        continue
    seen.add((r,c))
    print(r,c)
    if not (0 <= r < R and 0 <= c < C):
        continue
    if G[r][c] == '^':
        print('split')
        S1 += 1
        Q.append((r+1, c-1))
        Q.append((r+1, c+1))
    else:
        Q.append((r+1, c))



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
