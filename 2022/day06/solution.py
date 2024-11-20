#!/usr/local/bin/python3

import argparse
from collections import deque

def get_data(filename):
    return [line.rstrip() for line in open(filename, 'r')]

def solve(lines, n):
    for line in lines:
        for i in range(len(line)):
            if i >=3 and len(set(line[i:i+n])) == n:
                print("end of marker {}".format(i + n))
                break


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", metavar='filename', help = "input file",
                       type = str, default = "test.txt")
    args = parser.parse_args()

    print("<<{}>>".format(args.f))
    l = get_data(args.f)
    print("------------- A -------------")
    solve(l,4)
    print("------------- B -------------")
    solve(l,14)
    #print("-----------------------------")
