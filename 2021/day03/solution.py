#!/usr/local/bin/python3

import argparse
from collections import deque
import copy

def get_data(filename):
    return [line.rstrip() for line in open(filename, 'r')]


def solve(lines):
    ones = [0] * len(lines[0])
    zeros = [0] * len(lines[0])

    for line in lines:
        for i in range(len(line)):
            if int(line[i]) == 1:
                ones[i] += 1
            else:
                zeros[i] += 1
    a = 0
    b = 0
    for i in range(len(ones)):
        if ones[i] > zeros[i]:
            a += 2**(len(ones) -1  - i)
        else:
            b += 2**(len(ones) -1  - i)
    print("a, b, {} {} : solution {}".format(a, b, a*b))


def bintodec(binnum):
    a = 0
    for i in range(len(binnum)):
        if int(binnum[i]) == 1:
            a += 2**(len(binnum) -1  - i)
    return a


def solve2(lines):
    l1 = copy.deepcopy(lines)
    l2 = copy.deepcopy(lines)
    s1 = False
    s2 = False
    for bits in range(len(l1[0])):
        ls1 = [int(x[bits]) for x in l1]
        ls2 = [int(x[bits]) for x in l2]
        if s1 == False:
            if ls1.count(0) <= ls1.count(1):
                l1 = [x for x in l1 if int(x[bits]) == 1]
            else:
                l1 = [x for x in l1 if int(x[bits]) == 0]
            if len(l1) == 1:
                s1 = True
        if s2 == False:
            if ls2.count(0) <= ls2.count(1):
                l2 = [x for x in l2 if int(x[bits]) == 0]
            else:
                l2 = [x for x in l2 if int(x[bits]) == 1]
            if len(l2) == 1:
                s2 = True

    print(l1)
    print(l2)
    a = bintodec(l1[0])
    b = bintodec(l2[0])
    print("Solution {} * {} = {}".format(a, b, a * b))


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
