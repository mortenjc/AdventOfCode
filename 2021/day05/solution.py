#!/usr/local/bin/python3

import sys
from collections import defaultdict

S1 = 0
S2 = 0

ifile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'

with open(ifile) as fin:
    lines = ((fin.read().strip()).split('\n'))

for part in [1,2]:
    pts = defaultdict(int)
    for line in lines:
        f, _, t = line.split(' ')

        fx, fy = map(int, f.split(','))
        tx, ty = map(int, t.split(','))
        dx = tx - fx
        dy = ty - fy
        if dx != 0:
            dx = dx // abs(dx)
        if dy != 0:
            dy = dy // abs(dy)

        # ignore diagonals
        if dy != 0 and dx != 0 and part == 1:
            continue

        pos = (fx, fy) # start position

        pts[pos] += 1

        while True:
            pos = (pos[0]+dx, pos[1]+dy)
            pts[pos] += 1

            if pos == (tx, ty):
                break

    res = len([1 for x in pts if pts[x] > 1])
    if part == 1:
        S1 = res
    else:
        S2 = res

print("------------- A -------------")
print(f'S1 {S1}')
print("------------- B -------------")
print(f'S2 {S2}')
print("-----------------------------")
