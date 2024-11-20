#!/usr/local/bin/python3

import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

assert len(lines) == 1



dirs = [(0,-1), (1,0), (0,1), (-1,0)]
chg = {'L':-1, 'R':1}


def solve(part2):
    x = 0
    y = 0
    dir = 3
    SEEN = set()
    SEEN.add((0,0))
    for l in lines[0].split(','):
        l = l.strip()
        dir = (dir + chg[l[0]])%4
        dy, dx = dirs[dir]

        n = int(l[1:])

        if part2:
            for i in range(n):
                x = x + dx
                y = y + dy
                if (x, y) in SEEN:
                    return abs(x) + abs(y)
                SEEN.add((x, y))
        else:
            x += n * dx
            y += n * dy

    return abs(x) + abs(y)

S1 = solve(False)
S2 = solve(True)

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
