#!/usr/local/bin/python3

#from collections import deque
from collections import defaultdict

import sys

def isgood(l):
    asc_dec = (l == sorted(l) or l == sorted(l, reverse=True))
    ok = True
    for i in range(len(l)-1):
        if abs(l[i] - l[i+1]) not in [1,2,3]:
            ok = False
            break

    return (asc_dec and ok)



infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


for line in lines:
    l = list(map(int, line.split()))

    if isgood(l):
        S1 += 1

    for i in range(len(l)):
        if isgood(l[:i] + l[i+1:]):
            S2 += 1
            break


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
