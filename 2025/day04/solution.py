#!/usr/local/bin/python3

import numpy as np
import sys


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

G = [ [c for c in r] for r in lines ]

R = len(G)
C = len(G[0])

def adjcount(G, x, y):
    dirs = [(-1,-1), (0,-1), (1,-1), (-1,0), (1, 0), (-1,1), (0,1), (1,1)]
    nb = 0
    for dir in dirs:
        nc = x + dir[0]
        nr = y + dir[1]

        if 0 <= nr < R and 0 <= nc < C:
            if G[nr][nc] == '@':
                nb += 1
    return nb




#assert adjcount(G, 2, 0) == 3
nc = adjcount(G, 1, 0)
assert nc == 4

def printg(G):
    for r in G:
        print(''.join(r))



def removable(G, nr, nc):
    n = 0
    rm = []
    for r in range(nr):
        for c in range(nc):
            na = adjcount(G, r, c)
            if G[c][r] == '@' and na < 4:
                n += 1
                rm.append((c,r))
    return n, rm


S1, rm = removable(G, R, C)
S2 = S1
iter = 1
while True:
    print(f'removing {len(rm)} rolls')
    for rmc in rm:
        G[rmc[0]][rmc[1]] = '.'
    printg(G)
    n, rm = removable(G, R, C)
    S2 += n
    if n == 0:
        break



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
