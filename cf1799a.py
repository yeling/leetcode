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

def main(n , m, nums):
    ans = [-1] * n
    cache = set()
    index = n - 1

    for i,v in enumerate(nums):
        if v not in cache:
            ans[index] = i + 1
            index -= 1
            cache.add(v) 
        if index < 0:
            break
    print(*ans)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    nums = li()
    main(n , m, nums)
   
