#!/usr/local/bin/python3

import sys


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

nums = list(map(int,lines[0].split(',')))


if infile == 'puzzle.txt':
    n = 12
    v = 2
else:
    n = nums[1]
    v = nums[2]

def getvalue(lst, noun, verb):
    lst[1] = noun
    lst[2] = verb
    i = 0
    while (True):
        o = lst[i]
        if o == 99:
            break
        a = lst[lst[i+1]]
        b = lst[lst[i+2]]
        d = lst[i+3]
        if o == 1:
            #print(f'i {i}, add, a: {a}, b: {b}, d: {d}')
            lst[d] = a + b
        elif o == 2:
            #print(f'i {i}, mul, a: {a}, b: {b}, d: {d}')
            lst[d] = a * b
        else:
            assert False
        i += 4
    return lst[0]

S1 = getvalue(nums.copy(), n, v)

if infile == 'puzzle.txt':
    found = False
    for noun in range(100):
        for verb in range(100):
            value = getvalue(nums.copy(), noun, verb)
            if value == 19690720:
                found = True
                break
        if found:
            break
    S2 = 100 * noun + verb



print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
