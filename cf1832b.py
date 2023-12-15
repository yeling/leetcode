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

def solve2(n, k , nums):
    nums.sort()
    i = 0
    j = n - 1
    for ki in range(k):
        if nums[i] + nums[i + 1] > nums[j]:
            j -= 1
        else:
            i += 2
    ans = nums[i:j+1]
    # print(sum(ans))
    print(i,j, nums, sum(ans))
    return 

def solve(n, k , nums):
    nums.sort()
    pre = [0]*(n + 1)
    
    for i in range(n):
        pre[i + 1] = pre[i] + nums[i]
    total = pre[n]
    ans = 0
    for i in range(k+1):
        #i k-i
        temp = total - pre[2*i] - (pre[n] - pre[n - (k - i)])
        ans = max(ans, temp)

    print(ans)
    return 

# solve(5,1,[2, 5, 1, 10, 6])
caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    nums = li()
    solve(n, k , nums)
   
