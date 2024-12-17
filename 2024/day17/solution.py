#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import sys
import re
import math
import random



infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

if infile == 'puzzle.txt':
    pass
else:
    pass

with open(infile) as fin:
    init, prg = ((fin.read().strip()).split('\n\n'))

regs = {}

for reg in init.split('\n'):
    reg = reg.split(':')
    var = reg[0][-1]
    val = int(reg[1])
    regs[var] = val

pg = prg.split(':')[1].split(',')
pg = list(map(int, pg))

OP = {0:'adv', 1:'bxl', 2:'bst', 3:'jnz', 4:'bxc', 5:'out', 6:'bdv', 7:'cdv'}



matches = 0
def run(pg, regs, part2):
    n = regs['A']
    global matches
    pc = 0
    output = []
    while True:
        opc = pg[pc]
        opr = pg[pc + 1]

        if opr <= 3:
            cval = opr
            reg = 'I'
        elif opr <=6:
            reg = chr(ord('A') + (opr - 4))
            cval = regs[reg]
        else:
            cval = -1

        if opc == 0: # adv
            regs['A'] = regs['A']//2**cval
        elif opc == 1: # bxl
            regs['B'] = regs['B'] ^ opr
        elif opc == 2: # bst
            regs['B'] = cval % 8
        elif opc == 3: # jnz
            if regs['A'] != 0:
                pc = opr - 2
        elif opc == 4: # bxc
            regs['B'] = regs['B'] ^ regs['C']
        elif opc == 5: # out
            if part2:
                if cval%8 != pg[len(output)]: # mismatch
                    newmatch = False
                    if len(output) > matches:
                        matches = len(output)
                        newmatch = True
                    return output, newmatch
            output.append(cval%8)

        elif opc == 6: # bdv
            regs['B'] = regs['A']//(2**cval)
        elif opc == 7: # cdv
            regs['C'] = regs['A']//(2**cval)
        else:
            assert False
        pc += 2
        if pc >= len(pg):
            break

    return output, False




tregs = regs.copy()
res, newbest = run(pg, tregs, part2=False)

S1 = ','.join([str(x) for x in res])


i = 0
cst = 0
pow = 0
while True:
    tregs = regs.copy()
    ast = i * 8**pow + cst
    tregs['A'] = ast

    res, newbest = run(pg, tregs, part2=True)
    if newbest and matches > 3:
        pow = matches
        ostr = str(oct(ast))
        cst = int('0o' + ostr[-matches:], 8)
        print(f'new: i * 8**{pow} + {oct(cst)}')
        i = 0

    if res == pg:
        S2 = ast
        break
    i += 1

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
