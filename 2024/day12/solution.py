#!/usr/local/bin/python3

from collections import deque
from collections import defaultdict
import sys
import numpy as np
import matplotlib.pyplot as plt
import random

infile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'
print("<<{}>>".format(infile))

S1 = 0
S2 = 0


with open(infile) as fin:
    lines = ((fin.read().strip()).split('\n'))

G = [[l for l in x] for x in lines]
R = len(G)
C = len(G[0])


# Creating a black image using a NumPy array
image_height = R
image_width = C
my_image = np.zeros((image_height, image_width, 3), dtype=np.uint8)

# For plotting
def colourregion(image, region):
    cr = random.randint(50, 255)
    cg = random.randint(0, 155)
    cb = random.randint(50, 255)
    for r, c in region:
        image[r, c, 0] = cr  # Set red
        image[r, c, 1] = cg    # Set green
        image[r, c, 2] = cb    # Set blue


def region(G, sr, sc):
    Q = [(sr,sc)]
    ch = G[sr][sc]
    area = set()
    area.add((sr,sc))
    while Q:
        r,c = Q.pop(0)
        for dr,dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            rr = r+dr
            cc = c+dc
            if not (0<=rr<R and 0<=cc<C):
                continue
            if not G[rr][cc] == ch:
                continue
            if (rr,cc) in area:
                continue
            area.add((rr,cc))
            Q.append((rr,cc))
    return area



def neighb(area, r, c):
    #print(area, r, c)
    p = 0
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        rr = r + dr
        cc = c + dc
        if (rr, cc) in area:
            p += 1
    return p



def perim(area):
    p = 0
    for r, c in area:
        p += 4 - neighb(area, r, c)
    return p



def walk(area):
    found = False
    for r, c in area:
        if neighb(area, r, c) == 2: # corner
            break

    print('starting', r,c) # starting point



# find all regions
seen = set()
res = []
for r in range(R):
    for c in range(C):
        if (r,c) in seen:
            continue
        a = region(G, r, c)
        res.append(a)
        colourregion(my_image, a)
        for x in a:
            seen.add(x)

for i, a in enumerate(res):
    #print(i, len(a), perim(a))
    S1 += len(a)*perim(a)

walk(res[0])

#Show the black image using matplotlib
plt.imshow(my_image)
plt.axis('off')  # It helps when Turn off axes to remove the axis ticks and labels
plt.show()

print("------------- A -------------")
print('S1 ', S1)
print("------------- B -------------")
print('S2 ', S2)
print("-----------------------------")
