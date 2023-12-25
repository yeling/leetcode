
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

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int: 
        l = 0
        r = 2
        n = len(nums)
        nums.sort()
        # print(nums)
        pre = [0] * (n + 1)
        for i,v in enumerate(nums):
            pre[i + 1] = pre[i] + v
        ans = -1
        for i,v in enumerate(nums):
            if pre[i] > v:
                ans = max(ans, pre[i + 1])
        return ans
    
nums = [1,12,1,2,5,50,3]
nums = [5,5,5]
nums = [2,3,5]
sol = Solution()
print(sol.largestPerimeter(nums))
