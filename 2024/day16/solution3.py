#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import sys
import re
import math
import heapq



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


dirs = [(0,1), (1,0), (0,-1), (-1,0)] # e,s,w,n


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

start = (0,0)
end = (0,0)
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            sr,sc = (r,c)
            G[r][c] = '.'
        if G[r][c] == 'E':
            er,ec = (r,c)

print(sr, sc)
print(er, ec)


# return adjacent nodes to current location
def adjs(loc):
    r, c, di = loc
    yield 1000, (r, c, (di+1)%4)
    yield 1000, (r, c, (di-1)%4)
    dr, dc = dirs[di]
    rr, cc = r+dr, c+dc
    if G[rr][cc] != '#':
        yield 1, (rr, cc, di)



pq = []
di = 0
S1 = 1000000000
heapq.heappush(pq, (0, (sr, sc, di)))
dists = defaultdict(lambda: float('inf'))
while pq:
    dist, adj = heapq.heappop(pq)
    r, c, di = adj
    if r == er and c == ec:
        S1 = min(dist, S1)
        continue

    for d, adj2 in adjs((r,c,di)):
        if dist + d < dists[adj2]:
            dists[adj2] = dist + d
            heapq.heappush(pq, (dist + d, adj2))



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
