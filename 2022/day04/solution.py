#!/usr/local/bin/python3

import argparse

def get_data(filename):
    lines = [line.rstrip() for line in open(filename, 'r')]
    print("get_data() - read {} lines".format(len(lines)))
    return lines


def covered(a):
    return (a[0]&a[1] == a[1]) or (a[0]&a[1] == a[0])


def overlaps(a):
    return len(a[0]&a[1]) != 0


def make_range(rangestr):
    r = rangestr.split('-')
    return list(range(int(r[0]), int(r[1]) + 1))


def make_sets(line):
    reg = line.split(",")
    return set(make_range(reg[0])), set(make_range(reg[1]))


def solve1(lines):
    print("{} are covered".format(
        sum([covered(make_sets(line)) for line in lines])
    ))
    return


def solve2(lines):
    print("{} assignments overlap".format(
        sum([overlaps(make_sets(line)) for line in lines])
    ))
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", metavar='filename', help = "input file",
                       type = str, default = "test.txt")
    args = parser.parse_args()

    l = get_data(args.f)
    print("------------- A -------------")
    solve1(l)
    print("------------- B -------------")
    solve2(l)
    print("-----------------------------")
