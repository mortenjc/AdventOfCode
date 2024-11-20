#!/usr/local/bin/python3

import sys
import re
from copy import deepcopy
import numpy as np

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

x = [x.split(':') for x in lines]

root = 0
while root == 0:
    nx = []
    for v, e in x:
        try:
            exec(f'{v} = {e}')
        except:
            nx.append([v,e])
    x = nx

S1 = int(root)
S2 = 0


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
