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
    if nums.count(1) == n or n == 1:
        print(0)
        return
    if 1 in nums:
        print(-1)
        return
    m = INF
    mPos = -1
    for i,v in enumerate(nums):
        if v < m:
            m = v
            mPos = i
    
    index = 0
    ans = []
    while index < n:
        while(nums[index] > nums[mPos]):
            nums[index] = (nums[index] + nums[mPos] - 1)//nums[mPos]
            ans.append([index + 1, mPos + 1])
        if nums[index] < nums[mPos]:
            mPos = index
            index = 0
        else:
            index += 1

    print(len(ans))
    for v in ans:
        print(*v)

    return 

# nums = [3, 3, 4, 4]
# n = len(nums)
# main(n, nums)

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
