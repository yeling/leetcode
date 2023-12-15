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

def main2(n, c, d, nums):
    nums.sort()
    cache = set(nums)
    same = 0
    diff = n
    ans = diff * c + d
    for i in range(1,nums[-1]+1):
        if i in cache:
            same += 1
            diff -= 1
        temp = (i - same) * d + diff * c
        ans = min(ans, temp)
        # print(i, same, ans, temp)
    print(ans)
    return 

def main(n, c, d, nums):
    nums.sort()
    same = 0
    diff = n
    ans = diff * c + d
    start = 1
    for i,v in enumerate(nums):
        #重复的过滤
        if i > 0 and nums[i - 1] == v:
            continue
        else:
            if v == start:
                start += 1
            else:
                start = v
            same += 1
            diff -= 1
            temp = (v - same) * d + diff * c
            ans = min(ans, temp)
        # print(v, same, ans, temp)
            
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,c,d = li()
    nums = li()
    # main2(n, c, d, nums)
    main(n, c, d, nums)
   
