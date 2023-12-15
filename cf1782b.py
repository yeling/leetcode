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
    ans = 0
    if nums[0] > 0:
        ans = 1
    for i in range(n):
        if i + 1 > nums[i]:
            if i + 1 < n and nums[i + 1] > i + 1:
                ans += 1
            elif i + 1 == n:
                ans += 1
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
