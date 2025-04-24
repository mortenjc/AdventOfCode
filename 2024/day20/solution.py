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
    N = 50

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


G = [[x for x in l] for l in lines]
R = len(G)
C = len(G[0])


# unique directions for N ns
def mkdirs(len):
    dirs = set()
    for r in range(0,len+1):
        for c in range(0, len-r+1):
            if r == 0 and c == 0:
                continue
            dirs.add((r,c))
            dirs.add((-r,c))
            dirs.add((r,-c))
            dirs.add((-r,-c))
    return dirs


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




cost, path, CST  = getcost(0,0, 0, 0)
print('best cost without cheating', cost)

def solve(part2=False):
    D = defaultdict(int)
    chns = 2
    if part2:
        chns = 20
    testdirs = mkdirs(chns)
    tries = 0
    for r, c in path:
            if tries % 100 == 0:
                print(tries)
            assert G[r][c] != '#'
            for dr, dc in testdirs:
                rr, cc = r + dr, c + dc
                if not (0<=rr<R and 0<=cc<C):
                    continue
                if (rr,cc) not in path:
                    continue

                saved = CST[rr][cc] - CST[r][c] - abs(dr) - abs(dc)

                if saved > 0:
                    D[saved] += 1
                    #print('cheat (',r,c,') ->(',rr,cc,') saved ', saved)
            tries += 1
    return D


D1 = solve()
S1 = sum([D1[x] for x in D1 if x >= N])
print(S1)

D2 = solve(True)
S2 = sum([D2[x] for x in D2 if x >= N])


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
