#!/usr/local/bin/python3

#from collections import deque
from collections import defaultdict

import sys

def isgood(l):
    inc = 0
    dec = 0
    diff = 0
    for i in range(len(l)-1):
        a = l[i]
        b = l[i+1]
        if a > b:
            inc += 1
        if a < b:
            dec += 1
        if abs(a-b) in [1, 2, 3]:
            diff += 1
    if (inc == len(l) -1 or dec == len(l) -1 ) and diff == len(l) -1:
        return True
    return False



infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

l1 = []
l2 = []

for line in lines:
    l = list(map(int,(line.split())))

    if isgood(l):
        S1 += 1

    for i in range(len(l)):
        tmp = l.copy()
        tmp.pop(i)
        if isgood(tmp):
            S2 += 1
            break


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
