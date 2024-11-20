#!/usr/local/bin/python3

import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0

with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

key1 = '123\n456\n789'
key2 = '  1  \n 234 \n56789\n ABC \n  D  '

dir = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}

def solve(key):
    M = [[x for x in l] for l in key.split('\n')]
    ans = ''
    R = len(M)
    C = len(M[0])
    rr = -1
    cc = -1
    for r in range(R):
        for c in range(C):
            if M[r][c] == '5':
                rr = r
                cc = c

    for l in lines:
        for ch in l:
            dr, dc = dir[ch]
            nr = rr + dr
            nc = cc + dc
            if 0<=nr<R and 0<=nc<C and M[nr][nc] != ' ':
                rr = nr
                cc = nc
        ans = ans + M[rr][cc]
    return ans


S1 = solve(key1)
S2 = solve(key2)


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
