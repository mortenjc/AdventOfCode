#!/usr/local/bin/python3

import sys
import re
from copy import deepcopy
import numpy as np

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

M = {}
for line in lines:
    name, rest = line.split(':')
    M[name] = rest


def parse(name, h):
    if name == 'humn' and h != None:
        return int(h)

    op = M[name]
    res = op.split()
    if len(res) == 1:
        return int(res[0])
    else:
        assert len(res) == 3
        e1 = parse(res[0], h)
        e2 = parse(res[2], h)
        if name == 'root' and h != None:
            return e1 == e2
        if res[1] == '+':
            return e1 + e2
        elif res[1] == '-':
            return e1 - e2
        elif res[1] == '*':
            return e1 * e2
        elif res[1] == '/':
            return e1 // e2
        else:
            assert False
    print(res)

print('part I')
S1 = parse('root', None)

print('part II')
S2=0
i = 3678125408019
if parse('root', i):
    S2 = i


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
