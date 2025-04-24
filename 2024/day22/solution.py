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
    N = 100
else:
    N = 50

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

a = []
for line in lines:
    a.append(int(line))

delta = [[] for x in range(len(a))]
for j in range(2000):
    for i in range(len(a)):
        old = a[i]
        sn = gen(old)
        #print(j, i, old, sn)
        delta[i].append(old - sn)
        delta[i] = delta[i][-4:]
        if delta[i] == [-2,1,-1,3]:
            print('XX',i, j)
        a[i] = sn
        #print(j, i, delta)



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
