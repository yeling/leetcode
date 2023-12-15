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

def main(n, k, d, w, nums):
    ans = 0
    first = -1
    cnt = 0
    for v in nums:
        # print(first, cnt, ans)
        if first == -1:
            first = v
            cnt = 1
        else:
            if v > first + d + w:
                ans += 1
                first = v
                cnt = 1
            else:
                cnt += 1
                if cnt == k:
                    ans += 1
                    first = -1
                    cnt = 0
    if cnt != 0:
        ans += 1
    print(ans)
    return 

def main2(n, k, d, w, nums):
    ans = 0
    i = 0 
    j = 0
    while i < n:
        ans += 1
        j = i
        while j < n and nums[j] - nums[i] <= d + w and j - i < k:
            j += 1
        i = j
    print(ans)
    

caseNum = int(input())
for i in range(0, caseNum):
    n,k,d,w = li()
    nums = li()
    main(n, k, d, w, nums)
    # main2(n, k, d, w, nums)
   
