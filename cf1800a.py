# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main(n, s):
    #meou
    state = -1
    for v in s:
        if state == -1:
            if v == 'm' or v == 'M':
                state = 0
                continue
            else:
                print('NO')
                return
        elif state == 0:
            if v == 'm' or v == 'M':
                continue
            elif v == 'e' or v == 'E':
                state = 1
            else:
                print('NO')
                return
        elif state == 1:
            if v == 'e' or v == 'E':
                continue
            elif v == 'o' or v == 'O':
                state = 2
            else:
                print('NO')
                return
        elif state == 2:
            if v == 'o' or v == 'O':
                continue
            elif v == 'w' or v == 'W':
                state = 3
            else:
                print('NO')
                return
        elif state == 3:
            if v == 'w' or v == 'W':
                continue
            else:
                print('NO')
                return
    if state != 3:
        print('NO')
    else:
        print('YES')

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    main(n, s)
   
