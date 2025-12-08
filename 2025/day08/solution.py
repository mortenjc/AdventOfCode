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
    stop = 10
else:
    stop = 1000

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

P = []
for line in lines:
    x,y,z = map(int, line.split(','))
    P.append([x,y,z])


parent = [x for x in range(len(P))]

def find(i):
    if parent[i] != i:
        parent[i] = find(parent[i])
    return parent[i]

def union(i, j):
    parent[find(i)] = find(j)

D = defaultdict(list)
for a in range(len(P)):
    for b in range(a+1, len(P)):
        if a != b:
            A, B = P[a], P[b]
            l = (A[0]-B[0])**2 + (A[1]-B[1])**2 + (A[2]-B[2])**2
            D[l]=([a, b])

ln = [int(x) for x in D]
ln = sorted(ln)

conns = 0
for cnt, i in enumerate(ln):
    if cnt == stop:
        DD = defaultdict(int)
        for xx in range(len(parent)):
            DD[find(xx)] += 1
        S1 = math.prod(sorted(DD.values())[-3:])

    a, b = D[i]
    if find(a) != find(b):
        conns += 1
        union(a,b)

    if conns == len(P) - 1:
        aa = [find(x) for x in range(len(P))]
        if all(x == aa[0] for x in aa):
            S2 = P[a][0]*P[b][0]

    if S1 != 0 and S2 != 0:
        break

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
