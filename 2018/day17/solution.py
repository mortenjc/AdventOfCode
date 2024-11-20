#!/usr/local/bin/python3

import sys
from copy import deepcopy
#from collections import deque
#import defaultdict
#import functools
import numpy as np
from PIL import Image
import re


def makeimage(B):
    I = deepcopy(B)
    for r in range(len(I)):
        for c in range(len(I[r])):
            if I[r][c] == '#': I[r][c] = 255
            if I[r][c] == '.': I[r][c] = 0
            if I[r][c] == 'o': I[r][c] = 64
    na = np.array(I, dtype=np.uint8)
    im = Image.fromarray(na)
    im.save('result.png')


def addsand(B, x, i):
    s1 = 1000000
    y = 0
    dist = 0

    while (B[y+1][x] == '.' or B[y+1][x -1] == '.' or B[y+1][x+1] == '.' ):
        dist+=1
        if y == len(B) - 3:
            s1 = min(s1, i-1)
        for dx in [0, -1, 1]:
            if B[y+1][x+dx] == '.':
                B[y][x] = '.'
                B[y+1][x+dx] = 'o'
                x = x + dx
                break
        y+=1
    return dist, s1


# https://adventofcode.com/2018/day/17

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

xmi = 1000
xma = 0
yma = 0
y0 = 500
paths = []
for line in lines:
    #path = [(int(x.split(',')[0]), int(x.split(',')[1])) for x in line.split() if x != '->']
    x = re.search("^([xy])=(.*), ([xy]=)(.*)\.\.(.*)", line)
    a = int(x.group(2))
    b = int(x.group(4))
    c = int(x.group(5))
    if x.group(1) == 'x':
        print(f'({a},{b}) -> ({a},{c})')
        path = [(a,b), (a,c)]
    else:
        print(f'({b},{a}) -> ({c},{a})')
        path = [(b,a), (c,a)]

    paths.append(path)
    for p1 in path:
        xmi = min(xmi, p1[0])
        xma = max(xma, p1[0])
        yma = max(yma, p1[1])

Y = yma + 1 + 2
xoffs = Y
X = xma - xmi + 1 + 2 * xoffs
B = [['.' for _ in range(X)] for _ in range(Y)]

for i in range(X):
    B[Y-1][i] = '#'

#for l in B : print(''.join(l))


for path in paths:
    for i, p in enumerate(path[:-1]):
        p1, p2 = path[i:i+2]
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        x = p1[0] - xmi + xoffs
        y = p1[1]
        moves = max(abs(dx), abs(dy)) + 1
        dx = (dx//(abs(dx)) if dx !=0 else dx)
        dy = (dy//(abs(dy)) if dy != 0 else dy)

        for m in range(moves):
            B[y][x] = '#'
            x += dx
            y += dy


S1 = 1000000000
S2 = 0
i = 1
done = False
while (not done):
    d, s = addsand(B, y0 - xmi + xoffs, i)
    S1 = min(s, S1)
    if d == 0:
        S2 = i
        done = True
    i+=1

makeimage(B)

print("------------- A -------------")
print(f'S1 {S1}')
print("------------- B -------------")
print(f'S2 {S2}')
print("-----------------------------")
