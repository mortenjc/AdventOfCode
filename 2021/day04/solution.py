#!/usr/local/bin/python3

import sys

def bingo(board):
    for i in range(5):
        a = ''.join(board[i*5:i*5+5])
        b = ''.join([board[i + j*5] for j in range(5)])
        if  a == '.....' or b == '.....':
            return True
    return False

if __name__ == '__main__':
    ifile = sys.argv[1] if len(sys.argv) > 1 else 'test.txt'

    with open(ifile) as fin:
        lines = (("\n" + fin.read().strip()).split('\n\n'))

    numbers, *boards = lines
    numbers = list(numbers.strip().split(','))

    B = []
    for b in boards:
        B.append(''.join(b.replace('\n',' ')).split())
    W = [False for _ in range(len(B))]
    first = 0
    last = 0

    for n in numbers:
        for i in range(len(B)):
            if W[i]:
                continue
            for j in range(len(B[i])):
                if B[i][j] == n:
                    B[i][j] = '.'
            if bingo(B[i]):
                print(f'Bingo for board {i}')
                W[i] = True
                s = int(n) * sum([int(x) for x in B[i] if x != '.'])
                if first == 0:
                    first = s
                last = s
                continue

    print("------------- A -------------")
    print(f'First {first}')
    print("------------- B -------------")
    print(f'Last {last}')
    print("-----------------------------")
