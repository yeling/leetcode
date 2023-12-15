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

def main2(n, q, nums, qs):
    s = sum(nums)
    pre = [0]*(n+1)
    for i,v in enumerate(nums):
        pre[i + 1] = pre[i] + v

    for l,r,k in qs:
        tempS = 0
        for i in range(l, r+1):
            tempS += k - nums[i - 1]
        if (tempS + s)%2 == 1:
            print('Yes')
        else:
            print('No')
    return 

def main(n, q, nums, qs):
    s = sum(nums)
    pre = [0]*(n+2)
    for i,v in enumerate(nums):
        pre[i + 1] = pre[i] + v
    
    pre[n + 1] = pre[n]
    # print(pre)
    for l,r,k in qs:
        # print(l,r,k)
        tempS = (r - l + 1) * k - (pre[r - 1 + 1] - pre[l - 1])
        # for i in range(l, r+1):
        #     tempS += k - nums[i - 1]
        # print(tempS)
        if (tempS + s)%2 == 1:
            print('Yes')
        else:
            print('No')
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,q = li()
    nums = li()
    qs = []
    for j in range(q):
        qs.append(li())
    main(n, q, nums, qs)
   
