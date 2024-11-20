#!/usr/local/bin/python3

import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

text = lines[0]
l = len(text)
l2 = l//2
for i in range(len(text)):
    if text[i] == text[(i+1)%l]:
        S1 += int(text[i])
    if text[i] == text[(i+l2)%l]:
        S2 += int(text[i])

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
