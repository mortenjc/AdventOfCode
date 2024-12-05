#!/usr/local/bin/python3

#from collections import deque
from collections import defaultdict

import sys
import re


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


G= [[x for x in l] for l in lines]
R = len(G)
C = len(G[0])

print(G)

dirs = [(1,0), (-1,0), (0, 1), (0, -1), (1, -1), (1,1), (-1,1), (-1,-1)]

def findmas(G, c, r):
    assert G[c][r] == 'X'
    print(f'start at {c} {r}')
    p = 'MAS'
    n = 0
    AS = []
    for dir in dirs:
        dc = dir[0]
        dr = dir[1]
        cc = c
        rr = r
        print(f'  dir: {dir}')
        cnt = 0
        for i in range(3):
            cc += dc
            rr += dr
            #print(f'  {dc=} {dr=} {cc=} {rr=}')
            if not ((0 <= cc < C) and (0 <= rr < R)):
                print(f'   skip {cc} {rr}')
                break

            print(f'    {i=}, ({cc},{rr}), {G[cc][rr]} {p[i]}, {cnt=}')
            if G[cc][rr] == p[i]:
                if p[i] == 'A':
                    tmppos = (cc,rr)
                #print('  ch match')
                cnt += 1
            else:
                break
        if cnt == 3:
            print(f'    full match ({c},{r}), dir {dir}')
            AS.append(tmppos)
            n += 1
    return n, AS


for c in range(C):
    for r in range(R):
        ch = G[c][r]
        if ch != 'X':
            continue
        S1 += findmas(G, c, r)



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
