#!/usr/local/bin/python3

import numpy as np

import sys
import re

def has_repeats(str):
    repeats = 0
    l = len(str)
    if str[:l//2] * 2 == str:
        return True
    return False
    # for i in range(l//2):
    #     if l % (i+1) == 0:
    #         sstr = str[:i+1]
    #         print(f'len {i+1} divides {str}({l})')
    #         if sstr * (l//(i+1)) == str:
    #             repeats +=1
    # return repeats

def has_multiple_repeats(str):
    repeats = 0
    l = len(str)
    for i in range(l//2):
        if l % (i+1) == 0:
            sstr = str[:i+1]
            #print(f'len {i+1} divides {str}({l})')
            if sstr * (l//(i+1)) == str:
                return True


    return False

a = has_repeats('11111')
assert a == False
a = has_repeats('1111')
assert a == True
a = has_repeats('1212')
assert a == True
a = has_repeats('1432')
assert a == False


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))


ranges = lines[0].split(',')

for rng in ranges:
    #rng = rng[1:-1]
    #print(rng)
    ep = rng.split('-')
    ep =list(map(int,ep))
    #print(ep)
    for i in range(ep[0], ep[1]+1):
        print(i)
        if has_repeats(str(i)):
            S1 += i
        if has_multiple_repeats(str(i)):
            S2 += i



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
