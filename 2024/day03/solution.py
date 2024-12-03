#!/usr/local/bin/python3

#from collections import deque
from collections import defaultdict

import sys
import re


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

enable = True

def getprod(text, enable):
    ps1 = 0
    ps2 = 0

    x =re.findall('(don\'t\(\))|(do\(\))|(mul\(([0-9]+),([0-9]+)\))' , text)

    print(x)

    for  dont,do  ,op, a,b in x:
        print(op)
        if a!= '' and b !='':
            prod = int(a) * int(b)
            ps1 += prod
            if enable:
                ps2 += prod
                continue

        if dont  != '':
            print('state change disable')
            enable = False
            continue
        if do  != '':
            print('state change enable')
            enable = True
            continue

    return ps1, ps2, enable


with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

sub = 0
state = True
for line in lines:

    ps1, ps2, state = getprod(line, state)
    S1 += ps1
    S2 += ps2


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
