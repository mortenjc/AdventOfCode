#!/usr/local/bin/python3

import sys
from collections import defaultdict


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

seen = set()

x = 0
y = 0
seen.add((x,y))

line = lines[0]
pos = (0,0)
rpos = (0,0)
D = defaultdict(int)
D[pos] += 2

M = {'^':(0,1), 'v':(0,-1), '<':(-1,0), '>':(1,0)}

for i, c in enumerate(line):
    assert c in ['^', 'v', '>', '<']
    dx, dy = M[c]
    x += dx
    y += dy

    if i % 2 == 0: #santa
        pos = (pos[0]+dx, pos[1]+dy)
        D[pos] += 1
    else: # rsanta
        rpos = (rpos[0]+dx, rpos[1]+dy)
        D[rpos] += 1

    seen.add((x,y))

S1 = len(seen)
S2 = len(D)

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
