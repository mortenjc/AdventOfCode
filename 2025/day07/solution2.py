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
print(R, C)

for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            r0 = r
            c0 = c


Q = [(r0, c0, ' ')]
seen = set()
paths = set()
while len(Q) != 0:
    r,c, past = Q.pop(0)
    #print(r)

    if not (0 <= r < R and 0 <= c < C):
        continue

    if r == R - 1:
        paths.add(past)
        print('***', len(paths))
        continue

    if past in seen:
        print('prune')
        continue

    seen.add(past)




    if G[r][c] == '^':
        if not past+'l' in seen:
            Q.insert(0, (r+1, c-1, past+'l'))
        if not past+'r' in seen:
            Q.insert(0, (r+1, c+1, past+'r'))

    else:
        if not past+'d' in seen:
            Q.insert(0, (r+1, c, past+'d'))

S2 = len(paths)


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
