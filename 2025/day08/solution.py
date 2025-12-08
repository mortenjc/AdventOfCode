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

def d2(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

poss = []
D = defaultdict(list)
for line in lines:
    #print(line)
    x,y,z = line.split(',')
    x = int(x)
    y = int(y)
    z = int(z)
    poss.append([x,y,z])


parent = [x for x in range(len(poss))]

def find(i):
    if parent[i] != i:
        parent[i] = find(parent[i])
    return parent[i]

def UUnion(i, j):
    irep = find(i)
    jrep = find(j)
    parent[irep] = jrep


for a in range(len(poss)):
    for b in range(a, len(poss)):
        if a != b:
            l = d2(poss[a],poss[b])
            D[l].append([a, b])
            assert len(D[l][0]) == 2

ln = [int(x) for x in D]
cnt = 0
for i in sorted(ln):
    if cnt == stop:
        print('***** S1 condition *****')
        DD = defaultdict(int)
        for xx in range(len(parent)):
            root = find(xx)
            DD[root] += 1

        res = math.prod(sorted(DD.values())[-3:])

        S1 = res
    cnt += 1

    a, b = D[i][0]

    UUnion(a,b)


    if cnt > stop:
        aa = [find(x) for x in range(len(poss))]
        if all(x == aa[0] for x in aa):
            print('***** S2 condition *****')
            print(cnt, a,b, poss[a], poss[b])
            S2 = poss[a][0]*poss[b][0]

    if S1 != 0 and S2 != 0:
        break





print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
