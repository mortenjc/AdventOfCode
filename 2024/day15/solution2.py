#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import sys
import re
import math


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

moves = ''.join(moves.split('\n'))

mv = {'^':(-1,0), 'v':(1,0), '>':(0,1), '<':(0,-1)}

# Helper function - print grid
def printg(X, rpos, cpos):
    for r in range(len(X)):
        l = ''
        for c in range(len(X[0])):
            if r == rpos and c == cpos:
                l += '@'
            else:
                l += X[r][c]
        print(l)
    print()


# Move up or down
def moveud(G2, r, c, dr):
    dir = {'[':1, ']':-1}
    ccom = set()
    Q = []

    ch = G2[r][c]
    assert ch in '[]'

    Q.extend([(r, c), (r, c + dir[ch])])
    ccom.add((r, c))
    ccom.add((r, c + dir[ch]))

    while len(Q): # find connected
        rr, cc = Q.pop(0)
        nr = rr + dr
        ch = G2[nr][cc]
        if not ch in "[]":
            continue

        Q.extend([(nr,cc), (nr,cc + dir[ch])])
        ccom.add((nr,cc))
        ccom.add((nr,cc + dir[ch]))

    if any([G2[mr+dr][mc] == '#' for mr, mc in ccom]):
        return False

    mccom = set()
    for mr,mc in ccom:
        mccom.add((mr+dr, mc, G2[mr][mc]))
        G2[mr][mc] = '.'
    for mr, mc, ch in mccom:
        G2[mr][mc] = ch
    return True



def movelr(G, r, c, dc):
    assert G[r][c] in "[]"
    rr = r
    cc = c + dc
    dist = 0
    canmove = False
    while G[rr][cc] != '#':
        dist += 1
        if G[rr][cc] == '.':
            canmove = True
            break
        cc += dc
    if not canmove:
        return False

    for _ in range(dist):
        pc = cc - dc
        G[rr][cc] = G[rr][pc]
        cc = pc
    G[r][c] = '.'
    return True



# Construct G2 from G, find start (@)
G2 = []
for r in range(R):
    tmp = []
    for c in range(C):
        ch = G[r][c]
        if ch == 'O':
            tmp.extend(['[', ']'])
        elif ch == '@':
            rr = r
            cc = len(tmp)
            tmp.extend(['.', '.'])
        else:
            tmp.extend([ch, ch])
    G2.append(tmp)

R2 = len(G2)
C2 = len(G2[0])
assert R == R2 and C2 == C * 2



for i, move in enumerate(moves):
    assert move in "<>^v"
    (dr, dc) = mv[move]
    nr = rr + dr
    nc = cc + dc
    ch = G2[nr][nc]
    assert ch in '#.[]'
    moved = False
    if  ch == '#':
        continue # don't move
    elif ch == '.':
        moved = True
    elif dc != 0 and dr == 0: # left right
        moved = movelr(G2, nr, nc, dc)
    elif dc == 0 and dr != 0: # up down
        moved = moveud(G2, nr, nc, dr)
    if moved:
        rr = nr
        cc = nc


def score(X, ch):
    nr = len(X)
    nc = len(X[0])
    res = 0
    for r in range(nr):
        for c in range(nc):
            if X[r][c] == ch:
                res += 100 *r + c
    return res

printg(G2, rr, cc)

S2 = score(G2, '[')

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
