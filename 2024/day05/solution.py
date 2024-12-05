#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict

import sys
import re


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


with open(infile) as fin:
    rules, lines = ((fin.read().strip()).split('\n\n'))


def reorder(a, D):
    print(a)
    for r in D:
        bef = r[0]
        aft = r[1]

        if bef in a and aft in a:
            if not a.index(bef) < a.index(aft):
                print(f'swap {bef} and {aft}')
                tmp = a[a.index(bef)]
                a[a.index(bef)] = a[a.index(aft)]
                a[a.index(aft)] = tmp
                print(a)
    return a


D = []
DD = defaultdict(list)
for rule in rules.split('\n'):
    r = list(map(int,(rule.split('|'))))
    D.append(r)
    DD[r[1]].append(r[0])


for line in lines.split('\n'):
    a = list(map(int, line.split(',')))
    ra = a.copy()
    good = True
    for r in D:
        bef = r[0]
        aft = r[1]
        if bef in a and aft in a:
            if not a.index(bef) < a.index(aft):
                good = False
                break
    if good:
        S1 += a[len(a)//2]
    else:
        Q = deque(a)
        DD2 = defaultdict(list)
        for x in DD:
            if x in a:
                DD2[x] = [v for v in DD[x] if v in a]
        res = []
        while len(Q):
            elt = Q.popleft()
            if elt not in DD2 or DD2[elt] == []:
                res.append(elt)
                for x in DD2: # cleanup
                    if elt in DD2[x]:
                        DD2[x] = [v for v in DD2[x] if v != elt]
            else: # put at the end
                Q.append(elt)
        S2 += res[len(res)//2]


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
