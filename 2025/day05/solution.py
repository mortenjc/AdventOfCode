#!/usr/local/bin/python3

import numpy as np
import sys
import portion as p


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    rngs, goods = ((fin.read().strip()).split('\n\n'))


rngs = rngs.split('\n')
goods = goods.split('\n')

ranges = []
intvs = []
for rng in rngs:
    st, ed = rng.split('-')
    st = int(st)
    ed = int(ed)
    intvs.append(p.closed(st,ed))
    ranges.append([st, ed])


for good in goods:
    good = int(good)
    for r in ranges:
        if r[0] <= good <= r[1]:
            S1 += 1
            break

start = p.closed(0,0)
for intv in intvs:
    start = start | intv

for x in start[1:]:
    S2 += x.upper - x.lower +1

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
