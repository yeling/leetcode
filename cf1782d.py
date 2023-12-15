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
    print(nums)
    ans = 0
    i = 0
    j = 0
    while i < n:
        temp = 1
        while i + 1 < n and nums[i + 1] == nums[i]:
            temp += 1
            i += 1
        j = i
        while (nums[j] - nums[i]) % 2 == 1:
            
        


    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
