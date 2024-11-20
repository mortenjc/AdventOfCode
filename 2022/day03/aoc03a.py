#!/usr/local/bin/python3

import argparse


def get_data(filename):
    lines = [line.rstrip() for line in open(filename, 'r')]
    print("get_data - read {} lines".format(len(lines)))
    return lines


def value(char):
    if (char >= 'a' and char <= 'z'):
        return ord(char) - ord('a') + 1
    if (char >= 'A' and char <= 'Z'):
        return ord(char) - ord('A') + 27
    return 0


def solve(lines):
    sum = 0
    for line in lines:
        linelen = int(len(line))
        linelen2 = int(linelen/2)
        a = line[0:linelen2]
        b = line[linelen2:linelen]
        common=list(set(a)&set(b))
        #print("common letter {}, value {}".format(common[0], value(common[0])))
        sum = sum + value(common[0])
    print("SUM {}".format(sum))
    return


def solve2(lines):
    sum = 0
    for i in range(int(len(lines)/3)):
        a = lines[i * 3 + 0]
        b = lines[i * 3 + 1]
        c = lines[i * 3 + 2]
        common=list(set(a)&set(b)&set(c))
        #print("common letter {}, value {}".format(common[0], value(common[0])))
        sum = sum + value(common[0])
    print("SUM {}".format(sum))
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", metavar='filename', help = "input file",
                       type = str, default = "test.txt")
    args = parser.parse_args()

    l = get_data(args.f)
    print("------------- A -------------")
    solve(l)
    print("------------- B -------------")
    solve2(l)
    print("-----------------------------")
