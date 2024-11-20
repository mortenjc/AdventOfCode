#!/usr/local/bin/python3

import sys, os, math
from collections import deque

class AOC2022:
    def __init__(s, filename):
        s.f = filename
        s.S1 = 0
        s.S2 = 0

        s.blizzards = [set(), set(), set(), set()] # <>^v
        for r, line in enumerate(open(s.f).read().splitlines()[1:]):
            for c, item in enumerate(line[1:]):
                if item in '<>^v':
                    s.blizzards['<>^v'.find(item)].add((r,c))

        s.r = r
        s.c = c
        s.target = (r,c-1)
        s.lcm = c*r//math.gcd(r,c)
        print('target ',s.target)


    def solve(s):
        targets = [s.target, (-1,0)]
        stage = 0
        Q = deque([(0, -1, 0, stage)])
        seen = set()
        while Q:
            time, cr, cc, stage = Q.popleft()
            time += 1

            for dr, dc in [(0,1), (0,-1), (-1,0), (1,0), (0,0)]:
                nc = cc + dc
                nr = cr + dr

                if (nr,nc) == targets[stage%2]:
                    if stage == 0:
                        print(f'target {(nr,nc)} reached in ', time)
                        s.S1 = time
                    if stage == 2:
                        print(f'target {(nr,nc)} reached in ', time)
                        s.S2 = time
                        return
                    stage += 1

                if (nr < 0 or nc < 0 or nr > s.r or nc > s.c) and ((nr,nc) != (-1,0)) and ((nr,nc) not in targets):
                    continue

                for i, tr, tc in [(0,0,-1), (1,0,1), (2,-1,0), (3,1,0)]:
                    if ((nr - tr * time) % s.r, (nc - tc * time) % s.c) in s.blizzards[i]:
                        break
                else:
                    key = (nr, nc, time % s.lcm, stage)
                    if key in seen:
                        continue

                    seen.add(key)
                    Q.append((time, nr, nc, stage))
#
# #
#

if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'

    if infile == 'test.txt':
        m = AOC2022(infile)
    else:
        m = AOC2022(infile)


    # Part I & II
    m.solve()

    print("------------- A -------------")
    print('S1 ', m.S1)
    print("------------- B -------------")
    print('S2 ', m.S2)
    print("-----------------------------")
