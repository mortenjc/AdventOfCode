#!/usr/local/bin/python3

import argparse, sys
#import defaultdict


if __name__ == '__main__':
    ifile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
    print("<<{}>>".format(ifile))

    lines = [line.rstrip() for line in open(ifile, 'r')]
    #grid = [list( map(int, line)) for line in open(ifile).read().splitlines()]
    #print(grid)

    clk = 0
    X = 1
    signal = 0
    screen = [[' ' for _ in range(40)] for _ in range(6)]

    for line in lines:
        op, *res = line.split()

        if op == 'noop':
            signal += (clk * X if (clk - 20) % 40 == 0 else 0)
            screen[(clk//40)][clk%40] = (chr(9608) if abs(clk%40 - X) <= 1 else ' ')
            clk += 1
        elif op == 'addx':
            val = int(res[0])
            signal += (clk * X if (clk - 20) % 40 == 0 else 0)
            screen[(clk//40)][clk%40] = (chr(9608) if abs(clk%40 - X) <= 1 else ' ')
            clk += 1
            signal += (clk * X if (clk - 20) % 40 == 0 else 0)
            screen[(clk//40)][clk%40] = (chr(9608) if abs(clk%40 - X) <= 1 else ' ')
            X += val
            clk += 1


    print("------------- A -------------")
    print('Score ', signal)
    print("------------- B -------------")
    for r in range(6):
        print(''.join(screen[r]))
    print("-----------------------------")
