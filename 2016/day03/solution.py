#!/usr/local/bin/python3

import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

for line in lines:
    a = list(map(int, line.split()))
    a.sort()
    if a[0] + a[1] > a[2]:
        S1 += 1


assert len(lines)/3 == len(lines)//3
for i in range(3):
    for l in range(len(lines)//3):
        print(f'l {l}, i {i}')
        a = int(lines[l*3].split()[i])
        b = int(lines[l*3+1].split()[i])
        c = int(lines[l*3+2].split()[i])
        print(a,b,c)
        x = [a,b,c]
        x.sort()
        if x[0] + x[1] > x[2]:
            S2 += 1


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
