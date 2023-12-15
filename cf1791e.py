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

def main( n, nums):
    #
    ne = 0
    minN = INF
    maxN = -INF
    for i,v in enumerate(nums):
        if v <= 0:
            ne += 1
            nums[i] = -v
            maxN = max(maxN, v)
        else:
            minN = min(minN, v)
    # print(nums,  maxN)
    if ne % 2 == 0:
        print(sum(nums))
    else:
        if minN < -maxN:
            print(sum(nums) - 2 * minN)
        else:
            print(sum(nums) + 2 * maxN)
    return
    

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
