#!/usr/local/bin/python3

import numpy as np
import sys
#import portion as p
#from collections import defaultdict
#from functools import cache
import math
import matplotlib.pyplot as plt


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

if infile == 'test.txt':
    pass
else:
    pass

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

P = []
p1 = (94967, 50085)
p2 = (94967, 48699)
p1i = -1
p2i = -1
for i, line in enumerate(lines):
    x,y = map(int, line.split(','))
    if (x,y) == (p1):
        p1i = i
    if (x,y) == (p2):
        p2i = i
    P.append([x,y])

print(p1i, p2i)

def plot(arr, arr2):
    fig, ax = plt.subplots()
    X = [x[0]for x in arr]
    Y = [x[1]for x in arr]
    ax.plot(X,Y, linewidth=1.0)
    ax.scatter(X,Y, s=1)
    
    X = [x[0]for x in arr2]
    Y = [x[1]for x in arr2]
    ax.plot(X,Y, linewidth=1.0)
    plt.show()



i = p1i
founda = False
foundb = False
box = []
while True:
    i += 1
    i = i % len(P)
    if i == p1i:
        break
    px, py = P[i]
    #print(i, px, py)
    if not founda and px <= p1[0] and py >= p1[1]:
        ax, ay = px, py
        print(i, ax, ay, '   ', p1[0], p1[1])
        founda = True
    if founda and px <= 40000 and py <= ay:
        bx, by = px, py
        print(i, ax, ay, '   ', px, py)
        foundb = True
    if foundb == True and founda == True:
        sz = (abs(bx - p1[0]) + 1) * (abs(by - p1[1]) + 1)
        print('sz', sz)
        sz = (abs(bx - p1[0]) ) * (abs(by - p1[1]) )
        print('sz', sz)
        box.append([bx, by])
        box.append([bx, p1[1]])
        box.append([p1[0], p1[1]])
        box.append([p1[0], by])
        box.append([bx, by])
        break
    
plot(P, box)




    

S1 = max



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
