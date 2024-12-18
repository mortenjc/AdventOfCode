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
    n.append(list(map(int, line.split(','))))

G = [['.' for x in range(X)] for y in range(Y)]

for y in range(Y):
    for x in range(X):
        if [x,y] in n[:nn]:
            G[y][x] = '#'

def printg(G, py, px):
    for y in range(R):
        l = ''
        for x in range(C):
            ch = G[y][x]
            if y == py and x == px:
                l += 'O'
            else:
                l += ch
        print(l)


def run(i):
    pq = []

    heapq.heappush(pq, (0,0,0, (0,1)))
    heapq.heappush(pq, (0,0,0, (1,0)))
    SEEN = set()

    while len(pq):
        steps, x, y, dir = heapq.heappop(pq)
        #print(steps, r, c, dir)
        #printg(G, r, c)
        #print()

        if (x,y, dir) in SEEN:
            continue
        SEEN.add((x,y, dir))

        if x == xe and y == ye:
            return steps
            break

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            xx = x + dx
            yy = y + dy
            if not (0<=xx<X and 0<=yy<Y):
                continue
            if [yy,xx] in n[:i]:
                continue
            heapq.heappush(pq, (steps+1, xx,yy, (dx,dy)))
    return -1

S1 = run(nn)

mi = 1024
ma = len(n)
val = (mi + ma)//2
while ma != mi:
    print(mi, ma, val)
    res1 = run(val)
    if res1 != -1:
        mi = val
    else:
        ma = val
    newval = (mi+ma)//2
    if newval == val:
        print(val)
        break
    val = newval


S2 = ','.join(map(str,n[2907]))


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
