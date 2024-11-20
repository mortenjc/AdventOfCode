#!/usr/local/bin/python3

import sys
from collections import deque as de

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

#print(G)
#print(F)

Q=de([(0,  (),  'AA', 0)])
v=set()
best = 0

while Q:
    t, open, pos, flow = Q.popleft()
    print(t, open, pos, flow)
    if t==30:
        best = max(best, flow)
        continue
    if (open, pos) in v:
        continue # state seen before, ignore

    v.add((open, pos)) # remember current state
    #print('# ', open, pos)

    # sum up the current total flow we will have at t + 1
    for i in open:
        flow+=F[i]

    # always open closed valve first if not 0 flow
    if F[pos] != 0:
        if pos not in open:
            Q.append((t + 1, tuple(list(open)+[pos]), pos, flow))

    # then visit adjacent
    for adj in G[pos]:
        Q.append((t + 1, open, adj, flow))

S1 = best

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
