#!/usr/local/bin/python3

import argparse, sys
#import defaultdict

allowed_moves = [[ 2,0], [ 0, 2], [-2, 0], [ 0,-2],
                 [ 1,2], [ 1,-2], [-2, 1], [ 2, 1],
                 [-1,2], [-1,-2], [-2,-1], [ 2,-1],
                 [ 2,2], [ 2,-2], [-2, 2], [-2,-2]]


def move(h, t):
    d = [h[x] - t[x] for x in [0, 1]]
    if d in allowed_moves:
        d = [i//2 if abs(i) == 2 else i for i in d]
        return [t[x] + d[x] for x in [0, 1]]
    else:
        return t


if __name__ == '__main__':
    ifile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
    print("<<{}>>".format(ifile))

    lines = [line.rstrip() for line in open(ifile, 'r')]
    #grid = [list( map(int, line)) for line in open(ifile).read().splitlines()]
    #print(grid)

    m = {}
    m['U'] = [ 0, -1]
    m['D'] = [ 0,  1]
    m['L'] = [-1,  0]
    m['R'] = [ 1,  0]

    rope = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
    cova = []
    covb = []

    for line in lines:
        dir, moves = line.split()
        moves = int(moves)
        cova.append(rope[1])
        covb.append(rope[9])

        for i in range(moves):
            for j in range(len(rope) - 1):
                hi = j      # head index - leader
                ti = j + 1  # tail index - follower
                if j == 0: # update head
                    rope[hi] = [rope[hi][x] + m[dir][x] for x in [0, 1]]
                rope[ti] = move(rope[hi], rope[ti])
            cova.append(rope[1])
            covb.append(rope[9])

    sa = set(tuple(i) for i in cova)
    sb = set(tuple(i) for i in covb)
    print("------------- A -------------")
    print('cova', len(sa))
    print("------------- B -------------")
    print('covb', len(sb))
    print("-----------------------------")
