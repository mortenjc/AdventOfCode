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
    blocks = ((fin.read().strip()).split('\n\n'))

locks = set()
keys = set()
for kl in blocks:
    print(len(kl))

    G = kl.split('\n')
    R = len(G)
    C = len(G[0])
    res = [-1 for x in range(C)]
    for r in range(R):
        for c in range(C):
            if G[r][c] == '#':
                res[c] += 1
    if G[0] == '#####':
        #print('lock', res)
        locks.add(tuple(res))
    else:
        #print('key', res)
        keys.add(tuple(res))

print(locks)
print(keys)

sol = set()
for l in locks:
    for k in keys:
        #print(l, k, ' - ', [k[i]+ l[i] for i in range(len(k))])
        #print([k[i]+ l[i] < 6 for i in range(len(k))])
        if all([k[i]+ l[i] < 6 for i in range(len(k))]):
            S1 += 1
print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
