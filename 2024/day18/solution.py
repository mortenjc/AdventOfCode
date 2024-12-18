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
    xe = 70
    ye = 70
    X = 71
    Y = 71
    nn = 1024
else:
    xe = 6
    ye = 6
    X = 7
    Y = 7
    nn = 12

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

n = []
for line in lines:
    n.append(tuple(map(int, line.split(','))))



def run(blocks):
    pq = []
    heapq.heappush(pq, (0, 0,0, (0,1)))
    heapq.heappush(pq, (0, 0,0, (1,0)))
    SEEN = set()

    while len(pq):
        steps, x, y, dir = heapq.heappop(pq)
        if (x,y, dir) in SEEN:
            continue
        SEEN.add((x,y, dir))

        if x == xe and y == ye:
            return steps

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            xx, yy = x + dx, y + dy
            if (xx,yy) in blocks or not (0<=xx<X and 0<=yy<Y):
                continue
            heapq.heappush(pq, (steps+1, xx,yy, (dx,dy)))
    return -1

blocks = set(n[:nn])
S1 = run(blocks)


mi = nn
ma = len(n)
val = (mi + ma)//2
print('  min   test    max')
while ma != mi:
    print(f'{mi:6}{val:6}{ma:6}')
    blocks = set(n[:val])
    res = run(blocks)
    if res != -1:
        mi = val
    else:
        ma = val
    newval = (mi+ma)//2
    if newval == val:
        break
    val = newval


S2 = ','.join(map(str,n[val]))


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
