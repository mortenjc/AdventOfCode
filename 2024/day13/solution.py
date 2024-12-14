#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import sys
import re
import sympy as sym


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n\n'))

# G = [[l for l in x] for x in lines]
# R = len(G)
# C = len(G[0])

for block in lines:
    a, b, p = block.split('\n')
    res = re.search("X(.*), Y(.*)", a)
    a = (int(res[1]), int(res[2]))
    res = re.search("X(.*), Y(.*)", b)
    b = (int(res[1]), int(res[2]))
    res = re.search("X=(.*), Y=(.*)", p)
    p = (int(res[1]), int(res[2]))


    x,y = sym.symbols('x,y', integer=True)
    eq1 = sym.Eq(x*a[0] + y*b[0], 10000000000000+p[0])
    eq2 = sym.Eq(x*a[1] + y*b[1], 10000000000000+p[1])
    result = sym.solve([eq1,eq2],(x,y))

    if result != []:
        rx = result[x]
        ry = result[y]
        S2 += 3*rx + ry

    done = False
    for ba in range(100):
        for bb in range(100):
            if (ba*a[0] + bb*b[0] == p[0]) and (ba*a[1] + bb*b[1] == p[1]):
                done = True
                S1 += 3*(ba) + (bb)
                break
        if done:
            break



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
