#!/usr/local/bin/python3

#from collections import deque
#from collections import defaultdict
from collections import Counter

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


dirs = [(1,0), (-1,0), (0, 1), (0,-1), (1,-1), (1,1), (-1,1), (-1,-1)]

def findstr(G, c, r, s1):
    n = 0
    AS = []

    for dir in dirs:
        cc = c
        rr = r
        dc = dir[0]
        dr = dir[1]
        cnt = 0
        tmppos = ''
        for i in range(len(s1)):
            #print(f'    {i=}, ({cc},{rr}), {G[cc][rr]} {s1[i]}, {cnt=}')
            if G[cc][rr] == s1[i]:
                if s1[i] == 'A' and dir in [(1, -1), (1,1), (-1,1), (-1,-1)]:
                    tmppos = (cc,rr)
                #print('  ch match')
                cnt += 1

                cc += dc
                rr += dr
                #print(f'  {dc=} {dr=} {cc=} {rr=}')
                if not ((0 <= cc < C) and (0 <= rr < R)):
                    #print(f'   skip {cc} {rr}')
                    break
            else:
                break

        if cnt == len(s1):
            if tmppos != '':
                AS.append(tmppos)
            n += 1
    return n, AS


AS = []
for c in range(C):
    for r in range(R):
        n, _ = findstr(G, c, r, 'XMAS')
        S1 += n

        n, a = findstr(G, c, r, 'MAS')
        for x in a:
            AS.append(x)

c = Counter(AS)
S2 = sum([1 for x in c if c[x] >=2])


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
