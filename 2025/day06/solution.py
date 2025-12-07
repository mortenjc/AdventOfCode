#!/usr/local/bin/python3

import numpy as np
import sys
import portion as p
from collections import defaultdict
import math


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

def srch(G, be, ed, maxl):
    R = len(G)
    start = False
    end = False
    while start == False:
        nums = 0
        for i in range(R-1):
            if G[i][be] != ' ':
                nums += 1
        if nums != 0:
            start = True
            break
        be += 1

    while end == False:
        blanks = 0
        for i in range(R-1):
            if ed >= len(G[i]) or G[i][ed] == ' ':
                blanks += 1
        if blanks == R -1:
            end = True
            break
        ed += 1

    return (be, ed)



with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


G = [[c for c in line] for line in lines]
maxl = max([len(x) for x in lines])

be = 0
ed = 0
while (True):
    be, ed = srch(G, be, ed, maxl)
    op = G[-1][be]
    assert op in ['*', '+']

    res1 = [int(''.join(G[x][be:ed])) for x in range(len(G)-1)]
    res2 = []

    for i in range(be, ed):
        n = ''
        for j in range(len(lines)-1):
            try:
                n += G[j][i]
            except:
                n += ' '
        res2.append(int(n))
    if op == '*':
        S1 += math.prod(res1)
        S2 += math.prod(res2)
    else:
        S1 += sum(res1)
        S2 += sum(res2)

    be = ed + 1
    ed = be
    if be > maxl:
        break


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
