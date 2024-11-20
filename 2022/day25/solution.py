#!/usr/local/bin/python3

import sys, os, math
from collections import deque

class AOC2022:
    def __init__(s, filename):
        s.f = filename
        s.S1 = 0
        s.S2 = 0
        s.lines = open(s.f).read().splitlines()


    def to_snafu(s, number):
        d2s = {0:'0', 1:'1', 2:'2', 3:'=', 4:'-' }
        snafu = ''
        while number > 0:
            number, rem = divmod(number, 5)
            snafu += d2s[rem]
            if rem > 2:
                number += 1
        return snafu[::-1] if snafu else '0'


    def from_snafu(s, snafu):
        s2d = {'2':2, '1':1, '0':0, '-':-1, '=':-2}
        return sum([(s2d[d]*(5**i)) for i, d in enumerate(snafu[::-1])])


    def solve(s):
        for line in s.lines:
            res = s.from_snafu(line)
            print(res)
            s.S1 += res
        print('sum ', s.S1)

#
# #
#

if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'

    if infile == 'test.txt':
        m = AOC2022(infile)
    else:
        m = AOC2022(infile)


    # Part I & II
    m.solve()
    S1 = m.to_snafu(m.S1)

    print("------------- A -------------")
    print('S1 ', S1)
    print("------------- B -------------")
    print('S2 ', m.S2)
    print("-----------------------------")
