#!/usr/local/bin/python3

import sys
# from copy import deepcopy
# from collections import deque
from collections import defaultdict
# import functools
# import numpy as np
# from PIL import Image
#import re


def getsides(B):
    sides = 0
    L = set()
    for j in B:
        for l in L:
            d = abs(j[0] - l[0]) + abs(j[1] - l[1]) + abs(j[2] - l[2])
            if d == 1:
                #print(f' {j} and {l} are touching')
                sides -= 2

        #print(f'adding {j}, sides {sides}')
        sides += 6
        L.add(j)
    return sides


S1 = 0
S2 = 0

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

if infile == 'puzzle.txt':
    U = 30
else:
    U = 7

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


B = []
for line in lines:
    x, y, z = line.split(',')
    assert int(x) < 30
    assert int(y) < 30
    assert int(z) < 30
    B.append((int(x), int(y), int(z)))


# Part I
S1 = getsides(B)


# Part II
minZ = defaultdict(lambda: int(1e6))
minY = defaultdict(lambda: int(1e6))
minX = defaultdict(lambda: int(1e6))
maxZ = defaultdict(lambda: 0)
maxY = defaultdict(lambda: 0)
maxX = defaultdict(lambda: 0)
xmi = ymi = zmi = int(1e6)
xma = yma = zma = 0

for x,y,z in B:
    minZ[(x,y)] = min(z, minZ[(x,y)])
    maxZ[(x,y)] = max(z, maxZ[(x,y)])
    minY[(x,z)] = min(y, minY[(x,z)])
    maxY[(x,z)] = max(y, maxY[(x,z)])
    minX[(y,z)] = min(x, minX[(y,z)])
    maxX[(y,z)] = max(x, maxX[(y,z)])

    xmi = min(xmi, x)
    ymi = min(ymi, y)
    zmi = min(ymi, z)
    xma = max(xma, x)
    yma = max(yma, y)
    zma = max(zma, z)

print(f'## minX: ', minX)
print(f'## maxX: ', maxX)
print(f'## minY: ', minY)
print(f'## maxY: ', maxY)
print(f'## minZ: ', minZ)
print(f'## maxZ: ', maxZ)
print(xmi, xma, ymi, yma, zmi, zma)



PI = set() # potentially internal 'holes'
for i in range(0, U): # i == x
    for j in range(0, U): # j == y
        for k in range(0, U): # k == z
            p = (i,j,k)
            print(p)
            if p not in B:
                if (minX[(j,k)] < i < maxX[(j,k)]) and (minY[(i,k)] < j < maxY[(i,k)]) and (minZ[(i,j)] < k < maxZ[(i,j)]):
                   print(f'candidate {p}')
                   PI.add(p)
                else:
                    pass
                    print('p outside range ', p)
            else:
                print(f'p {p} already in B')


print(PI)
INT = []
for pi in PI:
    if not reaches_outside(pi, B):
        INT.append(pi)

p2sides = getsides(PI)
print('p2sides ', p2sides)
S2 = S1 + p2sides


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
