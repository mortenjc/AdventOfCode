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
    init, instr = ((fin.read().strip()).split('\n\n'))

R = {}

for l in init.split('\n'):

    var, val = l.split(':')

    val = int(val)
    R[var] = val

D = deque()

for l in instr.split('\n'):
    va, opr, vb, _, dst = l.split(' ')
    D.append((va, opr, vb, dst))

while len(D):
    va, opr, vb, dst = D.popleft()
    if dst in R:
        print(R)
        print(va, opr, vb, dst)
        assert False

    if not (va in R and vb in R):
        D.append((va, opr, vb, dst ))
        continue



    a,b = R[va], R[vb]
    if opr == 'XOR':
        res = a ^ b
    elif opr == 'OR':
        res = a | b
    elif opr == 'AND':
        res = a & b
    else:
        assert False
    R[dst] = res

a = []
for r in R:
    if r.startswith('z'):
        a.append(r)

for x in sorted(a):
    print(x, R[x])

res = 0
for x in R:
    if x.startswith('z'):
        sh = int(x[1:])
        tmp = R[x]<<sh
        res += tmp
        print(f'{x}:{R[x]}: exp {sh}, tmp {tmp}, res {res}')


S1 = res

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
