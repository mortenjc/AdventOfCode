#!/usr/local/bin/python3

from collections import defaultdict
import sys


infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

l = list(lines[0])
print(l)

def getl(l):
    res = []
    files = []
    free = []

    pos = 0
    fileno = 0
    for i, c in enumerate(l):
        c = int(c)
        if i % 2 == 0:
            num = i//2
            res += [num for x in range(c)]
            files.append((pos, c, fileno))
            pos += c
            fileno += 1
        else:
            res += ['.' for x in range(int(c))]
            free.append((pos, c))
            pos += c
    return res, files, free



a, files, unused = getl(l)
print(a)
print(files)
print(unused)


for (fpos, flen, fid) in reversed(files):
    for ix, (upos, ulen) in enumerate(unused):
        #print('file', fpos, flen, fid, 'unused', upos, ulen)
        if upos < fpos and ulen >= flen:
            #print('can be moved')
            for i in range(flen):
                a[upos + i] = fid
                a[fpos + i] = '.'
            unused[ix] = (upos + flen, ulen - flen)
            #print(a)
            #print(unused)
            break

for i, c in enumerate(a):
    if c != '.':
        c = int(c)
        S2 += i * c


print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
