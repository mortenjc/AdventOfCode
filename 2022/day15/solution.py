#!/usr/local/bin/python3

import sys
# from copy import deepcopy
# from collections import deque
#from collections import defaultdict
# import functools
# import numpy as np
# from PIL import Image
#import re

def valid(x, y, S):
    for (sx, sy, d) in S:
        if (abs(x-sx) + abs(y-sy)) <= d:
            return False
    return True

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

if infile == 'puzzle.txt':
    s1_y = 2000000
    s2_max = 4000000
else:
    s1_y = 10
    s2_max = 20

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

S = set()
B = set()
for line in lines:
    words = line.split()
    sx, sy = int(words[2][2:-1]), int(words[3][2:-1])
    bx, by = int(words[8][2:-1]), int(words[9][2:])
    bd = abs(sx - bx) + abs(sy - by)
    S.add((sx, sy, bd))
    B.add((bx, by))


# Part I
S1 = 0
y = s1_y
for x in range(-10000, 10000):
    y = s1_y
    if not valid(x, y, S) and (x, y) not in B:
        S1 += 1

# Part II
S2 = 0
res = (-1, -1)
done = False
for (sx, sy, d) in S:
    if done:
        break
    ymin = sy-d-1
    ymax = sy+d+1
    for y in range(ymin, ymax+1):
        dx = abs(d+1 - abs(sy -y))
        x1 = sx + dx
        x2 = sx - dx
        if not (0 <= x1 <= s2_max and 0 <= x2 <= s2_max and 0<= y <= s2_max):
            continue
        if valid(x1, y, S):
            res = (x1, y)
            done = True
        if valid(x2, y, S):
            res = (x2, y)
            done = True

print('x, y ', res)
S2 = 4000000*res[0] + res[1]


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
