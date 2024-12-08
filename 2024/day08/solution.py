#!/usr/local/bin/python3

from collections import defaultdict
import sys


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


G = [[x for x in l] for l in lines]
R = len(G)
C = len(G[0])

D = defaultdict(list)
seen = set()
seen2 = set()

for r in range(R):
    for c in range(C):
        ch = G[r][c]
        if ch != '.' and ch !='#':
            D[ch].append((r,c))
            seen2.add((r,c))

for d in D:
    lst = D[d]
    if len(lst) < 2:
        continue
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                continue
            done = False
            dr = lst[j][0] - lst[i][0]
            dc = lst[j][1] - lst[i][1]
            nr = lst[i][0] + dr
            nc = lst[i][1] + dc

            if 0 <= nr + dr < R and 0 <= nc + dc < C:
                seen.add((nr + dr,nc + dc))

            while not done:
                if not (0 <= nr < R and 0 <= nc < C):
                    done = True
                    break
                seen2.add((nr,nc))
                nr = nr + dr
                nc = nc + dc

S1 = len(seen)
S2  = len(seen2)

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
