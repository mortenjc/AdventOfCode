#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import sys
import re
import math
import random
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



def gen(sn):
    n = sn * 64
    sn = (sn ^ n) % 16777216
    n = sn // 32
    sn = (sn ^ n) % 16777216
    n = sn * 2048
    sn = (sn ^ n) % 16777216
    return sn


sns = []
for line in lines:
    sns.append(int(line))


n = len(sns)
sold = [0 for x in range(n)]
trades = 2000

values = [[0 for x in range(trades)] for y in range(n)]
dicts = [defaultdict(int) for y in range(n)]
delta = [[] for x in range(n)]

patts = set()


D = {}
SEEN = set()
for t in range(trades):
    for i in range(n):
        old = sns[i]
        if old in SEEN:
            sn = D[old]
        else:
            sn = gen(old)
            D[old] = sn
            SEEN.add(old)
        sns[i] = sn
        price = old % 10
        values[i][t] = price

        if t != 0:
            delta[i].append(values[i][t]-values[i][t-1])
            delta[i] = delta[i][-4:]
            
            if tuple(delta[i]) not in dicts[i] and len(delta[i]) == 4:
                dicts[i][tuple(delta[i])] += price
                patts.add(tuple(delta[i]))


#
maxval = 0
for patt in patts:
    #print(patt)
    val = 0
    for i in range(n):
        val += dicts[i][patt]
    if val > maxval:
        print(val, patt)
        maxval = val





print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
