#!/usr/local/bin/python3

import numpy as np
import sys



def has_repeats(str: str) -> []:
    r2 = False
    rn = False
    l = len(str)
    for i in range(l//2):
        if l % (i+1) == 0:
            sstr = str[:i+1]
            if sstr * (l//(i+1)) == str:
                if 2*len(sstr) == l:
                    r2 = True
                rn = True

    return [r2, rn]


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


ranges = lines[0].split(',')

for rng in ranges:
    ep =list(map(int, rng.split('-')))

    for i in range(ep[0], ep[1]+1):
        r2, rn = has_repeats(str(i))
        if r2:
            S1 += i
        if rn:
            S2 += i

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
