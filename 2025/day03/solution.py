#!/usr/local/bin/python3

import numpy as np
import sys

def pprint(narr, iarr):
    res = ""
    for i, n in enumerate(narr):
        if i in iarr:
            res += f'({n})'
        else:
            res += f'{n}'
    print(' ', res)


def move(narr, ival, st, ed):
    best = 0
    besti = -1
    if st >= ed:
        return (best, besti, 1)
    for i in range(ed-1, st -1, -1):
        n = narr[i]
        if n>= ival:
            if n>= best:
                best = n
                besti = i
    return (best, besti, 0)


def getmax(s1):
    max = 0
    for i in range(len(s1) -1):
        for j in range(i+1, len(s1)):
            n = s1[i] + s1[j]
            if int(n) > max:
                max = int(n)
    print('max', max)
    return max

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0
sz = 12

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

for line in lines:
    S1 += getmax(line)

    nums = [int(x) for x in line]
    l = len(nums)
    idxs = [x for x in range(l-sz, l) ]
    assert len(idxs) == sz
    pprint(nums, idxs)

    st = 0
    ed = len(nums) - sz
    for n in range(sz):
        val = nums[idxs[n]]
        b, bi, end = move(nums, val, st, ed)
        if bi == -1:
            break
        idxs[n] = bi
        st = bi + 1
        ed += 1

    pprint(nums, idxs)


    res = ""
    for i in range(sz):
        res += str(nums[idxs[i]])
    print('JOLT', res)
    S2 += int(res)

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
