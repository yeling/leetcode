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

def main(n,k):
    l = 1
    r = n
    ans = []
    while l <= r:
        i = 0
        while i < k - 1 and l < r:
            ans.append(r)
            r -= 1
            i += 1
        if l <= r:
            ans.append(l)
        l += 1
    print(*ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    main(n,k)
   
