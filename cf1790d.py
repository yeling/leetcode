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
    ans = 0
    cache = defaultdict(int)
    for v in nums:
        cache[v] += 1
    keys = list(cache.keys())
    keys.sort()
    # print(keys, cache)
    for i in range(keys[0],keys[-1]):
        if cache[i] > cache[i + 1]:
            ans += cache[i] - cache[i + 1]
    # print(ans)
    ans += cache[keys[-1]]
    print(ans)
    return 

def main(n, nums):
    ans = 0
    cache = defaultdict(int)
    for v in nums:
        cache[v] += 1
    keys = list(cache.keys())
    keys.sort()
    # print(keys, cache)
    for i in range(0,len(keys) - 1):
        if keys[i] + 1 == keys[i + 1]:
            if cache[keys[i]] > cache[keys[i + 1]]:
                ans += cache[keys[i]] - cache[keys[i + 1]]
        else:
            ans += cache[keys[i]] 
        # print(i, keys[i], ans)
    # print(ans)
    ans += cache[keys[-1]]
    print(ans)
    return 


caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
