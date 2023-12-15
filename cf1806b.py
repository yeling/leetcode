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

def main2(n, nums):
    # print(n, nums)
    n = len(nums)
    cache = defaultdict(int)
    for v in nums:
        cache[v] += 1
    ans = 0
    allKey = list(cache.keys())
    allKey.sort()
    left = n
    for v in allKey:
        if v > ans:
            print(ans)
            return 
        else:
            if cache[v] <= left - cache[v] + 1:
                print(v)
                return 
            else:
                ans = v + 1
                left -= cache[v]
    print(ans)
    return 

def main(n, nums):
    # print(n, nums)
    n = len(nums)
    mi = min(nums)
    if mi > 0:
        print(0)
        return 
    if nums.count(0) == n:
        print(1)
    elif nums.count(0) <= n - nums.count(0) + 1:
        print(0)
    elif nums.count(0) + nums.count(1) < n:
        print(1)
    else:
        print(2)
    

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
