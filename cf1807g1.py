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

def main(n, nums):
    nums.sort()
    dis = 1
    if nums[0] > 1:
        print('No')
        return 
    for i in range(1,n):
        if nums[i] <= dis:
            dis += nums[i]
        else:
            print('No')
            return 
        # print(nums[i], dis)
    print('Yes')  
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
