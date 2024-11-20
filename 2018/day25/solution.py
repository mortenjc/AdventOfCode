#!/usr/local/bin/python3

import argparse, sys


def solve(grid):
    visible = best = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if isvisible(grid, c, r):
                visible += 1
            best = max(viewdist(grid, c, r), best)


def base(conn, i):
    while True:
        if conn[i] == i:
            #print('base ', i)
            return i
        else:
            i = conn[i]
            #print('iteration ', i)


if __name__ == '__main__':
    ifile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
    print("<<{}>>".format(ifile))

    #lines = [line for line in open(ifile).read().splitlines()]
    lines = [line for line in open(ifile)]
    input = []
    for line in lines:
        input.append([eval(x) for x in line.strip().split(',')])
    lines = input

    # solve
    conn = [i for i in range(len(lines))]

    for i in range(len(lines)):
        for j in range(len(lines)):
            assert len(lines[i]) == 4
            v = [abs(lines[i][x] - lines[j][x]) for x in range(len(lines[i]))]
            md = sum(v)
            if md <= 3 and i != j:
                print('md {} for ({},{})'.format(md, i, j))
                #print(v)
                if conn[j] == j and conn[i] == i: # both unused
                    conn[j] = base(conn, i)
                if conn[j] != j and conn[i] != i: # merge
                    ni = min(conn[i], conn[j])
                    nj = max(conn[i], conn[j])
                    for t in range(len(conn)):
                        if conn[t] == nj:
                            conn[t] = base(conn, ni)
                elif conn[j] == j:
                    conn[j] = base(conn, i)
                else:
                    conn[i] = base(conn, j)
                print(conn)
    print(conn)

    print("------------- A -------------")
    l = list(set(conn))
    print("constellations {}".format(len(l)))
    #print("------------- B -------------")
    #print("best    {}".format(best))
    print("-----------------------------")
