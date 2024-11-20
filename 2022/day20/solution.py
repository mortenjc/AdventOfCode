#!/usr/local/bin/python3

import sys
from copy import deepcopy

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

NUMS = []
NUMS2 = []
mix = {}
mix2 = {}
for i, line in enumerate(lines):
    val = int(line)
    NUMS.append(val)
    mix[i] = val
    NUMS2.append(val * 811589153)
    mix2[i] = val * 811589153

def shuffle(mymix, numbers):
    l = len(numbers)
    msg = []
    for i, n in enumerate(numbers):
        msg.append([n, False])

    for i in mymix:
        val = mymix[i]
        if val == 0:
            continue
        mi = msg.index([val, False])
        msg[mi] = [val, True]
        ni = (mi + val) % (l-1)
        msg.insert(ni, msg.pop(mi))

    return [x for [x, B] in msg]


S1 = 0
S2 = 0
r = 1
M = mix
res = NUMS
for part in [1, 2]:
    if part == 2:
        r = 10
        M = mix2
        res = NUMS2

    for i in range(r):
        res = shuffle(M, res)
        print(f'part {part}, round {i+1}: {res[:4]} ...')

    a = [ res[(D + res.index(0))%len(res)] for D in [1000, 2000, 3000] ]
    if part == 1:
        S1 = sum(a)
    else:
        S2 = sum(a)

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
