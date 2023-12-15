# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main(n, k, nums):
    #0, 1, -1
    #分组
    cache = [set() for _ in range(k)]
    change = 0
    for i,v in enumerate(nums):
        cache[(i+1)%k].add(v)
    # print(cache)
    for i in range(k):
        for v in cache[i]:
            if v%k != i:
                change += 1
    # print(change)
    if change == 0:
        print(0)
    elif change == 2:
        print(1)
    else:
        print(-1)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    nums = li()
    main(n, k, nums)
   
