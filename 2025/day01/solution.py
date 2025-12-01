#!/usr/local/bin/python3

import numpy as np

import sys


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


angle = 50

for line in lines:
    dir = line[0]
    ang = int(line[1:])

    assert dir in ['L', 'R']
    assert 0 < ang

    if dir == 'L':
        step = -1
    else:
        step = 1

    for i in range(abs(ang)):
        angle += step
        angle %= 100
        if angle == 0:
            S2 += 1

    if angle == 0:
        S2 -= 1
        S1 += 1




S2 += S1





print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
