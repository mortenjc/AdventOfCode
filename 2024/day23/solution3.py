#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import sys
import re
import math
import random
import heapq

from graphe.digraph import digraph
from graphe.digraph import ksscc
from graphe import draw




infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

if infile == 'puzzle.txt':
    pass
else:
    pass

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))



V = {}
E = defaultdict(list)

for line in lines:
    a,b = line.split('-')
    E[a].append(b)
    E[b].append(a)
NV = len(V)

a = list(E.keys())
for t in range(10000):
    random.shuffle(a)
    match = True
    group = []
    for x in










print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
