#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import copy

import sys
import re


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


def printg(G):
    print()
    for l in G:
        print(''.join(l))

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


G = [[x for x in l] for l in lines]
R = len(G)
C = len(G[0])

print(G)
print(C)
print(R)

for c in range(C):
    for r in range(R):
        if G[r][c] == '^':
            pos = (r,c)


def solve(G, pos):
    state = set()
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    cdir = 0
    done = False
    seen = set()
    state = set()
    seen.add(pos)
    state.add((pos, cdir))

    loop = False
    while not done:
        dir = dirs[cdir]
        rr = pos[0] + dir[0]
        cc = pos[1] + dir[1]
        #print(f'({pos[0]},{pos[1]}) -> ({cc},{rr})')
        if not (0 <= cc < C and 0 <= rr < R):
            done = True
            break

        if G[rr][cc] != '#':
            rr = pos[0] + dir[0]
            cc = pos[1] + dir[1]
        else:
            while G[rr][cc] == '#':
                cdir = (cdir + 1) % 4
                dir = dirs[cdir]
                rr = pos[0] + dir[0]
                cc = pos[1] + dir[1]
                if not (0 <= cc < C and 0 <= rr < R):
                    done = True
                    break

        pos = (rr,cc)
        nstate = (pos, cdir)
        if nstate in state:
            loop = True
            done = True
            break
        state.add(nstate)
        seen.add(pos)
    return len(seen), loop


n, l = solve(G, pos)
assert l == False
S1 = n



for c in range(C):
    for r in range(R):
        if G[r][c] == '#':
            continue
        ch = G[r][c]
        G[r][c] = '#'
        n, l = solve(G, pos)
        if l:
            #print(f'loop ({r},{c})')
            S2 +=1
        G[r][c] = ch

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
