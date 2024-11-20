#!/usr/local/bin/python3

import argparse
from collections import deque

def get_data(filename):
    return [line.rstrip() for line in open(filename, 'r')]

def solve(lines):
    x = 0
    y = 0
    for line in lines:
        dir, dist = line.split(' ')
        if dir[0] == 'd':
            y += int(dist)
        if dir[0] == 'u':
            y -= int(dist)
        if dir[0] == 'f':
            x += int(dist)
    print("x, y: {} {}: {}".format(x, y, x*y))

def solve2(lines):
    x = 0
    y = 0
    aim = 0
    for line in lines:
        dir, dist = line.split(' ')
        if dir[0] == 'd':
            aim += int(dist)
        if dir[0] == 'u':
            aim -= int(dist)
        if dir[0] == 'f':
            x += int(dist)
            y += int(dist) * aim
    print("x, y: {} {}: {}".format(x, y, x*y))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", metavar='filename', help = "input file",
                       type = str, default = "test.txt")
    args = parser.parse_args()

    print("<<{}>>".format(args.f))
    l = get_data(args.f)
    print("------------- A -------------")
    solve(l)
    print("------------- B -------------")
    solve2(l)
    print("-----------------------------")
