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
    dst = ord(s[0])
    pos = -1
    for i in range(n):
        if ord(s[-1-i]) == dst and pos == -1:
            pos = i
        elif ord(s[-1-i]) < dst:
            dst = ord(s[-1-i])
            pos = i
    pos = n - 1 - pos
    ans = [s[pos], *s[0:pos],*s[pos+1:]]
    print(''.join(ans))
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    main(n, s)
