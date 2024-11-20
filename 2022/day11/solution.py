#!/usr/local/bin/python3

import argparse, sys
#import defaultdict
from copy import deepcopy
import math

if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
    print("<<{}>>".format(infile))
    data = open(infile).read().strip()
    lines = [x for x in data.split('\n')]

    C = []
    I = []
    OP = []
    DIV = []
    TRUE = []
    FALSE = []

    for monkey in data.split('\n\n'):
        m,si,op,div,tt,tf = monkey.split('\n')
        I.append([int(x) for x in si.split(':')[1].split(',')])
        words = op.split()
        op = ''.join(words[-3:])
        OP.append(lambda old, op=op:eval(op))
        DIV.append(int(div.split()[3]))
        TRUE.append(int(tt.split()[5]))
        FALSE.append(int(tf.split()[5]))

    START = deepcopy(I)

    lcm = 1
    for i in DIV:
        lcm *= (lcm*i)//math.gcd(lcm, i)

    # inspect
    S = [0, 0]
    for part in [0, 1]:
        I = deepcopy(START)
        C = [0 for _ in range(len(I))]
        for r in range((20 if part == 0 else 10000)):
            for m in range(len(C)):
                for ix in range(len(I[m])):
                    item = I[m][ix]
                    C[m] += 1
                    if part == 0:
                        item = OP[m](item)//3
                    else:
                        item = OP[m](item)
                        item = item%lcm
                    if item % DIV[m] == 0:
                        I[TRUE[m]].append(item)
                    else:
                        I[FALSE[m]].append(item)
                I[m] = []

        print('# END OF ROUND {}'.format(r+1))
        result = sorted(C)
        S[part] = result.pop() * result.pop()


    print("------------- A -------------")
    print('S1', S[0])
    print("------------- B -------------")
    print('S2', S[1])
    print("-----------------------------")
