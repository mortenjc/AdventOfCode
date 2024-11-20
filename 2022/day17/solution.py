#!/usr/local/bin/python3

import sys
#from collections import deque
#import functools

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

assert len(lines) == 1

def get_piece(t, y):
    if t==0:
        return set([(2, y), (3, y), (4,y), (5,y)])
    elif t==1:
        return set([(3, y), (2,y+1), (3, y+1), (4, y+1), (3, y+2)])
    elif t==2:
        return set([(2,y), (3, y), (4, y), (4, y+1), (4,y+2)])
    elif t==3:
        return set([(2, y), (2, y+1), (2, y+2), (2, y+3)])
    elif t==4:
        return set([(2,y), (3,y), (2,y+1), (3,y+1)])
    else:
        assert False

def move_left(piece):
    if any([x==0 for (x, y )in piece]):
        return piece
    return set([(x-1, y) for (x,y) in piece])

def move_right(piece):
    if any([x==6 for (x, y )in piece]):
        return piece
    return set([(x+1, y) for (x,y) in piece])

def move_down(piece):
    return set([(x, y-1) for (x,y) in piece])

def move_up(piece):
    return set([(x, y+1) for (x,y) in piece])

def draw(R):
    maxY = max([y for (x,y) in R])
    for y in range(maxY,0,-1):
        for x in range(7):
            if (x,y) in R:
                line += '#'
            else:
                line += ' '
        print('|'+line+'|')
    print('+-------+')


R = set([(x,0) for x in range(7)])
i = 0
for t in range(2022):
    print(t)
    y = max([y for (x,y) in R]) + 4
    p = get_piece(t%5, y)

    done = False
    while not done:
        w = lines[0][i%len(lines[0])]
        if w == '>':
            p = move_right(p)
            if p & R:
                p = move_left(p)
        else:
            p = move_left(p)
            if p & R:
                p = move_right(p)
        i += 1
        p = move_down(p)
        if p & R:
            p = move_up(p)
            R = R|p
            done = True

S1 =  max([y for (x,y) in R])

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
