#!/usr/local/bin/python3

import sys


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


def divides(lst):
    for num in lst:
        for denum in lst:
            if num == denum:
                continue
            if num/denum == num//denum:
                return num//denum

for line in lines:
    print(line)
    nums = list(map(int, line.split()))
    S1 += max(nums) - min(nums)
    S2 += divides(nums)


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
