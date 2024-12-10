#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import sys


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

G = [[int(l) for l in x] for x in lines]
R = len(G)
C = len(G[0])

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

print(G)
Q = deque()
start = []
for r in range(R):
    for c in range(C):
        if G[r][c] == 0:
            Q.append((r,c,r,c,0))

for x in Q:
    print(x)

D = defaultdict(int)
seen = set()
while len(Q):
    sr, sc, r, c, n = Q.popleft()
    print(sr, sc, r, c, n)
    if (sr, sc, r,c, n) in seen:
        continue
    seen.add((sr, sc, r,c, n))
    if n == 9:
        D[(sr,sc)] += 1
        S1 += 1
        continue
    n += 1
    for d in dirs:
        rr = r + d[0]
        cc = c + d[1]
        if not (0 <= rr < R and 0 <= cc < C):
            continue
        if G[rr][cc] == n:
            Q.append((sr,sc,rr,cc,n))

print(D)


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
