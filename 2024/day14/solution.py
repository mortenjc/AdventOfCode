#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import sys
import re
import math


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

if infile == 'puzzle.txt':
    mx = 101
    my = 103
else:
    mx = 11
    my = 7

def makeg(robs):
    G = [['.' for x in range(mx)] for y in range(my)]
    for (x,y,_,_) in robs:
        G[y][x] = '#'
    return G

def printg(G):
    for row in G:
        print(''.join(row))
    print()



def hasline(G):
    for line in G:
        if line.count('.') > mx - 15:
            continue
        res = re.search('(#+)', ''.join(line))
        if res:
            if len(res[1]) > 15:
                return True
    return False



with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

rob = []
for line in lines:
    r = re.search('p=(.*),(.*) v=(.*),(.*)', line)
    rob.append((int(r[1]),int(r[2]),int(r[3]),int(r[4])))



def update(secs):
    for j, (x, y, vx, vy) in enumerate(rob):
        x += vx * secs
        y += vy * secs
        x = x % mx
        y = y % my
        rob[j] = (x, y, vx, vy)


xb = mx//2
yb = my//2
i = 0
while True:
    update(1)
    i += 1
    #print(i)
    if i == 100:
        cnt = defaultdict(int)
        for (x, y, vx, vy) in rob:
            if x < xb and y < yb:
                cnt[0] += 1
            elif x > xb and y < yb:
                cnt[1] += 1
            elif x < xb and y > yb:
                cnt[2] += 1
            elif x > xb and y > yb:
                cnt[3] += 1
        S1 = math.prod(cnt.values())

    G = makeg(rob)
    if hasline(G):
        printg(G)
        S2 = i
        break


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
