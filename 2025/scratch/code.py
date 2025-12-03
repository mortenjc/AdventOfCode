
import sys

# lines = [
#     '987654321111111',
#     '811111111111119',
#     '234234234234278',
#     '818181911112111'
# ]

f = open('puzzle.txt')

lines = f.read().split('\n')


def pprint(narr, iarr):
    res = ""
    for i, n in enumerate(narr):
        if i in iarr:
            res += f'({n})'
        else:
            res += f'{n}'
    print(' ', res)


def move(narr, ival, st, ed):
    best = 0
    besti = -1
    if st >= ed:
        return (best, besti, 1)
    for i in range(ed-1, st -1, -1):
        n = narr[i]
        if n>= ival:
            if n>= best:
                best = n
                besti = i
    return (best, besti, 0)

S2 = 0
sz = 12
for line in lines:
    print()
    nums = [int(x) for x in line]
    l = len(nums)
    idxs = [x for x in range(l-sz, l) ]
    assert len(idxs) == sz
    pprint(nums, idxs)

    st = 0
    ed = len(nums) - sz
    for n in range(sz):
        val = nums[idxs[n]]
        b, bi, end = move(nums, val, st, ed)
        if bi == -1:
            break

        idxs[n] = bi
        st = bi + 1
        ed += 1

        pprint(nums, idxs)


    res = ""
    print(' ')
    for i in range(sz):
        print(i, idxs[i])
        res += str(nums[idxs[i]])
    print('JOLT', res)
    S2 += int(res)

print(S2)

