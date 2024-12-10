#!/usr/local/bin/python3

from collections import defaultdict
import sys


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

l = list(lines[0])
print(l)

def getl(l):
    res = []
    for i, c in enumerate(l):
        if i % 2 == 0:
            num = i//2
            res += [num for x in range(int(c))]
        else:
            res += ['.' for x in range(int(c))]
    return res


a = getl(l)
j = len(a) - 1
i = 0
print(a)
while True:
    #print(i, j)
    while a[i] != '.':
        i += 1
    while a[j] == '.':
        j -= 1
    if i >= j:
        break
    a[i] = a[j]
    a[j] = '.'
    #print(i, j, ''.join(a))


for i, c in enumerate(a):
    #print(i, c)
    if c != '.':
        S1 += i * int(c)


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
