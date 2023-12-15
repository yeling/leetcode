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

def main(k,n):
    ans = list(range(1, k + 1))
    # print(ans)
    d = 1
    s = 0
    while s + d <= n - k:
        s += d
        d += 1
    d -= 1
    # print(d,s)
    j = 1
    s = 0
    if d >= k:
        d = k
    for i in range(-d,0):
        s += j
        ans[i] += s
        j += 1
    print(*ans)
    return 

# main(5, 9)

caseNum = int(input())
for i in range(0, caseNum):
    k, n = li()
    main(k,n)
   
