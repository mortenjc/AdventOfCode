#!/usr/local/bin/python3

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

for r in range(R):
    for c in range(C):
        if G[r][c] == '^':
            pos = (r,c)

dirs = [(-1,0), (0,1), (1,0), (0,-1)]

def solve(G, pos):
    cdir = 0
    seen = set()
    state = set()
    seen.add(pos)
    state.add((pos, cdir))

    loop = False
    while True:
        dir = dirs[cdir]
        rr = pos[0] + dir[0]
        cc = pos[1] + dir[1]
        if not (0 <= cc < C and 0 <= rr < R):
            break

        if G[rr][cc] == '#':
            cdir = (cdir + 1) % 4
            continue

        pos = (rr,cc)
        nstate = (pos, cdir)
        if nstate in state:
            loop = True
            break
        state.add(nstate)
        seen.add(pos)
    return seen, loop


seen, loop, = solve(G, pos)
assert loop == False
S1 = len(seen)


for r in range(R):
    for c in range(C):
        if (r, c) not in seen:
            continue
        if G[r][c] == '#':
            continue
        G[r][c] = '#'
        _, loop, = solve(G, pos)
        if loop:
            S2 +=1
        G[r][c] = '.'

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
