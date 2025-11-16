#!/usr/local/bin/python3

import sys
from collections import defaultdict
import re


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

claims = defaultdict(int)
sz = defaultdict(int)
claimlist = defaultdict(list)

reg = re.compile('#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)')

total = len(lines)
clset = set()
for line in lines:
    res = re.match(reg, line)
    cl = int(res.group(1))
    lo = int(res.group(2))
    to = int(res.group(3))
    w = int(res.group(4))
    h = int(res.group(5))
    sz[cl] = w * h
    clset.add(cl)
    for nx in range(w):
        for ny in range(h):
            pos = (lo + nx, to + ny)
            claims[pos] += 1
            claimlist[pos].append(cl)

S1 = len([x for x in claims if claims[x] >= 2])

ignore = set()
for x in claimlist:
    b = claimlist[x]
    if len(b) > 1:
        for y in b:
            ignore.add(y)

S2 = list(clset - ignore)[0]



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
