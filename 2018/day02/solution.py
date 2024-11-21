#!/usr/local/bin/python3

import sys
from collections import defaultdict


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

c2 = 0
c3 = 0
for line in lines:
    d = defaultdict(int)
    for c in line:
        d[c] += 1
    if 2 in d.values():
        c2 += 1
    if 3 in d.values():
        c3 += 1

S1 = c2 * c3


def diff(s1, s2):
    assert len(s1) == len(s2)
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count == 1


def rem(s1, s2):
    res = ''
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            res += s1[i]
    return res


l = len(lines)
done = False
for i in range(l-1):
    for j in range(i+1, l):
        ss1 = lines[i]
        ss2 = lines[j]
        if diff(ss1, ss2):
            S2 = rem(ss1, ss2)
            done = True
            break
    if done:
        break



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
