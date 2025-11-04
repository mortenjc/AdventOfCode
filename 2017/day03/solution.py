#!/usr/local/bin/python3

import sys
import math as m


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

def ranges(r):
    if r == 1:
        return 1, 1, 1, 1, 1
    end = r ** 2
    start = end - 2*r - 2*(r-2) + 1

    mind = (r-1)//2
    maxd = r -1
    return r, start, end, mind, maxd


for r in range(1, 10, 2):
    print(ranges(r))



n = 289326

def getR(n):
    r = 1
    while True:
        r, st, ed, mi, ma = ranges(r)

        if st <= n <= ed:
            print(f'found R {r}')
            return r, st, ed, mi, ma
        r += 2

r, st, ed, mi, ma = getR(n)
print(r, st, ed, mi, ma)

cur = ed
d = ma
dec = True
while True:
    if n == cur:
        print(n, d)
        S1 = d
        break
    cur -= 1
    if dec:
        d -= 1
        if d == mi:
            dec = False
    else:
        d += 1
        if d == ma:
            dec = True


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
