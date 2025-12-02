#!/usr/local/bin/python3

import numpy as np

import sys


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


for line in lines:
    print(line)


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
