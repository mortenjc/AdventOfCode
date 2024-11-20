#!/usr/local/bin/python3

import sys
from copy import deepcopy
from collections import deque
#from collections import defaultdict
# import functools
# import numpy as np
# from PIL import Image
#import re


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

if infile == 'puzzle.txt':
    pass
else:
    pass

with open(infile) as fin:
    lines = ((fin.read().strip()).replace('.', ' ').split('\n'))

BP = []
for line in lines:
    a = line.split()
    cor = int(a[6])
    ccl = int(a[12])
    cob1 = int(a[18])
    cob2 = int(a[21])
    cge1 = int(a[27])
    cge2 = int(a[30])
    BP.append([cor, ccl, cob1, cob2, cge1, cge2])


#
         # costs
def solve(cor, ccl, cob1, cob2, cge1, cge2, time):
    maxor = max(cor, ccl, cob1, cge1)
    best = 0
    S = (0,0,0,0, 1,0,0,0, time)
    SEEN = set()
    Q = deque([S])
    while Q:
        o, cl, ob, ge, r1, r2, r3, r4, t = Q.popleft()
        best = max(best, ge)
        if t <= 0:
            continue

        # if r1 >= maxor:
        #     r1 = maxor
        # if r2 >= max()

        state = (o, cl, ob, ge, r1, r2, r3, r4)
        if state in SEEN:
            continue
        SEEN.add(state)

        if len(SEEN) %10000000 == 0:
            print(t, best, state)

        #assert o>=0 and cl>=0 and ob>=0 and ge>=0, state

        Q.append((o+r1, cl+r2, ob+r3, ge+r4, r1, r2, r3, r4, t-1))

        # only consider two best matches
        app = 0
        if o >= cge1 and ob >= cge2:
            Q.append((o-cge1+r1, cl+r2, ob-cge2+r3, ge+r4, r1, r2, r3, r4+1, t-1))
        else:
            if o >= cob1 and cl >= cob2 and r3 < cge2:
                Q.append((o-cob1+r1, cl-cob2+r2, ob+r3, ge+r4, r1, r2, r3+1, r4, t-1))
                app += 1
            if o >= ccl and r2 < cob2:
                Q.append((o-ccl +r1, cl+r2, ob+r3, ge+r4, r1, r2+1, r3, r4, t-1))
                app += 1
            if o >= cor and r1 < maxor and app < 2:
                Q.append((o-cor+r1, cl+r2, ob+r3, ge+r4, r1+1, r2, r3, r4, t-1))

    return best

print('part I')
S1 = 0
for i, b in enumerate(BP):
    cor, ccl, cob1, cob2, cge1, cge2  = b
    res = solve(cor, ccl, cob1, cob2, cge1, cge2, 24)
    print('S1: Blueprint ', i, ' res ', res)
    S1 += res * (i+1)
    print('S1 (running)', S1)

print('part II')
S2 = 1
for i, b in enumerate(BP[:3]):
    cor, ccl, cob1, cob2, cge1, cge2  = b
    res = solve(cor, ccl, cob1, cob2, cge1, cge2, 32)
    print('S2: Blueprint ', i, ' res ', res)
    S2 *= res
    print('S2 (running)', S2)

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
