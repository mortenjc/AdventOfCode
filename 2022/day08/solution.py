#!/usr/local/bin/python3

import argparse, sys


def isvisible(board, c, r):
    n = len(board)
    h = board[r][c]

    if all(board[r][i] < h for i in range(c)):
        return True
    if all(board[r][i] < h for i in range(c+1, n)):
        return True
    if all(board[i][c] < h for i in range(r)):
        return True
    if all(board[i][c] < h for i in range(r+1, n)):
        return True
    return False


def viewdist(board, c, r):
    n = len(board)
    h = board[r][c]
    dl = dr = dt = db = 0
    for i in range(c - 1, -1, -1):
        dl += 1
        if (board[r][i] >= h):
            break
    for i in range(c + 1, n):
        dr += 1
        if (board[r][i] >= h):
            break
    for i in range(r - 1, -1, -1):
        dt += 1
        if (board[i][c] >= h):
            break
    for i in range(r+1, n):
        db += 1
        if (board[i][c] >= h):
            break
    return dl * dr * dt * db


def solve(grid):
    visible = best = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if isvisible(grid, c, r):
                visible += 1
            best = max(viewdist(grid, c, r), best)

    print("------------- A -------------")
    print("visible {}".format(visible))
    print("------------- B -------------")
    print("best    {}".format(best))
    print("-----------------------------")


if __name__ == '__main__':
    ifile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
    print("<<{}>>".format(ifile))

    #lines = [line.rstrip() for line in open(ifile, 'r')]
    grid = [list( map(int, line)) for line in open(ifile).read().splitlines()]
    #print(grid)
    solve(grid)
