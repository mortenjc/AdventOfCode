#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import sys
import re
import math
import random
import heapq

from graphe.graph import graph
from graphe.graph import bfs
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
        print('adding', a)
        V[a] = len(V)
        NN.append(a)
    if not a in V:
        print('adding', b)
        V[a] = len(V)
        NN.append(b)
    E[a].append(b)

print(V)
print(E)
NV = len(V)
print(NV)


MG = graph.Graph(NV)

SEEN = set()

for vert in V:
    print(E[vert])
    for edge in E[vert]:
        a = V[vert]
        b = V[edge]
        if (a,b) in SEEN:
            continue
        SEEN.add((a,b))
        SEEN.add((b,a))
        print(vert, a,edge,b)
        MG.add_edge(a,b)



# for adj in E:
#     for other in E[adj]:
#         a = ni[adj]
#         b = ni[other]
#         if (a,b) in SEEN:
#             continue
#         SEEN.add((a,b))
#         SEEN.add((b,a))
#         MG.add_edge(a, b)


fig = draw.Draw()
fig.set_names(NN)
fig.node_attr(style='', fontcolor='black', fontsize='10')
fig.draw(MG)







print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
