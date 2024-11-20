#!/usr/local/bin/python3

import sys
# from copy import deepcopy
from collections import deque
# from collections import defaultdict
# import functools
# import numpy as np
# from PIL import Image
# import networkx as nx
# import re
from graph_tools.all import *


def sortmoves(m):
    test = {}
    for i in m:
        test[F[i]] = i
    return [test[i] for i in sorted(test)]


def visit(pos, Q, G, F, V):
    print('Visiting ', pos)
    flow = 0
    if not pos in V:
        V.add(pos)
        flow = F[pos]
    return G[pos], flow


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


G = {}
F = {}
ug = Graph(directed=False)
v_name = ug.new_vertex_property("str")
#v_flow = ug.new_vertex_property("int")
for line in lines:
    l2 = line.replace(',', '')
    words = l2.split()
    v = words[1]
    f = int(words[4][5:-1])
    c = words[9:]
    print(v, f, c)
    F[v] = f
    G[v] = c
    for m in c:
        v1 = ug.add_vertex(1)
        v_name[v1]=v
        v2 = ug.add_vertex(1)
        v_name[v2]=m
        ug.add_edge(v1, v2)

graph_draw(ug, vertex_text=ug.vertex_index, output="two-nodes.pdf")

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
