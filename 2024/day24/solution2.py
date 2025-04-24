#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import sys
import re
import math
import random
import heapq



random.seed(10)

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

def getz(XX, c):
    res = 0
    for x in XX:
        if x.startswith(c):
            sh = int(x[1:])
            tmp = XX[x]<<sh
            res += tmp
            #print(f'{x}:{R[x]}: exp {sh}, tmp {tmp}, res {res}')
    return res

if infile == 'puzzle.txt':
    pass
else:
    pass

with open(infile) as fin:
    init, instr = ((fin.read().strip()).split('\n\n'))



def makeR(initlst):
    R = {}
    for l in initlst.split('\n'):
        var, val = l.split(':')
        val = int(val)
        R[var] = val
    return R


def makeR2(x,y):
    R = {}
    for i in range(45):
        R[f'x{i:02}'] = x & 1
        R[f'y{i:02}'] = y & 1

        x = x >> 1
        y = y >> 1
    return R





def makeinstr(instrlst, swp):
    D = deque()
    for l in instrlst.split('\n'):
        va, opr, vb, _, dst = l.split(' ')
        if swp != []:
            if dst in swp:
                #print('swapping', dst, 'to other', swp)
                if swp[0] == dst:
                    dst = swp[0]
                else:
                    dst = swp[1]
        D.append((va, opr, vb, dst))
    return D
#
#
#



def solve(RR, DD):
    while len(DD):
        va, opr, vb, dst = DD.popleft()
        if dst in RR:
            assert False

        if not (va in RR and vb in RR):
            DD.append((va, opr, vb, dst ))
            continue

        a = RR[va]
        b = RR[vb]
        if opr == 'XOR':
            res = a ^ b
        elif opr == 'OR':
            res = a | b
        elif opr == 'AND':
            res = a & b
        RR[dst] = res
    return RR

#R = makeR(init)


def errcount(swp):
    ecount = 0
    for i in range(0,2000):
        ra = random.randint(0, 11165536)
        rb = random.randint(0, 11165536)
        #ra = 2**i + 2**(i+1)
        #rb = 2**i #+ 2**(i+1)
        D = makeinstr(instr, swp)
        R2 = makeR2(ra,rb)
        #print(R2)


        RR = solve(R2, D)
        x = getz(RR, 'x')
        y = getz(RR, 'y')
        z = getz(RR, 'z')
        e = x + y
        if z != x + y:
            ecount += 1
            # print('error')
            # print(f'x {x:>20} {bin(x)[2:]:>50}')
            # print(f'y {y:>20} {bin(y)[2:]:>50}')
            # print(f'z {z:>20} {bin(z)[2:]:>50}')
            # print(f'e {e:>20} {bin(e)[2:]:>50}')

    print('error count', ecount)

#swaps = ['mcg', 'z21', 'vgs', 'z33', 'mtw', 'fdv', 'wnt', 'dqr', 'z45']
swaps = ['mcg', 'z21', 'vgs', 'mtw']
for sw in swaps:
    if sw == 'vgs':
        continue
    print('swap', 'vgs', sw)
    errcount([sw, 'vgs'])
print('baseline')
errcount([])

# print("------------- A -------------")
# print('S1 ', S1)
# print("------------- B -------------")
# print('S2 ', S2)
# print("-----------------------------")
