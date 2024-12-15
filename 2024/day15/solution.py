#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import sys
import re
import math


mv = {'^':(-1,0), 'v':(1,0), '>':(0,1), '<':(0,-1)}

DIRS4 = [(1,0), (-1,0), (0,1), (0,-1)]
DIRS8 = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)]

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

if infile == 'puzzle.txt':
    pass
else:
    pass

with open(infile) as fin:
    map, moves = ((fin.read().strip()).split('\n\n'))

G = [[x for x in l] for l in map.split('\n')]
R = len(G)
C = len(G[0])

def movebox(G, r, c, dr, dc):
    assert G[r][c] == 'O'
    rr = r + dr
    cc = c + dc
    dist = 0
    space = 0
    while G[rr][cc] != '#':
        print(rr,cc)
        dist += 1
        if G[rr][cc] == '.':
            print('found space at', rr, cc)
            space = 1
            break
        rr += dr
        cc += dc
    if not space:
        return False
    assert G[rr][cc] == '.'
    for i in range(dist):
        pr = rr - dr
        pc = cc - dc
        G[rr][cc] = G[pr][pc]
        rr = pr
        cc = pc
    G[r][c] = '.'
    return True


def printg(G, rr, cc):
    for r in range(R):
        l = ''
        for c in range(C):
            if r == rr and c == cc:
                l += '@'
            else:
                l += G[r][c]
        print(l)
    print()



moves = ''.join(moves.split('\n'))

rr = 0
cc = 0
for r in range(R):
    for c in range(C):
        if G[r][c] == '@':
            rr = r
            cc = c
            G[r][c] = '.'

for i, move in enumerate(moves):
    print(i, move)
    assert move in "<>^v"
    (dr, dc) = mv[move]
    nr = rr + dr
    nc = cc + dc
    if G[nr][nc] == '#':
        pass # don't move
    elif G[nr][nc] == '.':
        rr = nr
        cc = nc
    elif G[nr][nc] == 'O':
        print('move box')
        moved = movebox(G, nr, nc, dr, dc)
        if moved:
            rr = nr
            cc = nc
    printg(G, rr, cc)

for r in range(R):
    for c in range(C):
        if G[r][c] == 'O':
            S1 += r*100 +c

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
