#!/usr/local/bin/python3

import sys
#import defaultdict
#from copy import deepcopy
import functools
#from collections import deque


def compare(l, r):
    if isinstance(l, list) and isinstance(r, int):
        r = [r]

    if isinstance(l, int) and isinstance(r, list):
        l = [l]

    if isinstance(l, int) and isinstance(r, int):
        if l == r:
            return 0
        if l < r:
            return -1
        else:
            return 1

    if isinstance(l, list) and isinstance(r, list):
        i = 0
        while i < len(l) and i < len(r):
            c = compare(l[i], r[i])
            if c == -1:
                return -1
            if c == 1:
                return 1
            i += 1

        if i == len(l) and i < len(r):
            return -1
        elif i < len(l) and i == len(r):
            return 1
        else:
            return 0



infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

with open(infile) as fin:
        lines = ((fin.read().strip()).split('\n\n'))

# part 1
S1 = 0
for i, line in enumerate(lines):
    pair = i + 1
    l, r = map(eval, line.replace('\n', ' ').split())
    if compare(l, r) == -1:
        S1 += pair


#part 2
all = []
for line in lines:
    first, second = line.replace('\n', ' ').split()
    all.append(eval(first))
    all.append(eval(second))
all.append([[2]])
all.append([[6]])

sorted(all, key=functools.cmp_to_key(compare))

S2 = 1
for i, val in enumerate(all):
    if val == [[2]] or val == [[6]]:
        S2 = S2 * (i + 1)

print("------------- A -------------")
print(f'S1 {S1}')
print("------------- B -------------")
print(f'S2 {S2}')
print("-----------------------------")
