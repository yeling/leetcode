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

def getAllfactor(k):
    if k == 1 or k == 0:
        return 1
    ans = 2
    i = 2
    while i * i <= k:
        if k % i == 0:
            ans += 1
            if i * i != k:
                ans += 1
        i += 1
    return ans


def main(n,nums):
    next = defaultdict(int)
    dp = defaultdict(int)
    for v in nums:
        next = defaultdict(int) 
        for k in dp:
            next[k ^ v] += 1
        next[v] += 1
        dp = next
        print(dp)
    ans = 0
    dp = next
    for k in dp:
        temp = getAllfactor(k)
        if temp & 1== 0:
            ans += dp[k]
    print(ans)

    return 

def main2(n,nums):
    ans = 0
    dp = defaultdict(int)
    for i in range(n):
        for j in range(i,n):
            temp = nums[i]
            for k in range(i + 1,j + 1):
                temp ^= nums[k]
            f = getAllfactor(temp)
            dp[temp] += 1
            if f & 1 == 0:
                ans += 1
            # print(i,j, ans, dp)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n,nums)
    main2(n,nums)
