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



def moveupdown(G2, r, c, dr):
    ccom = set()
    Q = [(r,c)]
    ccom.add((r, c))
    if G2[r][c] == '[':
        Q.append((r, c+1))
        ccom.add((r, c+1))
    elif G2[r][c] == ']':
        Q.append((r, c-1))
        ccom.add((r, c-1))
    else:
        assert False
    print(ccom)
    while len(Q):
        rr, cc = Q.pop(0)
        nr = rr + dr
        print(f'rr, cc ({rr},{cc}), nr, nc ({nr},{cc}) ch {G2[nr][cc]}')
        if G2[nr][cc] == "[":
            print('[ at', nr, cc, 'add', nr, cc+1)
            Q.append((nr,cc))
            Q.append((nr,cc+1))
            ccom.add((nr,cc))
            ccom.add((nr,cc+1))
        elif G2[nr][cc] == "]":
            print('] at', nr, cc, 'add', nr, cc -1)
            Q.append((nr,cc))
            Q.append((nr,cc-1))
            ccom.add((nr,cc))
            ccom.add((nr,cc-1))
        else:
            pass
    print('connected', ccom)
    canmove = True
    for mr,mc in ccom:
        if G2[mr+dr][mc] == '#':
            canmove = False
    if not canmove:
        return False


    mccom = set()
    for mr,mc in ccom:
        mccom.add((mr+dr, mc, G2[mr][mc]))
        G2[mr][mc] = '.'
    for mr, mc, ch in mccom:
        G2[mr][mc] = ch
    print(mccom)

    return True



def movebox(G, r, c, dc):
    assert G[r][c] in "[]"
    rr = r
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
        cc += dc
    if not space:
        return False
    assert G[rr][cc] == '.'
    for i in range(dist):
        pc = cc - dc
        G[rr][cc] = G[rr][pc]
        cc = pc
    G[r][c] = '.'
    return True


def printg(G, rr, cc):
    for r in range(R2):
        l = ''
        for c in range(C2):
            if r == rr and c == cc:
                l += '@'
            else:
                l += G[r][c]
        print(l)
    print()


G2 = []
for r in range(R):
    tmp = []
    for c in range(C):
        ch = G[r][c]
        if ch == 'O':
            tmp.append('[')
            tmp.append(']')
        elif ch == '@':
            tmp.append('@')
            tmp.append('.')
        else:
            tmp.append(ch)
            tmp.append(ch)
    G2.append(tmp)
R2 = len(G2)
C2 = len(G2[0])
assert R == R2 and C2 == C * 2


moves = ''.join(moves.split('\n'))

rr = 0
cc = 0
for r in range(R2):
    for c in range(C2):
        if G2[r][c] == '@':
            rr = r
            cc = c
            G2[r][c] = '.'

printg(G2, rr, cc)

for i, move in enumerate(moves):
    print(i, move)
    assert move in "<>^v"
    (dr, dc) = mv[move]
    nr = rr + dr
    nc = cc + dc
    if G2[nr][nc] == '#':
        pass # don't move
    elif G2[nr][nc] == '.':
        rr = nr
        cc = nc
    elif G2[nr][nc] in '[]' and dc != 0 and dr == 0: # left right
        print('move box - left right')
        moved = movebox(G2, nr, nc, dc)
        if moved:
            rr = nr
            cc = nc
    elif G2[nr][nc] in '[]' and dc == 0 and dr != 0:
        print(f'move box(es) - up down (start ({nr},{nc}))')
        moved = moveupdown(G2, nr, nc, dr)
        if moved:
            rr = nr
            cc = nc
    printg(G2, rr, cc)

for r in range(R2):
    for c in range(C2):
        if G2[r][c] == '[':
            S2 += 100 *r + c

# for r in range(R):
#     for c in range(C):
#         if G[r][c] == 'O':
#             S1 += r*100 +c

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
