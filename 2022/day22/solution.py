#!/usr/local/bin/python3

import sys, os
import matplotlib.pyplot as plt

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))
data = open(infile).read()
lines = data.split('\n')

for i, line in enumerate(lines):
    if len(line) != len(lines[0]):
        nl = line + ' '*(len(lines[0]) - len(line))
        lines[i] = nl

maze = lines[:len(lines) - 3]
#assert len(maze) == 200
for line in maze:
    assert len(line) == len(maze[0])
    for c in line:
        assert c == ' ' or c =='#' or c == '.'
inst = lines[-2:-1]


for i, line in enumerate(maze):
    assert len(line) == len(maze[0]), i


xdim = len(maze[0])
ydim = len(maze)
xmax = xdim-1
ymax = ydim-1
pos = (maze[0].index('.'), 0)
print('dimensions ', xdim, ydim)
print(f'startpos {pos}')

assert maze[0][0] == ' '
dirs = {(1,0):'R', (-1,0):'L', (0,1):'D', (0,-1):'U'}
vals = {'R':0, 'D':1, 'L':2, 'U':3}
cs = {'R':'>', 'D':'v', 'L':'<', 'U':'^'}



def draw(x,y,n):
    print('   ---------------------')
    for i, line in enumerate(maze):
        if i >= max(0, y-n) and i <= min(ymax, y+n):
            print(f'{i:3} | {line}|')
    print('   ---------------------')


def rotate(x, y, d):
    if d=='L':
        return y, -x
    elif d=='R':
        return -y, x
    else:
        assert False, d


def boundary(x,y):
    return x<0 or y<0 or x>xmax or y>ymax


def wrap(x, y, dx, dy):
    orgx = x
    orgy = y
    dx = -dx
    dy = -dy
    while True:
        nx = x + dx
        ny = y + dy
        if boundary(nx,ny):
            if maze[y][x] == '#':
                return orgx, orgy
            else:
                return x, y

        if maze[ny][nx]==' ':
            if maze[y][x] == '#':
                return orgx, orgy
            else:
                return x, y
        else:
            x = nx
            y = ny
    assert False


def update(x,y,c, plot):
    l = [p for p in maze[y]]
    l[x] = c
    maze[y] = ''.join(l)
    if plot:
        draw(x,y,10)


def move(x, y, n, dx, dy):
    for i in range(n):
        nx = x+dx
        ny = y+dy
        if boundary(nx,ny):
            x, y = wrap(x, y, dx, dy)
        elif maze[ny][nx] == '#':
            break
        elif maze[ny][nx] == ' ':
            x, y = wrap(x, y, dx, dy)
        else:
            x = nx
            y = ny
        update(x,y, cs[dirs[(dx,dy)]],0)

    return x, y


x = pos[0]
y = pos[1]
dx = 1
dy = 0
instr = inst[0].replace('R', ',R,').replace('L',',L,').split(',')
update(x,y,'>',1)
for cmd in instr:
    print(f'cmd {cmd}, x,y ({x},{y}), dir ({dx},{dy})')
    if cmd in ['L', 'R']:
        dx, dy = rotate(dx, dy, cmd)
        update(x,y,cs[dirs[(dx,dy)]], 1)
    else:
        x, y = move(x,y, int(cmd), dx, dy)
        update(x,y,cs[dirs[(dx,dy)]], 1)



row = y+1
col = x+1
dir = dirs[(dx,dy)]
dirv = vals[dirs[(dx,dy)]]
print(f'row {row}, col {col}, dir {dir}, dir value {dirv}')
S1 = (y+1)*1000 + 4 * (x+1) + vals[dirs[(dx,dy)]]
print(f'S1 = 1000 * {row} + 4 * {col} + {dirv} = {S1}')

S2 = 0

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
