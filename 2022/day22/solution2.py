#!/usr/local/bin/python3

import sys, os
import matplotlib.pyplot as plt

class MMap:
    def __init__(s, N, filename):
        s.N = N

        print("<<{}>>".format(filename))
        data = open(filename).read()
        lines = data.split('\n')

        for i, line in enumerate(lines):
            if len(line) != len(lines[0]):
                nl = line + ' '*(len(lines[0]) - len(line))
                lines[i] = nl

        s.maze = lines[:len(lines) - 3]

        assert len(s.maze)%s.N == 0
        assert len(s.maze[0])%s.N == 0

        for line in s.maze:
            assert len(line) == len(s.maze[0])
            for c in line:
                assert c == ' ' or c =='#' or c == '.'

        inst = lines[-2:-1]
        s.instr = inst[0].replace('R', ',R,').replace('L',',L,').split(',')

        s.xdim = len(s.maze[0])
        s.ydim = len(s.maze)
        s.xmax = s.xdim-1
        s.ymax = s.ydim-1
        pos = (s.maze[0].index('.'), 0)
        print(f'dimensions {s.xdim}x{s.ydim}')
        print(f'startpos   {pos}')

        # State variables
        s.x = pos[0]
        s.y = pos[1]
        s.r = s.region(s.x, s.y)
        s.dx = 1
        s.dy = 0

        s.dirs = {(1,0):'R', (-1,0):'L', (0,1):'D', (0,-1):'U'}
        s.vals = {'R':0, 'D':1, 'L':2, 'U':3}
        s.cs={'R':'>', 'D':'v', 'L':'<', 'U':'^'}

        s.regs = { (0,0):0, (1,0):0, (2,0):1, (3,0):0,
                   (0,1):2, (1,1):3, (2,1):4, (3,1):0,
                   (0,2):0, (1,2):0, (2,2):5, (3,2):6 }

        s.trns = {
                '1U':'2D', '1D':'4D', '1R':'6L', '1L':'3D',
                '2R':'3R', '2U':'1D', '2L':'6U', '2D':'5U',
                '3L':'2L', '3R':'4R', '3U':'1R', '3D':'5R',
                '4U':'1U', '4D':'5D', '4L':'3L', '4R':'6D',
                '5R':'6R', '5U':'4U', '5D':'2U', '5L':'3U',
                '6L':'5L', '6U':'4L', '6D':'2R', '6R':'1L'
               }


    def region(s, x,y):
        return s.regs[x//s.N, y//s.N]


    def rotate(s, x, y, d):
        if d=='L':
            return y, -x
        elif d=='R':
            return -y, x
        else:
            assert False, d


    def boundary(s, r, x, y):
        return x<0 or y<0 or x>s.xmax or y>s.ymax or s.region(x,y) != r


    def draw(s,x,y,n):
        print('   ---------------------')
        for i, line in enumerate(s.maze):
            if i >= max(0, y-n) and i <= min(ymax, y+n):
                print(f'{i:3} | {line}|')
        print('   ---------------------')

#
# #
#

if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'

    if infile == 'test.txt':
        m = MMap(4, infile)
    else:
        print('not implemented yet')
        sys.exit()
        m = MMap(50, infile)

    print(m.x)
#
#
# def wrap(x, y, dx, dy):
#     orgx = x
#     orgy = y
#     dx = -dx
#     dy = -dy
#     while True:
#         nx = x + dx
#         ny = y + dy
#         if boundary(nx,ny):
#             if maze[y][x] == '#':
#                 return orgx, orgy
#             else:
#                 return x, y
#         c = maze[ny][nx]
#         if c==' ':
#             if maze[y][x] == '#':
#                 return orgx, orgy
#             else:
#                 return x, y
#         else:
#             x = nx
#             y = ny
#     assert False
#
#
# def update(x,y,c, plot):
#     l = [p for p in maze[y]]
#     l[x] = c
#     l = ''.join(l)
#     maze[y] = l
#     if plot:
#         draw(x,y,10)
#
# def move(x, y, n, dx, dy):
#     for i in range(n):
#         nx = x+dx
#         ny = y+dy
#         if boundary(nx,ny):
#             x, y = wrap(x, y, dx, dy)
#         elif maze[ny][nx] == '#':
#             break
#         elif maze[ny][nx] == ' ':
#             x, y = wrap(x, y, dx, dy)
#         else:
#             x = nx
#             y = ny
#         update(x,y, cs[dirs[(dx,dy)]],0)
#
#     return x, y
#
#

#
# update(x,y,'>',1)
# for cmd in instr:
#     print(f'cmd {cmd}, x,y ({x},{y}), dir ({dx},{dy})')
#     if cmd in ['L', 'R']:
#         dx, dy = rotate(dx, dy, cmd)
#         update(x,y,cs[dirs[(dx,dy)]], 1)
#     else:
#         x, y = move(x,y, int(cmd), dx, dy)
#         update(x,y,cs[dirs[(dx,dy)]], 1)
#
#
#
    row = m.y+1
    col = m.x+1
    dir = dirs[(m.dx,m.dy)]
    dirv = vals[dir]
    print(f'row {row}, col {col}, dir {dir}, dir value {dirv}')
    S1 = (row)*1000 + 4 * col + dirv
    print(f'S1 = 1000 * {row} + 4 * {col} + {dirv} = {S1}')

    S2 = 0

    print("------------- A -------------")
    print('S1 ', S1)
    print("------------- B -------------")
    print('S2 ', S2)
    print("-----------------------------")
