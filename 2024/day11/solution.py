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

for line in lines:
    lst = line.split()

    L = defaultdict(int)
    for s in lst:
        L[s] += 1

    D = {'0':['1']}
    for i in range(75):
        NL = defaultdict(int)
        for s in L:
            mul = L[s]
            if s in D:
                val = D[s]
            elif len(s) % 2 == 0: # even
                val = [str(int(s[:len(s)//2])), str(int(s[len(s)//2:]))]
            else:
                val = [str(int(s)*2024)]
            D[s] = val
            for v in val:
                NL[v] += mul

        L = NL
        if i == 24:
            S1 = sum([L[l] for l in L])

S2 = sum([L[l] for l in L])

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
