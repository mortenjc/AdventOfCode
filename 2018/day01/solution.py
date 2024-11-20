#!/usr/local/bin/python3

import argparse, sys


if __name__ == '__main__':
    ifile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
    print("<<{}>>".format(ifile))

    lines = [line for line in open(ifile).read().splitlines()]
    vals = [eval(x) for x in lines]

    s = set()
    f = 0
    n = 0
    res = 0
    done = False
    while not done:
        for i in vals:
            f += i
            print(n, f, len(s))
            s.add(f)
            n += 1
            if len(s) != n:
                done = True
                res = f
                break



    print("------------- A -------------")
    print(sum(vals))
    print("------------- B -------------")
    print("freq    {}".format(res))
    print("-----------------------------")
