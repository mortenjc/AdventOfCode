#!/usr/local/bin/python3

import sys
import itertools as it


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

if infile == 'test.txt':
    pass
else:
    pass

S1 = 0
S2 = 0


def press(presses, buttons, value):
    comb = it.combinations_with_replacement(buttons, presses)
    for c in comb:
        c = list(c)
        res =0
        for btns in c:
            for btn in btns:
                res ^= 2**btn
            if res == value:
                print('solution found in ', presses, 'presses', btns)
                return btns
    return []
        

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

FS = []
BTN = []
for line in lines:
    x = line.split()
    FS.append(x[0][1:-1])
    ys = [list(map(int,y[1:-1].split(','))) for y in x[1:-1]]
    BTN.append(ys)

for i in range(len(lines)):
    n = sum(2**j for j, c in enumerate(FS[i]) if c =='#')
    print(FS[i], n)

    for r in range(1, 9):
        if press(r, BTN[i], n) != []:
            S1 += r
            break
    else:
        print(i, 'too few iterations')
        sys.exit()


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
