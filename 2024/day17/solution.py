#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import sys
import re
import math



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
    print(reg)
    var = reg[0][-1]
    val = int(reg[1])
    regs[var] = val

pg = prg.split(':')[1].split(',')
pg = list(map(int, pg))

assert len(pg) == 14

OP = {0:'adv', 1:'bxl', 2:'bst', 3:'jnz', 4:'bxc', 5:'out', 6:'bdv', 7:'cdv'}


SEEN = set()
def run(pg, regs):
    pc = 0
    output = []
    while True:
        if pc >= len(pg):
            print('normal exit')
            break

        opc = pg[pc]
        opr = pg[pc + 1]

        lval = opr
        if opr <= 3:
            cval = opr
            reg = 'I'
        elif opr <=6:
            reg = chr(ord('A') + (opr - 4))
            cval = regs[reg]
        else:
            cval = -1
            pass

        print(f'pc {pc}: opcode {opc} ({OP[opc]}), lval {lval}, reg {reg}, cval {cval}')

        if (pc, regs['A'], regs['B'], regs['C']) in SEEN:
            print('loop')
            break
        SEEN.add((pc, regs['A'], regs['B'], regs['C']))
        
        if opc == 0: # ADV
            denum = 2**cval
            num = regs['A']
            regs['A'] = num//denum
            #print(f'adv: A = {num}/{denum}')

        elif opc == 1: # BXL
            regs['B'] = regs['B'] ^ lval
            #print(f'bxl: B = {regs['B']} xor {lval}')

        elif opc == 2: #BST
            regs['B'] = cval % 8
            #print(f'bst: B = {cval} % 8')

        elif opc == 3: # JNZ
            if regs['A'] != 0:
                #print(f'jnz: pc = pc + {lval}')
                pc = lval - 2

        elif opc == 4: # BXC
            #print(f'bxc: {regs['B']} ^ {regs['C']}')
            regs['B'] = regs['B'] ^ regs['C']

        elif opc == 5: # out
            #print(f'out: {cval%8}')
            output.append(cval%8)

        elif opc == 6: # bdv
            #print(f'bdv: B = {regs['A']}//{(2**cval)}')
            regs['B'] = regs['A']//(2**cval)

        elif opc == 7: # cdv
            #print(f'cdv: C = {regs['A']}//{(2**cval)}')
            regs['C'] = regs['A']//(2**cval)

        else:
            #print(opc)
            assert False
        pc += 2
        #print(regs)

    return output


tregs = regs.copy()
#tregs['A'] = 117440
res = run(pg, tregs)
print(res)
S1 = ','.join(list(map(str,res)))


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
