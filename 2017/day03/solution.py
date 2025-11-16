#!/usr/local/bin/python3

from collections import defaultdict

import sys
import math as m


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

n = 289326

vals = defaultdict(int)    # value for a (x,y) coordinate
vals2 = defaultdict(int)
coords = defaultdict(dict) # coordinate for number n

coords[1] = (0,0)
vals[(0,0)] = 1
vals2[(0,0)] = 1

x = 0
y = 0
nn = 1
dc =  [(1,0), (0,1), (-1,0), (0,-1)]
dc2 = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1, -1), (-1, 1), (-1, -1)]
dir = 0


def sumnghbr(x,y):
    if (x,y) == (0,0):
        return 1
    return sum([ vals2[ (x + d[0], y + d[1]) ] for d in dc2])


# turn if there are no neighbors to either side
def getdir(x, y, dir):
    sum = 0
    for dx, dy in [dc[(dir + 1)%4], dc[(dir - 1)%4]]:
        sum += vals[(x+dx, y+dy)]
    if sum == 0:
        return (dir + 1)%4
    return dir


while True:
    if S2 == 0:
        tmp = sumnghbr(x,y)
        vals2[(x,y)] = tmp
        if tmp > n:
            S2 = tmp

    if nn == n:
        S1 = abs(x)+abs(y)
        break

    dx, dy = dc[dir]
    x += dx
    y += dy
    newpos = (x, y)
    nn += 1
    vals[newpos] = nn

    coords[nn] = newpos
    newdir = getdir(x,y, dir)
    dir = newdir



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
