#!/usr/local/bin/python3

import sys
import re
from copy import deepcopy
import numpy as np

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

prg = []
for line in lines:
    m, op = line.split(':')
    m = m.strip()
    op=op.strip()
    prg.append([m, op])


def solve(prg, p2, hval):
    done = False
    vals = {}
    end = len(prg)

    if p2:
        for i, p in enumerate(prg):
            if p[0] == 'humn':
                p[1] = str(hval)

    while not done:
        subs = 0
        prg = [x for x in prg if x != ['','']]
        for i ,l in enumerate(prg):
            m = l[0]
            op = l[1]

            if p2 and m == 'root':
                tmp = deepcopy(op)
                a, b = tmp.split('+')
                a = a.strip()
                b = b.strip()
                if a in vals and b in vals:
                    if vals[a] == vals[b]:
                        return 0
                    else:
                        return np.sign(vals[a]-vals[b])
                else:
                    continue

            if m in vals or m == '':
                continue

            res = re.findall(r'\b[a-z]{4}\b',op)
            if len(res) == 0: # only numbers left
                val = int(eval(op))
                vals[m] = val
                prg[i]=['','']
            else:
                for s in res:
                    if s in vals:
                        subs += 1
                        news = str(vals[s])
                        op = op.replace(s, news)
                prg[i] = [m, op]
        if len(vals) == end:
            done = True
    return vals['root']


S1 = solve(prg, False, 0)

print('part II')
S2 = 0
val = 4000000000000
ac = deepcopy(prg)
if solve(ac, True, val) < 0:
    upper = -val
    lower = val
else:
    upper = val
    lower = -val

while True:
    pc = deepcopy(prg)
    print(f'bisect [{upper};{lower}]')
    c = (upper + lower)//2
    sa = solve(pc, True, c)
    if sa == -1:
        lower = c
    elif sa == 1:
        upper = c
    elif sa == 0:
        print(c)
        S2 = c
        break
    else:
        assert False, sa


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
