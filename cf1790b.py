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

def main(n, s, r):
    m = s - r
    ans = [0] * n
    ans[0] = m
    for i in range(1,n):
        ans[i] = 1
        r -= 1
    for i in range(1,n):
        if r > m - 1:
            ans[i] += m - 1
            r -= m - 1
        elif r > 0:
            ans[i] += r
            r = 0
        else:
            break
    print(*ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,s,r = li()
    main(n, s, r)
   
