#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)


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


def ways1(sr, sc):
    Q = deque([(sr,sc)])
    seen = set()
    ans = 0
    while Q:
        r, c = Q.popleft()
        if (r,c) in seen:
            continue
        seen.add((r, c))
        if G[r][c] == 0:
            ans += 1
        for dr, dc in dirs:
            rr = r + dr
            cc = c + dc
            if 0<=rr<R and 0<=cc<C and G[rr][cc] == G[r][c] - 1:
                Q.append((rr,cc))
    return ans


# Dynamic programming
DP = {}
def ways(r,c):
    if G[r][c] == 0:
        return 1
    if (r,c) in DP:
        return DP[(r,c)]
    ans = 0
    for dr,dc in dirs:
        rr = r + dr
        cc = c + dc
        if 0<=rr<R and 0<=cc<C and G[rr][cc] == G[r][c] - 1:
            ans += ways(rr,cc)
    DP[(r,c)] = ans
    return ans


for r in range(R):
    for c in range(C):
        if G[r][c] == 9:
            S1 += ways1(r,c)
            S2 += ways(r,c)

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
