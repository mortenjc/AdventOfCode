#!/usr/local/bin/python3

import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


def fuel(n):
    f = 0
    while True:
        df = n//3 -2
        if df <=0:
            break
        f += df
        n = df
    return f


for l in lines:
    S1 += int(l)//3 - 2
    S2 += fuel(int(l))

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
