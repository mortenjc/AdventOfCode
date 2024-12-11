#!/usr/local/bin/python3

import sys
from collections import defaultdict

S1 = 0
S2 = 0

ifile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'

with open(ifile) as fin:
    lines = ((fin.read().strip()).split('\n'))

nums = list(map(int, lines[0].split(',')))

D = defaultdict(int)
for i in nums:
    D[i] += 1

for i in range(256):
    ND = defaultdict(int)
    for j in range(8):
        ND[j] = D[j+1]
    ND[6] += D[0]
    ND[8] = D[0]

    D = ND
    if i == 79:
        S1 = sum([D[x] for x in D])

S2 = sum([D[x] for x in D])

print("------------- A -------------")
print('S1', S1)
print("------------- B -------------")
print('S2', S2)
print("-----------------------------")
