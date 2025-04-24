#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import sys
import re
import math
import random
import heapq





infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

def getval(regs, c):
    res = 0
    for reg in regs:
        if reg.startswith(c):
            sh = int(regs[1:])
            tmp = regs[reg]<<sh
            res += tmp
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





def makeinstr(instrlst):
    D = {}
    for l in instrlst.split('\n'):
        va, opr, vb, _, dst = l.split(' ')
        D[dst] = (va, vb, opr)
    return D
#
#
#


def touched(reg, R, D):
    ts = set()
    def dfs(reg, dpt):
        if reg in ts:
            return
        # else
        ts.add(reg)
        if reg in R:
            if dpt <= 3:
                print('   '*dpt, reg)
            return
        # else
        a, b, op = D[reg]
        if dpt <= 3:
            print('   '*dpt, reg, op, '(', a, b, ')')

        dfs(a, dpt+1)
        dfs(b, dpt+1)

    dfs(reg, 0)
    return ts


RR = makeR(init)
DD = makeinstr(instr)
res = touched(sys.argv[2], RR, DD)
#print(res)
# res = touched('z01', RR, DD)
# print(res)
# res = touched('z02', RR, DD)
# print(res)
# res = touched('z03', RR, DD)
# print(res)




print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
