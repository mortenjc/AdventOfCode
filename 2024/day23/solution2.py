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
NN = []

for line in lines:
    a,b = line.split('-')
    if not a in V:
        V[a] = len(V)
        NN.append(a)
    if not a in V:
        V[a] = len(V)
        NN.append(b)
    E[a].append(b)
    E[b].append(a)
NV = len(V)

# print(V)
# print(E)
#print(NV)


SEEN = set()
for v1 in V:
    for v2 in E[v1]:
        for v3 in E[v1]:
            if v2==v3 :
                continue

            if tuple(sorted([v1, v2, v3])) in SEEN:
                continue
            SEEN.add(tuple(sorted([v1, v2, v3])))

            if v1 in E[v2] and v1 in E[v3] and v2 in E[v3]:
                if any([x.startswith('t') for x in [v1, v2, v3]]):
                    S1 += 1





DG = digraph.Digraph(NV)

for vert in V:
    for other in E[vert]:
        #print(vert, other)
        DG.add_edge(V[vert], V[other])

SCC = ksscc.KnSSCC(DG)
print(SCC.id)
print(f'DG has {SCC.get_count()} components')



fig = draw.Draw(digraph=True)
fig.set_names(NN)
fig.node_attr(fontsize='10')
fig.draw(DG)








print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
