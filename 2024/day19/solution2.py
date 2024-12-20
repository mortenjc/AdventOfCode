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

designs = lines[0].split(',')

designs = [x.strip() for x in designs]





def works(l):
    w = []
    found = False
    for des in designs:
        if len(des) > len(l):
            continue
        if l.startswith(des):
            print('  design', des, 'matches')
            if l == des:
                found = True
            #print('append', l[len(des):])
            w.append(l[len(des):])
    return w, found


for line in lines[2:]:
    print(f'*** {line} ***')
    SEEN = set()
    Q = []
    cnt = 0
    Q.append(line)
    while len(Q):
        l = Q.pop(0)
        if l == []:
            continue
        if l in SEEN:
            print('pruned', l)
            continue
        SEEN.add(l)
        print(f'POP: {l} ({len(l)})')

        lst, done = works(l)
        if done:
            cnt += 1
        for l2 in lst:
            Q.append(l2)
    print(cnt)
    S2 += cnt



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
