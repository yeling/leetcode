
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
    def countPairs(self, nums: List[int], target: int) -> int:    
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
    
nums = [-1,1,2,3,1]
target = 2
nums = [-6,2,5,-2,-7,-1,3]
target = -2
sol = Solution()
print(sol.countPairs(nums, target))
