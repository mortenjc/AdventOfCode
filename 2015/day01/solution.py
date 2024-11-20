#!/usr/local/bin/python3

import sys
from collections import Counter


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

assert len(lines) == 1

C = Counter(' '.join(lines[0]).split())

S1 = C['('] - C[')']

floor = 0
for i, c in enumerate(' '.join(lines[0]).split()):
    pos = i + 1
    floor += 1 if c == '(' else -1
    if floor == -1:
        S2 = pos
        break

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
