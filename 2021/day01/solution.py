#!/usr/local/bin/python3

import argparse
from collections import deque

def get_data(filename):
    return [line.rstrip() for line in open(filename, 'r')]

def solve(lines):
    increases = 0
    numbers = list(map(int, lines))
    print(numbers)
    for i in range(len(numbers)):
        if i>=1 and (numbers[i] > numbers[i-1]):
            increases += 1
    print(increases)

def solve2(lines):
    increases = 0
    numbers = list(map(int, lines))
    print(numbers)
    for i in range(len(numbers)):
        if i >=3:
            print(numbers[i-2:i+1])
            print(numbers[i-3:i])
            a = sum(numbers[i-2:i+1])
            b = sum(numbers[i-3:i])
            print(a)
            if (a > b):
                increases += 1
    print(increases)


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
