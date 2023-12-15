# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def solve(n, nums):
    pos = 0
    next = 0
    for i,v in enumerate(nums):
        if v == n:
            pos = i
        elif v == n - 1:
            next = i
    r = 0
    if pos == 0:
        r = next - 1
    else:
        r = pos - 1
    if r == n - 2 and nums[n - 2] < nums[0]:
        l = r = n -1
    else:
        l = r
        for i in range(r-1, -1, -1):
            if nums[i] >= nums[0]:
                l = i
            else:
                break
    ans = nums[r+1:]
    # print(l,r)

    for i in range(r, l - 1, -1):
        # print(i)
        if i >= 0:
            ans.append(nums[i])
    if l > 0:
        ans += nums[0:l]
    print(*ans)
    

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)
   
