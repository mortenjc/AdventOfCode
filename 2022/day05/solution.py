#!/usr/local/bin/python3

import argparse
from collections import deque

def get_data(filename):
    lines = [line.rstrip() for line in open(filename, 'r')]
    print("get_data - read {} lines".format(len(lines)))
    return lines


# def one_is_covered(a, b):
#     return (a&b == b) or (a&b == a)


# def regions_overlap(a, b):
#     return a&b


# def make_range(rangestr):
#     a = rangestr.split('-')[0]
#     b = rangestr.split('-')[1]
#     l = list(range(int(a), int(b)+1))
#     return l

# def make_sets(line):
#     regions = line.split(",")
#     rb = set(make_range(regions[0]))
#     ra = set(make_range(regions[1]))
#     return ra, rb


def move(n, f, t):
    for i in range(n):
        t.append(f.pop())

def move2(n, f, t):
    tmp = deque()
    for i in range(n):
        tmp.append(f.pop())
    for i in range(n):
        t.append(tmp.pop())


def scan(lines):
    cols = 0
    for line in lines:
        if len(line) == 0:
            return cols
        if line[-1] != ']':
            cols = int(line.split(' ')[-1])

def solve(lines, mm):
    state_parse = 0
    state_move = 1
    state = state_parse

    piles = []
    for i in range(scan(lines)):
        piles.append(deque())

    for line in lines:
        #print(line)
        if state == state_parse:
            max = len(line)
            for i in range(1, max - 1, 4):
                index = (i - 1)//4
                c = line[i]
                if c != ' ':
                    piles[index].appendleft(c)

        if state == state_move:
            i, n, i2, f, i3, t = line.split(' ')
            if mm:
                move2(int(n), piles[int(f) - 1], piles[int(t)- 1])
            else:
                move(int(n), piles[int(f) - 1], piles[int(t)- 1])

        if (len(line) == 0): # empty line
            state = state_move


    print("".join([p[-1] for p in piles]))
    return



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", metavar='filename', help = "input file",
                       type = str, default = "test.txt")
    args = parser.parse_args()

    l = get_data(args.f)
    print("------------- A -------------")
    solve(l, 0)
    print("------------- B -------------")
    solve(l, 1)
    #print("-----------------------------")
