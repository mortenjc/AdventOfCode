#!/usr/local/bin/python3

import sys
#from collections import deque
import functools


#-------------------------------------------------------------------------------

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

G = {} # graph
F = {} # flow
for line in lines:
    line = line.replace(',', '')
    words = line.split()
    node = words[1]
    flow = int(words[4][5:-1])
    conns = words[9:]
    #print(node, flow, conns)
    F[node] = flow
    G[node] = conns

print(G)


@functools.lru_cache(maxsize=None)
def maxflow(cur, opened, min_left):
    if min_left <= 0:
        return 0
    #print(opened, timeleft)
    best = 0
    val = F[pos] * (min_left - 1)

    for





S1 = maxflow('AA', (), 30, ('AA',))








print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
