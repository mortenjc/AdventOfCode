#!/usr/local/bin/python3

import argparse
from collections import deque
import copy

def get_data(filename):
    return [line.rstrip() for line in open(filename, 'r')]


def getdir(curdir):
    dir = ''.join(curdir)
    if dir[:2] == '//':
        dir = dir[1:]
    return dir


def addsize(dict, dirlist, size):
    lst = copy.deepcopy(dirlist)
    for i in range(len(lst)):
        dir = getdir(lst)
        if dict.get(dir) == None:
            dict[dir] = size
        else:
            dict[dir] += size
        lst.pop()


def solve(lines):
    state_nav = 1
    state_ls = 2
    state = state_nav
    curdir = ''
    dirlist = []
    sizes = {}
    for line in lines:
        res = line.split(' ')
        if res[0] == '$' and res[1] == 'ls':
            state = state_ls
            cursize = 0
            continue

        if res[0] == '$':
            state = state_nav


        if state == state_nav:
            if res[2] != '..':
                if res[2] == '/':
                    dirlist = ['/']
                else:
                    dirlist.append('/' + res[2])
            else: # ..
                dirlist.pop()

            curdir = getdir(dirlist)
            continue

        if state == state_ls:
            if res[0] != 'dir':
                addsize(sizes, dirlist, int(res[0]))

    dirs = [sizes[x] for x in sizes if sizes[x] <= 100000]
    print("total size of dirs <= 100000: {}".format(sum(dirs)))
    return sizes



def solve2(sizes):
    tofree = 30000000 - (70000000 - sizes['/'])
    used = sizes['/']
    avail = 70000000 - sizes['/']
    print("Total space     70000000")
    print("used space      {}".format(used))
    print("available space {}".format(avail))
    print("needed space    30000000")
    print("must free       {}".format(tofree))
    a = [sizes[x] for x in sizes if sizes[x] >= tofree]
    a.sort()
    print("smallest dir    {}".format(a[0]))



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", metavar='filename', help = "input file",
                       type = str, default = "test.txt")
    args = parser.parse_args()

    print("<<{}>>".format(args.f))
    l = get_data(args.f)
    print("------------- A -------------")
    sz = solve(l)
    print("------------- B -------------")
    solve2(sz)
    print("-----------------------------")
