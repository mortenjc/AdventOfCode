#!/usr/local/bin/python3

import sys
#import defaultdict
from copy import deepcopy
from collections import deque

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

# init
G = lines
R = len(G)
C = len(G[0])

ele = [[0 for _ in range(C)] for _ in range(R)]
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            ele[r][c]= 1
        elif G[r][c] == 'E':
            ele[r][c] = 26
        else:
            ele[r][c] = ord(G[r][c]) - ord('a') + 1


def solve(G, ele, part):
    Q = deque()
    # setup initial conditions
    for r in range(R):
        for c in range(C):
            if part == 1:
                if G[r][c] == 'S':
                    Q.append(((r,c), 0))
            else:
                if ele[r][c] == 1:
                    Q.append(((r,c), 0))

    # iterate
    S = set()
    while Q:
        (r, c), d = Q.popleft()
        if (r,c) in S:
            continue
        S.add((r,c))
        if G[r][c]== 'E':
            return d
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            rr = r + dr
            cc = c + dc
            if 0<=rr<R and 0<=cc<C and ele[rr][cc]<=1+ele[r][c]:
                Q.append(((rr,cc), d+1))

print("------------- A -------------")
print(solve(G, ele, 1))
print("------------- B -------------")
print(solve(G, ele, 2))
print("-----------------------------")
