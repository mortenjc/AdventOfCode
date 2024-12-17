#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import sys
import re
import math



infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

if infile == 'puzzle.txt':
    pass
else:
    pass

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

G = [[x for x in l] for l in lines]
BEST = [[1000000000 for x in l] for l in lines]
R = len(G)
C = len(G[0])


def printg(M, rr, cc, id, path):
    print(rr,cc, id, dirs[id], cdir[dirs[id]])
    for r in range(len(M)):
        l = ''
        for c, ch in enumerate(M[r]):
            if (r,c) in path:
                l += 'O'
            elif r == rr and c == cc:
                l += cdir[dirs[id]]
            else:
                l += ch
        print(l)
    print()

start = (0,0)
end = (0,0)
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            start = (r,c)
            G[r][c] = '.'
        if G[r][c] == 'E':
            end = (r,c)

print(start)
print(end)

dirs = [(0,1), (1,0), (0,-1), (-1,0)] # e,s,w,n
cdir = {(0,1):'>', (1,0):'v', (0,-1):'>', (-1,0):'^'}
idir = 0

Q = []

cost = 0
best = 1000000000


SEEN = set()
P2SEEN = set()

path = []
bestl = []
Q.append((start[0], start[1], idir, cost, path))
while len(Q):
    r, c, id, cost, path = Q.pop(0)
    #print(f'({r},{c}):{cdir[dirs[id]]} - cost {cost}')
    #printg(G,r,c,id)

    if cost < BEST[r][c]:
        BEST[r][c] = cost


    if G[r][c] == 'E':
        if cost < best:
            best = cost
        printg(G, r, c, id, path)
        print(f'*** END *** cost {cost}, best {best}')
        bestl.append((cost, path))
        continue

    SEEN.add((r, c))

    # we're here now. Try move and rotate

    # move
    dir = dirs[id]
    rr = r + dir[0]
    cc = c + dir[1]
    if G[rr][cc] != '#':
        if not (rr,cc) in SEEN or BEST[rr][cc] > cost + 1:
            #print(f'move {dir}')
            Q.append((rr,cc, id, cost + 1, path + [(rr,cc)]))
    for i in [1,3]:
        nid = (id + i)%4
        dir = dirs[nid]
        rr = r + dir[0]
        cc = c + dir[1]
        if G[rr][cc] != '#':
            if not (rr, cc) in SEEN or BEST[rr][cc] > cost + 1000 :
                #print(f'rotate {i}')
                Q.append((r,c, nid, cost + 1000, path + [(r,c)]))


S1 = best

P2SEEN = set()
for (c, p) in bestl:
    if c == best:
        print('best', best, 'len', len(p))
        for p2 in p:
            P2SEEN.add(p2)

S2 = len(P2SEEN)

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
