#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import sys
import re
import math
import random
import heapq



infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

if infile == 'puzzle.txt':
    N = 100
else:
    N = 20

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


G = [[x for x in l] for l in lines]
R = len(G)
C = len(G[0])


dots=0
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            sr, sc = r, c
        if G[r][c] == 'E':
            er, ec = r, c
        if G[r][c] == '.':
            dots+=1


def getcost(ctr, ctc, nr, nc):
    cheated = False
    hq =[]
    cost = 0
    cheats = 0
    SEEN = set()
    path =  []
    CST = [[10**6 for x in l] for l in G]
    heapq.heappush(hq, (cost, sr,sc))

    while len(hq):
        cost, r, c = heapq.heappop(hq)
        if (cost, r, c) in SEEN:
            continue
        SEEN.add((cost, r, c))

        if cost >= CST[r][c]:
            continue
        CST[r][c] = cost

        path.append((r,c))

        if r == er and c == ec:
            return cost, path, CST

        if r == ctr and c == ctc and cheated == False: #
            #print(f'cheating at ({r},{c})')
            heapq.heappush(hq, (cost+2, nr, nc))
            cheated = True
            continue

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            rr, cc = r + dr, c + dc
            if (0<=rr<R and 0<=cc<C) and G[rr][cc] != '#':
                #print(f'add ({rr},{cc})')
                heapq.heappush(hq, (cost+1, rr, cc))

    return -1, [], CST


D = defaultdict(int)

cost, path, CST  = getcost(0,0, 0, 0)

#nc, _, _ = getcost(1,7,1,9)

print('regular best cost', cost)
for r, c in path:
        if G[r][c] == '#':
            continue
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            rr, cc = r + dr, c + dc
            if not (0<=rr<R and 0<=cc<C):
                continue
            if G[rr][cc] != '#':
                continue
            rr, cc = rr + dr, cc + dc
            if not (0<=rr<R and 0<=cc<C):
                continue
            if G[rr][cc] == '#':
                continue

            if (rr,cc) not in path:
                continue

            saved = CST[rr][cc] - CST[r][c] - 2

            if saved > 0:
                D[saved] += 1
                #print('cheat (',r,c,') ->(',rr,cc,') saved ', saved)

S1 = sum([D[x] for x in D if x >= N])



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
