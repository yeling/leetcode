
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
from heapq import *
import string
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

def allH():
    ret = list(range(10))
    n = 10000
    for i in range(1,n):
        temp = str(i)
        ret.append(int(temp + temp[::-1]))
        for j in range(10):
            ret.append(int(temp + str(j)+ temp[::-1]))
    return ret
all = allH()
all.sort()
# print(len(all))

class Solution:
    #TLE 363 / 645
    # 639 / 645 
    def minimumCost2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        pre = [0] * (n + 1)
        for i,v in enumerate(nums):
            pre[i + 1] = pre[i] + v
        ans = INF
        for i in all:
            pos = bisect_left(nums, i)
            ans = min(ans, pos * i - pre[pos] + pre[n] - pre[pos] - (n - pos) * i)

        return ans
    
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        pre = [0] * (n + 1)
        for i,v in enumerate(nums):
            pre[i + 1] = pre[i] + v
        ans = INF
        s = bisect_left(all, nums[0])
        e = bisect_right(all, nums[-1])
        e = min(e + 1, len(all))
        # print(s, e, nums, all[0:10])
        for i in range(s-1,e):
            v = all[i]
            pos = bisect_left(nums, v)
            ans = min(ans, pos * v - pre[pos] + pre[n] - pre[pos] - (n - pos) * v)

        return ans
    
nums = [1,2,3,4,5]
nums = [10,12,13,14,15]
nums = [22,33,22,33,22]
# 30, 20
nums = [102,103,105,106,109]
sol = Solution()
print(sol.minimumCost(nums))
