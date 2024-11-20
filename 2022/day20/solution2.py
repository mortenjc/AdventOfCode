#!/usr/local/bin/python3

import sys

class Node:
    def __init__(self, n):
        self.n = n
        self.l = None
        self.r = None

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

with open(infile) as fin:
    num = [int(n) for n in (fin.read().strip()).split('\n')]


def solve(nums, part):
    x = [Node(int(n)) for n in nums]
    m = len(x)-1
    for i in range(len(x)):
        x[i].r = x[(i+1)%len(x)]
        x[i].l = x[(i-1)%len(x)]
        if part == 2:
            x[i].n *= 811589153

    for _ in range(1 if part == 1 else 10):
        for k in x:
            if k.n == 0:
                z = k
                continue
            p = k
            if k.n > 0:
                for _ in range(k.n % m):
                    p = p.r
            if k.n < 0:
                for _ in range((-k.n + 1) % m):
                    p = p.l
            if k == p:
                continue
            k.l.r = k.r
            k.r.l = k.l
            p.r.l = k
            k.r = p.r
            k.l = p
            p.r = k

    ans = 0
    for _ in range(3):
        for _ in range(1000):
            z = z.r
        ans+= z.n
    return ans

S1 = solve(num, 1)
S2 = solve(num, 2)

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
