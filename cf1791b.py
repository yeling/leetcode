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
    dst = (1,1)
    start = [0,0]
    for v in s:
        # UUURDDL
        if v == 'U':
            start[1] += 1
        elif v == 'D':
            start[1] -= 1
        elif v == 'R':
            start[0] += 1
        elif v == 'L':
            start[0] -= 1
        if start[0] == 1 and start[1] == 1:
            print('Yes')
            return
    print('No')
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    main(n, s)
   
