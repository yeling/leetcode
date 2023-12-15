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
    ans = [0] * n
    ans[0] = nums[0]
    for i,v in enumerate(nums):
        if v == ans[i]:
            ans[i + 1] = 0
        elif i and v <= nums[i - 1]:
            ans[i] = v
            ans[i + 1] = 0
        else:
            ans[i + 1] = v
    print(*ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
